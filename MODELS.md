# Model Reference

> **⚠️ Important**: Model sizes represent BOTH download size AND active RAM/VRAM usage during generation. A 5.5GB model downloads 5.5GB and uses ~5.5GB RAM while running. Ensure you have sufficient free memory before generating.

## Available Models

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

---

## Model Comparison Table

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

---

## Memory Optimization Tips

1. Use **SD 1.5** models (1, 3-5) for systems with <16GB RAM
2. Use **Playground v2.5** (Model 6) for mid-range systems with 16GB+ RAM
3. Close other applications before generating
4. Use smaller base resolutions (512-1024) for faster generation
5. ⚠️ Avoid Model 8 (Chroma-GGUF) - currently broken

## Best Quality Tips

1. Use **FLUX.1-schnell** (Model 2) for maximum detail
2. Write detailed prompts (FLUX supports 512 tokens!)
3. Use higher base resolutions (1536-2048) for large prints
4. Experiment with different models - each has unique strengths
