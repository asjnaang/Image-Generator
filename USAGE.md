# Usage Guide

## Quick Start

### Basic Usage

```bash
# Simple generation with default settings
python generate_images.py food_prompts.json

# Specify output directory
python generate_images.py food_prompts.json output/

# Compare multiple models
python generate_images.py food_prompts.json output/ multi
```

---

## JSON Format

### Simple Format (uses model defaults)
```json
{
  "sunset_mountain": "A breathtaking sunset over majestic snow-capped mountains, vibrant orange and pink sky with wispy clouds, dramatic lighting, golden hour glow, serene alpine landscape, professional nature photography, high detail, 8k quality, stunning vista",
  "forest_path": "A peaceful winding forest path through tall ancient trees, dappled sunlight filtering through dense green canopy, moss-covered ground, ethereal morning mist, tranquil woodland atmosphere, natural beauty, photorealistic, high resolution"
}
```

See `simple_prompts.json` for a complete example with 5 detailed prompts.

### Advanced Format (custom aspect ratio & resolution)
```json
{
  "sunset_mountain_square": {
    "prompt": "A breathtaking sunset over majestic snow-capped mountains, vibrant orange and pink sky with wispy clouds, dramatic lighting, golden hour glow, serene alpine landscape, professional nature photography, high detail, 8k quality, stunning vista",
    "aspect_ratio": "square",
    "base_resolution": 1024
  },
  "ocean_waves_landscape": {
    "prompt": "Powerful ocean waves crashing on pristine sandy beach at golden hour, dramatic sea spray, warm sunset lighting, turquoise water, foam and texture, coastal seascape, dynamic motion, professional seascape photography, vivid colors, high detail",
    "aspect_ratio": "landscape",
    "base_resolution": 1536
  }
}
```

See `sample_poster_prompts.json` for a complete example with all 5 aspect ratios and detailed prompts.

---

## Aspect Ratios

| Name | Ratio | Best For |
|------|-------|----------|
| `square` | 1:1 | Icons, thumbnails, Instagram posts |
| `portrait` | 2:3 | Posters, phone wallpapers |
| `portrait_wide` | 3:4 | Standard photo prints |
| `landscape` | 3:2 | Desktop wallpapers, photography |
| `landscape_wide` | 16:9 | YouTube thumbnails, presentations |
| `cinematic` | 21:9 | Ultra-wide banners, headers |

---

## Resolution Modes

### Mode 1: Use JSON-defined resolutions (Recommended)
Each prompt can specify its own aspect ratio and resolution in the JSON file. Most flexible option.

### Mode 2: Override all with single aspect ratio
Force all images to use the same aspect ratio and resolution. Good for batch processing with consistent output.

### Mode 3: Use model defaults
Ignore JSON aspect ratios and use each model's default resolution. Fastest option.

---

## Usage Examples

### Simple Generation (Beginners)
```bash
python generate_images.py simple_prompts.json output/
# When prompted:
# 1. Select model: 1 (SD v1.5 - fastest, lowest memory)
# 2. Resolution mode: 3 (Use model defaults - 512x512)
```

This generates 5 simple images using the lightweight SD v1.5 model. Perfect for testing!

### Generate Food Icons (512x512)
```bash
python generate_images.py food_prompts.json assets/foods/
# When prompted:
# 1. Select model: 2 (FLUX.1-schnell)
# 2. Resolution mode: 3 (Use model defaults)
```

### Generate with Custom Aspect Ratios
```bash
python generate_images.py sample_poster_prompts.json posters/
# When prompted:
# 1. Select model: 2 (FLUX.1-schnell)
# 2. Resolution mode: 1 (Use JSON-defined resolutions)
```

This generates the same 5 simple prompts but with different aspect ratios:
- `sunset_mountain_square` → 1024x1024 (square)
- `forest_path_portrait` → 683x1024 (portrait 2:3)
- `ocean_waves_landscape` → 1536x1024 (landscape 3:2)
- `city_skyline_portrait_wide` → 768x1024 (portrait wide 3:4)
- `flower_garden_cinematic` → 1536x656 (cinematic 21:9)

