import streamlit as st
import pandas as pd
from openai import OpenAI

# -----------------------
# PAGE CONFIG
# -----------------------

st.set_page_config(page_title="Smart Student Portal")

st.title("🎓 Smart Student Portal")

menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Dashboard",
        "GPA Calculator",
        "Finance AI Chatbot",
        "Attendance Tracker"
    ]
)

# -----------------------
# DASHBOARD
# -----------------------

if menu == "Dashboard":

    st.header("Welcome Student")

    st.write("Features:")
    st.write("✅ GPA Calculator")
    st.write("✅ Finance AI Tutor")
    st.write("✅ Attendance Tracker")

# -----------------------
# GPA CALCULATOR
# -----------------------

elif menu == "GPA Calculator":

    st.header("GPA Calculator")

    subjects = st.number_input(
        "Number of Subjects",
        min_value=1,
        max_value=10,
        step=1
    )

    total_points = 0
    total_credits = 0

    grade_map = {
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }

    for i in range(subjects):

        st.subheader(f"Subject {i+1}")

        grade = st.selectbox(
            f"Grade {i+1}",
            list(grade_map.keys()),
            key=i
        )

        credits = st.number_input(
            f"Credit Hours {i+1}",
            min_value=1,
            max_value=5,
            step=1,
            key=f"c{i}"
        )

        total_points += grade_map[grade] * credits
        total_credits += credits

    if st.button("Calculate GPA"):

        gpa = total_points / total_credits

        st.success(f"Your GPA is: {round(gpa, 2)}")

# -----------------------
# OPENAI CHATBOT
# -----------------------

elif menu == "Finance AI Chatbot":

    st.header("Finance AI Tutor")

    api_key = st.text_input(
        "Enter OpenAI API Key",
        type="password"
    )

    question = st.text_area("Ask Finance Question")

    if st.button("Ask AI"):

        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a finance tutor for university students."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content

        st.write(answer)

# -----------------------
# ATTENDANCE TRACKER
# -----------------------

elif menu == "Attendance Tracker":

    st.header("Attendance Calculator")

    attended = st.number_input(
        "Classes Attended",
        min_value=0
    )

    total = st.number_input(
        "Total Classes",
        min_value=1
    )

    if st.button("Calculate Attendance"):

        percentage = (attended / total) * 100

        st.success(
            f"Attendance Percentage: {round(percentage,2)}%"
        )