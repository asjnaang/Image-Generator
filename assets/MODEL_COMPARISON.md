# 🎨 AI Image Generation Model Comparison

> **Visual quality comparison across 7 different AI models**
> Generated on Apple Silicon M1 Pro (32GB RAM) using MPS acceleration

---

## 📌 About This Comparison

This comparison showcases how different AI models perform across various **real-world prompts** - scenarios you'd actually want to generate (sunsets, landscapes, nature, cityscapes, etc.).

However, it's important to understand that some models excel at **photorealistic reproduction** while others are specifically designed for **artistic interpretation, stylization, and imaginative concepts**. The model that works best depends entirely on your prompt category and creative intent.

### 🚀 What This Script Enables

This image generation tool goes far beyond simple single-image generation:

- **📝 Multi-Prompt Processing**: Express a single idea through multiple prompts, each addressing different aspects and perspectives
- **⚡ Batch Generation**: Process all variations simultaneously, not sequentially - massive time savings
- **🎯 Multi-Concept Support**: Not limited to one idea - generate multiple concepts with multiple variations in one run
- **📐 Multi-Resolution Output**: Generate the same prompt in different sizes and aspect ratios (square, portrait, landscape, cinematic) simultaneously
- **🎨 Multi-Model Comparison**: Run your prompts through multiple AI models at once to compare outputs and choose the best result

**In short**: One execution can generate multiple ideas → each with multiple prompt variations → across multiple models → in multiple aspect ratios. Complete creative flexibility with maximum efficiency.

---

## 📊 Model Overview

| Model | Size | Speed (M1 Pro) | Steps | Resolution | Quality | Use Case |
|-------|------|----------------|-------|------------|---------|----------|
| **SD v1.5** | 5.5GB | ⚡⚡⚡ Fastest (~30s) | 40 | Up to 768px | ⭐⭐⭐ | Quick tests, prototyping |
| **Counterfeit v2.5** | 4.3GB | ⚡⚡ Fast (~1m 16s) | 40 | Up to 768px | ⭐⭐⭐⭐ | Photorealistic details |
| **Realistic Vision v5.1** | 4.3GB | ⚡⚡ Fast (~1m 17s) | 40 | Up to 768px | ⭐⭐⭐⭐⭐ | Best photorealism |
| **DreamShaper v8** | 5.5GB | ⚡⚡ Fast (~1m 17s) | 40 | Up to 768px | ⭐⭐⭐⭐ | Versatile, artistic |
| **SDXL Base 1.0** | 14.2GB | 🚀 Moderate (~2-3m) | 30 | Up to 1536px | ⭐⭐⭐⭐ | High-res quality |
| **Playground v2.5** | 13.9GB | 🚀 Moderate (~2-3m) | 30 | Up to 1536px | ⭐⭐⭐⭐ | Beautiful aesthetics |
| **FLUX.1-schnell** | 33.7GB | 🐢 Slow (~7-8m) | 4 | Up to 2048px | ⭐⭐⭐⭐⭐ | Highest quality |

---

## 🖼️ Image Comparisons

> 💡 **Tip:** Click on any image to view it in full size!

### 1️⃣ Sunset Mountain (Square 1024×1024)

<table>
<tr>
<td width="33%" align="center">

**FLUX.1-schnell**
<a href="flux-schnell/sunset_mountain_square.png"><img src="flux-schnell/sunset_mountain_square.png" width="280"/></a>
*Highest quality, 4-step generation*

</td>
<td width="33%" align="center">

**Realistic Vision v5.1**
<a href="realistic-vision-v5.1/sunset_mountain_square.png"><img src="realistic-vision-v5.1/sunset_mountain_square.png" width="280"/></a>
*Photorealistic output*

</td>
<td width="33%" align="center">

**DreamShaper v8**
<a href="dreamshaper-v8/sunset_mountain_square.png"><img src="dreamshaper-v8/sunset_mountain_square.png" width="280"/></a>
*Artistic versatility*

</td>
</tr>
<tr>
<td width="33%" align="center">

**Counterfeit v2.5**
<a href="counterfeit-v2.5/sunset_mountain_square.png"><img src="counterfeit-v2.5/sunset_mountain_square.png" width="280"/></a>
*Fine photorealistic details*

</td>
<td width="33%" align="center">

