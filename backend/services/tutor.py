from services.llm import generate_response


def tutor(question, language, conversation_history=None):
    """Generate an educational response with conversation context."""

    if conversation_history is None:
        conversation_history = []

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

Do NOT use Roman Urdu.
"""

    else:
        language_instruction = """
Respond in a balanced Urdu-English bilingual style.

Use Urdu script for the main explanation and English for
important technical terminology.

Use natural Pakistani Urdu rather than Hindi vocabulary.

Do NOT use Roman Urdu.
"""

    conversation_text = ""

    for message in conversation_history[-10:]:
        conversation_text += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    prompt = f"""
You are EduMentor AI, a helpful university-level tutor.

{language_instruction}

Previous conversation:
{conversation_text}

Current student question:
{question}

Answer the student's current question using the previous
conversation as context when relevant.

Give an accurate educational explanation.
Use examples when useful.

If the student refers to something using words such as
"it", "that", "this", or "the example", use the previous
conversation to understand what they mean.

Do not make up information.
"""

    return generate_response(prompt)