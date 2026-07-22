import streamlit as st

# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="Modern Calculator",
    page_icon="🧮",
    layout="centered"
)

# -------------------- CUSTOM CSS --------------------

st.markdown("""
<style>

.stApp {
    background-color: #0F172A;
    color: white;
}

h1 {
    text-align: center;
    color: #38BDF8;
}

.result-box {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    margin-top: 20px;
    border: 2px solid #38BDF8;
}

div.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 50px;
    font-size: 20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- FUNCTIONS --------------------


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


# -------------------- SESSION STATE --------------------

if "history" not in st.session_state:
    st.session_state.history = []

# -------------------- SIDEBAR --------------------

with st.sidebar:
    st.title("About")

    st.write("""
    ### Modern Calculator v2.0

    Built using:
    - Python
    - Streamlit

    Features:
    - Modern UI
    - Dark Theme
    - Calculation History
    - Error Handling
    """)

# -------------------- MAIN UI --------------------

st.title("🧮 MODERN CALCULATOR")

st.write("Perform basic arithmetic operations with a beautiful interface.")

num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# -------------------- BUTTONS --------------------

col1, col2, col3, col4 = st.columns(4)

result = None

with col1:
    if st.button("+"):
        result = add(num1, num2)
        st.session_state.history.append(
            f"{num1} + {num2} = {result}")

with col2:
    if st.button("-"):
        result = subtract(num1, num2)
        st.session_state.history.append(
            f"{num1} - {num2} = {result}")

with col3:
    if st.button("×"):
        result = multiply(num1, num2)
        st.session_state.history.append(
            f"{num1} × {num2} = {result}")

with col4:
    if st.button("÷"):
        result = divide(num1, num2)
        st.session_state.history.append(
            f"{num1} ÷ {num2} = {result}")

# -------------------- RESULT CARD --------------------

if result is not None:

    st.markdown(
        f"""
        <div class="result-box">
            Result: {result}
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------- HISTORY --------------------

st.markdown("---")

st.subheader("Recent Calculations")

if st.session_state.history:

    for item in reversed(st.session_state.history[-5:]):
        st.write(f"• {item}")

else:
    st.write("No calculations yet.")