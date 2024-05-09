uv venv -p 3.10
$env:UV_EXTRA_INDEX_URL = "https://download.pytorch.org/whl/cu121"
# Or use extra command line without UV_EXTRA_INDEX_URL
# uv pip install torch==2.1.2+cu121 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
uv pip install -r requirements.txt
.venv\Scripts\activate
