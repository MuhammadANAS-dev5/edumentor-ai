from services.llm import generate_response
from services.learning_profile import build_learning_profile


def generate_study_plan(language):
    """Generate a personalized study plan from the student's performance."""

    profile = build_learning_profile()

    if not profile["has_data"]:
        return {
            "success": False,
            "message": (
                "Complete at least one quiz before generating "
                "a personalized study plan."
            )
        }

    weakest_topic = profile["weakest_topic"]
    strongest_topic = profile["strongest_topic"]
    average_percentage = profile["average_percentage"]
    weakest_score = profile["weakest_score"]

    if language == "English":

        language_instruction = """
Write the study plan completely in English.
Use clear and simple language suitable for a university student.
"""

    elif language == "Urdu":

        language_instruction = """
Write the study plan primarily in Urdu script.
Use natural Pakistani Urdu.

Keep technical terms such as C++, Python, OOP,
algorithms, programming, database, API, and AI in English.

Do not use Roman Urdu.
"""

    else:

        language_instruction = """
Write the study plan in a natural Urdu-English bilingual style.

Use Urdu script for explanations and English for
important technical terminology.

Do not use Roman Urdu.
"""

    prompt = f"""
You are EduMentor AI, a personalized university tutor.

{language_instruction}

Create a practical study plan for the student.

Student performance:

Overall average:
{average_percentage}%

Weakest topic:
{weakest_topic}

Weakest topic score:
{weakest_score}%

Strongest topic:
{strongest_topic}

Recommended difficulty:
{profile["recommended_difficulty"]}

Learning status:
{profile["learning_status"]}

Create a short 7-day study plan.

The plan must contain:

Day 1:
Day 2:
Day 3:
Day 4:
Day 5:
Day 6:
Day 7:

For each day include:
- Topic
- Learning activity
- Practice activity

Give extra attention to the weakest topic.

Keep the plan realistic for a university student.

Do not invent personal information about the student.
"""

    try:
        response = generate_response(prompt)

        return {
            "success": True,
            "plan": response
        }

    except Exception as error:

        return {
            "success": False,
            "message": f"Could not generate study plan: {error}"
        }