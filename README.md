# 🎨 AI Image Generator v4.0

## **100% FREE • FULLY OFFLINE • NO PAID APIs • BATCH GENERATION • MULTI-MODEL COMPARISON**

A powerful, professional-grade image generation tool that runs **completely offline** on your own hardware. Generate unlimited images with **zero costs**, no paid subscriptions, no per-image charges, and complete privacy. Perfect for developers, designers, content creators, and anyone who needs high-quality AI-generated images.

> **⚠️ Setup Note**: Requires free HuggingFace account for model downloads. Some models may require accepting license terms on HuggingFace website. No ongoing API costs or per-image charges.

---

## 🚀 Why This Tool?

### 💰 **Completely Free Forever**
- ✅ **No paid API services** - runs 100% locally (free HuggingFace account needed for downloads)
- ✅ **Zero per-image costs** - generate thousands of images at no cost
- ✅ **No rate limits** - generate as many images as you want
- ✅ **All models are open-source** - free to use commercially
- ⚠️ **One-time setup**: Free HuggingFace token for model downloads, some models require license acceptance

### 🔒 **Total Privacy & Offline**
- ✅ **Works completely offline** - no internet required after model download
- ✅ **Your prompts never leave your computer** - complete privacy
- ✅ **No data collection** - no telemetry, no tracking
- ✅ **Local processing only** - your images stay on your machine

### ⚡ **Optimized for Local Hardware**
- ✅ **FLUX.1-schnell uses only 4 steps** - fastest FLUX model available
- ✅ **Batch processing** - generate 10, 50, 100+ images unattended
- ✅ **Multi-model comparison** - test multiple models simultaneously
- ✅ **Performance scales with available resources** - faster with more free RAM, CPU cores, or GPU VRAM
- ⚠️ **Speed depends on your hardware** - see Performance Notes below

### 🎯 **Professional Features**
- ✅ **7 production-ready AI models** - from lightweight (4GB) to ultra-quality (34GB)
- ✅ **Custom aspect ratios** - Square, Portrait, Landscape, Cinematic, and more
- ✅ **Per-image resolution control** - specify resolution for each image via JSON
- ✅ **Poster generation** - Create 2x3 portraits, 21:9 banners, any ratio you need
- ✅ **Cross-platform** - Mac (Apple Silicon), NVIDIA GPUs, or CPU
- ⚠️ **1 broken model** - Chroma-GGUF awaiting diffusers GGUF loader fix

---

## ✨ Key Features

### 🎨 **7 Working AI Models + 1 Broken (Awaiting Fix)**
| Model | Size | Quality | Speed | Status | Best For |
|-------|------|---------|-------|--------|----------|
| **FLUX.1-schnell** ⭐ | 34GB | ⭐⭐⭐⭐⭐ | ⚡⚡⚡⚡⚡ | ✅ Working | Highest quality, 512-token prompts |
| **SDXL Base** | 14GB | ⭐⭐⭐⭐ | ⚡⚡⚡ | ✅ Working | High resolution, detailed |
| **Playground v2.5** | 14GB | ⭐⭐⭐⭐ | ⚡⚡⚡ | ✅ Working | Beautiful aesthetics |
| **Realistic Vision** | 4GB | ⭐⭐⭐ | ⚡⚡⚡⚡ | ✅ Working | Photorealistic, food images |
| **DreamShaper** | 6GB | ⭐⭐⭐ | ⚡⚡⚡⚡ | ✅ Working | Versatile, artistic |
| **SD v1.5** | 6GB | ⭐⭐⭐ | ⚡⚡⚡⚡⚡ | ✅ Working | Fastest, lightweight |
| **Counterfeit** | 4GB | ⭐⭐⭐ | ⚡⚡⚡⚡ | ✅ Working | Fine details |
| **Chroma-GGUF** | 7GB | N/A | N/A | ⚠️ **BROKEN** | GGUF loader incompatibility |

