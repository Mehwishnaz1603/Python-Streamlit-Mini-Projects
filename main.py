import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="BMI Calculator App", page_icon="🧮", layout="centered")

# --- BACKGROUND COLOR ---
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f0f8ff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- SESSION STATE FOR HISTORY ---
if "bmi_history" not in st.session_state:
    st.session_state.bmi_history = []

# --- TITLE ---
st.title("🧮 BMI Calculator")

# --- INPUTS ---
height = st.slider("📏 Enter your height (cm):", min_value=100, max_value=250, value=170)
weight = st.slider("🏋️ Enter your weight (kg):", min_value=20, max_value=200, value=70)

# --- CALCULATION ---
bmi = weight / ((height / 100) ** 2)

# --- CLASSIFICATION & COLOR ---
if bmi < 18.5:
    status = "Underweight 😟"
    color = "orange"
elif 18.5 <= bmi < 25:
    status = "Normal weight ✅"
    color = "green"
elif 25 <= bmi < 30:
    status = "Overweight ⚠️"
    color = "darkorange"
else:
    status = "Obesity ❗"
    color = "red"

# --- DISPLAY RESULT ---
st.markdown(f"<h3 style='color:{color};'>Your BMI is: {bmi:.2f} — {status}</h3>", unsafe_allow_html=True)

# --- BMI CATEGORIES ---
with st.expander("📊 BMI Categories"):
    st.markdown("""
    - **Underweight**: BMI < 18.5  
    - **Normal weight**: 18.5 ≤ BMI < 25  
    - **Overweight**: 25 ≤ BMI < 30  
    - **Obesity**: BMI ≥ 30  
    """)

# --- SAVE TO HISTORY ---
if st.button("💾 Save this BMI"):
    st.session_state.bmi_history.append({
        "height": height,
        "weight": weight,
        "bmi": round(bmi, 2),
        "status": status
    })
    st.success("BMI saved to session history!")

# --- HISTORY ---
if st.session_state.bmi_history:
    st.subheader("📜 BMI History (This Session)")
    for i, entry in enumerate(reversed(st.session_state.bmi_history), 1):
        st.write(f"{i}. Height: {entry['height']} cm | Weight: {entry['weight']} kg | BMI: {entry['bmi']} — {entry['status']}")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 0.9em;'>
        🧮 Built with ❤️ using Streamlit | Made by <b>Mehwish Naz</b><br>
        © 2025 BMI Calculator App
    </div>
    """,
    unsafe_allow_html=True
)
