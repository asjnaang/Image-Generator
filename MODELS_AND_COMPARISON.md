# 🎨 Models & Visual Comparison

> **Complete model reference with visual quality comparisons**
> Generated on Apple Silicon M1 Pro (32GB RAM) using MPS acceleration

---

## 📌 About This Guide

This guide showcases how different AI models perform across various **real-world prompts** - scenarios you'd actually want to generate (sunsets, landscapes, nature, cityscapes, etc.).

**Important**: Some models excel at **photorealistic reproduction** while others are designed for **artistic interpretation, stylization, and imaginative concepts**. The model that works best depends entirely on your prompt category and creative intent.

### 🚀 What This Tool Enables

This image generation tool goes far beyond simple single-image generation:

- **📝 Multi-Prompt Processing**: Express a single idea through multiple prompts, each addressing different aspects and perspectives
- **⚡ Batch Generation**: Process all variations simultaneously, not sequentially - massive time savings
- **🎯 Multi-Concept Support**: Not limited to one idea - generate multiple concepts with multiple variations in one run
- **📐 Multi-Resolution Output**: Generate the same prompt in different sizes and aspect ratios (square, portrait, landscape, cinematic) simultaneously
- **🎨 Multi-Model Comparison**: Run your prompts through multiple AI models at once to compare outputs and choose the best result

**In short**: One execution can generate multiple ideas → each with multiple prompt variations → across multiple models → in multiple aspect ratios. Complete creative flexibility with maximum efficiency.

---

## 📋 Available Models

> **⚠️ Important**: Model sizes represent BOTH download size AND active RAM/VRAM usage during generation. A 5.5GB model downloads 5.5GB and uses ~5.5GB RAM while running.

### Model 1: Stable Diffusion v1.5
- **Size**: 5.5GB (download + active RAM usage)
- **Access**: Open (no license acceptance needed)
- **Resolution**: 512-768px
- **Speed**: ⚡⚡⚡⚡⚡ (~30s on M1 Pro)
- **Best For**: Quick testing, prototyping, low memory systems
- **Quality**: ⭐⭐⭐ Good baseline

### Model 2: FLUX.1-schnell ⭐ HIGHEST QUALITY
- **Size**: 33.7GB (download + active RAM usage)
- **Access**: Open (no license acceptance needed)
- **Resolution**: 512-2048px
- **Speed**: 🐢 (~7-8 min per image on M1 Pro)
- **Features**: 512 token prompts, exceptional detail, 4 diffusion steps
- **Best For**: Absolute best quality, production finals
- **Quality**: ⭐⭐⭐⭐⭐ Unmatched detail
- **RAM Requirement**: ~24GB free RAM/VRAM during generation

### Model 3: Realistic Vision v5.1 ⭐ BEST SPEED/QUALITY
- **Size**: 4.3GB (download + RAM usage)
- **Access**: Open (no license needed)
- **Resolution**: 512-768px
- **Speed**: ⚡⚡⚡ (~1m 20s on M1 Pro)
- **Best For**: Photorealistic images, food photography, nature
- **Quality**: ⭐⭐⭐⭐⭐ Excellent photorealism

### Model 4: DreamShaper v8
- **Size**: 5.5GB (download + RAM usage)
- **Access**: Open (no license needed)
- **Resolution**: 512-768px
- **Speed**: ⚡⚡⚡ (~1m 20s on M1 Pro)
- **Best For**: Versatile, handles artistic and realistic prompts
- **Quality**: ⭐⭐⭐⭐ Very good all-rounder

### Model 5: Counterfeit v2.5
- **Size**: 4.3GB (download + RAM usage)
- **Access**: Open (no license needed)
- **Resolution**: 512-768px
- **Speed**: ⚡⚡⚡ (~1m 15s on M1 Pro)
- **Best For**: Fine details, faces, textures
- **Quality**: ⭐⭐⭐⭐ Excellent for details

### Model 6: Playground v2.5
- **Size**: 13.9GB (download + RAM usage)
- **Access**: Open (no license needed)
- **Resolution**: 512-1536px
- **Speed**: ⚡⚡ (~2-3 min on M1 Pro)
- **Best For**: Beautiful aesthetics, artistic images
- **Quality**: ⭐⭐⭐⭐ Gorgeous compositions
- **RAM Requirement**: ~12GB free RAM/VRAM

