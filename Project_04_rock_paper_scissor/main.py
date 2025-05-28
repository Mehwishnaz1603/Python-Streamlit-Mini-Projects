import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Rock, Paper, Scissors", page_icon="🎮", layout="centered")


# --- TITLE ---
st.title("🎮 Rock, Paper, Scissors Game!")
st.write("Choose your move and try to beat the computer!")

# --- GAME CHOICES ---
choices = ["rock", "paper", "scissor"]
emoji = {"rock": "🪨", "paper": "📄", "scissor": "✂️"}

# --- INIT SCORE ---
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0

# --- USER CHOICE ---
user_choice = st.selectbox("👉 Your Choice:", choices, format_func=lambda x: f"{emoji[x]} {x.title()}")

# --- PLAY BUTTON ---
if st.button("▶️ Play!"):
    computer_choice = random.choice(choices)
    
    st.markdown(f"💻 **Computer Chose:** {emoji[computer_choice]} {computer_choice.title()}")
    
    if user_choice == computer_choice:
        st.info("🤝 It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        st.session_state.user_score += 1
        st.success("🎉 You win!")
        st.balloons()
    else:
        st.session_state.computer_score += 1
        st.error("😞 You lose, computer wins!")

# --- SCORE DISPLAY ---
st.markdown(f"### 🏆 Scoreboard")
st.markdown(f"**You:** {st.session_state.user_score} | **Computer:** {st.session_state.computer_score}")

# --- RESET BUTTON ---
if st.button("🔄 Reset Scores"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.success("✅ Scores have been reset!")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        🎮 Game built with ❤️ by <b>Mehwish Naz</b> | © 2025 Rock-Paper-Scissors App
    </div>
""", unsafe_allow_html=True)
