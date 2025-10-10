"""
Stable Diffusion Image Batch Generator v4.0 - WITH ASPECT RATIO CONTROL
Optimized for M1 Pro 32GB | Cross-platform: Mac (MPS), NVIDIA (CUDA), CPU
With FLUX.1-schnell support and custom aspect ratios

Version: 4.0 - Added aspect ratio control, poster generation support
Features:
- 7 verified working models (SD 1.5, SDXL, FLUX) + 1 broken (GGUF - awaiting fix)
- Custom aspect ratios (square, portrait, landscape, cinematic)
- Per-prompt resolution control via JSON
- Model info display (size, access type)
"""

import os
import json
import sys
import warnings
import torch
from diffusers import StableDiffusionPipeline, StableDiffusionXLPipeline, FluxPipeline, FluxTransformer2DModel, GGUFQuantizationConfig
from huggingface_hub import hf_hub_download

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Model definitions - ONLY WORKING MODELS
MODELS = {
    "1": {
        "name": "Stable Diffusion v1.5 (Fast, Baseline)",
        "id": "runwayml/stable-diffusion-v1-5",
        "type": "sd15",
        "resolution": (512, 512),
        "steps": 40,
        "max_tokens": 77,
        "folder_name": "sd-v1.5",
        "size": "5.5GB",
        "access": "Open",
        "description": "Fastest, lightweight, good for testing",
        "supports_aspect_ratios": True,
        "min_resolution": 512,
        "max_resolution": 768
    },
    "2": {
        "name": "FLUX.1-schnell (Ultra Fast, Highest Quality)",
        "id": "black-forest-labs/FLUX.1-schnell",
        "type": "flux",
        "resolution": (1024, 1024),
        "steps": 4,
        "max_tokens": 512,
        "folder_name": "flux-schnell",
        "size": "33.7GB",
        "access": "Open",
        "description": "RECOMMENDED - Best quality, 4 steps, 512 token prompts",
        "supports_aspect_ratios": True,
        "min_resolution": 512,
        "max_resolution": 2048
    },
    "3": {
        "name": "Realistic Vision v5.1 (Photorealistic)",
        "id": "SG161222/Realistic_Vision_V5.1_noVAE",
        "type": "sd15",
        "resolution": (768, 768),
        "steps": 40,
        "max_tokens": 77,
        "folder_name": "realistic-vision-v5.1",
        "size": "4.3GB",
        "access": "Open",
        "description": "Best for realistic food photography",
        "supports_aspect_ratios": True,
        "min_resolution": 512,
        "max_resolution": 768
    },
    "4": {
        "name": "DreamShaper v8 (Versatile, High Quality)",
        "id": "Lykon/DreamShaper",
        "type": "sd15",
        "resolution": (768, 768),
        "steps": 40,
        "max_tokens": 77,
        "folder_name": "dreamshaper-v8",
        "size": "5.5GB",
        "access": "Open",
        "description": "Great all-rounder, artistic and realistic",
        "supports_aspect_ratios": True,
        "min_resolution": 512,
        "max_resolution": 768
    },
    "5": {
        "name": "Counterfeit v2.5 (Photorealistic Details)",
        "id": "gsdf/Counterfeit-V2.5",
        "type": "sd15",
        "resolution": (768, 768),
        "steps": 40,
        "max_tokens": 77,
        "folder_name": "counterfeit-v2.5",
        "size": "4.3GB",
        "access": "Open",
        "description": "Excellent detail and faces",
        "supports_aspect_ratios": True,
        "min_resolution": 512,
        "max_resolution": 768
    },
    "6": {
        "name": "Playground v2.5 (Best Aesthetics)",
        "id": "playgroundai/playground-v2.5-1024px-aesthetic",
        "type": "sdxl",
        "resolution": (1024, 1024),
        "steps": 30,
        "max_tokens": 77,
        "folder_name": "playground-v2.5",
        "size": "13.9GB",
        "access": "Open",
        "description": "Beautiful aesthetic quality",
        "supports_aspect_ratios": True,
        "min_resolution": 512,
        "max_resolution": 1536
    },
    "7": {
        "name": "SDXL Base 1.0 (High Quality, Slower)",
        "id": "stabilityai/stable-diffusion-xl-base-1.0",
        "type": "sdxl",
        "resolution": (1024, 1024),
        "steps": 30,
        "max_tokens": 77,
        "folder_name": "sdxl-base-1.0",
        "size": "14.2GB",
        "access": "Open",
        "description": "High quality SDXL, slower generation",
        "supports_aspect_ratios": True,
        "min_resolution": 512,
        "max_resolution": 1536
    },
    "8": {
        "name": "Chroma-GGUF Q5 ⚠️ CURRENTLY BROKEN",
        "id": "silveroxides/Chroma-GGUF",
        "gguf_file": "chroma-unlocked-v27/chroma-unlocked-v27-Q5_0.gguf",
        "base_model": "black-forest-labs/FLUX.1-schnell",
        "type": "flux-gguf",
        "resolution": (1024, 1024),
        "steps": 20,
        "max_tokens": 512,
        "folder_name": "chroma-gguf-q5",
        "size": "7.1GB",
        "access": "Open",
        "description": "⚠️ GGUF loader incompatibility - KeyError: 'time_in.in_layer.weight' - awaiting diffusers fix",
        "supports_aspect_ratios": True,
        "min_resolution": 512,
        "max_resolution": 2048,
        "status": "broken"
    }
}

