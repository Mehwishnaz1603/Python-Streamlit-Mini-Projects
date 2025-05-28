import streamlit as st
import random

# --- Page Config ---
st.set_page_config(page_title="🎯 Number Guessing Game", layout="centered")
# --- TITLE ---
st.title("🎮 Number Guesing Game!")
st.write("Choose your move and try to beat the computer!")


# --- Custom CSS + Footer ---
st.markdown("""
    <style>
        .stButton > button {
            background-color: #ff6600;
            color: white;
            padding: 0.5em 1em;
            font-size: 16px;
        }
        .footer {
            margin-top: 3em;
            padding: 1em;
            text-align: center;
            font-size: 0.9em;
            color: #6c757d;
            border-top: 1px solid #ddd;
        }
        .footer a {
            color: #ff6600;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# --- Initialize Session State ---
def initialize_game(difficulty_level):
    difficulty_settings = {
        "Easy (1–50)": (1, 50, 10),
        "Medium (1–100)": (1, 100, 7),
        "Hard (1–500)": (1, 500, 5)
    }
    low, high, max_attempts = difficulty_settings[difficulty_level]
    st.session_state.low = low
    st.session_state.high = high
    st.session_state.target = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.max_attempts = max_attempts
    st.session_state.guess_history = []
    st.session_state.game_over = False
    st.session_state.difficulty = difficulty_level

# --- Difficulty Selection ---
if 'target' not in st.session_state:
    st.markdown("### 🕹️ Select Difficulty to Start:")
    difficulty = st.selectbox("Difficulty", ["Easy (1–50)", "Medium (1–100)", "Hard (1–500)"])
    if st.button("Start Game"):
        initialize_game(difficulty)
    st.stop()

# --- Game Title & Info ---
st.title("🎯 Number Guessing Game")
st.markdown(f"Guess a number between **{st.session_state.low}** and **{st.session_state.high}**")
st.markdown(f"🧠 Difficulty: **{st.session_state.difficulty}** | 🔁 Attempts Left: **{st.session_state.max_attempts - st.session_state.attempts}**")

# --- User Input ---
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=st.session_state.low,
                            max_value=st.session_state.high, step=1, key="user_guess")
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        st.session_state.guess_history.append(guess)

        if guess < st.session_state.target:
            st.info("🔼 Too low! Try a higher number.")
        elif guess > st.session_state.target:
            st.info("🔽 Too high! Try a lower number.")
        else:
            st.success(f"🎉 Correct! The number was **{st.session_state.target}**.")
            st.balloons()
            st.session_state.game_over = True

        if st.session_state.attempts >= st.session_state.max_attempts and not st.session_state.game_over:
            st.session_state.game_over = True
            st.error(f"❌ Game Over! The number was **{st.session_state.target}**.")

# --- Show Guess History ---
if st.session_state.attempts > 0:
    st.markdown("### 📉 Your Guesses:")
    st.write(st.session_state.guess_history)

# --- Play Again Button ---
if st.session_state.game_over:
    if st.button("🔁 Play Again"):
        initialize_game(st.session_state.difficulty)

# --- Footer ---
st.markdown("""
<div class="footer">
    🛠️ Built by <b> Mehwish Naz </b> ❤️ using <a href="https://streamlit.io" target="_blank">Streamlit</a> |
    <a href="https://github.com/mehwishnaz1603/" target="_blank">GitHub Repo</a><br>
    © 2025 Number Guessing Game
</div>
""", unsafe_allow_html=True)