### Model 7: SDXL Base 1.0
- **Size**: 14.2GB (download + RAM usage)
- **Access**: Open (no license needed)
- **Resolution**: 512-1536px
- **Speed**: ⚡⚡ (~2-3 min on M1 Pro)
- **Best For**: High resolution, detailed images
- **Quality**: ⭐⭐⭐⭐ Excellent for high-res
- **RAM Requirement**: ~12GB free RAM/VRAM

### Model 8: Chroma-GGUF ⚠️ CURRENTLY BROKEN
- **Size**: 7.1GB (quantized)
- **Status**: ⚠️ **BROKEN** - GGUF loader incompatibility
- **Error**: `KeyError: 'time_in.in_layer.weight'`
- **Note**: Kept for future retrying when diffusers updates GGUF support
- **Alternative**: Use Model 2 (FLUX.1-schnell) for best quality

---

## 🎯 Quick Model Selection

> **Understanding Trade-offs**: No single model is "best" - each balances speed, quality, and specialization differently. Choose based on your specific needs.

| Your Need | Recommended Model | Why |
|-----------|------------------|-----|
| **Fastest results** | SD v1.5 | ~30s per image, great for testing |
| **Best quality/speed balance** | Realistic Vision v5.1 | Excellent photorealism in ~1m 20s |
| **Absolute best quality** | FLUX.1-schnell | Unmatched detail, ~7-8 min |
| **Photorealistic images** | Realistic Vision v5.1 or Counterfeit | Natural photos, food, nature |
| **Artistic/Stylized** | DreamShaper or Playground | Versatile aesthetics |
| **High resolution** | SDXL Base or FLUX | Best for large prints |
| **Low memory (<16GB)** | SD v1.5, Counterfeit, Realistic Vision, DreamShaper | 4-6GB models |

### Speed Tiers

| Speed Tier | Models | Generation Time | When to Use |
|------------|--------|----------------|-------------|
| ⚡ **Fast** | SD v1.5, Counterfeit, Realistic Vision, DreamShaper | ~30s - 1m 20s | Quick iterations, testing, most daily work |
| 🚀 **Moderate** | SDXL Base, Playground v2.5 | ~2-3 min | High quality needed, moderate time OK |
| 🐢 **Slow** | FLUX.1-schnell | ~7-8 min | Absolute best quality, production finals |

---

## 💾 Memory Requirements

| RAM Available | Recommended Models | Notes |
|--------------|-------------------|-------|
| **<16GB** | SD v1.5, Counterfeit, Realistic Vision, DreamShaper | Use 4-6GB models only |
| **16-32GB** | All except FLUX | Can run most models comfortably |
| **32GB+** | All models including FLUX | Full access to all options |

### Memory Optimization Tips

1. **Close other applications** before generating
2. **Use lower resolutions** (512-1024) for faster generation and less memory
3. **Start with smaller models** (SD v1.5) to test prompts
4. ⚠️ **Avoid Model 8** (Chroma-GGUF) - currently broken

---

## 🖼️ Visual Comparisons

> 💡 **Tip:** Click on any image to view it in full size!

### 1️⃣ Sunset Mountain (Square 1024×1024)

<table>
<tr>
<td width="33%" align="center">

**FLUX.1-schnell**
<a href="assets/flux-schnell/sunset_mountain_square.png"><img src="assets/flux-schnell/sunset_mountain_square.png" width="280"/></a>
*Highest quality, 4-step generation*

</td>
<td width="33%" align="center">

**Realistic Vision v5.1**
<a href="assets/realistic-vision-v5.1/sunset_mountain_square.png"><img src="assets/realistic-vision-v5.1/sunset_mountain_square.png" width="280"/></a>
*Photorealistic output*

</td>
<td width="33%" align="center">

**DreamShaper v8**
<a href="assets/dreamshaper-v8/sunset_mountain_square.png"><img src="assets/dreamshaper-v8/sunset_mountain_square.png" width="280"/></a>
*Artistic versatility*

</td>
</tr>
<tr>
<td width="33%" align="center">

**Counterfeit v2.5**
<a href="assets/counterfeit-v2.5/sunset_mountain_square.png"><img src="assets/counterfeit-v2.5/sunset_mountain_square.png" width="280"/></a>
*Fine photorealistic details*

