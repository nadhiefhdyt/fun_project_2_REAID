import streamlit as st
import requests
import json

# ========== CONFIG ==========
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

# ========== HEADER ==========
st.markdown("""
    <h1 style='text-align: center;'>🤖 AI Chatbot - Bubble Style</h1>
    <p style='text-align: center; font-size: 16px; color: gray;'>
        Powered by <code>mistralai/mistral-7b-instruct:free</code> via OpenRouter 🌐
    </p>
""", unsafe_allow_html=True)

# ========== MODEL & API ==========
model = "mistralai/mistral-7b-instruct:free"


def get_ai_response(messages_payload):
    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
    except KeyError:
        st.error("❌ API key tidak ditemukan. Tambahkan ke .streamlit/secrets.toml")
        return "⚠️ API key tidak tersedia."

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
                "HTTP-Referer": "http://localhost:8501",
                "X-Title": "Streamlit Chatbot"
            },
            data=json.dumps({
                "model": model,
                "messages": messages_payload,
                "max_tokens": 1000,
                "temperature": 0.7
            }),
            timeout=15  # Error handling: time-out
        )

        if response.status_code != 200:
            st.error(f"API Error {response.status_code}: {response.text}")
            return "⚠️ Terjadi error saat memanggil API."

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "⚠️ Waktu tunggu habis. Coba lagi nanti."
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error jaringan: {str(e)}"
    except Exception as e:
        return f"⚠️ Error tidak diketahui: {str(e)}"

# ========== SESSION ==========
if "messages" not in st.session_state:
    st.session_state.messages = []

# ========== RIWAYAT CHAT ==========
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ========== INPUT USER ==========
if prompt := st.chat_input("Tulis pesan di sini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Berpikir..."):
            messages_for_api = st.session_state.messages.copy()
            ai_reply = get_ai_response(messages_for_api)

        st.markdown(ai_reply)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
