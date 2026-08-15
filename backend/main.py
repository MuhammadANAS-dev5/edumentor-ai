from services.tutor import tutor


print("================================")
print("       EduMentor AI Tutor")
print("================================")

question = input("Ask your question: ")

answer = tutor(question)

print("\nEduMentor:")
print(answer)