if [ ! -d ".venv" ]; then
    uv venv -p 3.10
fi

uv pip install -r requirements.txt
source .venv/bin/activate
