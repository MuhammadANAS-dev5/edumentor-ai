def tutor(question):
    question = question.strip()

    if not question:
        return "Please enter a question."

    return f"I received your question: {question}"


print("================================")
print("       EduMentor AI Tutor")
print("================================")

question = input("Ask your question: ")

answer = tutor(question)

print("\nEduMentor:")
print(answer)