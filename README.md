# MonoTone 🧠💬

MonoTone is a sleek and intelligent sentiment analysis application designed to interpret the emotional tone of short, conversational content. Whether you're analyzing chat messages, social media posts, user feedback, or even speech from video clips, MonoTone helps you instantly identify the underlying sentiment in both text and voice.

## 🔍 Sentiment Labels

MonoTone classifies input into one of four custom sentiment categories:

- **Positive** — Expresses joy, excitement, appreciation, or other upbeat emotions  
- **Negative** — Conveys sadness, frustration, anger, or dissatisfaction  
- **Neutral** — Factual or emotionally flat messages  
- **Mixed** — Contains both positive and negative emotions or ambiguous tones  

These labels reflect the emotional complexity found in natural, informal communication.

## 🎥 Video-to-Sentiment Workflow

MonoTone supports **sentiment analysis directly from video clips** using the following process:

### How It Works

1. 📹 **Video Input**  
   Upload or reference a short video clip (e.g., `.mp4`, `.mov`).

2. 🔊 **Audio Extraction**  
   The system automatically extracts the audio track from the video using tools like `ffmpeg`.

3. 🧾 **Speech Transcription (Whisper)**  
   The audio is transcribed into text using OpenAI’s **Whisper** model, which excels at handling real-world, informal speech.

4. 🧠 **Sentiment Classification**  
   The resulting transcript is passed into MonoTone’s sentiment classifier, outputting one of: **Positive**, **Negative**, **Neutral**, or **Mixed**.

> This makes MonoTone a powerful tool for analyzing emotion in interviews, YouTube clips, vlogs, or any video content with speech.

## ✨ Features

- 🎥 Sentiment analysis from video speech
- 🔊 Audio-to-text support via Whisper
- 🧠 Fine-tuned transformer-based NLP sentiment model
- 🎯 Four-label sentiment output: Positive, Negative, Neutral, and Mixed
- 📁 Optimized for short, casual, or emotional content
- 🧪 Trained on a custom dataset of 2000+ labeled entries
- 🔄 Easily extendable and customizable
- 💻 Modular design for smooth integration into other tools

## 🛠️ Tech Stack

- Python  
- Hugging Face Transformers  
- PyTorch  
- OpenAI Whisper  
- FFmpeg (for audio extraction)  
- Google Colab (for training)  
- Scikit-learn, Pandas, NumPy  

## 📦 Dataset

MonoTone is trained on a custom dataset of 2000 short conversational sentences, labeled as **Positive**, **Negative**, **Neutral**, or **Mixed**. Labels were automatically assigned using a combination of rules and pre-trained model insights, designed to match the tone of real-world conversations.