**Playground v2.5**
<a href="playground-v2.5/sunset_mountain_square.png"><img src="playground-v2.5/sunset_mountain_square.png" width="280"/></a>
*Aesthetic-focused*

</td>
<td width="33%" align="center">

**SDXL Base 1.0**
<a href="sdxl-base-1.0/sunset_mountain_square.png"><img src="sdxl-base-1.0/sunset_mountain_square.png" width="280"/></a>
*High-quality SDXL*

</td>
</tr>
<tr>
<td colspan="3" align="center">

**SD v1.5**
<a href="sd-v1.5/sunset_mountain_square.png"><img src="sd-v1.5/sunset_mountain_square.png" width="280"/></a>
*Fast baseline model*

</td>
</tr>
</table>

**Prompt:** *"A breathtaking sunset over majestic snow-capped mountains, vibrant orange and pink sky..."*

---

### 2️⃣ Forest Path (Portrait 680×1024)

<table>
<tr>
<td width="33%" align="center">

**FLUX.1-schnell**
<a href="flux-schnell/forest_path_portrait.png"><img src="flux-schnell/forest_path_portrait.png" width="240"/></a>
*Superior detail & lighting*

</td>
<td width="33%" align="center">

**Realistic Vision v5.1**
<a href="realistic-vision-v5.1/forest_path_portrait.png"><img src="realistic-vision-v5.1/forest_path_portrait.png" width="240"/></a>
*Natural photorealism*

</td>
<td width="33%" align="center">

**DreamShaper v8**
<a href="dreamshaper-v8/forest_path_portrait.png"><img src="dreamshaper-v8/forest_path_portrait.png" width="240"/></a>
*Balanced quality*

</td>
</tr>
<tr>
<td width="33%" align="center">

**Counterfeit v2.5**
<a href="counterfeit-v2.5/forest_path_portrait.png"><img src="counterfeit-v2.5/forest_path_portrait.png" width="240"/></a>
*Detailed textures*

</td>
<td width="33%" align="center">

**Playground v2.5**
<a href="playground-v2.5/forest_path_portrait.png"><img src="playground-v2.5/forest_path_portrait.png" width="240"/></a>
*Artistic interpretation*

</td>
<td width="33%" align="center">

**SDXL Base 1.0**
<a href="sdxl-base-1.0/forest_path_portrait.png"><img src="sdxl-base-1.0/forest_path_portrait.png" width="240"/></a>
*Clean rendering*

</td>
</tr>
<tr>
<td colspan="3" align="center">

**SD v1.5**
<a href="sd-v1.5/forest_path_portrait.png"><img src="sd-v1.5/forest_path_portrait.png" width="240"/></a>
*Lightweight generation*

</td>
</tr>
</table>

**Prompt:** *"A peaceful winding forest path through tall ancient trees, dappled sunlight filtering through canopy..."*

---

### 3️⃣ Ocean Waves (Landscape 1536×1024)

<table>
<tr>
<td width="33%" align="center">

**FLUX.1-schnell**
<a href="flux-schnell/ocean_waves_landscape.png"><img src="flux-schnell/ocean_waves_landscape.png" width="320"/></a>
*Dynamic motion & detail*

</td>
<td width="33%" align="center">

**Realistic Vision v5.1**
<a href="realistic-vision-v5.1/ocean_waves_landscape.png"><img src="realistic-vision-v5.1/ocean_waves_landscape.png" width="320"/></a>
*Photographic quality*

</td>
<td width="33%" align="center">

**DreamShaper v8**
<a href="dreamshaper-v8/ocean_waves_landscape.png"><img src="dreamshaper-v8/ocean_waves_landscape.png" width="320"/></a>
*Artistic waves*

</td>
</tr>
<tr>
<td width="33%" align="center">

**Counterfeit v2.5**
<a href="counterfeit-v2.5/ocean_waves_landscape.png"><img src="counterfeit-v2.5/ocean_waves_landscape.png" width="320"/></a>
*Rich water details*

</td>
<td width="33%" align="center">

**Playground v2.5**
<a href="playground-v2.5/ocean_waves_landscape.png"><img src="playground-v2.5/ocean_waves_landscape.png" width="320"/></a>
*Painterly aesthetic*

</td>
<td width="33%" align="center">

