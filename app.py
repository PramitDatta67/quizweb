import streamlit as st
import json
import os

# Quiz data structure
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which language is primarily used in Streamlit?",
        "options": ["Java", "Python", "C++", "JavaScript"],
        "answer": "Python"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Tech Modern Language",
            "Home Tool Markup Language",
            "Hyperlinks and Text Markup Language"
        ],
        "answer": "Hyper Text Markup Language"
    }
]

def main():
    st.title("Quiz Application")
    
    # Initialize session state
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_completed = False
        st.session_state.selected_option = None
        st.session_state.answer_submitted = False
    
    # Display quiz progress
    st.subheader(f"Question {st.session_state.current_question + 1} of {len(quiz_data)}")
    progress_bar = st.progress((st.session_state.current_question + 1) / len(quiz_data))
    
    if not st.session_state.quiz_completed:
        # Display current question
        current_q = quiz_data[st.session_state.current_question]
        st.write(f"**{current_q['question']}**")
        
        # Display options as radio buttons
        selected = st.radio(
            "Select your answer:",
            current_q['options'],
            key=f"question_{st.session_state.current_question}",
            disabled=st.session_state.answer_submitted
        )
        
        st.session_state.selected_option = selected
        
        # Submit button
        if not st.session_state.answer_submitted:
            if st.button("Submit"):
                st.session_state.answer_submitted = True
                if selected == current_q['answer']:
                    st.session_state.score += 1
                    st.success("Correct! 🎉")
                else:
                    st.error(f"Wrong! The correct answer is: {current_q['answer']}")
        
        # Next question or finish quiz
        if st.session_state.answer_submitted:
            if st.session_state.current_question < len(quiz_data) - 1:
                if st.button("Next Question"):
                    st.session_state.current_question += 1
                    st.session_state.answer_submitted = False
                    st.session_state.selected_option = None
                    st.rerun()
            else:
                if st.button("Finish Quiz"):
                    st.session_state.quiz_completed = True
                    st.rerun()
    else:
        # Quiz completed - show results
        st.header("Quiz Completed!")
        st.subheader(f"Your score: {st.session_state.score}/{len(quiz_data)}")
        st.write(f"Percentage: {(st.session_state.score / len(quiz_data)) * 100:.2f}%")
        
        # Restart quiz button
        if st.button("Restart Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.quiz_completed = False
            st.session_state.selected_option = None
            st.session_state.answer_submitted = False
            st.rerun()

if __name__ == "__main__":
    main()