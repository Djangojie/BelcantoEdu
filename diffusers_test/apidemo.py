from diffusers import AudioDiffusionPipeline
import torch
import librosa

# 加载模型（确保已手动下载权重）
pipe = AudioDiffusionPipeline.from_pretrained(
    "teticio/audio-diffusion-256",
    torch_dtype=torch.float16,
    local_files_only=True
).to("cuda")

# 生成Mel频谱图
result = pipe(
    num_steps=100,    # 推理步数
    guidance=3.0,     # 文本引导系数
    audio_length=5.0  # 音频时长（秒）
)

# 保存原始Mel图
mel = result.images[0]
mel.save("mel_spectrogram.png")

# 转换为音频波形
audio = pipe.mel_to_audio(mel)
librosa.output.write_wav("generated_audio.wav", audio, sr=22050)