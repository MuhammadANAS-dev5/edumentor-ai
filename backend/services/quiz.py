import json

from services.llm import generate_response


def generate_quiz(topic, difficulty, number_of_questions, language):
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

Language preference:
{language}

Language rules:

If the language is English:
- Write the questions in English.
- Write all options in English.
- Write explanations in English.

If the language is Urdu:
- Write questions in Urdu script.
- Write options in Urdu script.
- Keep technical terms such as C++, Python, OOP,
  algorithm, class, object, API, and AI in English
  when appropriate.
- Write explanations in Urdu script.

If the language is Bilingual:
- Write the main explanation in Urdu and English.
- Use Urdu script for Urdu.
- Keep important technical terminology in English.

Return ONLY valid JSON.

The JSON must have this structure:

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
            "explanation": "Explanation"
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
        if response is None:
            raise json.JSONDecodeError("Empty response", "", 0)

        quiz = json.loads(response)
        return quiz

    except json.JSONDecodeError:
        return {
            "error": "The AI returned an invalid quiz format.",
            "raw_response": response
        }