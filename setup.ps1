if (-not (Test-Path .venv)) {
    uv venv -p 3.10
    uv pip install torch==2.1.2+cu121 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    uv pip install -r requirements.txt
}

.venv\Scripts\activate