### Compare Multiple Models
```bash
python generate_images.py sample_poster_prompts.json comparison/ multi
# When prompted:
# 1. Select models: 2,6,7 (FLUX, Playground, SDXL)
# 2. Resolution mode: 1 (Use JSON-defined)
# Output: comparison/flux-schnell/, comparison/playground-v2.5/, comparison/sdxl-base-1.0/
# Note: Avoid Model 8 (Chroma-GGUF) - currently broken
```

### Override All with Landscape 4K
```bash
python generate_images.py any_prompts.json output/
# When prompted:
# 1. Select model: 2 (FLUX.1-schnell)
# 2. Resolution mode: 2 (Override all)
# 3. Aspect ratio: 4 (Landscape 3:2)
# 4. Base resolution: 2048
```

---

## Prompt Writing Tips

- **Be specific**: "Fresh red apple on white background" > "apple"
- **Add details**: Include colors, lighting, style, mood, atmosphere
- **Use descriptive adjectives**: "breathtaking", "majestic", "vibrant", "dramatic", "serene"
- **Specify quality**: "professional photography", "high detail", "8k quality", "photorealistic"
- **Mention lighting**: "golden hour", "soft natural lighting", "dramatic lighting", "warm sunset"
- **Add style keywords**: "nature photography", "architectural photography", "macro photography"
- **For SD 1.5 models**: Aim for ~77 tokens (our examples use this limit)
- **For FLUX**: Take advantage of 512 tokens - add even more detail, botanical names, measurements, textures
- **For food**: Mention freshness, arrangement, lighting style, specific ingredients

---

## Performance Notes

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

**Apple M1 Pro 32GB (MPS, ~20GB Free RAM)** - Actual Test Results:
| Model | Resolution | Steps | Time | Memory Used |
|-------|------------|-------|------|-------------|
| SD v1.5 | 768x768 | 40 | ~30s | ~4GB |
| Counterfeit v2.5 | 768x768 | 40 | ~1m 15s | ~4GB |
| Realistic Vision v5.1 | 768x768 | 40 | ~1m 20s | ~4GB |
| DreamShaper v8 | 768x768 | 40 | ~1m 20s | ~4GB |
| Playground v2.5 | 1536x1024 | 30 | ~2-3 min | ~12GB |
| SDXL Base | 1536x1024 | 30 | ~2-3 min | ~12GB |
| **FLUX.1-schnell** | 1536x1024 | 4 | **~7-8 min** | ~24GB |

**NVIDIA RTX 3090 24GB (CUDA, ~18GB Free VRAM)** - Estimated:
| Model | Resolution | Steps | Time | VRAM Used |
|-------|------------|-------|------|-----------|
| SD v1.5 | 512x512 | 40 | 10-20s | ~3GB |
| Realistic Vision / DreamShaper | 768x768 | 40 | 20-30s | ~4GB |
| SDXL Base | 1024x1024 | 30 | 45-90s | ~10GB |
| Playground v2.5 | 1024x1024 | 30 | 45-90s | ~10GB |
| **FLUX.1-schnell** | 1024x1024 | 4 | **~2-3 min** | ~20GB |

**CPU-Only (16-core Ryzen, 32GB RAM)** - Estimated:
| Model | Resolution | Steps | Time | RAM Used |
|-------|------------|-------|------|----------|
| SD v1.5 | 512x512 | 40 | 5-10 min | ~8GB |
| SDXL Base | 1024x1024 | 30 | 15-30 min | ~16GB |

> **Important Notes**:
> - Times vary significantly based on prompt complexity, image resolution, available system resources, and background processes
> - **FLUX.1-schnell**: Despite using only 4 inference steps, it's the SLOWEST model (~7-8 min on M1 Pro) because each step is computationally intensive
> - "schnell" refers to the 4-step optimization, not real-world speed - FLUX prioritizes quality over speed
> - For fastest results, use SD v1.5 (~30s), Counterfeit/Realistic Vision (~1m 15s), or DreamShaper (~1m 20s)
