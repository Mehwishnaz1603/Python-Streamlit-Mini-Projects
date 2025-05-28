import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="📊 Interactive Data Dashboard", layout="wide")

# --- Custom CSS Styling ---
st.markdown(
    """
    <style>
        .main {
            background-color: #f8f9fa;
        }
        h1 {
            color: #ff6600;
            text-align: center;
        }
        .stButton > button {
            background-color: #ff6600;
            color: white;
            font-size: 16px;
            border: none;
            padding: 0.5em 1em;
        }
        .stSidebar .sidebar-content {
            background-color: #f0f0f5;
        }
        .footer {
            margin-top: 3em;
            padding: 1em;
            text-align: center;
            color: #6c757d;
            font-size: 0.9em;
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
    """,
    unsafe_allow_html=True
)

# Title
st.title("📊 Interactive Data Dashboard")

# Sidebar - File Upload
st.sidebar.header("📂 Upload Your CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Sidebar - Data Filter
    st.sidebar.header("🔍 Filter Data")
    columns = df.columns.tolist()
    selected_column = st.sidebar.selectbox("Filter by column", columns)
    unique_values = df[selected_column].dropna().unique()
    selected_value = st.sidebar.selectbox("Value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]

    # Main - Data Display
    st.subheader("📌 Data Preview")
    st.dataframe(filtered_df, height=300)

    st.subheader("📈 Data Summary")
    st.write(filtered_df.describe())

    # Main - Chart
    st.subheader("📊 Data Visualization")

    col1, col2 = st.columns(2)
    with col1:
        x_column = st.selectbox("X-axis column", columns, key="x_axis")
    with col2:
        y_column = st.selectbox("Y-axis column", columns, key="y_axis")

    if st.button("Generate Line Chart"):
        if x_column == y_column:
            st.warning("⚠️ Please select different columns for X and Y axes.")
        else:
            try:
                st.line_chart(filtered_df.set_index(x_column)[y_column])
            except Exception as e:
                st.error(f"❌ Could not generate chart: {e}")
else:
    st.info("📥 Please upload a CSV file from the sidebar to begin.")

# --- Footer ---
st.markdown(
    """
    <div class="footer">
        🛠️ Built by <b>Mehwish Naz</b> ❤️ using <a href="https://streamlit.io" by Mehwish Naz target="_blank">Streamlit</a> |
        GitHub: <a href="https://github.com/mehwishnaz1603/" target="_blank">View Code</a><br>
        © 2025 Data Dashboard App
    </div>
    """,
    unsafe_allow_html=True
)
