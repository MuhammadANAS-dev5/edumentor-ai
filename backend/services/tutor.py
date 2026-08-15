from services.llm import generate_response


def tutor(question, language="English"):
    question = question.strip()

    if not question:
        return "Please enter a question."

    prompt = f"""
You are EduMentor AI, a helpful educational tutor.

Student question:
{question}

Response language:
{language}

Explain the concept clearly and at an appropriate level for a student.
"""

    response = generate_response(prompt)

    return response