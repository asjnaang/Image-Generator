# Troubleshooting Guide

## Common Issues and Solutions

### Out of Memory Errors

**Symptoms**: Process crashes with "Out of memory" or similar errors

**Solutions**:
- Use smaller models (SD 1.5 models: 1, 3-5)
- Reduce `base_resolution` in JSON
- Close other applications
- Use CPU mode (slower but works)

---

### Black/Blank Images

**Symptoms**: Images generate but appear completely black

**Solutions**:
- Try different model (Models 2, 6, 7 work best)
- Check prompt quality
- Verify model downloaded correctly

---

### RuntimeWarning: Invalid Value Encountered in Cast (MPS/Apple Silicon)

**Symptoms**: 
```
RuntimeWarning: invalid value encountered in cast
  images = (images * 255).round().astype("uint8")
```
Images appear black or corrupted.

**Root Cause**: On Apple Silicon with MPS backend, using `float16` or `bfloat16` causes the VAE decoder to produce NaN values.

**Solution**: ✅ **FIXED in v4.0**
- The script now uses `float32` for all operations on MPS devices
- This prevents NaN values in the VAE decoder
- Images generate correctly without black outputs

**Technical Details**:
- MPS (Metal Performance Shaders) has precision issues with float16/bfloat16
- The VAE decoder produces NaN values when using reduced precision
- float32 is stable on MPS and produces valid images
- Trade-off: Slightly slower but reliable image generation

---

### Chroma-GGUF (Model 8) Errors

**Symptoms**: 
```
KeyError: 'time_in.in_layer.weight'
```

**Status**: Currently broken due to GGUF loader incompatibility

**Solution**: 
- Use Model 2 (FLUX.1-schnell) instead for best quality
- Model 8 will be fixed when diffusers library updates GGUF support

---

### Model Download Issues

**Symptoms**: Models fail to download or timeout

**Solutions**:
- Check internet connection
- Verify HuggingFace Hub access token is set up correctly
- Models download automatically on first use
- Check available disk space

---

### Safety Checker Warnings (SD 1.5 Models)

**Symptoms**:
```
You have passed a non-standard module <function>. We cannot verify whether it has the correct type
Expected types for safety_checker: (...), got <class 'function'>.
```

**Status**: ✅ **FIXED in v4.0**
- Safety checker is now properly disabled by passing `None`
- No more type checking warnings
- False positive NSFW detections are prevented

---

### Deprecation Warnings

**Symptoms**:
```
`torch_dtype` is deprecated! Use `dtype` instead!
```

**Status**: These are warnings from the diffusers library, not errors
- They don't affect functionality
- Will be addressed in future diffusers updates
- Safe to ignore for now

---

### Unsafe Serialization Warnings

**Symptoms**:
```
An error occurred while trying to fetch ... diffusion_pytorch_model.safetensors
Defaulting to unsafe serialization. Pass `allow_pickle=False` to raise an error instead.
```

**Status**: This is normal for some older models
- Some models (like DreamShaper) use pickle format instead of safetensors
- The script handles this automatically
- Safe to ignore - models load correctly

---

## Getting Help

If you encounter issues not covered here:

1. Check the console output for specific error messages
2. Verify system requirements are met
3. Ensure all dependencies are installed correctly
4. Try with a different model to isolate the issue
5. Check available RAM/VRAM before generation

## Known Limitations

1. **Model 8 (Chroma-GGUF)**: Currently broken, awaiting diffusers library fix
2. **MPS Performance**: Slower than CUDA but more reliable with float32
3. **Memory Usage**: Large models require significant free RAM/VRAM
4. **First Run**: Initial model downloads can take time depending on connection speed
