
from sympy.parsing.sympy_parser import null
import streamlit as st
import pandas as pd

# ---------------- TITLE ----------------
st.title("🎓 Student Dashboard")

# ---------------- SIDEBAR ----------------
st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Choose Page",
    ["Home", "About"]
)

# ---------------- HOME PAGE ----------------
if option == "Home":

    st.header("Student Information")

    # Messages
    st.success("Login Successful")
    st.error("Invalid Password")
    st.warning("Please Enter All Fields")
    st.info("This is Information")

    # Columns
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Enter Name")
        if name != "":
            st.success("Welcome " + name)
        else:
            st.error("Please Enter Your Name")
        age = st.number_input("Enter Age",1,100)
        if age != 0.00:
            st.success("You are " + str(age) + " years old")
        else:
            st.error("Please Enter Your Age")

    with col2:
        course = st.selectbox(
            "Choose Course",
            ["Python", "AI", "Data Science"]
        )

        gender = st.radio(
            "Gender",
            ["Male", "Female"]
        )

    agree = st.checkbox("I Agree")

    value = st.slider("Skill Level", 0, 100)

    # Submit Button
    if st.button("Submit"):

        st.success("Form Submitted Successfully")

        st.subheader("Student Details")

        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Course:", course)
        st.write("Gender:", gender)
        st.write("Skill Level:", value)

    # ---------------- DATA TABLE ----------------
    st.header("Student Records")

    data = pd.DataFrame({
        "Name": ["Aman", "Riya"],
        "Age": [22, 24]
    })

    st.dataframe(data)

    # ---------------- TABS ----------------
    tab1, tab2 = st.tabs(["Overview", "Form"])

    with tab1:
        st.write("Dashboard Overview")

    with tab2:

        with st.form("my_form"):

            student = st.text_input("Student Name")

            submit = st.form_submit_button("Submit")

            if submit:
                st.success("Form Submitted")

# ---------------- ABOUT PAGE ----------------
if option == "About":

    st.header("About")

    st.info("This dashboard is created using Streamlit.")

