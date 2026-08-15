from services.llm import generate_response


def tutor(question, language):
    """Generate an educational response in the selected language."""

    if language == "English":
        language_instruction = """
Respond completely in English.

Use clear, simple English suitable for a university student.
Use technical terminology correctly.
"""

    elif language == "Urdu":
        language_instruction = """
Respond primarily in Urdu using Urdu script.

Use natural Pakistani Urdu rather than Hindi vocabulary.

Keep commonly used technical terms in English, including:
AI, machine learning, Python, C++, programming, class, object,
function, method, variable, algorithm, database, API, software,
framework, code, debugging, and OOP.

Explain difficult technical concepts in simple Urdu.

Example style:
"Polymorphism ایک OOP concept ہے جس میں ایک ہی interface
مختلف implementations کے ساتھ کام کر سکتا ہے۔"

Do NOT use Roman Urdu.
Do NOT translate technical programming terms unnecessarily.
"""

    else:
        language_instruction = """
Respond in a balanced Urdu-English bilingual style.

Use Urdu script for the main explanation and English for
important technical terminology.

Use natural Pakistani Urdu rather than Hindi vocabulary.

Technical terms such as AI, Python, C++, OOP, class, object,
function, algorithm, database, API, and programming should
remain in English.

For difficult concepts:
1. Explain the idea in simple Urdu.
2. Give a short English explanation or example.

Do NOT use Roman Urdu.
"""

    prompt = f"""
You are EduMentor AI, a helpful university-level tutor.

{language_instruction}

Student's question:
{question}

Give an accurate educational explanation.

Use examples when useful.

If the concept involves programming, include a small
example when appropriate.

Do not make up information.
"""

    return generate_response(prompt)