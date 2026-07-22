import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Modern Calculator",
    page_icon="🧮",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    padding-top: 2rem;
}
h1 {
    text-align: center;
}
.result {
    font-size: 28px;
    font-weight: bold;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Functions
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


# Title
st.title("🧮 Modern Calculator")
st.write("Perform basic arithmetic operations with a clean interface.")

# Inputs
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

operation = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Button
if st.button("Calculate"):

    if operation == "Addition":
        result = add(num1, num2)

    elif operation == "Subtraction":
        result = subtract(num1, num2)

    elif operation == "Multiplication":
        result = multiply(num1, num2)

    else:
        result = divide(num1, num2)

    st.success(f"Result: {result}")