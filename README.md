# 🎵 Detune

## 🔧 Tools & Technologies

- **Demucs** – Deep learning model for separating vocals, drums, bass, and other stems  
- **FFmpeg** – For audio extraction, manipulation, and combining  
- **yt-dlp** – To download YouTube videos for local processing and testing

## 🧠 What I Learned

- Basics of source separation and audio preprocessing  
- Working with Python audio libraries and deep learning models for music analysis  
- Integrating multiple tools (`yt-dlp`, `FFmpeg`, `Demucs`) into a functional pipeline

## 🚀 Future Plans

I plan to extend this project into a **real-time background music remover** with low-latency audio stream processing, enabling live vocal enhancement or in-call background music suppression.

## 📦 Installation

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

>⚠️ Note: You must also install FFmpeg manually and ensure it is added to your system PATH

## ▶️ Usage

Run the script and follow the prompt to enter a YouTube video URL:

```bash
python detune.py
```

The script will:
1. 🎬 Download the video using yt-dlp  
2. 🎧 Extract audio using FFmpeg  
3. 🎙️ Separate vocals using Demucs  
4. 🔄 Merge the isolated vocals back into the original video  
5. 🎧 Output: output_video.mp4 – a video with only vocals retained


