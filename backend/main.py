from services.tutor import tutor


def choose_language():
    """Ask the student to select a response language."""

    print("\nChoose your language:")
    print("1. English")
    print("2. Urdu")
    print("3. Bilingual")

    while True:
        choice = input("Enter your choice (1-3): ").strip()

        languages = {
            "1": "English",
            "2": "Urdu",
            "3": "Bilingual"
        }

        if choice in languages:
            return languages[choice]

        print("Invalid choice. Please enter 1, 2, or 3.")


def main():
    print("================================")
    print("       EduMentor AI Tutor")
    print("================================")
    print("Your bilingual AI learning assistant.")

    language = choose_language()

    print(f"\nLanguage selected: {language}")
    print("\nType 'exit' whenever you want to quit.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("\nThank you for using EduMentor AI!")
            break

        if not question:
            print("Please enter a question.")
            continue

        print("\nEduMentor is thinking...\n")

        answer = tutor(question, language)

        print("EduMentor:")
        print(answer)


if __name__ == "__main__":
    main()