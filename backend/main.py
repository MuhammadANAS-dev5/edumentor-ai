from services.tutor import tutor


print("================================")
print("       EduMentor AI Tutor")
print("================================")

print("\nChoose your language:")
print("1. English")
print("2. Urdu")
print("3. Bilingual")

language_choice = input("Enter your choice (1-3): ").strip()

languages = {
    "1": "English",
    "2": "Urdu",
    "3": "Bilingual"
}

if language_choice not in languages:
    print("Invalid choice. Please select 1, 2, or 3.")
else:
    language = languages[language_choice]

    question = input("\nAsk your question: ")

    answer = tutor(question, language)

    print("\nEduMentor:")
    print(answer)