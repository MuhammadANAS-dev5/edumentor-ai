from services.tutor import tutor


def choose_language():
    """Ask the student to select a response language."""

    print("\nChoose your language:")
    print("1. English")
    print("2. Urdu")
    print("3. Bilingual")

    languages = {
        "1": "English",
        "2": "Urdu",
        "3": "Bilingual"
    }

    while True:
        choice = input("Enter your choice (1-3): ").strip()

        if choice in languages:
            return languages[choice]

        print("Invalid choice. Please enter 1, 2, or 3.")


def ask_question(language):
    """Allow the student to ask an educational question."""

    question = input("\nEnter your question: ").strip()

    if not question:
        print("Please enter a question.")
        return

    print("\nEduMentor is thinking...\n")

    answer = tutor(question, language)

    print("EduMentor:")
    print(answer)


def explain_topic(language):
    """Ask the AI to explain a specific topic."""

    topic = input("\nEnter the topic you want to learn: ").strip()

    if not topic:
        print("Please enter a topic.")
        return

    question = (
        f"Teach me about {topic}. "
        "Start with a simple definition, explain the main concepts, "
        "and give a practical example."
    )

    print("\nEduMentor is preparing your explanation...\n")

    answer = tutor(question, language)

    print("EduMentor:")
    print(answer)


def show_menu():
    """Display the main application menu."""

    print("\n================================")
    print("         EduMentor AI")
    print("================================")
    print("1. Ask a Question")
    print("2. Explain a Topic")
    print("3. Generate Quiz")
    print("4. Summarize Text")
    print("5. Study Plan")
    print("6. Exit")


def main():
    print("================================")
    print("       Welcome to EduMentor")
    print("================================")
    print("Your bilingual AI learning assistant.")

    language = choose_language()

    print(f"\nLanguage selected: {language}")

    while True:
        show_menu()

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            ask_question(language)

        elif choice == "2":
            explain_topic(language)

        elif choice == "3":
            print("\nQuiz mode will be implemented in the next step.")

        elif choice == "4":
            print("\nSummarization mode will be implemented soon.")

        elif choice == "5":
            print("\nStudy Plan mode will be implemented soon.")

        elif choice == "6":
            print("\nThank you for using EduMentor AI!")
            break

        else:
            print("\nInvalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()