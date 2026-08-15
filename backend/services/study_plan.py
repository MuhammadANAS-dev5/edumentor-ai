from services.llm import generate_response


def generate_study_plan(topic, score, language):
    """Generate a personalized study plan using AI."""

    prompt = f"""
You are EduMentor AI, a personalized educational assistant.

Create a 7-day study plan for a university student.

Weak topic:
{topic}

Current quiz performance:
{score:.1f}%

Preferred language:
{language}

The student needs to improve in this topic.

Create a practical and realistic 7-day study plan.

For each day include:
- Main topic
- What to learn
- One practical activity

The plan should gradually increase in difficulty.

End with a short motivational message.

Keep the explanation clear and student-friendly.
"""

    return generate_response(prompt)