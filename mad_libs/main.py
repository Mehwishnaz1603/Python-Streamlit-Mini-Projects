import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mad Libs Game", page_icon="📖", layout="centered")

# --- BACKGROUND COLOR + FOOTER STYLE ---
st.markdown("""
    <style>
        .stApp {
            background-color: #f9f9f9;
            padding-bottom: 80px;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            font-size: 0.9em;
            color: gray;
            background-color: #e0eafc;
            padding: 10px 0;
        }
        .story-box {
            background-color: #ffffff;
            padding: 1.5em;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.title("📖 Personalized Mad Libs Game")
st.write("Fill in the blanks to create a fun story about yourself!")

# --- INPUT FORM ---
with st.form("mad_libs_form"):
    name = st.text_input("Your Name")
    age = st.text_input("Your Age")
    hobby = st.text_input("Your Favorite Hobby")
    personality = st.text_input("Describe Yourself in One Word")
    fav_place = st.text_input("A Place You Love Visiting")
    dream_job = st.text_input("Your Dream Job")
    submitted = st.form_submit_button("Generate Story")

# --- DISPLAY STORY IF COMPLETE ---
if submitted:
    if name and age and hobby and personality and fav_place and dream_job:
        story = f"""
        <div class='story-box'>
            <h3>📚 Here's Your Story!</h3>
            <p>
                Meet <b>{name}</b>, a <b>{age}</b>-year-old who is known to be very <b>{personality}</b> and absolutely loves <b>{hobby}</b>.
                When {name} has free time, they love visiting <b>{fav_place}</b>. <br><br>
                One day, {name} hopes to fulfill their dream of becoming a <b>{dream_job}</b>. <br>
                The journey ahead is full of excitement and endless possibilities! 🌟
            </p>
        </div>
        """
        st.markdown(story, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please fill in all the blanks to generate your story!")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        📝 Created with ❤️ by <b>Mehwish Naz</b> | © 2025 Mad Libs Game
    </div>
""", unsafe_allow_html=True)
