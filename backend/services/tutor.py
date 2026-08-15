from services.llm import generate_response


def tutor(question, language):
    """Generate an educational response in the selected language."""

    if language == "English":
        language_instruction = """
Respond completely in English.
Use simple and clear language suitable for a university student.
"""

    elif language == "Urdu":
        language_instruction = """
Respond completely in Urdu.
Use Urdu script.
Keep important technical terms such as
Python, C++, OOP, algorithm, API, and AI in English
when appropriate.
"""

    else:
        language_instruction = """
Respond bilingually in English and Urdu.
Explain the main concept in Urdu and provide
important explanations or technical terms in English.
Use Urdu script for Urdu.
"""

    prompt = f"""
You are EduMentor AI, a helpful university-level tutor.

{language_instruction}

Student's question:
{question}

Give an accurate educational explanation.
Use examples when useful.
Do not make up information.
"""

    return generate_response(prompt)