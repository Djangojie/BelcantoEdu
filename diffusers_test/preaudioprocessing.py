import os
from pydub import AudioSegment


def process_audio(input_dir: str, output_dir: str, target_duration=6000):
    """
    批量处理音频：裁剪到6秒，不足则循环填充
    参数说明：
    - input_dir: 输入文件夹路径（已处理采样率的音频）
    - output_dir: 输出文件夹路径（符合6秒要求的音频）
    - target_duration: 目标时长（毫秒，默认6000ms=6秒）
    """
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        if not os.path.isfile(input_path):
            continue

        try:
            # 读取音频文件（自动识别格式）
            audio = AudioSegment.from_file(input_path)
            duration = len(audio)  # 当前音频时长（毫秒）

            # 处理逻辑
            if duration >= target_duration:
                # 裁剪前6秒
                processed = audio[:target_duration]
            else:
                # 计算需要循环的次数（向上取整）
                loops = (target_duration // duration) + 1
                # 生成循环音频并截取前6秒
                processed = (audio * loops)[:target_duration]

            # 构建输出路径（保留原格式）
            output_path = os.path.join(output_dir, filename)
            # 导出文件
            processed.export(output_path, format=filename.split(".")[-1])
            print(f"[成功] {filename} → 6秒")
        except Exception as e:
            print(f"[失败] {filename}, 错误: {str(e)}")


if __name__ == "__main__":
    process_audio(input_dir="E:\ykj\sporan\Audio_diffusion", output_dir="E:\ykj\sporan\Audio_diffusion_new")
