# 🎭 BERT Sentiment Analyzer

A transformer-based NLP sentiment analysis web app built using Python, Streamlit, Hugging Face Transformers, and DistilBERT.

## 🚀 Live Demo

[Click Here](https://bert-sentiment-analyzer-aryan.streamlit.app/)

## 📌 Features

- Positive sentiment detection
- Negative sentiment detection
- Mixed/Neutral sentiment detection using custom NLP logic
- Confidence score display
- Confidence progress bar
- Streamlit web interface
- Pre-trained DistilBERT transformer model

## 🛠️ Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- DistilBERT
- PyTorch
- NLP

## 🧠 Project Concept

This project uses a pre-trained DistilBERT model fine-tuned for sentiment analysis.  
The user enters a movie review, and the model predicts whether the sentiment is positive, negative, or mixed/neutral.

## ⚙️ How It Works

1. User enters a movie review.
2. The text is processed by a pre-trained DistilBERT sentiment model.
3. The model predicts sentiment with a confidence score.
4. Custom logic detects mixed/neutral sentiment for complex reviews.
5. The result is displayed through a Streamlit web interface.

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
