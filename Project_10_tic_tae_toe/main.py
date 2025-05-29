import streamlit as st
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="🎮",
    layout="centered"
)

# Sidebar settings
st.sidebar.header("Settings")
dark_mode = st.sidebar.toggle("Dark Mode", value=False)

# Game state initialization
if 'board' not in st.session_state:
    st.session_state.board = np.full((3, 3), "")
if 'current_player' not in st.session_state:
    st.session_state.current_player = "X"
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'winner' not in st.session_state:
    st.session_state.winner = None

# --- Game Logic Functions ---
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i, j] == player for j in range(3)) or all(board[j, i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i, i] == player for i in range(3)) or all(board[i, 2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != "" for cell in board.flatten())

def make_move(row, col):
    if st.session_state.game_over or st.session_state.board[row, col] != "":
        return
    st.session_state.board[row, col] = st.session_state.current_player
    if check_winner(st.session_state.board, st.session_state.current_player):
        st.session_state.game_over = True
        st.session_state.winner = st.session_state.current_player
    elif is_board_full(st.session_state.board):
        st.session_state.game_over = True
        st.session_state.winner = "Draw"
    else:
        st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

def reset_game():
    st.session_state.board = np.full((3, 3), "")
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

# --- UI Styling ---
board_bg = "#222" if dark_mode else "#f9f9f9"
text_color = "#fff" if dark_mode else "#000"
st.markdown(
    f"""
    <style>
    div[data-testid="stButton"] > button {{
        width: 80px;
        height: 80px;
        font-size: 32px;
        background-color: {board_bg} !important;
        color: {text_color} !important;
        border: 2px solid #888;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 5px;
    }}
    @media (max-width: 600px) {{
        div[data-testid="stButton"] > button {{
            width: 60px !important;
            height: 60px !important;
            font-size: 24px !important;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- App Title ---
st.title("Tic Tac Toe Game")
st.markdown("A classic two-player game built with Streamlit")

# --- Game Status ---
if st.session_state.game_over:
    if st.session_state.winner == "Draw":
        st.subheader("Game Over: It's a Draw! 🤝")
    else:
        st.subheader(f"Game Over: Player {st.session_state.winner} wins! 🎉")
else:
    st.subheader(f"Current Player: {st.session_state.current_player}")

# --- Game Board ---
st.write("---")
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        cell_value = st.session_state.board[row, col]
        button_label = cell_value if cell_value else " "
        button_key = f"cell_{row}_{col}"
        with cols[col]:
            if st.button(button_label, key=button_key):
                make_move(row, col)
                st.rerun()

# --- Reset Button ---
st.write("---")
if st.button("New Game", type="primary"):
    reset_game()
    st.rerun()

# --- Instructions ---
with st.expander("How to Play"):
    st.write("""
    1. Players take turns placing X or O on the board.
    2. The first player to get 3 in a row (horizontally, vertically, or diagonally) wins.
    3. If the board is full with no winner, it's a draw.
    4. Use the sidebar to toggle Dark Mode.
    """)

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: gray;'>
        🎮 Built by <b> Mehwish Naz</b> ❤️ using Streamlit |
        <a href='https://github.com/mehwishnaz1603' target='_blank'>GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