</td>
<td width="33%" align="center">

**Playground v2.5**
<a href="assets/playground-v2.5/sunset_mountain_square.png"><img src="assets/playground-v2.5/sunset_mountain_square.png" width="280"/></a>
*Aesthetic-focused*

</td>
<td width="33%" align="center">

**SDXL Base 1.0**
<a href="assets/sdxl-base-1.0/sunset_mountain_square.png"><img src="assets/sdxl-base-1.0/sunset_mountain_square.png" width="280"/></a>
*High-quality SDXL*

</td>
</tr>
<tr>
<td colspan="3" align="center">

**SD v1.5**
<a href="assets/sd-v1.5/sunset_mountain_square.png"><img src="assets/sd-v1.5/sunset_mountain_square.png" width="280"/></a>
*Fast baseline model*

</td>
</tr>
</table>

---

### 2️⃣ Forest Path (Portrait 680×1024)

<table>
<tr>
<td width="33%" align="center">

**FLUX.1-schnell**
<a href="assets/flux-schnell/forest_path_portrait.png"><img src="assets/flux-schnell/forest_path_portrait.png" width="180"/></a>

</td>
<td width="33%" align="center">

**Realistic Vision v5.1**
<a href="assets/realistic-vision-v5.1/forest_path_portrait.png"><img src="assets/realistic-vision-v5.1/forest_path_portrait.png" width="180"/></a>

</td>
<td width="33%" align="center">

**DreamShaper v8**
<a href="assets/dreamshaper-v8/forest_path_portrait.png"><img src="assets/dreamshaper-v8/forest_path_portrait.png" width="180"/></a>

</td>
</tr>
<tr>
<td width="33%" align="center">

**Counterfeit v2.5**
<a href="assets/counterfeit-v2.5/forest_path_portrait.png"><img src="assets/counterfeit-v2.5/forest_path_portrait.png" width="180"/></a>

</td>
<td width="33%" align="center">

**Playground v2.5**
<a href="assets/playground-v2.5/forest_path_portrait.png"><img src="assets/playground-v2.5/forest_path_portrait.png" width="180"/></a>

</td>
<td width="33%" align="center">

**SDXL Base 1.0**
<a href="assets/sdxl-base-1.0/forest_path_portrait.png"><img src="assets/sdxl-base-1.0/forest_path_portrait.png" width="180"/></a>

</td>
</tr>
<tr>
<td colspan="3" align="center">

**SD v1.5**
<a href="assets/sd-v1.5/forest_path_portrait.png"><img src="assets/sd-v1.5/forest_path_portrait.png" width="180"/></a>

</td>
</tr>
</table>

---

### 3️⃣ Ocean Waves (Landscape 1536×1024)

<table>
<tr>
<td width="33%" align="center">

**FLUX.1-schnell**
<a href="assets/flux-schnell/ocean_waves_landscape.png"><img src="assets/flux-schnell/ocean_waves_landscape.png" width="280"/></a>

</td>
<td width="33%" align="center">

**Realistic Vision v5.1**
<a href="assets/realistic-vision-v5.1/ocean_waves_landscape.png"><img src="assets/realistic-vision-v5.1/ocean_waves_landscape.png" width="280"/></a>

</td>
<td width="33%" align="center">

**DreamShaper v8**
<a href="assets/dreamshaper-v8/ocean_waves_landscape.png"><img src="assets/dreamshaper-v8/ocean_waves_landscape.png" width="280"/></a>

</td>
</tr>
<tr>
<td width="33%" align="center">

**Counterfeit v2.5**
<a href="assets/counterfeit-v2.5/ocean_waves_landscape.png"><img src="assets/counterfeit-v2.5/ocean_waves_landscape.png" width="280"/></a>

</td>
<td width="33%" align="center">

**Playground v2.5**
<a href="assets/playground-v2.5/ocean_waves_landscape.png"><img src="assets/playground-v2.5/ocean_waves_landscape.png" width="280"/></a>

</td>
<td width="33%" align="center">

**SDXL Base 1.0**
<a href="assets/sdxl-base-1.0/ocean_waves_landscape.png"><img src="assets/sdxl-base-1.0/ocean_waves_landscape.png" width="280"/></a>

</td>
</tr>
<tr>
<td colspan="3" align="center">

