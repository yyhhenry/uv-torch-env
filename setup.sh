#!/bin/bash

if [ ! -d ".venv" ]; then
    uv venv -p 3.11
fi

if [ -f "requirements-torch.txt" ]; then
    uv pip install -r requirements-torch.txt --extra-index-url https://download.pytorch.org/whl/cu121
fi

uv pip install -r requirements.txt

source .venv/bin/activate
