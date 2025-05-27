import streamlit as st
import random
import string

# --- PAGE CONFIG ---
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")


# --- TITLE ---
st.title("🔐 Random Password Generator")
st.write("Customize your password and generate it instantly!")

# --- USER OPTIONS ---
length = st.slider("🔢 Password Length:", min_value=4, max_value=100, value=12)
use_upper = st.checkbox("Include Uppercase Letters (A-Z)", value=True)
use_lower = st.checkbox("Include Lowercase Letters (a-z)", value=True)
use_digits = st.checkbox("Include Numbers (0-9)", value=True)
use_symbols = st.checkbox("Include Symbols (!@#$...)", value=True)

# --- GENERATE PASSWORD ---
def generate_password(length, upper, lower, digits, symbols):
    characters = ""
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    if not characters:
        return None
    return ''.join(random.choice(characters) for _ in range(length))

# --- BUTTON ---
if st.button("🚀 Generate Password"):
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    if password:
        st.success("✅ Your Password is Ready!")
        st.code(password, language="text")
        st.download_button("📥 Download Password as .txt", data=password, file_name="password.txt")
    else:
        st.warning("⚠️ Please select at least one character type.")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        🔐 Built with ❤️ by <b>Mehwish Naz</b> | © 2025 Secure Password Generator
    </div>
""", unsafe_allow_html=True)
