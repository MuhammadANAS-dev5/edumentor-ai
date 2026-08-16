from services.llm import generate_response


def generate_remediation(
    question,
    student_answer,
    correct_answer,
    explanation,
    language
):
    """Generate personalized feedback after a wrong answer."""

    if language == "English":
        language_instruction = """
Respond in clear English.
"""

    elif language == "Urdu":
        language_instruction = """
Respond primarily in Urdu script.
Use natural Pakistani Urdu.
Keep technical terms such as C++, Python, OOP,
algorithm, class, object, and function in English.
Do not use Roman Urdu.
"""

    else:
        language_instruction = """
Respond in a balanced Urdu-English bilingual style.
Use Urdu script for the main explanation and
English for important technical terminology.
Do not use Roman Urdu.
"""

    prompt = f"""
You are EduMentor AI, a personalized educational tutor.

{language_instruction}

A student answered a quiz question incorrectly.

Question:
{question}

Student's answer:
{student_answer}

Correct answer:
{correct_answer}

Existing explanation:
{explanation}

Your task is to help the student understand the mistake.

Provide exactly these sections:

1. What went wrong
2. Correct concept
3. Quick example
4. Practice question

Keep the explanation concise and student-friendly.

Do not criticize the student.
Focus on helping them learn from the mistake.
"""

    return generate_response(prompt)