**SDXL Base 1.0**
<a href="sdxl-base-1.0/ocean_waves_landscape.png"><img src="sdxl-base-1.0/ocean_waves_landscape.png" width="320"/></a>
*Photorealistic approach*

</td>
</tr>
<tr>
<td colspan="3" align="center">

**SD v1.5**
<a href="sd-v1.5/ocean_waves_landscape.png"><img src="sd-v1.5/ocean_waves_landscape.png" width="320"/></a>
*Fast generation*

</td>
</tr>
</table>

**Prompt:** *"Powerful ocean waves crashing on pristine sandy beach at golden hour, dramatic sea spray..."*

---

### 4️⃣ City Skyline (Portrait Wide 768×1024)

<table>
<tr>
<td width="33%" align="center">

**FLUX.1-schnell**
<a href="flux-schnell/city_skyline_portrait_wide.png"><img src="flux-schnell/city_skyline_portrait_wide.png" width="260"/></a>
*Sharp architectural details*

</td>
<td width="33%" align="center">

**Realistic Vision v5.1**
<a href="realistic-vision-v5.1/city_skyline_portrait_wide.png"><img src="realistic-vision-v5.1/city_skyline_portrait_wide.png" width="260"/></a>
*Realistic night scene*

</td>
<td width="33%" align="center">

**DreamShaper v8**
<a href="dreamshaper-v8/city_skyline_portrait_wide.png"><img src="dreamshaper-v8/city_skyline_portrait_wide.png" width="260"/></a>
*Atmospheric rendering*

</td>
</tr>
<tr>
<td width="33%" align="center">

**Counterfeit v2.5**
<a href="counterfeit-v2.5/city_skyline_portrait_wide.png"><img src="counterfeit-v2.5/city_skyline_portrait_wide.png" width="260"/></a>
*Urban detail mastery*

</td>
<td width="33%" align="center">

**Playground v2.5**
<a href="playground-v2.5/city_skyline_portrait_wide.png"><img src="playground-v2.5/city_skyline_portrait_wide.png" width="260"/></a>
*Enhanced atmosphere*

</td>
<td width="33%" align="center">

**SDXL Base 1.0**
<a href="sdxl-base-1.0/city_skyline_portrait_wide.png"><img src="sdxl-base-1.0/city_skyline_portrait_wide.png" width="260"/></a>
*Modern architecture*

</td>
</tr>
<tr>
<td colspan="3" align="center">

**SD v1.5**
<a href="sd-v1.5/city_skyline_portrait_wide.png"><img src="sd-v1.5/city_skyline_portrait_wide.png" width="260"/></a>
*Basic quality*

</td>
</tr>
</table>

**Prompt:** *"Modern metropolitan city skyline at night, illuminated glass skyscrapers reflecting in water..."*

---

### 5️⃣ Flower Garden (Cinematic 1536×656)

<table>
<tr>
<td width="33%" align="center">

**FLUX.1-schnell**
<a href="flux-schnell/flower_garden_cinematic.png"><img src="flux-schnell/flower_garden_cinematic.png" width="320"/></a>
*Vibrant colors, rich detail*

</td>
<td width="33%" align="center">

**Realistic Vision v5.1**
<a href="realistic-vision-v5.1/flower_garden_cinematic.png"><img src="realistic-vision-v5.1/flower_garden_cinematic.png" width="320"/></a>
*Natural flower details*

</td>
<td width="33%" align="center">

**DreamShaper v8**
<a href="dreamshaper-v8/flower_garden_cinematic.png"><img src="dreamshaper-v8/flower_garden_cinematic.png" width="320"/></a>
*Dreamy garden scene*

</td>
</tr>
<tr>
<td width="33%" align="center">

**Counterfeit v2.5**
<a href="counterfeit-v2.5/flower_garden_cinematic.png"><img src="counterfeit-v2.5/flower_garden_cinematic.png" width="320"/></a>
*Botanical accuracy*

</td>
<td width="33%" align="center">

**Playground v2.5**
<a href="playground-v2.5/flower_garden_cinematic.png"><img src="playground-v2.5/flower_garden_cinematic.png" width="320"/></a>
*Artistic color grading*

</td>
<td width="33%" align="center">

**SDXL Base 1.0**
<a href="sdxl-base-1.0/flower_garden_cinematic.png"><img src="sdxl-base-1.0/flower_garden_cinematic.png" width="320"/></a>
*Natural rendering*

