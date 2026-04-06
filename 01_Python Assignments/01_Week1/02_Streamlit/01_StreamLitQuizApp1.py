import streamlit as st
import pandas as pd
import altair as alt

# Title
st.title("Quiz App")

# Questions and answers
quiz = {
    "What is 2 + 2?": "4",
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "Who wrote Hamlet?": "Shakespeare",
    "What is 5 * 6?": "30"
}

# Store user answers
user_answers = {}

st.header("Answer the following questions:")

# Input fields for each question
for question in quiz:
    user_answers[question] = st.text_input(question)

# Submit button
if st.button("Submit"):
    correct = 0
    wrong = 0
    wrong_answers = {}

    # Check answers
    for question, answer in quiz.items():
        if user_answers[question].strip().lower() == answer.strip().lower():
            correct += 1
        else:
            wrong += 1
            wrong_answers[question] = answer

    # Calculate score percentage
    score = (correct / len(quiz)) * 100

    # Show pass/fail
    if score >= 60:
        st.success(f"PASSED! Your score is {score:.2f}%")
    else:
        st.error(f"FAILED! Your score is {score:.2f}%")

    # Show the right answers for wrong questions
    if wrong_answers:
        st.subheader("Questions you got wrong:")
        for question, correct_answer in wrong_answers.items():
            st.markdown(f"**{question}** → Correct answer: **{correct_answer}**")

    # Show graph using Altair with colors
    st.subheader("Quiz Results")
    result_df = pd.DataFrame({
        "Category": ["Correct", "Wrong"],
        "Count": [correct, wrong]
    })

    chart = alt.Chart(result_df).mark_bar().encode(
        x='Category',
        y='Count',
        color=alt.condition(
            alt.datum.Category == "Correct",
            alt.value("green"),
            alt.value("red")
        )
    )
    st.altair_chart(chart, use_container_width=True)