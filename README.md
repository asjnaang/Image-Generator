# 🎨 AI Image Generator v4.0

## **100% FREE • FULLY OFFLINE • NO PAID APIs • BATCH GENERATION • MULTI-MODEL COMPARISON**

A powerful, professional-grade image generation tool that runs **completely offline** on your own hardware. Generate unlimited images with **zero costs**, no paid subscriptions, no per-image charges, and complete privacy.

> **⚠️ Setup Note**: Requires free HuggingFace account for model downloads. No ongoing API costs or per-image charges.

---

## 📚 Documentation

- **[Installation Guide](INSTALLATION.md)** - System requirements, dependencies, and setup
- **[Models & Comparison](MODELS_AND_COMPARISON.md)** - Complete model reference with visual quality comparisons
- **[Usage Guide](USAGE.md)** - How to use the tool, examples, and tips
- **[Troubleshooting](TROUBLESHOOTING.md)** - Common issues and solutions

---

## 🚀 Quick Start

```bash
# Simple generation (uses simple_prompts.json)
python generate_images.py simple_prompts.json output/

# With custom aspect ratios (uses sample_poster_prompts.json)
python generate_images.py sample_poster_prompts.json output/

# Compare multiple models
python generate_images.py sample_poster_prompts.json output/ multi
```

**First time?** Check the [Installation Guide](INSTALLATION.md) for setup instructions.

**Example Files Included:**
- `simple_prompts.json` - 5 detailed prompts optimized for quality (sunset, forest, ocean, city, flowers)
- `sample_poster_prompts.json` - Same 5 prompts with custom aspect ratios (square, portrait, landscape, portrait wide, cinematic)

Both files use detailed, descriptive prompts (~77 tokens) for better image quality.

---

## ✨ Key Features

### 💰 **Completely Free**
- No paid API services - runs 100% locally
- Zero per-image costs
- No rate limits
- All models are open-source

### 🔒 **Total Privacy**
- Works completely offline after model download
- Your prompts never leave your computer
- No data collection or tracking

### 🎨 **7 Working AI Models**
From lightweight (4GB) to ultra-quality (34GB). Each model specializes in different strengths - photorealism, artistic style, speed, or maximum quality. See [Models & Comparison](MODELS_AND_COMPARISON.md) for visual examples.

### 🚀 **Multi-Dimensional Generation**
This tool goes far beyond simple single-image generation:
- **One idea → Multiple variations**: Express concepts through different prompt perspectives
- **Batch everything**: Process multiple ideas × multiple prompts × multiple models × multiple aspect ratios - all in one execution
- **Compare models instantly**: Run the same prompts through all 7 models simultaneously to find the perfect match

### 📐 **Custom Aspect Ratios**
Square, Portrait, Landscape, Cinematic, and more. Per-image resolution control via JSON.

### ⚡ **Maximum Efficiency**
No sequential processing - everything runs in parallel. Generate dozens of variations while you grab coffee.

---

## 🎯 What Makes This Special?

### vs. Cloud Services

| Feature | This Tool | MidJourney | DALL-E 3 |
|---------|-----------|------------|----------|
| **Cost** | FREE | $10-60/mo | $0.04/img |
| **Privacy** | 100% Private | Public | Stored |
| **Offline** | ✅ Yes | ❌ No | ❌ No |
| **Batch Mode** | ✅ Unlimited | ❌ Limited | ❌ No |
| **Multi-Model** | ✅ 7 models | ❌ 1 model | ❌ 1 model |

### Use Cases
- **Content Creators**: Unlimited thumbnails, banners, social media graphics
- **Designers**: Mockups, concepts, and variations without stock photo costs
- **Developers**: App icons, food images, UI elements for projects
- **Marketers**: Product visuals, ads, promotional materials at zero cost

---

## 📁 Project Structure

```
docs/images/
├── generate_images.py              # Main script
├── README.md                       # This file (overview)
├── INSTALLATION.md                 # Setup guide
├── MODELS.md                       # Model reference
├── USAGE.md                        # Usage examples
├── TROUBLESHOOTING.md              # Common issues
├── simple_prompts.json             # Simple example (5 basic prompts)
├── sample_poster_prompts.json      # Advanced example (custom aspect ratios)
└── assets/[output folders]/        # Generated images
```

---

## 🔄 Version History

### v4.0 (Current) - MPS Fix & Documentation Restructure
- ✅ **Fixed MPS NaN issue** - Changed to float32 on Apple Silicon to prevent black images
- ✅ **Removed unnecessary defensive logic** - Cleaner, simpler code
- ✅ **Fixed safety_checker warnings** - Proper None assignment
- ✨ Added custom aspect ratio control (6 presets)
- ✨ Per-prompt resolution control via JSON
- ✨ Three resolution modes (JSON, Override, Default)
- 📝 Split documentation into focused files (INSTALLATION, MODELS, USAGE, TROUBLESHOOTING)
- ⚠️ Marked Chroma-GGUF (Model 8) as broken due to GGUF loader incompatibility

### v3.1
- ⚠️ Attempted GGUF loading (unsuccessful)
- Added Chroma-GGUF model support (now broken - awaiting fix)

### v3.0
- Added FLUX.1-schnell support
- Multi-model comparison mode
- Cross-platform device detection

---

## 🤝 Contributing

**Found a better model?** We welcome improvements! See our **[Models & Comparison Guide](MODELS_AND_COMPARISON.md#-contribute--improve)** for:
- How to test new models with `sample_poster_prompts.json`
- PR requirements (code, outputs, metrics, documentation)
- Performance benchmarking guidelines

Help the community discover better models for image generation! 🎨

---

## 📄 License

MIT License - Free for personal and commercial use

## 🙏 Acknowledgments

- Black Forest Labs (FLUX.1-schnell)
- Stability AI (Stable Diffusion)
- HuggingFace (Model hosting & diffusers library)
- All model creators and the open-source AI community
