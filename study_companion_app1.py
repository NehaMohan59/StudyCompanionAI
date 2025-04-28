import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

MODEL_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
from transformers import pipeline

# ---------------------- BOT CLASS ----------------------
class AIStudyCompanion:
    def __init__(self):
        # Directly load the model pipeline
        self.generator = pipeline("text2text-generation", model="google/flan-t5-base")

    def generate_response(self, prompt):
        try:
            result = self.generator(prompt, max_length=1024, do_sample=False)
            return result[0]['generated_text'].strip()
        except Exception as e:
            return f"Error: {e}"

    def explain_topic(self, topic):
        prompt = f"Explain the topic '{topic}' in simple and clear language, like teaching a 10-year-old student. Use short paragraphs and examples where possible."
        return self.generate_response(prompt)

    def generate_flashcards(self, topic):
        prompt = f"Create exactly 5 flashcards based on the topic '{topic}'. Format them clearly as Question and Answer pairs, numbered from 1 to 5."
        return self.generate_response(prompt)

    def create_quiz(self, topic):
        prompt = f"Create 5 multiple-choice questions (MCQs) based on the topic '{topic}'. Each question should have 4 options (A, B, C, D) and indicate the correct answer after each question."
        return self.generate_response(prompt)

    def summarize_notes(self, notes):
        prompt = f"Summarize the following notes in a short, clear paragraph. Highlight only the most important points and avoid unnecessary repetition: {notes}"
        return self.generate_response(prompt)

    def ask_question(self, question):
        prompt = f"Answer the following question in a simple, easy-to-understand way, using examples if needed: {question}"
        return self.generate_response(prompt)

# ---------------------- STREAMLIT APP ----------------------
def main():
    st.title("🤖 AI Study Companion Bot (Local Model Version)")
    st.write("Helping you study smarter with Generative AI!")

    bot = AIStudyCompanion()

    menu = ["Explain a Topic", "Generate Flashcards", "Create a Quiz", "Summarize Notes", "Ask a Question"]
    choice = st.sidebar.selectbox("Select an Action", menu)

    if choice == "Explain a Topic":
        topic = st.text_input("Enter the topic you want explained:")
        if st.button("Explain"):
            if topic:
                explanation = bot.explain_topic(topic)
                st.success("📖 Explanation:")
                st.write(explanation)

    elif choice == "Generate Flashcards":
        topic = st.text_input("Enter the topic for flashcards:")
        if st.button("Generate Flashcards"):
            if topic:
                flashcards = bot.generate_flashcards(topic)
                st.success("🧠 Flashcards:")
                st.write(flashcards)

    elif choice == "Create a Quiz":
        topic = st.text_input("Enter the topic for the quiz:")
        if st.button("Create Quiz"):
            if topic:
                quiz = bot.create_quiz(topic)
                st.success("📝 Quiz:")
                st.write(quiz)

    elif choice == "Summarize Notes":
        notes = st.text_area("Paste your study notes here:")
        if st.button("Summarize"):
            if notes:
                summary = bot.summarize_notes(notes)
                st.success("📝 Summary:")
                st.write(summary)

    elif choice == "Ask a Question":
        question = st.text_input("Enter your question:")
        if st.button("Get Answer"):
            if question:
                answer = bot.ask_question(question)
                st.success("🤖 Answer:")
                st.write(answer)

if __name__ == "__main__":
    main()