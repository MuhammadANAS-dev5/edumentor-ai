from services.llm import generate_response


def tutor(question):
    question = question.strip()

    if not question:
        return "Please enter a question."

    response = generate_response(question)

    return response