> **⚠️ Model 8 (Chroma-GGUF) Status**: Currently broken due to diffusers library GGUF loader incompatibility. Error: `KeyError: 'time_in.in_layer.weight'`. Model is kept in the tool for future retrying when diffusers updates their GGUF support. Use Model 2 (FLUX.1-schnell) for best quality instead.

### 📐 **Professional Aspect Ratios**
- **Square (1:1)** - Social media posts, icons, thumbnails
- **Portrait (2:3)** - Posters, phone wallpapers, Pinterest
- **Portrait Wide (3:4)** - Standard prints, Instagram Stories
- **Landscape (3:2)** - Desktop wallpapers, photography
- **Landscape Wide (16:9)** - YouTube thumbnails, presentations
- **Cinematic (21:9)** - Ultra-wide banners, website headers

### 🔥 **Advanced Capabilities**
- **Batch Generation** - Process 100+ images in one command
- **Multi-Model Mode** - Compare up to 7 models side-by-side automatically
- **JSON-Based Control** - Define all parameters in simple JSON files
- **Flexible Resolutions** - 512px to 2048px, per-image or global
- **Three Resolution Modes** - JSON-defined, Override all, or Model defaults

---

## 📋 Installation & Prerequisites

### System Requirements

**Minimum** (SD 1.5 models):
- 16GB RAM
- 8GB VRAM (or M1/M2 with 16GB unified memory)
- 20GB disk space

**Recommended** (FLUX/SDXL):
- 32GB RAM
- 16GB+ VRAM (or M1/M2 Pro/Max with 32GB+ unified memory)
- 50GB disk space

**Optimal**:
- Apple M1/M2 Pro/Max/Ultra
- NVIDIA RTX 3090/4090
- 64GB+ RAM

### Software Installation

#### 1. Install Python 3.8+

**macOS** (via Homebrew):
```bash
brew install python@3.11
```

