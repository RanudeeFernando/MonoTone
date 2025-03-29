from moviepy import VideoFileClip
import whisper
import os
import requests
import time

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
video_path = os.path.join(project_root, "backend/my_vid.mp4")
audio_path = os.path.join(project_root, "backend/audio.wav")
transcript_path = os.path.join(project_root, "backend/transcript.txt")

audio_path = extract_audio(video_path, audio_path)
transcript = transcribe_audio(audio_path)

with open(transcript_path, "w", encoding="utf-8") as f:
    f.write(transcript)


ASSEMBLYAI_API_KEY = "cb14b7ca7a8c4877802093c5b9ffd60f"
audio_file_path = os.path.join(project_root,"backend/audio.wav")

# Step 1: Upload your audio
def upload_audio(file_path):
    headers = {'authorization': ASSEMBLYAI_API_KEY}
    with open(file_path, 'rb') as f:
        response = requests.post(
            'https://api.assemblyai.com/v2/upload',
            headers=headers,
            data=f
        )
    return response.json()['upload_url']

# Step 2: Start transcription with diarization enabled
def request_transcription(audio_url):
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json_data = {
        "audio_url": audio_url,
        "speaker_labels": True
    }
    headers = {
        "authorization": ASSEMBLYAI_API_KEY,
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json_data, headers=headers)
    return response.json()['id']

# Step 3: Poll until the transcription is ready
def wait_for_result(transcript_id):
    endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
    headers = {"authorization": ASSEMBLYAI_API_KEY}

    while True:
        response = requests.get(endpoint, headers=headers)
        data = response.json()
        if data['status'] == 'completed':
            return data
        elif data['status'] == 'error':
            raise Exception(f"Transcription failed: {data['error']}")
        time.sleep(3)

# Run it all together
audio_url = upload_audio(audio_file_path)
transcript_id = request_transcription(audio_url)
result = wait_for_result(transcript_id)

new_transcript_path = os.path.join(project_root, "backend/diarized_transcript.txt")

# Save diarized output
with open(new_transcript_path, "w", encoding="utf-8") as f:
    for utterance in result['utterances']:
        f.write(f"[Speaker {utterance['speaker']}]: {utterance['text']}\n")

