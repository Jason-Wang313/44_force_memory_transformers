import json, math, os, random
from dataclasses import dataclass

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

OUT = "docs"
os.makedirs(OUT, exist_ok=True)

SEED = 7
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

def make_data(n=1200, T=24, d=4):
    X = np.zeros((n, T, d), dtype=np.float32)
    y = np.zeros((n, T), dtype=np.float32)
    regime = np.zeros((n, T), dtype=np.float32)
    for i in range(n):
        r = 0
        mem = 0.0
        for t in range(T):
            if t in (7, 15):
                r = 1 - r
            regime[i, t] = r
            force = np.random.randn() * 0.1 + (2.0 if r == 1 else -2.0)
            slip = np.random.randn() * 0.3
            X[i, t, 0] = force
            X[i, t, 1] = slip
            X[i, t, 2] = r
            X[i, t, 3] = np.sin(0.3 * t)
            # target requires using force memory when regime persists,
            # but stale force is harmful immediately after a switch.
            if t == 0 or regime[i, t] != regime[i, t-1]:
                mem = 0.0
            else:
                mem = 0.8 * mem + 0.2 * force
            y[i, t] = 1.0 if (mem + 0.3 * slip + 0.2 * r) > 0.25 else 0.0
    return X, y, regime

class FlatTransformer(nn.Module):
    def __init__(self, d=4, h=32):
        super().__init__()
        self.inp = nn.Linear(d, h)
        enc_layer = nn.TransformerEncoderLayer(d_model=h, nhead=4, dim_feedforward=64, batch_first=True)
        self.tr = nn.TransformerEncoder(enc_layer, num_layers=2)
        self.out = nn.Linear(h, 1)
    def forward(self, x):
        z = self.inp(x)
        z = self.tr(z)
        return self.out(z).squeeze(-1)

class ForgetMemoryTransformer(nn.Module):
    def __init__(self, d=4, h=32):
        super().__init__()
        self.inp = nn.Linear(d, h)
        self.gru = nn.GRUCell(h, h)
        self.forget = nn.Linear(h, 1)
        self.out = nn.Linear(h, 1)
        self.h = h
    def forward(self, x):
        B, T, D = x.shape
        h = torch.zeros(B, self.h, device=x.device)
        outs = []
        for t in range(T):
            z = torch.tanh(self.inp(x[:, t]))
            gate = torch.sigmoid(self.forget(z))
            # Explicit forgetting: when the gate is high, preserve more memory;
            # when low, actively decay stale force state.
            h = self.gru(z, h * gate)
            outs.append(self.out(h))
        return torch.cat(outs, dim=1)

def train(model, Xtr, ytr, Xte, yte, epochs=12):
    device = torch.device("cpu")
    model.to(device)
    opt = optim.Adam(model.parameters(), lr=2e-3)
    loss_fn = nn.BCEWithLogitsLoss()
    Xtr = torch.tensor(Xtr, device=device)
    ytr = torch.tensor(ytr, device=device)
    Xte = torch.tensor(Xte, device=device)
    yte = torch.tensor(yte, device=device)
    for _ in range(epochs):
        model.train()
        opt.zero_grad()
        logits = model(Xtr)
        loss = loss_fn(logits, ytr)
        loss.backward()
        opt.step()
    model.eval()
    with torch.no_grad():
        pred = (torch.sigmoid(model(Xte)) > 0.5).float()
        acc = (pred == yte).float().mean().item()
        # Evaluate specifically right after switches.
        switch_idx = torch.tensor([7, 15], device=device)
        sw = (pred[:, switch_idx] == yte[:, switch_idx]).float().mean().item()
    return acc, sw

def main():
    X, y, regime = make_data()
    n = len(X)
    idx = np.random.permutation(n)
    tr = idx[:900]
    te = idx[900:]
    Xtr, ytr = X[tr], y[tr]
    Xte, yte = X[te], y[te]
    results = {}
    for name, model in [
        ("flat_transformer", FlatTransformer()),
        ("forget_memory_transformer", ForgetMemoryTransformer()),
    ]:
        acc, sw = train(model, Xtr, ytr, Xte, yte)
        results[name] = {"overall_acc": acc, "switch_acc": sw}
    Path = __import__("pathlib").Path
    Path(OUT, "synthetic_results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
