$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$DataDir = Join-Path $Root "data"
$DownloadsPdf = "C:\Users\wangz\Downloads\44.pdf"
$LocalPdf = Join-Path $Root "main.pdf"
$BuildStatus = Join-Path $DataDir "build_status.json"

New-Item -ItemType Directory -Force -Path $DataDir | Out-Null

Push-Location $Root
try {
    pdflatex -interaction=nonstopmode -halt-on-error main.tex | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "pdflatex failed on initial pass"
    }
    bibtex main | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "bibtex failed"
    }
    foreach ($pass in 1..3) {
        pdflatex -interaction=nonstopmode -halt-on-error main.tex | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "pdflatex failed on pass $pass"
        }
    }

    if (-not (Test-Path -LiteralPath $LocalPdf)) {
        throw "Expected PDF was not produced: $LocalPdf"
    }

    Copy-Item -LiteralPath $LocalPdf -Destination $DownloadsPdf -Force
    Remove-Item -LiteralPath $LocalPdf -Force

    $hash = Get-FileHash -LiteralPath $DownloadsPdf -Algorithm SHA256

    $status = [ordered]@{
        paper = 44
        status = "final_v3_full_scale"
        canonical_pdf = $DownloadsPdf
        canonical_sha256 = $hash.Hash
        local_pdf_removed = -not (Test-Path -LiteralPath $LocalPdf)
        built_at = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss zzz")
    }

    $status | ConvertTo-Json | Set-Content -Path $BuildStatus -Encoding UTF8
}
finally {
    Pop-Location
}
