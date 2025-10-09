"""
Stable Diffusion Image Batch Generator v3 - CLEAN VERSION
Optimized for M1 Pro 32GB | Cross-platform: Mac (MPS), NVIDIA (CUDA), CPU
With FLUX.1-schnell support - Only working models included

Version: 3.1 - Cleaned, only verified working models
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
        "description": "Fastest, lightweight, good for testing"
    },
    "2": {
        "name": "FLUX.1-schnell (Ultra Fast, Highest Quality)",
        "id": "black-forest-labs/FLUX.1-schnell",
        "type": "flux",
        "resolution": (1024, 1024),
        "steps": 4,
        "max_tokens": 512,
        "folder_name": "flux-schnell",
        "description": "RECOMMENDED - Best quality, 4 steps, 512 token prompts"
    },
    "3": {
        "name": "Realistic Vision v5.1 (Photorealistic)",
        "id": "SG161222/Realistic_Vision_V5.1_noVAE",
        "type": "sd15",
        "resolution": (768, 768),
        "steps": 40,
        "max_tokens": 77,
        "folder_name": "realistic-vision-v5.1",
        "description": "Best for realistic food photography"
    },
    "4": {
        "name": "DreamShaper v8 (Versatile, High Quality)",
        "id": "Lykon/DreamShaper",
        "type": "sd15",
        "resolution": (768, 768),
        "steps": 40,
        "max_tokens": 77,
        "folder_name": "dreamshaper-v8",
        "description": "Great all-rounder, artistic and realistic"
    },
    "5": {
        "name": "Counterfeit v2.5 (Photorealistic Details)",
        "id": "gsdf/Counterfeit-V2.5",
        "type": "sd15",
        "resolution": (768, 768),
        "steps": 40,
        "max_tokens": 77,
        "folder_name": "counterfeit-v2.5",
        "description": "Excellent detail and faces"
    },
    "6": {
        "name": "Playground v2.5 (Best Aesthetics)",
        "id": "playgroundai/playground-v2.5-1024px-aesthetic",
        "type": "sdxl",
        "resolution": (1024, 1024),
        "steps": 30,
        "max_tokens": 77,
        "folder_name": "playground-v2.5",
        "description": "Beautiful aesthetic quality"
    },
    "7": {
        "name": "SDXL Base 1.0 (High Quality, Slower)",
        "id": "stabilityai/stable-diffusion-xl-base-1.0",
        "type": "sdxl",
        "resolution": (1024, 1024),
        "steps": 30,
        "max_tokens": 77,
        "folder_name": "sdxl-base-1.0",
        "description": "High quality SDXL, slower generation"
    },
    "8": {
        "name": "Chroma-GGUF Q5 (FLUX-based, Memory Efficient)",
        "id": "silveroxides/Chroma-GGUF",
        "gguf_file": "chroma-unlocked-v27/chroma-unlocked-v27-Q5_0.gguf",
        "base_model": "black-forest-labs/FLUX.1-schnell",
        "type": "flux-gguf",
        "resolution": (1024, 1024),
        "steps": 20,
        "max_tokens": 512,
        "folder_name": "chroma-gguf-q5",
        "description": "FLUX-based 8.9B model with GGUF quantization for lower VRAM usage"
    }
}

def load_prompts(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def select_single_model():
    print("\n" + "="*80)
    print("SINGLE MODEL MODE - Select ONE model")
    print("="*80)
    for key, model in MODELS.items():
        print(f"\n{key}. {model['name']}")
        print(f"   Resolution: {model['resolution'][0]}x{model['resolution'][1]} | "
              f"Tokens: {model['max_tokens']} | Steps: {model['steps']}")
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
        print(f"{key}. {model['name']} → {model['folder_name']}/")

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
        dtype = torch.bfloat16
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
        if dtype == torch.float16:
            pipe = StableDiffusionXLPipeline.from_pretrained(
                model_id, torch_dtype=dtype, use_safetensors=True, variant="fp16"
            )
        else:
            pipe = StableDiffusionXLPipeline.from_pretrained(
                model_id, torch_dtype=dtype, use_safetensors=True
            )
    else:  # sd15
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=dtype)

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

def generate_with_model(model_info, prompts, base_output_dir, device, dtype, multi_mode=False):
    output_dir = os.path.join(base_output_dir, model_info["folder_name"]) if multi_mode else base_output_dir
    os.makedirs(output_dir, exist_ok=True)

    pipe = load_pipeline(model_info, device, dtype)

    height, width = model_info["resolution"]
    steps = model_info["steps"]
    model_type = model_info["type"]

    print("="*80)
    print(f"🎨 GENERATING: {model_info['name']}")
    print(f"📁 Output: {output_dir}")
    print(f"📐 {width}x{height} | {steps} steps | {len(prompts)} images")
    print("="*80 + "\n")

    success_count = 0
    error_count = 0

    for idx, (filename, prompt) in enumerate(prompts.items(), 1):
        print(f"[{idx}/{len(prompts)}] {filename}.png")
        print(f"💬 {prompt[:80]}{'...' if len(prompt) > 80 else ''}")

        try:
            generator = torch.Generator("cpu" if device == "mps" else device).manual_seed(42)

            if model_type in ["flux", "flux-gguf"]:
                # FLUX models (including GGUF quantized)
                image = pipe(
                    prompt,
                    num_inference_steps=steps,
                    guidance_scale=3.5 if model_type == "flux-gguf" else 0.0,
                    height=height,
                    width=width,
                    max_sequence_length=256,
                    generator=generator
                ).images[0]

                from PIL import Image
                image = image.resize((512, 512), Image.Resampling.LANCZOS)
            else:
                # SD 1.5 / SDXL models
                image = pipe(
                    prompt,
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

    total_success = 0
    total_error = 0

    for model_idx, model_info in enumerate(selected_models, 1):
        if multi_mode:
            print("\n" + "🔹"*80)
            print(f"MODEL {model_idx}/{len(selected_models)}")
            print("🔹"*80 + "\n")

        success, errors = generate_with_model(model_info, prompts, output_dir, device, dtype, multi_mode)

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
        print("Image Generator v3.1 - FLUX + Stable Diffusion")
        print("="*80)
        print("\nUsage:")
        print("  python generate_images_v3.py <prompts.json> [output_dir] [multi]")
        print("\nExamples:")
        print("  python generate_images_v3.py food_prompts.json")
        print("  python generate_images_v3.py food_prompts.json assets/")
        print("  python generate_images_v3.py food_prompts.json assets/ multi")
        print("\nRecommended:")
        print("  Model 2 (FLUX.1-schnell) - Best quality, fastest, 512 token prompts")
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