**SD v1.5**
<a href="assets/sd-v1.5/ocean_waves_landscape.png"><img src="assets/sd-v1.5/ocean_waves_landscape.png" width="280"/></a>

</td>
</tr>
</table>

---

### 4️⃣ City Skyline (Portrait Wide 768×1024)

<table>
<tr>
<td width="33%" align="center">

**FLUX.1-schnell**
<a href="assets/flux-schnell/city_skyline_portrait_wide.png"><img src="assets/flux-schnell/city_skyline_portrait_wide.png" width="200"/></a>

</td>
<td width="33%" align="center">

**Realistic Vision v5.1**
<a href="assets/realistic-vision-v5.1/city_skyline_portrait_wide.png"><img src="assets/realistic-vision-v5.1/city_skyline_portrait_wide.png" width="200"/></a>

</td>
<td width="33%" align="center">

**DreamShaper v8**
<a href="assets/dreamshaper-v8/city_skyline_portrait_wide.png"><img src="assets/dreamshaper-v8/city_skyline_portrait_wide.png" width="200"/></a>

</td>
</tr>
<tr>
<td width="33%" align="center">

**Counterfeit v2.5**
<a href="assets/counterfeit-v2.5/city_skyline_portrait_wide.png"><img src="assets/counterfeit-v2.5/city_skyline_portrait_wide.png" width="200"/></a>

</td>
<td width="33%" align="center">

**Playground v2.5**
<a href="assets/playground-v2.5/city_skyline_portrait_wide.png"><img src="assets/playground-v2.5/city_skyline_portrait_wide.png" width="200"/></a>

</td>
<td width="33%" align="center">

**SDXL Base 1.0**
<a href="assets/sdxl-base-1.0/city_skyline_portrait_wide.png"><img src="assets/sdxl-base-1.0/city_skyline_portrait_wide.png" width="200"/></a>

</td>
</tr>
<tr>
<td colspan="3" align="center">

**SD v1.5**
<a href="assets/sd-v1.5/city_skyline_portrait_wide.png"><img src="assets/sd-v1.5/city_skyline_portrait_wide.png" width="200"/></a>

</td>
</tr>
</table>

---

### 5️⃣ Flower Garden (Cinematic 1536×656)

<table>
<tr>
<td width="33%" align="center">

**FLUX.1-schnell**
<a href="assets/flux-schnell/flower_garden_cinematic.png"><img src="assets/flux-schnell/flower_garden_cinematic.png" width="280"/></a>

</td>
<td width="33%" align="center">

**Realistic Vision v5.1**
<a href="assets/realistic-vision-v5.1/flower_garden_cinematic.png"><img src="assets/realistic-vision-v5.1/flower_garden_cinematic.png" width="280"/></a>

</td>
<td width="33%" align="center">

**DreamShaper v8**
<a href="assets/dreamshaper-v8/flower_garden_cinematic.png"><img src="assets/dreamshaper-v8/flower_garden_cinematic.png" width="280"/></a>

</td>
</tr>
<tr>
<td width="33%" align="center">

**Counterfeit v2.5**
<a href="assets/counterfeit-v2.5/flower_garden_cinematic.png"><img src="assets/counterfeit-v2.5/flower_garden_cinematic.png" width="280"/></a>

</td>
<td width="33%" align="center">

**Playground v2.5**
<a href="assets/playground-v2.5/flower_garden_cinematic.png"><img src="assets/playground-v2.5/flower_garden_cinematic.png" width="280"/></a>

</td>
<td width="33%" align="center">

**SDXL Base 1.0**
<a href="assets/sdxl-base-1.0/flower_garden_cinematic.png"><img src="assets/sdxl-base-1.0/flower_garden_cinematic.png" width="280"/></a>

</td>
</tr>
<tr>
<td colspan="3" align="center">

**SD v1.5**
<a href="assets/sd-v1.5/flower_garden_cinematic.png"><img src="assets/sd-v1.5/flower_garden_cinematic.png" width="280"/></a>

</td>
</tr>
</table>

---

## 📊 Detailed Performance Analysis

*All timings from Apple M1 Pro 32GB with ~20GB free RAM. Times vary with prompt complexity and system load.*

### Performance by Resolution

