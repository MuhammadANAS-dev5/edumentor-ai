import json

from services.llm import generate_response


def generate_quiz(topic, difficulty, number_of_questions):
    """
    Generate a multiple-choice quiz using the LLM.
    """

    prompt = f"""
You are EduMentor AI, an educational quiz generator.

Create a multiple-choice quiz for a university student.

Topic:
{topic}

Difficulty:
{difficulty}

Number of questions:
{number_of_questions}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "questions": [
        {{
            "question": "Question text",
            "options": {{
                "A": "Option A",
                "B": "Option B",
                "C": "Option C",
                "D": "Option D"
            }},
            "correct_answer": "A",
            "explanation": "Short explanation of why the answer is correct."
        }}
    ]
}}

Rules:
- Create exactly {number_of_questions} questions.
- Every question must have exactly four options.
- Only one option must be correct.
- correct_answer must be A, B, C, or D.
- Keep questions educational and relevant to the topic.
- Do not include Markdown.
- Do not include any text outside the JSON.
"""

    response = generate_response(prompt)

    try:
        quiz = json.loads(response)
        return quiz

    except json.JSONDecodeError:
        return {
            "error": "The AI returned an invalid quiz format.",
            "raw_response": response
        }