AI Study Companion

Final Project Submission – COT6930 – Spring 2025  
Group: Genesis  
Members: Neha Mohana, Smruthi Sharath Bejwadi, Tribhuvana Avvaru

Project Overview

**AI Study Companion** is an intelligent, student-friendly web application that supports academic learning using Hugging Face Generative AI models.
It provides explanations, flashcards, quizzes, summaries, and answers to academic questions through an easy-to-use Streamlit interface, all without any subscription cost.

Tech Stack

- **Python** (Streamlit, requests)
- **Generative AI Model**: `google/flan-t5-large` (Hugging Face Inference API)
- **Frontend**: Streamlit Web App
- **Backend**: Smart prompt engineering, Hugging Face model interaction

Solution Features

- Explain topics clearly with examples.
- Generate organized flashcards with questions and answers.
- Create multiple-choice quizzes with correct answers.
- Summarize lengthy study notes into concise key points.
- Answer free-form academic questions intelligently.

Solution Flow

1. Student selects a function: **Explain**, **Flashcards**, **Quiz**, **Summarize**, or **Ask**.
2. System builds a smart, detailed prompt based on the selection.
3. Sends prompt to `google/flan-t5-large` model hosted on Hugging Face.
4. Receives organized response.
5. Displays the formatted output through the Streamlit interface.

If user input is empty or API fails, the app gracefully notifies the user.

Functional Requirements

| Feature | Priority | Complexity | Expected Outcome |
|--------|----------|------------|------------------|
| Explain a topic | High | Medium | Short, clear explanation with examples |
| Create MCQs | High | Medium | Well-formed multiple-choice quizzes |
| Generate Flashcards | High | Medium | Flashcards with Q&A |
| Summarize Notes | High | Medium | Clear and short summaries |
| Free-style Question Answering | High | Medium | Friendly detailed answer |
| Validate user input | High | Low | Prompt warning if input is missing |
| API Error Handling | High | Medium | Smooth handling of API failures |
| Local and Online Deployment | Medium | Medium | Access via localhost or Hugging Face Spaces |

Non-Functional Requirements

- Fast responses (<20 seconds)
- Free to use with no subscriptions
- Simple, attractive, accessible UI (Streamlit)
- Privacy: No storage of user inputs
- Platform compatible (Windows, Mac, Linux)
- Secure error handling
- Open-source compliant

Solution Architecture

- **Streamlit Web Interface**: Accepts user input and displays output.
- **Input Validator**: Checks empty or invalid inputs.
- **Prompt Builder**: Constructs intelligent prompts.
- **Hugging Face Inference API**: Calls the AI model.
- **Response Formatter**: Organizes the model's outputs.
- **Session Manager**: Stores and displays user history during the session.

System Modeling

Sequence Diagram Highlights:
- Student selects a function.
- Input validated.
- Prompt built.
- API call made.
- Response formatted and displayed.
- Session history recorded.

Class/Object Diagram:
- `StudentUser` interacts with `WebInterface`
- `UserInputValidator`, `PromptBuilder`, `HuggingFaceInferenceAPI`, and `ResponseFormatter` manage workflow.
- `SessionManager` logs session interactions.

Prototype Implementation

- Application Script: `study_companion_app.py`
- Framework: Streamlit App
- AI Model: `google/flan-t5-large` via Hugging Face Inference API
- Deployment: Locally via Streamlit or on Hugging Face Spaces

How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/NehaMohan59/StudyCompanionAI.git
cd StudyCompanionAI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your `.env` file:
```env
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

4. Run the application:
```bash
streamlit run study_companion_app.py
```

5. Open the Streamlit URL (usually http://localhost:8501) to interact.

Repository

GitHub Repository: [StudyCompanionAI](https://github.com/NehaMohan59/StudyCompanionAI)


Screenshots

- Dropdown menu to select study support tools.
- Example of explaining "What is GenAI".
- Example of flashcard generation for "Reinforcement Learning".
- Example quiz created for "Biology".
- Example summary notes.
- Example factual question answering.

Academic Context

Developed by Genesis Group for **COT6930 – Advanced Topics in Artificial Intelligence** at **Florida Atlantic University** (Spring 2025).

Created by **Genesis**