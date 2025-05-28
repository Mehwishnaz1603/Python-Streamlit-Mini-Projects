import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Countdown Timer App", page_icon="⏲️", layout="centered")

# --- BACKGROUND STYLE ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f8ff;
        padding-bottom: 80px;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        font-size: 0.85em;
        color: gray;
        background-color: #e0eafc;
        padding: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.title("⏲️ Countdown Timer")
st.write("Set a duration and watch it count down in real-time with a progress bar.")

# --- INPUT ---
duration = st.number_input("🕒 Enter time in seconds:", min_value=1, max_value=3600, value=10, step=1)

# --- TIMER START ---
if st.button("▶️ Start Timer"):
    timer_placeholder = st.empty()
    progress_bar = st.progress(0)
    for i in range(duration, 0, -1):
        timer_placeholder.markdown(f"## ⏳ {i} seconds remaining...")
        progress_bar.progress((duration - i + 1) / duration)
        time.sleep(1)
    timer_placeholder.markdown("## ⌛ Time's up!")
    progress_bar.progress(1)
    st.balloons()
    st.success("✅ Countdown completed!")

# --- RESET ---
if st.button("🔄 Reset Timer"):
    st.rerun()

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        ⏲️ Built with ❤️ using Streamlit | Made by <b>Mehwish Naz</b> <br>  © 2025 Countdown Timer App
    </div>
""", unsafe_allow_html=True)