# Predefined aspect ratios for poster/image generation
ASPECT_RATIOS = {
    "square": {"name": "Square (1:1)", "ratio": 1.0},
    "portrait": {"name": "Portrait (2:3)", "ratio": 2/3},
    "portrait_wide": {"name": "Portrait Wide (3:4)", "ratio": 3/4},
    "landscape": {"name": "Landscape (3:2)", "ratio": 3/2},
    "landscape_wide": {"name": "Landscape Wide (16:9)", "ratio": 16/9},
    "cinematic": {"name": "Cinematic (21:9)", "ratio": 21/9}
}

def load_prompts(json_path):
    """Load prompts from JSON file.

    Format can be:
    1. Simple: {"image_name": "prompt text"}
    2. Advanced: {"image_name": {"prompt": "text", "aspect_ratio": "portrait", "base_resolution": 1024}}
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Normalize to advanced format
    prompts = {}
    for key, value in data.items():
        if isinstance(value, str):
            prompts[key] = {"prompt": value, "aspect_ratio": "square", "base_resolution": None}
        else:
            prompts[key] = {
                "prompt": value.get("prompt", ""),
                "aspect_ratio": value.get("aspect_ratio", "square"),
                "base_resolution": value.get("base_resolution", None)
            }

    return prompts

def calculate_resolution(aspect_ratio_key, base_resolution, model_info):
    """Calculate width and height based on aspect ratio and base resolution.

    Args:
        aspect_ratio_key: Key from ASPECT_RATIOS (e.g., "portrait", "landscape")
        base_resolution: Base resolution (height for portrait, width for landscape, or side for square)
        model_info: Model information dict with min/max resolution constraints

    Returns:
        (width, height) tuple
    """
    if aspect_ratio_key not in ASPECT_RATIOS:
        aspect_ratio_key = "square"

    ratio = ASPECT_RATIOS[aspect_ratio_key]["ratio"]

    # If no base resolution specified, use model default
    if base_resolution is None:
        return model_info["resolution"]

    # Constrain to model limits
    min_res = model_info["min_resolution"]
    max_res = model_info["max_resolution"]
    base_resolution = max(min_res, min(max_res, base_resolution))

    # Calculate dimensions based on aspect ratio
    if ratio == 1.0:  # Square
        width = height = base_resolution
    elif ratio < 1.0:  # Portrait (height > width)
        height = base_resolution
        width = int(height * ratio)
    else:  # Landscape (width > height)
        width = base_resolution
        height = int(width / ratio)

    # Ensure dimensions are divisible by 8 (requirement for diffusion models)
    width = (width // 8) * 8
    height = (height // 8) * 8

    # Final constraint check
    width = max(min_res, min(max_res, width))
    height = max(min_res, min(max_res, height))

    return (width, height)

def select_resolution_mode():
    """Let user choose resolution/aspect ratio mode."""
    print("\n" + "="*80)
    print("RESOLUTION MODE")
    print("="*80)
    print("1. Use JSON-defined resolutions (prompts can specify custom aspect ratios)")
    print("2. Override all with single aspect ratio")
    print("3. Use model defaults (ignore JSON aspect ratios)")
    print("="*80)

    while True:
        choice = input("\nSelect mode (1-3, recommend 1): ").strip()
        if choice in ["1", "2", "3"]:
            if choice == "2":
                # Show aspect ratio options
                print("\n" + "="*80)
                print("ASPECT RATIOS")
                print("="*80)
                for idx, (key, info) in enumerate(ASPECT_RATIOS.items(), 1):
                    print(f"{idx}. {info['name']} - Ratio: {info['ratio']:.2f}")
                print("="*80)

                while True:
                    ar_choice = input("\nSelect aspect ratio (1-6): ").strip()
                    try:
                        ar_idx = int(ar_choice) - 1
                        if 0 <= ar_idx < len(ASPECT_RATIOS):
                            ar_key = list(ASPECT_RATIOS.keys())[ar_idx]

                            # Ask for base resolution
                            base_res = input("Enter base resolution (e.g., 1024): ").strip()
                            try:
                                base_res = int(base_res)
                                return ("override", ar_key, base_res)
                            except ValueError:
                                print("❌ Invalid resolution number")
                        else:
                            print("❌ Invalid choice")
                    except ValueError:
                        print("❌ Invalid input")

            return ("json" if choice == "1" else "default", None, None)

        print("❌ Invalid. Please select 1-3.")

def select_single_model():
    print("\n" + "="*80)
    print("SINGLE MODEL MODE - Select ONE model")
    print("="*80)
    for key, model in MODELS.items():
        print(f"\n{key}. {model['name']}")
        print(f"   Size: {model['size']} | Access: {model['access']} | Tokens: {model['max_tokens']} | Steps: {model['steps']}")
        print(f"   Resolution: {model['min_resolution']}-{model['max_resolution']}px | Default: {model['resolution'][0]}x{model['resolution'][1]}")
        print(f"   {model['description']}")

    print("\n" + "="*80)

    while True:
        choice = input("\nSelect model (1-8, recommend 2 for FLUX): ").strip()
        if choice in MODELS:
            return [MODELS[choice]]
        print("❌ Invalid. Please select 1-8.")

def select_multiple_models():
    print("\n" + "="*80)
    print("MULTI MODEL MODE - Compare multiple models")
    print("="*80)
    for key, model in MODELS.items():
        print(f"{key}. {model['name']} ({model['size']}) → {model['folder_name']}/")

    print("="*80)

    while True:
        choices = input("\nSelect models (e.g., 2,3,6): ").strip()
        selected_keys = [c.strip() for c in choices.split(",")]

        if all(key in MODELS for key in selected_keys):
            return [MODELS[key] for key in selected_keys]

        print("❌ Invalid. Use numbers 1-8 separated by commas.")

def detect_device():
    if torch.cuda.is_available():
        device = "cuda"
        dtype = torch.float16
        device_name = f"CUDA ({torch.cuda.get_device_name(0)})"
    elif torch.backends.mps.is_available():
        device = "mps"
        # Use float32 on MPS - float16/bfloat16 causes NaN in VAE decoder
        dtype = torch.float32
        device_name = "Apple Silicon (MPS)"
    else:
        device = "cpu"
        dtype = torch.float32
        device_name = "CPU"

    print(f"🖥️  Device: {device_name}")
    return device, dtype

def load_pipeline(model_info, device, dtype):
    model_id = model_info["id"]
    model_type = model_info["type"]

    print(f"\n🔄 Loading: {model_info['name']}")

    if model_type == "flux-gguf":
        gguf_file = model_info["gguf_file"]
        base_model = model_info.get("base_model", "black-forest-labs/FLUX.1-schnell")

        print("   📦 Loading GGUF quantized transformer")
        print(f"   Repository: {model_id}")
        print(f"   File: {gguf_file}")

        gguf_path = hf_hub_download(
            repo_id=model_id,
            filename=gguf_file,
            repo_type="model"
        )
        print(f"   ✅ Downloaded to: {gguf_path}")

        quantization_config = GGUFQuantizationConfig(compute_dtype=dtype)

        transformer = FluxTransformer2DModel.from_single_file(
            gguf_path,
            quantization_config=quantization_config,
            torch_dtype=dtype
        )

        pipe = FluxPipeline.from_pretrained(
            base_model,
            transformer=transformer,
            torch_dtype=dtype
        )
    elif model_type == "flux":
        pipe = FluxPipeline.from_pretrained(model_id, torch_dtype=dtype)
    elif model_type == "sdxl":
        pipe = StableDiffusionXLPipeline.from_pretrained(
            model_id, torch_dtype=dtype, use_safetensors=True
        )
    else:  # sd15
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=dtype,
            safety_checker=None,
            requires_safety_checker=False
        )

    pipe = pipe.to(device)

    if model_type == "flux-gguf":
        pipe.enable_model_cpu_offload()
        if hasattr(pipe, "vae"):
            pipe.vae.enable_slicing()
            pipe.vae.enable_tiling()
        print("   🔧 Applied GGUF memory optimizations")
    elif model_type != "flux":
        pipe.enable_attention_slicing()
        if device == "mps":
            pipe.enable_model_cpu_offload()

    print(f"✅ Loaded!\n")
    return pipe

def generate_with_model(model_info, prompts, base_output_dir, device, dtype, multi_mode=False, resolution_mode=("default", None, None)):
    output_dir = os.path.join(base_output_dir, model_info["folder_name"]) if multi_mode else base_output_dir
    os.makedirs(output_dir, exist_ok=True)

    pipe = load_pipeline(model_info, device, dtype)

    steps = model_info["steps"]
    model_type = model_info["type"]

    print("="*80)
    print(f"🎨 GENERATING: {model_info['name']}")
    print(f"📁 Output: {output_dir}")
    print(f"🔧 Resolution Mode: {resolution_mode[0]}")
    print(f"📐 {steps} steps | {len(prompts)} images")
    print("="*80 + "\n")

    success_count = 0
    error_count = 0

    for idx, (filename, prompt_data) in enumerate(prompts.items(), 1):
        # Extract prompt text and resolution info
        if isinstance(prompt_data, str):
            prompt_text = prompt_data
            aspect_ratio = "square"
            base_res = None
        else:
            prompt_text = prompt_data["prompt"]
            aspect_ratio = prompt_data.get("aspect_ratio", "square")
            base_res = prompt_data.get("base_resolution", None)

        # Determine resolution based on mode
        mode, override_ar, override_res = resolution_mode
        if mode == "override":
            width, height = calculate_resolution(override_ar, override_res, model_info)
        elif mode == "json":
            width, height = calculate_resolution(aspect_ratio, base_res, model_info)
        else:  # default
            width, height = model_info["resolution"]

        print(f"[{idx}/{len(prompts)}] {filename}.png ({width}x{height})")
        print(f"💬 {prompt_text[:80]}{'...' if len(prompt_text) > 80 else ''}")

        try:
            generator = torch.Generator("cpu" if device == "mps" else device).manual_seed(42)

            if model_type in ["flux", "flux-gguf"]:
                # FLUX models (including GGUF quantized)
                # Note: Removed automatic 512x512 resize to preserve aspect ratio
                image = pipe(
                    prompt_text,
                    num_inference_steps=steps,
                    guidance_scale=3.5 if model_type == "flux-gguf" else 0.0,
                    height=height,
                    width=width,
                    max_sequence_length=256,
                    generator=generator
                ).images[0]
            else:
                # SD 1.5 / SDXL models
                image = pipe(
                    prompt_text,
                    num_inference_steps=steps,
                    guidance_scale=7.5,
                    height=height,
                    width=width,
                    generator=generator
                ).images[0]

            output_path = os.path.join(output_dir, f"{filename}.png")
            image.save(output_path, optimize=True, quality=95)

            file_size = os.path.getsize(output_path)
            print(f"✅ {file_size // 1024} KB\n")
            success_count += 1

        except Exception as e:
            print(f"❌ Error: {str(e)}\n")
            error_count += 1

    del pipe
    if device == "cuda":
        torch.cuda.empty_cache()
    elif device == "mps":
        torch.mps.empty_cache()

    return success_count, error_count

def main(json_path, output_dir="assets/foods", multi_mode=False):
    print(f"\n📂 Loading: {json_path}")
    prompts = load_prompts(json_path)
    print(f"✅ {len(prompts)} prompts loaded")

    device, dtype = detect_device()

    if multi_mode:
        selected_models = select_multiple_models()
        print(f"\n✅ {len(selected_models)} models selected\n")
    else:
        selected_models = select_single_model()

    # Select resolution mode
    resolution_mode = select_resolution_mode()

    total_success = 0
    total_error = 0

    for model_idx, model_info in enumerate(selected_models, 1):
        if multi_mode:
            print("\n" + "🔹"*80)
            print(f"MODEL {model_idx}/{len(selected_models)}")
            print("🔹"*80 + "\n")

        success, errors = generate_with_model(model_info, prompts, output_dir, device, dtype, multi_mode, resolution_mode)

        total_success += success
        total_error += errors

    print("\n" + "="*80)
    print("🎉 COMPLETE!")
    print("="*80)
    if multi_mode:
        print(f"Models: {len(selected_models)}")
    print(f"✅ Success: {total_success}")
    if total_error > 0:
        print(f"❌ Failed: {total_error}")
    print(f"📁 {output_dir}")
    print("="*80)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n" + "="*80)
        print("Image Generator v4.0 - FLUX + Stable Diffusion + Aspect Ratios")
        print("="*80)
        print("\nUsage:")
        print("  python generate_images_v3.py <prompts.json> [output_dir] [multi]")
        print("\nExamples:")
        print("  python generate_images_v3.py food_prompts.json")
        print("  python generate_images_v3.py food_prompts.json assets/")
        print("  python generate_images_v3.py food_prompts.json assets/ multi")
        print("  python generate_images_v3.py sample_poster_prompts.json posters/")
        print("\nJSON Format:")
        print('  Simple:  {"name": "prompt text"}')
        print('  Advanced: {"name": {"prompt": "text", "aspect_ratio": "portrait", "base_resolution": 1024}}')
        print("\nAspect Ratios:")
        print("  square, portrait (2:3), portrait_wide (3:4), landscape (3:2),")
        print("  landscape_wide (16:9), cinematic (21:9)")
        print("\nRecommended:")
        print("  Model 2 (FLUX.1-schnell) - Best quality, fastest, 512 token prompts")
        print("\n⚠️  Known Issues:")
        print("  Model 8 (Chroma-GGUF) - BROKEN: GGUF incompatibility, awaiting diffusers fix")
        print("\nModel Sizes:")
        print("  SD 1.5: ~5GB | SDXL: ~14GB | FLUX: ~34GB")
        print("\n" + "="*80)
        sys.exit(1)

    json_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] != "multi" else "assets/"
    multi_mode = "multi" in sys.argv

    try:
        main(json_path, output_dir, multi_mode)
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
