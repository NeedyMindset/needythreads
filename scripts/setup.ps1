# NeedyThreads setup for Windows: installs Python if missing, then the two
# packages the publishing layer needs, then saves your Publora keys in
# ~/.needythreads/.env. Safe to run again.
# Writing posts does not need any of this; only publishing and images do.
#
# Run from PowerShell:  .\scripts\setup.ps1

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot

function Test-Python {
    try {
        & python -c "import sys; sys.exit(0 if sys.version_info[0] == 3 else 1)" 2>$null
        return ($LASTEXITCODE -eq 0)
    } catch {
        return $false
    }
}

if (Test-Python) {
    Write-Host "Python is already installed."
} else {
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        Write-Host "winget was not found. Install Python from https://www.python.org/downloads/"
        Write-Host "(tick 'Add python.exe to PATH' on the first screen), then run this script again."
        exit 1
    }
    Write-Host "Installing Python 3.12 with winget..."
    winget install --id Python.Python.3.12 --exact --scope user --accept-package-agreements --accept-source-agreements --silent
    $env:Path = [Environment]::GetEnvironmentVariable('Path', 'User') + ';' + [Environment]::GetEnvironmentVariable('Path', 'Machine')
    if (-not (Test-Python)) {
        Write-Host "Python is installed but this window cannot see it yet."
        Write-Host "Close PowerShell, open a new one, and run this script again."
        exit 1
    }
}

Write-Host "Installing the Python packages..."
$requirements = Join-Path $root 'requirements.txt'
if (Test-Path $requirements) {
    python -m pip install --quiet -r $requirements
} else {
    python -m pip install --quiet "requests>=2.31.0" "python-dotenv>=1.2.4"
}
if ($LASTEXITCODE -ne 0) {
    Write-Host "pip failed. See the Troubleshooting table in the README."
    exit 1
}

Write-Host ""
Write-Host "Connecting Publora (press Enter to skip, posts then stay in draft mode)..."
python (Join-Path $PSScriptRoot 'configure_env.py')

Write-Host ""
Write-Host "Done. Python and the packages are ready."
