def tutor(question):
    question = question.strip()

    if not question:
        return "Please enter a question."

    return f"I received your question: {question}"
