# 🤖 Chatbot Mistral 7B - Bubble Style

Ini adalah chatbot seperti ChatGPT yang dibuat menggunakan Streamlit dan model Mistral 7B (gratis) dari OpenRouter.

## 🎯 Fitur
- UI bubble-style seperti ChatGPT
- Model ringan dan gratis: `mistralai/mistral-7b-instruct:free`
- Menyimpan riwayat percakapan di sesi
- Terhubung ke OpenRouter API dengan aman via `secrets.toml`
- Penanganan error otomatis

## 🛠️ Cara Menjalankan

1. Install Dependensi
```bash
pip install streamlit requests

2. Buat Folder .streamlit dan File secrets.toml
# File: .streamlit/secrets.toml
OPENROUTER_API_KEY = "ISI_API_KEY_MU_DI_SINI"

3. streamlit run app.py


