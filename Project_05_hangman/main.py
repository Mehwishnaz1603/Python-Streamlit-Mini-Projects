import streamlit as st
import random

# --------- CONFIG ---------
st.set_page_config(page_title="Hangman Game App", page_icon="🕹️", layout="centered")

# --------- FOOTER WITH CUSTOM CSS ---------
custom_footer = """
<style>
.footer {
    position: relative;
    bottom: 0;
    width: 100%;
    margin-top: 3em;
    padding: 1em 0;
    background-color: #f5f5f5;
    text-align: center;
    font-size: 0.9em;
    color: #6c757d;
    border-top: 1px solid #ddd;
}

.footer a {
    color: #0366d6;
    text-decoration: none;
    font-weight: 500;
}

.footer a:hover {
    text-decoration: underline;
    color: #004080;
}
</style>

<div class="footer">
    🛠️ Developed with ❤️ using <a href="https://streamlit.io" target="_blank">Streamlit</a><br>
    © 2025 Hangman Web App · <a href="https://github.com/yourusername/hangman-streamlit" target="_blank">View Code on GitHub</a>
</div>
"""

st.markdown(custom_footer, unsafe_allow_html=True)


# --------- CONSTANTS ---------
WORD_LIST = ['python', 'hangman', 'streamlit', 'challenge', 'developer', 'interface', 'algorithm']
MAX_TRIES = 8
HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ==='''
]

# --------- INIT GAME ---------
def initialize_game():
    st.session_state.word = random.choice(WORD_LIST).lower()
    st.session_state.display = ['_'] * len(st.session_state.word)
    st.session_state.tries_left = MAX_TRIES
    st.session_state.guessed_letters = set()
    st.session_state.game_over = False
    st.session_state.won = False

def guess_letter(letter):
    if letter in st.session_state.guessed_letters or st.session_state.game_over:
        return

    st.session_state.guessed_letters.add(letter)

    if letter in st.session_state.word:
        for idx, char in enumerate(st.session_state.word):
            if char == letter:
                st.session_state.display[idx] = letter
    else:
        st.session_state.tries_left -= 1

    if '_' not in st.session_state.display:
        st.session_state.won = True
        st.session_state.game_over = True
    elif st.session_state.tries_left == 0:
        st.session_state.game_over = True

# --------- PAGE HEADER ---------
st.title("🕹️ Hangman Game")
st.subheader("A classic word-guessing game built with Streamlit")
st.markdown("Guess the word one letter at a time. You have 6 tries. Good luck!")

# --------- GAME INIT ---------
if 'word' not in st.session_state:
    initialize_game()

# --------- LAYOUT ---------
col1, col2 = st.columns([1, 2])

with col1:
    st.text("HANGMAN STATUS")
    st.code(HANGMAN_PICS[MAX_TRIES - st.session_state.tries_left], language="text")

with col2:
    st.markdown(f"**Word:** {' '.join(st.session_state.display)}")
    st.markdown(f"**Guessed Letters:** `{', '.join(sorted(st.session_state.guessed_letters))}`")
    st.markdown(f"**Tries Left:** `{st.session_state.tries_left}`")
    st.markdown(f"**Word Length:** {len(st.session_state.word)} letters")

# --------- GUESS INPUT ---------
if not st.session_state.game_over:
    with st.form("guess_form", clear_on_submit=True):
        letter = st.text_input("Enter a letter:", max_chars=1).lower()
        submitted = st.form_submit_button("Guess")
        if submitted:
            if letter.isalpha() and len(letter) == 1:
                guess_letter(letter)
            else:
                st.warning("Please enter a single alphabetical character.")

# --------- GAME RESULT ---------
if st.session_state.game_over:
    if st.session_state.won:
        st.success(f"🎉 You won! The word was **{st.session_state.word}**.")
    else:
        st.error(f"💀 You lost. The word was **{st.session_state.word}**.")

    st.button("🔁 Play Again", on_click=initialize_game)
    
# --------- FOOTER ---------
st.markdown("""<hr style="margin-top: 3em; margin-bottom: 1em;">""", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: center; color: grey; font-size: 0.9em;">
        🛠️ Developed with ❤️ using <a href="https://streamlit.io" target="_blank">Streamlit</a><br>
        © 2025 Hangman Web App · GitHub: <a href="https://github.com/mehwishnaz1603/" target="_blank">View Code</a>
    </div>
    """,
    unsafe_allow_html=True
)

