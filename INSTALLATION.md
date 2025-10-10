# Installation Guide

## System Requirements

### Minimum (SD 1.5 models)
- 16GB RAM
- 8GB VRAM (or M1/M2 with 16GB unified memory)
- 20GB disk space

### Recommended (FLUX/SDXL)
- 32GB RAM
- 16GB+ VRAM (or M1/M2 Pro/Max with 32GB+ unified memory)
- 50GB disk space

### Optimal
- Apple M1/M2 Pro/Max/Ultra
- NVIDIA RTX 3090/4090
- 64GB+ RAM

---

## Software Installation

### 1. Install Python 3.8+

**macOS** (via Homebrew):
```bash
brew install python@3.11
```

**Linux/Windows**: Download from [python.org](https://python.org)

### 2. Install PyTorch

**macOS (Apple Silicon)**:
```bash
pip3 install torch torchvision torchaudio
```

**Linux/Windows (NVIDIA GPU)**:
```bash
# CUDA 11.8
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# CUDA 12.1
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**CPU Only** (any platform):
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### 3. Install Required Libraries

```bash
# Core dependencies
pip3 install diffusers transformers accelerate

# HuggingFace Hub (for model downloads)
pip3 install huggingface-hub

# Image processing
pip3 install pillow

# Optional: for better performance
pip3 install xformers  # NVIDIA only, significantly speeds up generation
```

### Complete One-Line Install

**macOS (Apple Silicon)**:
```bash
pip3 install torch torchvision torchaudio diffusers transformers accelerate huggingface-hub pillow
```

**Linux/Windows (NVIDIA)**:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 && \
pip3 install diffusers transformers accelerate huggingface-hub pillow xformers
```

**CPU Only**:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && \
pip3 install diffusers transformers accelerate huggingface-hub pillow
```

### 4. Verify Installation

```bash
python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.cuda.is_available()}'); print(f'MPS: {torch.backends.mps.is_available()}')"
```

Expected output (Mac): `MPS: True`  
Expected output (NVIDIA): `CUDA: True`

---

## HuggingFace Setup (Required)

### Create Free HuggingFace Account
1. Go to [huggingface.co](https://huggingface.co) and sign up (free)
2. Go to [Settings > Access Tokens](https://huggingface.co/settings/tokens)
3. Click "New token" → Create a **Read** token
4. Copy the token

### Set Up Token (choose one method)

**Method 1: Login via CLI** (Recommended):
```bash
huggingface-cli login
# Paste your token when prompted
```

**Method 2: Environment Variable**:
```bash
# Add to ~/.bashrc or ~/.zshrc
export HUGGINGFACE_TOKEN="your_token_here"
```

**Method 3: Python Code** (for scripts):
```python
from huggingface_hub import login
login(token="your_token_here")
```

### Accept Model Licenses (if needed)
- Visit model pages on HuggingFace
- Click "Agree and access repository" for gated models
- Examples: FLUX.1, SDXL (most models are ungated)

> **Note**: Token is only used for downloading models. No data is sent to HuggingFace during generation.