**Linux/Windows**: Download from [python.org](https://python.org)

#### 2. Install PyTorch

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

#### 3. Install Required Libraries

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

#### Complete One-Line Install

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

#### 4. Verify Installation

```bash
python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.cuda.is_available()}'); print(f'MPS: {torch.backends.mps.is_available()}')"
```

Expected output (Mac): `MPS: True`
Expected output (NVIDIA): `CUDA: True`

#### 5. HuggingFace Setup (Required)

**Create Free HuggingFace Account**:
1. Go to [huggingface.co](https://huggingface.co) and sign up (free)
2. Go to [Settings > Access Tokens](https://huggingface.co/settings/tokens)
3. Click "New token" → Create a **Read** token
4. Copy the token

**Set Up Token** (choose one method):

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

**Accept Model Licenses** (if needed):
- Visit model pages on HuggingFace
- Click "Agree and access repository" for gated models
- Examples: FLUX.1, SDXL (most models are ungated)

> **Note**: Token is only used for downloading models. No data is sent to HuggingFace during generation.

---

## 🎯 What Makes This Special?

### 💡 **Use Cases**

1. **Content Creators** - Generate unlimited thumbnails, banners, social media graphics
2. **Designers** - Create mockups, concepts, and variations without stock photo costs
3. **Developers** - Generate app icons, food images, UI elements for projects
4. **Marketers** - Product visuals, ads, promotional materials at zero cost
5. **Indie Projects** - Professional quality images without budget constraints
6. **Learning & Experimentation** - Try different models and techniques freely

### 🆚 **vs. Cloud Services**

| Feature | This Tool | MidJourney | DALL-E 3 | Stable Diffusion Online |
|---------|-----------|------------|----------|-------------------------|
| **Cost** | FREE | $10-60/mo | $0.04/img | $10-50/mo |
| **Privacy** | 100% Private | Public | Stored | Varies |
| **Offline** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Batch Mode** | ✅ Unlimited | ❌ Limited | ❌ No | ⚠️ Limited |
| **Multi-Model** | ✅ 7 models | ❌ 1 model | ❌ 1 model | ⚠️ Varies |
| **API Limits** | ✅ None | ⚠️ 200/day | ⚠️ Pay/use | ⚠️ Varies |
| **Speed** | Varies* | 30-60s | 10-20s | Varies |
| **Customization** | ✅ Full | ⚠️ Limited | ❌ None | ⚠️ Limited |

*Speed depends heavily on your hardware (see Performance Notes section)

## 🚀 Quick Start

### Basic Usage

```bash
# Simple generation with default settings
python generate_images_v3.py food_prompts.json

# Specify output directory
python generate_images_v3.py food_prompts.json output/

# Compare multiple models
python generate_images_v3.py food_prompts.json output/ multi
```

### JSON Format

**Simple Format** (uses model defaults):
```json
{
  "image_name": "A beautiful sunset over mountains"
}
```

**Advanced Format** (custom aspect ratio & resolution):
```json
{
  "image_name": {
    "prompt": "A beautiful sunset over mountains",
    "aspect_ratio": "landscape",
    "base_resolution": 1536
  }
}
```

## 📐 Aspect Ratios

| Name | Ratio | Best For |
|------|-------|----------|
| `square` | 1:1 | Icons, thumbnails, Instagram posts |
| `portrait` | 2:3 | Posters, phone wallpapers |
| `portrait_wide` | 3:4 | Standard photo prints |
| `landscape` | 3:2 | Desktop wallpapers, photography |
| `landscape_wide` | 16:9 | YouTube thumbnails, presentations |
| `cinematic` | 21:9 | Ultra-wide banners, headers |

## 🎨 Models

> **⚠️ Important**: Model sizes represent BOTH download size AND active RAM/VRAM usage during generation. A 5.5GB model downloads 5.5GB and uses ~5.5GB RAM while running. Ensure you have sufficient free memory before generating.

### Model 1: Stable Diffusion v1.5
- **Size**: 5.5GB (download + active RAM usage)
- **Access**: Open (no license acceptance needed)
- **Resolution**: 512-768px
- **Best For**: Quick testing, low memory systems
- **Speed**: ⚡⚡⚡⚡⚡

### Model 2: FLUX.1-schnell ⭐ RECOMMENDED
- **Size**: 33.7GB (download + active RAM usage)
- **Access**: Open (no license acceptance needed)
- **Resolution**: 512-2048px
- **Best For**: Highest quality, detailed images
- **Speed**: ⚡⚡⚡⚡⚡ (only 4 diffusion steps!)
- **Features**: 512 token prompts, exceptional detail
- **RAM Requirement**: ~24GB free RAM/VRAM during generation

### Model 3: Realistic Vision v5.1
- **Size**: 4.3GB (download + RAM usage)
- **Access**: Open (no license needed)
- **Resolution**: 512-768px
- **Best For**: Photorealistic images, food photography
- **Speed**: ⚡⚡⚡

### Model 4: DreamShaper v8
- **Size**: 5.5GB (download + RAM usage)
- **Access**: Open (no license needed)
- **Resolution**: 512-768px
- **Best For**: Versatile, artistic and realistic mix
- **Speed**: ⚡⚡⚡

### Model 5: Counterfeit v2.5
- **Size**: 4.3GB (download + RAM usage)
- **Access**: Open (no license needed)
- **Resolution**: 512-768px
- **Best For**: Fine details, faces
- **Speed**: ⚡⚡⚡

### Model 6: Playground v2.5
- **Size**: 13.9GB (download + RAM usage)
- **Access**: Open (no license needed)
- **Resolution**: 512-1536px
- **Best For**: Beautiful aesthetics, artistic images
- **Speed**: ⚡⚡⚡
- **RAM Requirement**: ~12GB free RAM/VRAM

### Model 7: SDXL Base 1.0
- **Size**: 14.2GB (download + RAM usage)
- **Access**: Open (no license needed)
- **Resolution**: 512-1536px
- **Best For**: High quality, detailed images
- **Speed**: ⚡⚡
- **RAM Requirement**: ~12GB free RAM/VRAM

### Model 8: Chroma-GGUF ⚠️ CURRENTLY BROKEN
- **Size**: 7.1GB (quantized)
- **Access**: Open
- **Resolution**: N/A
- **Status**: ⚠️ **BROKEN** - GGUF loader incompatibility
- **Error**: `KeyError: 'time_in.in_layer.weight'`
- **Note**: Kept for future retrying when diffusers updates GGUF support
- **Alternative**: Use Model 2 (FLUX.1-schnell) for best quality

## 💡 Usage Examples

### Generate Food Icons (512x512)
```bash
python generate_images_v3.py food_prompts.json assets/foods/
# When prompted:
# 1. Select model: 2 (FLUX.1-schnell)
# 2. Resolution mode: 3 (Use model defaults)
```

### Generate Posters (Various Aspect Ratios)
```bash
python generate_images_v3.py sample_poster_prompts.json posters/
# When prompted:
# 1. Select model: 2 (FLUX.1-schnell)
# 2. Resolution mode: 1 (Use JSON-defined resolutions)
```

### Compare Multiple Models
```bash
python generate_images_v3.py sample_poster_prompts.json comparison/ multi
# When prompted:
# 1. Select models: 2,6,7 (FLUX, Playground, SDXL)
# 2. Resolution mode: 1 (Use JSON-defined)
# Output: comparison/flux-schnell/, comparison/playground-v2.5/, comparison/sdxl-base-1.0/
# Note: Avoid Model 8 (Chroma-GGUF) - currently broken
```

### Override All with Landscape 4K
```bash
python generate_images_v3.py any_prompts.json output/
# When prompted:
# 1. Select model: 2 (FLUX.1-schnell)
# 2. Resolution mode: 2 (Override all)
# 3. Aspect ratio: 4 (Landscape 3:2)
# 4. Base resolution: 2048
```

## 🎯 Resolution Modes

### Mode 1: Use JSON-defined resolutions (Recommended)
Each prompt can specify its own aspect ratio and resolution in the JSON file. Most flexible option.

### Mode 2: Override all with single aspect ratio
Force all images to use the same aspect ratio and resolution. Good for batch processing with consistent output.

### Mode 3: Use model defaults
Ignore JSON aspect ratios and use each model's default resolution. Fastest option.

## 🔧 Advanced Tips

### Memory Optimization
1. Use **SD 1.5** models (1, 3-5) for systems with <16GB RAM
2. Use **Playground v2.5** (Model 6) for mid-range systems with 16GB+ RAM
3. Close other applications before generating
4. Use smaller base resolutions (512-1024) for faster generation
5. ⚠️ Avoid Model 8 (Chroma-GGUF) - currently broken

### Best Quality Results
1. Use **FLUX.1-schnell** (Model 2) for maximum detail
2. Write detailed prompts (FLUX supports 512 tokens!)
3. Use higher base resolutions (1536-2048) for large prints
4. Experiment with different models - each has unique strengths

### Prompt Writing Tips
- **Be specific**: "Fresh red apple on white background" > "apple"
- **Add details**: Include colors, lighting, style, mood
- **For FLUX**: Take advantage of 512 tokens - add botanical names, measurements, textures
- **For food**: Mention freshness, arrangement, lighting style

## 📊 Performance Notes

### ⚠️ Important: Speed Depends on Your Hardware

Generation speed varies **dramatically** based on:

1. **Available Free RAM** (not total RAM)
   - More free RAM = faster generation
   - Close other applications before generating
   - MacOS/Linux: Use `Activity Monitor` or `htop` to check free memory

2. **Processor Utilization**
   - **GPU (CUDA/Metal)**: Fastest, uses GPU cores/VRAM
   - **CPU**: Slower, uses available CPU threads
   - Background processes reduce available compute

3. **Hardware Configuration**
   - Apple Silicon (M1/M2/M3): Uses unified memory (MPS backend)
   - NVIDIA GPU: Uses dedicated VRAM (CUDA backend)
   - CPU-only: Slowest but works on any machine

### Reference Benchmarks

**Apple M1 Pro 32GB (MPS, ~20GB Free RAM)**:
| Model | Resolution | Steps | Time | Memory Used |
|-------|------------|-------|------|-------------|
| SD v1.5 | 512x512 | 40 | 1-2 min | ~4GB |
| FLUX.1-schnell | 1024x1024 | 4 | 2-4 min | ~24GB |
| SDXL Base | 1024x1024 | 30 | 3-5 min | ~12GB |
| Playground v2.5 | 1024x1024 | 30 | 3-5 min | ~12GB |

**NVIDIA RTX 3090 24GB (CUDA, ~18GB Free VRAM)**:
| Model | Resolution | Steps | Time | VRAM Used |
|-------|------------|-------|------|-----------|
| SD v1.5 | 512x512 | 40 | 10-20s | ~3GB |
| FLUX.1-schnell | 1024x1024 | 4 | 30-60s | ~20GB |
| SDXL Base | 1024x1024 | 30 | 45-90s | ~10GB |

**CPU-Only (16-core Ryzen, 32GB RAM)**:
| Model | Resolution | Steps | Time | RAM Used |
|-------|------------|-------|------|----------|
| SD v1.5 | 512x512 | 40 | 5-10 min | ~8GB |
| SDXL Base | 1024x1024 | 30 | 15-30 min | ~16GB |

> **Note**: Times vary significantly based on prompt complexity, image resolution, available system resources, and background processes. These are rough estimates only.

## 🐛 Troubleshooting

### Out of Memory Errors
- Use smaller models (SD 1.5 models: 1, 3-5)
- Reduce base_resolution in JSON
- Close other applications
- Use CPU mode (slower but works)

### Black/Blank Images
- Try different model (Models 2, 6, 7 work best)
- Check prompt quality
- Verify model downloaded correctly

### Chroma-GGUF (Model 8) Errors
- **Status**: Currently broken due to GGUF loader incompatibility
- **Error**: `KeyError: 'time_in.in_layer.weight'`
- **Solution**: Use Model 2 (FLUX.1-schnell) instead for best quality
- **Future**: Will be fixed when diffusers updates GGUF support

### Model Download Issues
- Check internet connection
- Verify HuggingFace Hub access
- Models download automatically on first use

## 📁 Project Structure

```
docs/images/
├── generate_images_v3.py          # Main script
├── README.md                       # This file
├── sample_poster_prompts.json     # Example posters (5 aspect ratios)
├── food_prompts_final_fixes.json  # Food/lifestyle icons
└── [output folders]/              # Generated images
```

## 🔄 Version History

### v4.0 (Current)
- ✨ Added custom aspect ratio control (6 presets)
- ✨ Per-prompt resolution control via JSON
- ✨ Model info display (size, access type, capabilities)
- ✨ Three resolution modes (JSON, Override, Default)
- 📝 Comprehensive documentation
- ⚠️ Marked Chroma-GGUF (Model 8) as broken due to GGUF loader incompatibility

### v3.1
- ⚠️ Attempted GGUF loading (unsuccessful)
- Added Chroma-GGUF model support (now broken - awaiting fix)
- Removed non-working models
- Updated model descriptions

### v3.0
- Added FLUX.1-schnell support
- Multi-model comparison mode
- Cross-platform device detection

## 🤝 Contributing

This tool is being prepared for public release. Feedback and contributions welcome!

## 📄 License

MIT License - Free for personal and commercial use

## 🙏 Acknowledgments

- Black Forest Labs (FLUX.1-schnell)
- Stability AI (Stable Diffusion)
- HuggingFace (Model hosting & diffusers library)
- All model creators and the open-source AI community
