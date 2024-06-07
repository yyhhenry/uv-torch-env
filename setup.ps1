if (-not (Test-Path .venv)) {
    uv venv -p 3.10
}

uv pip install -r requirements.txt

.venv\Scripts\activate
