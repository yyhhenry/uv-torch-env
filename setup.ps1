if (-not (Test-Path .venv)) {
    uv venv -p 3.10
}

if (Test-Path requirements-torch.txt) {
    uv pip install -r requirements-torch.txt --extra-index-url https://download.pytorch.org/whl/cu121
}

uv pip install -r requirements.txt

.venv\Scripts\activate
