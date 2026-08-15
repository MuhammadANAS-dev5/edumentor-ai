from services.tutor import tutor


print("================================")
print("       EduMentor AI Tutor")
print("================================")

print("\nChoose your language:")
print("1. English")
print("2. Urdu")
print("3. Bilingual")

language_choice = input("Enter your choice (1-3): ")

languages = {
    "1": "English",
    "2": "Urdu",
    "3": "Bilingual"
}

language = languages.get(language_choice, "English")

question = input("\nAsk your question: ")

answer = tutor(question, language)

print("\nEduMentor:")
print(answer)