| Model | 768×768 | 1536×1024 | 1536×656 | Average | Notes |
|-------|---------|-----------|----------|---------|-------|
| **SD v1.5** | ~30s | ~45s | ~35s | **~37s** | Consistent speed across resolutions |
| **Counterfeit v2.5** | ~1m 16s | ~1m 3s | ~1m 2s | **~1m 14s** | Optimized for mid-res |
| **Realistic Vision v5.1** | ~2m 0s | ~1m 3s | ~1m 2s | **~1m 22s** | Faster at higher res |
| **DreamShaper v8** | ~2m 0s | ~1m 4s | ~1m 4s | **~1m 23s** | Stable performance |
| **Playground v2.5** | ~2m 0s | ~3m 0s | ~2m 30s | **~2m 30s** | Scales with resolution |
| **SDXL Base 1.0** | ~2m 24s | ~3m 45s | ~2m 18s | **~2m 49s** | Higher res = slower |
| **FLUX.1-schnell** | ~5m 40s | ~7m 45s | ~7m 56s | **~7m 7s** | Quality over speed |

### Model Characteristics Summary

| Model | Strength | Speed | Memory | Best Use Case |
|-------|----------|-------|--------|---------------|
| **SD v1.5** | Fast iterations | ~30s | 5.5GB | Quick tests, prototyping |
| **Counterfeit v2.5** | Fine details | ~1m 15s | 4.3GB | Detailed faces, textures |
| **Realistic Vision v5.1** | Photorealism | ~1m 20s | 4.3GB | Food, nature, photos |
| **DreamShaper v8** | Versatility | ~1m 20s | 5.5GB | Mixed artistic/realistic |
| **Playground v2.5** | Aesthetics | ~2m 30s | 13.9GB | Beautiful compositions |
| **SDXL Base 1.0** | High resolution | ~2m 50s | 14.2GB | Large prints, detailed |
| **FLUX.1-schnell** | Maximum quality | ~7-8m | 33.7GB | Absolute best output |

---

## 🔧 How to Generate Your Own

### Single Model
```bash
python generate_images.py prompts.json output/
# Select model based on your needs (see guide above)
# Resolution mode: 1 (JSON-defined)
```

### Multi-Model Comparison
```bash
python generate_images.py prompts.json output/ multi
# Select models: 1,2,3,4,5,6,7 (test all models)
# Resolution mode: 1 (JSON-defined)
# Output: separate folders for each model
```

### Sample JSON Format
```json
{
  "sunset_mountain": {
    "prompt": "A breathtaking sunset over majestic snow-capped mountains, vibrant orange and pink sky with wispy clouds, dramatic lighting, golden hour glow, serene alpine landscape, professional nature photography, high detail, 8k quality, stunning vista",
    "aspect_ratio": "square",
    "base_resolution": 1024
  },
  "ocean_waves": {
    "prompt": "Powerful ocean waves crashing on pristine sandy beach at golden hour, dramatic sea spray, warm sunset lighting, turquoise water, foam and texture, coastal seascape, dynamic motion, professional seascape photography, vivid colors, high detail",
    "aspect_ratio": "landscape",
    "base_resolution": 1536
  }
}
```

### Supported Aspect Ratios

| Name | Ratio | Example Resolution | Best For |
|------|-------|-------------------|----------|
| `square` | 1:1 | 1024×1024 | Icons, thumbnails, Instagram |
| `portrait` | 2:3 | 683×1024 | Posters, phone wallpapers |
| `portrait_wide` | 3:4 | 768×1024 | Standard photo prints |
| `landscape` | 3:2 | 1536×1024 | Desktop wallpapers |
| `landscape_wide` | 16:9 | 1820×1024 | YouTube thumbnails |
| `cinematic` | 21:9 | 1536×656 | Ultra-wide banners |

---

## 🤝 Contribute & Improve

**Found a better model?** We welcome contributions! If you discover a model that:
- Produces better quality than our current options
- Offers superior performance (speed/quality balance)
- Works well with the `sample_poster_prompts.json` test set

**Please submit a PR with:**
1. Model configuration added to `generate_images.py`
2. Test results using `sample_poster_prompts.json`
3. Output images in `assets/your-model-name/`
4. Performance metrics (timing on your hardware)
5. Updated comparison in this file

Your contributions help everyone find the best models for their needs! 🎨

---

*Generated with ❤️ using HuggingFace Diffusers on Apple Silicon*