</td>
</tr>
<tr>
<td colspan="3" align="center">

**SD v1.5**
<a href="sd-v1.5/flower_garden_cinematic.png"><img src="sd-v1.5/flower_garden_cinematic.png" width="320"/></a>
*Simplified detail*

</td>
</tr>
</table>

**Prompt:** *"Vibrant colorful flower garden in full bloom, red roses, yellow tulips, purple lavender..."*

---

## 🎯 Model Recommendations

### 🏆 **FLUX.1-schnell** - Highest Quality
- ✅ **Best quality** output with superior detail
- ✅ **512-token prompts** for detailed descriptions
- ✅ **Handles high resolutions** (up to 2048px)
- ✅ **Only 4 inference steps** (but slower per step)
- ⚠️ **Slowest model** (~7-8 min per image on M1 Pro)
- ⚠️ Requires 32GB+ RAM for large resolutions on Apple Silicon

### 📸 **Realistic Vision v5.1** - Best for Photorealism
- ✅ **Photorealistic output** - looks like real photos
- ✅ **Small size** (4.3GB) but excellent quality
- ✅ **Fast generation** (40 steps)
- ✅ **Perfect for food, nature, portraits**
- 🎯 **Recommended for:** Product photography, realistic scenes

### 🎨 **DreamShaper v8** - Versatile All-Rounder
- ✅ **Great balance** between artistic and realistic
- ✅ **Versatile** - handles many subjects well
- ✅ **Small footprint** (5.5GB)
- ✅ **Reliable quality** across different prompts
- 🎯 **Recommended for:** General purpose, varied subjects

### 🌟 **Counterfeit v2.5** - Photorealistic Details
- ✅ **Excellent detail** and texture work
- ✅ **Small size** (4.3GB)
- ✅ **Great for faces** and fine details
- ✅ **Fast generation**
- 🎯 **Recommended for:** Character art, detailed scenes

### 🎨 **Playground v2.5** - Beautiful Aesthetics
- ✅ **Gorgeous artistic** output
- ✅ **Great color grading**
- ✅ **Good resolution support** (up to 1536px)
- ⚠️ **Slower** (30 steps)
- 🎯 **Recommended for:** Artistic renders, aesthetic images

### ⚡ **SDXL Base 1.0** - Balanced Performance
- ✅ **High quality** SDXL architecture
- ✅ **Fast on Apple Silicon** with optimizations
- ✅ **Good resolution support**
- ✅ **Versatile** for various subjects
- 🎯 **Recommended for:** High-res needs, professional work

### 🚀 **SD v1.5** - Lightweight & Fast
- ✅ **Smallest size** (5.5GB)
- ✅ **Very fast** generation
- ✅ **Good for testing/prototyping**
- ⚠️ Lower quality compared to newer models
- 🎯 **Recommended for:** Quick tests, iterations

---

## ⚙️ Technical Details

### Memory Optimizations Applied

**FLUX.1-schnell on Apple Silicon (MPS):**
```python
pipe.enable_sequential_cpu_offload()  # Intelligent GPU/CPU model swapping
pipe.vae.enable_slicing()             # VAE memory optimization
pipe.vae.enable_tiling()              # Process in tiles
torch_dtype = torch.bfloat16          # Half precision (saves 50% memory)
```

**SD 1.5 / SDXL / Realistic Vision / DreamShaper / Counterfeit on MPS:**
```python
pipe.enable_attention_slicing()       # Attention memory optimization
pipe.enable_model_cpu_offload()       # CPU offloading
torch_dtype = torch.float32           # Full precision for stability
```

### Aspect Ratio Support

All models support custom aspect ratios:
- **Square** (1:1) - 1024×1024
- **Portrait** (2:3) - 680×1024
- **Portrait Wide** (3:4) - 768×1024
- **Landscape** (3:2) - 1536×1024
- **Landscape Wide** (16:9) - 1824×1024
- **Cinematic** (21:9) - 1536×656

---

## 📊 Performance & Characteristics

> **Understanding the Trade-offs**: No single model is "best" - each balances speed, quality, and specialization differently. Choose based on your specific needs.

