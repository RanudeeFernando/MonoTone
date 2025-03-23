from moviepy.video.io.VideoFileClip import VideoFileClip
import whisper
import os

def extract_audio(video_path, audio_path="audio.wav"):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    return audio_path

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    print("Transcript:\n")
    print(result["text"])
    return result["text"]

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
video_path = os.path.join(project_root, "backend/my_video.mp4")
audio_path = os.path.join(project_root, "backend/audio.wav")
transcript_path = os.path.join(project_root, "backend/transcript.txt")

audio_path = extract_audio(video_path, audio_path)
transcript = transcribe_audio(audio_path)

with open(transcript_path, "w", encoding="utf-8") as f:
    f.write(transcript)
