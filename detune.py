import os
os.environ["DEMUCS_AUDIO_BACKEND"] = "ffmpeg"
import subprocess
import yt_dlp

def download_video(url, output_file="input_video.mp4"):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'outtmpl': output_file
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def extract_audio(video_file, audio_file="audio.wav"):
    subprocess.run([
        "ffmpeg", "-y", "-i", video_file, "-vn", "-acodec", "pcm_s16le", audio_file
    ])

def separate_vocals(audio_file):
    print("🎧 Running Demucs externally (CLI workaround)")
    subprocess.run([
        "demucs", "--two-stems", "vocals", audio_file, "-n", "mdx", "-o", "separated"
    ])

def merge_vocals_back(video_file, vocals_file, output_file="output_video.mp4"):
    if not os.path.exists(vocals_file):
        print(f"❌ Error: Could not find '{vocals_file}'.")
        return
    subprocess.run([
        "ffmpeg", "-y",
        "-i", video_file,
        "-i", vocals_file,
        "-map", "0:0", "-map", "1:0",
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        output_file
    ])


def main():
    url = input("Enter video link: ")
    download_video(url)
    extract_audio("input_video.mp4")
    separate_vocals("audio.wav")
    vocals_path = os.path.join("separated", "mdx", "audio", "vocals.wav")
    merge_vocals_back("input_video.mp4", vocals_path)
    print("✅ Done! Vocal-only video saved as 'output_video.mp4'.")

if __name__ == "__main__":
    main()