| Model | Quality | Speed (M1 Pro) | Strength | Memory | Best Use Case |
|-------|---------|----------------|----------|--------|---------------|
| **SD v1.5** | ⭐⭐⭐ | ~30s | Fast iterations | 5.5GB | Quick tests, prototyping |
| **Counterfeit v2.5** | ⭐⭐⭐⭐ | ~1m 15s | Fine details | 4.3GB | Detailed faces, textures |
| **Realistic Vision v5.1** | ⭐⭐⭐⭐⭐ | ~1m 20s | Photorealism | 4.3GB | Food, nature, photos |
| **DreamShaper v8** | ⭐⭐⭐⭐ | ~1m 20s | Versatility | 5.5GB | Mixed artistic/realistic |
| **Playground v2.5** | ⭐⭐⭐⭐ | ~2m 30s | Aesthetics | 13.9GB | Beautiful compositions |
| **SDXL Base 1.0** | ⭐⭐⭐⭐ | ~2m 50s | High resolution | 14.2GB | Large prints, detailed |
| **FLUX.1-schnell** | ⭐⭐⭐⭐⭐ | ~7-8m | Maximum quality | 33.7GB | Absolute best output |

### 🎯 Detailed Performance by Resolution

| Model | 768×768 | 1536×1024 | 1536×656 | Notes |
|-------|---------|-----------|----------|-------|
| **SD v1.5** | ~30s | ~45s | ~35s | Consistent speed across resolutions |
| **Counterfeit v2.5** | ~1m 16s | ~1m 3s | ~1m 2s | Optimized for mid-res |
| **Realistic Vision v5.1** | ~2m 0s | ~1m 3s | ~1m 2s | Faster at higher res |
| **DreamShaper v8** | ~2m 0s | ~1m 4s | ~1m 4s | Stable performance |
| **Playground v2.5** | ~2m 0s | ~3m 0s | ~2m 30s | Scales with resolution |
| **SDXL Base 1.0** | ~2m 24s | ~3m 45s | ~2m 18s | Higher res = slower |
| **FLUX.1-schnell** | ~5m 40s | ~7m 45s | ~7m 56s | Quality over speed |

*Actual test results on M1 Pro 32GB. Times vary with prompt complexity.*

### 💡 Choosing the Right Model

- **Need speed?** → SD v1.5, Counterfeit, Realistic Vision (~30s - 1m 20s)
- **Need quality?** → FLUX, Realistic Vision (~7m, ~1m 20s respectively)
- **Balanced approach?** → DreamShaper, SDXL, Playground (~1m 20s - 3m)
- **Photorealistic?** → Realistic Vision, Counterfeit (excellent at ~1m 15s)
- **Artistic/Stylized?** → DreamShaper, Playground (versatile aesthetics)
- **Maximum detail?** → FLUX (unmatched but slowest)

---

## 🔧 How to Generate Your Own

### Single Model
```bash
python generate_images.py prompts.json assets/
# Select model based on your needs (see table above)
# Resolution mode: 1 (JSON-defined)
```

### Multi-Model Comparison
```bash
python generate_images.py prompts.json assets/ multi
# Select models: 2,3,4,5,6,7 (compare all)
# Resolution mode: 1 (JSON-defined)
```

### Sample JSON Format
```json
{
  "image_name": {
    "prompt": "Your detailed prompt here...",
    "aspect_ratio": "landscape",
    "base_resolution": 1536
  }
}
```

---

## 📝 Model Recommendations

**Highest quality (when time allows):** **FLUX.1-schnell** - Unmatched detail and quality, but requires 32GB+ RAM and ~7-8 minutes per image. Worth the wait for final production work.

**Best speed/quality balance:** **Realistic Vision v5.1** - Excellent photorealism in ~1m 20s. Perfect for most real-world use cases.

**Most versatile:** **DreamShaper v8** - Handles both artistic and realistic prompts beautifully in ~1m 20s.

**Fine detail specialist:** **Counterfeit v2.5** - Excels at detailed textures and faces in ~1m 15s.

**Aesthetic focus:** **Playground v2.5** - Creates gorgeous, artistic compositions in ~2-3 minutes.

**High-resolution work:** **SDXL Base 1.0** - Excellent quality at higher resolutions in ~2-3 minutes.

**Fastest iteration:** **SD v1.5** - Quick testing and prototyping in ~30 seconds.

---

## 🤝 Contribute & Improve

**Found a better model or better version of existing model?** 

We welcome contributions! If you discover a model that:
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
