import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Guess the Number", page_icon="🎲", layout="centered")

# --- BACKGROUND STYLE ---
st.markdown("""
    <style>
        .stApp {
            background-color: #f2f7ff;
            padding-bottom: 80px;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            font-size: 0.85em;
            color: gray;
            background-color: #e9f0f7;
            padding: 10px 0;
        }
        .guess-box {
            background-color: #ffffff;
            padding: 1em;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        }
    </style>
""", unsafe_allow_html=True)

# --- INIT GAME STATE ---
if "low" not in st.session_state:
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = random.randint(1, 100)
    st.session_state.attempts = 1
    st.session_state.history = []
    st.session_state.success = False

# --- TITLE ---
st.title("🎯 Computer Guess The Number")
st.write("Think of a number between **1 and 100**, and let the computer try to guess it!")

# --- DISPLAY GUESS ---
with st.container():
    st.markdown(f"<div class='guess-box'><h3>🤖 Is your number: <span style='color:#3366cc'>{st.session_state.guess}</span>?</h3></div>", unsafe_allow_html=True)

# --- INPUT FORM ---
with st.form("feedback_form", clear_on_submit=True):
    feedback = st.text_input("🗣️ Enter 'b' = too big, 's' = too small, 'c' = correct").strip().lower()
    submitted = st.form_submit_button("Submit Feedback")

# --- FEEDBACK HANDLING ---
if submitted:
    if feedback not in ["b", "s", "c"]:
        st.error("🚫 Please enter only 'b', 's', or 'c'.")
    else:
        st.session_state.history.append(st.session_state.guess)

        if feedback == "c":
            st.success(f"🎉 The computer guessed your number: {st.session_state.guess} in {st.session_state.attempts} attempts!")
            st.session_state.success = True

        elif feedback == "b":
            st.session_state.high = st.session_state.guess - 1
        elif feedback == "s":
            st.session_state.low = st.session_state.guess + 1

        if feedback in ["b", "s"]:
            if st.session_state.low > st.session_state.high:
                st.error("❗ Conflicting hints! You may have made a mistake.")
            else:
                st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
                st.session_state.attempts += 1
                st.rerun()

# --- GAME STATUS ---
if not st.session_state.success:
    st.info(f"🕹️ Attempts so far: {st.session_state.attempts}")
    if st.session_state.history:
        st.write("📜 Guess history:", ", ".join(str(g) for g in st.session_state.history))

# --- PLAY AGAIN ---
if st.session_state.success:
    if st.button("🔁 Play Again"):
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.guess = random.randint(1, 100)
        st.session_state.attempts = 1
        st.session_state.history = []
        st.session_state.success = False
        st.rerun()

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        💻 Made with ❤️ <b> Mehwish Naz </b> using Streamlit | © 2025 Guess The Number Game
    </div>
""", unsafe_allow_html=True)
