import streamlit as st
from datetime import date
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Birthday Wisher", page_icon="🎂", layout="centered")

# --- STYLE ---
st.markdown("""
    <style>
    .stApp {
        background-color: #fff7f0;
        padding-bottom: 80px;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        font-size: 0.9em;
        color: gray;
        background-color: #ffe9d6;
        padding: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.title("🎉 Happy Birthday Wisher 🎂")

# --- INPUT ---
name = st.text_input("🎈 Enter the birthday person's name:")
birthday = st.date_input("📅 Enter their birthday:")

today = date.today()

# --- BUTTON ---
if st.button("🎁 Send Birthday Wish"):
    if name:
        if birthday.month == today.month and birthday.day == today.day:
            with st.spinner("Preparing surprise 🎈..."):
                time.sleep(1)
                st.write("🎈")
                time.sleep(0.5)
                st.write("🎈🎈")
                time.sleep(0.5)
                st.write("🎈🎈🎈")
                time.sleep(0.5)
            st.success(f"🎉 Happy Birthday, {name}! 🎂\n\nWishing you a day full of smiles and joy!")
            st.balloons()
        else:
            st.info(f"Hi {name}, your birthday is on {birthday.strftime('%B %d')} — we’ll be ready to celebrate! 🎊")
    else:
        st.warning("⚠️ Please enter a name to send the wish!")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        🎂 Built with ❤️ by <b>Mehwish Naz </b> | © 2025 Birthday Wisher App
    </div>
""", unsafe_allow_html=True)
