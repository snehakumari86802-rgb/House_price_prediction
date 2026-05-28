import streamlit as st


st.set_page_config(page_title="Calculator App",layout="wide",initial_sidebar_state="expanded"
)

st.title("Calculator App")

st.header("Simple Calculator Using Streamlit")
st.subheader(
    "Perform basic arithmetic operations like Addition, "
    "Subtraction, Multiplication, and Division."
)


num1 = st.number_input("Enter the first number:",min_value=0.0,max_value=100.0,value=0.0)

num2 = st.number_input("Enter the second number:",min_value=0.0,max_value=100.0,value=0.0)


operation = st.selectbox("Select an operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)


if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")

    elif operation == "Division":

        if num2 == 0:
            st.error("Cannot divide by zero.")

        else:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")

with st.sidebar:

    st.header("About the app")
    st.write("## This is a simple calculator app built in the streamlit framework")
    st.write("You can perform basic arithmetic operations like addition, subtraction, multiplication, and division.")
    st.write("Enter the numbers you want to calculate")
