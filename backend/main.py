from services.tutor import tutor
from services.quiz import generate_quiz
from services.performance import (
    save_quiz_result,
    get_performance_summary,
    recommend_difficulty
)
from services.study_plan import generate_study_plan
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



def quiz_mode(language):
    """Generate and conduct an interactive quiz."""

    print("\n========== Quiz Mode ==========")

    topic = input("Enter quiz topic: ").strip()

    if not topic:
        print("Please enter a topic.")
        return

    print("\nChoose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    recommended_difficulty = recommend_difficulty(topic)

    print(
        f"\nEduMentor recommendation: "
        f"{recommended_difficulty}"
    )

    print(
        "This recommendation is based on your "
        "previous performance in this topic."
    )
    difficulty_options = {
        "1": "Easy",
        "2": "Medium",
        "3": "Hard"
    }

    while True:
        difficulty_choice = input("Choose difficulty (1-3): ").strip()

        if difficulty_choice in difficulty_options:
            difficulty = difficulty_options[difficulty_choice]
            break

        print("Invalid choice. Please select 1, 2, or 3.")

    while True:
        number_input = input("Number of questions (1-10): ").strip()

        if number_input.isdigit():
            number_of_questions = int(number_input)

            if 1 <= number_of_questions <= 10:
                break

        print("Please enter a number between 1 and 10.")

    print("\nGenerating your quiz...")
    
    quiz = generate_quiz(
        topic,
        difficulty,
        number_of_questions,
        language
    )

    if "error" in quiz:
        print("\nCould not generate the quiz.")
        print(quiz["error"])
        return

    questions = quiz.get("questions", [])

    if not questions:
        print("\nThe AI did not return any questions.")
        return

    score = 0

    print("\n================================")
    print("          YOUR QUIZ")
    print("================================")

    for index, question_data in enumerate(questions, start=1):

        print(f"\nQuestion {index}/{len(questions)}")
        print(question_data["question"])

        options = question_data["options"]

        print(f"A. {options['A']}")
        print(f"B. {options['B']}")
        print(f"C. {options['C']}")
        print(f"D. {options['D']}")

        while True:
            answer = input("\nYour answer (A-D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Please enter A, B, C, or D.")

        correct_answer = question_data["correct_answer"]

        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {correct_answer}")

        print(f"Explanation: {question_data['explanation']}")

    percentage = (score / len(questions)) * 100

    save_quiz_result(
    topic,
    difficulty,
    score,
    len(questions)
)

    print("\n================================")
    print("          QUIZ RESULTS")
    print("================================")

    print(f"Score: {score}/{len(questions)}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage >= 80:
        performance = "Excellent"

    elif percentage >= 60:
        performance = "Good"

    else:
        performance = "Needs Improvement"

    print(f"Performance: {performance}")

    print("\n================================")
    print("       STUDY RECOMMENDATION")
    print("================================")

    if percentage >= 80:
        print(f"You have a strong understanding of {topic}.")
        print("Try a harder quiz or move to the next topic.")

    elif percentage >= 60:
        print(f"You have a basic understanding of {topic}.")
        print("Review the concepts you got wrong and practice again.")

    else:
        print(f"You need more practice with {topic}.")
        print("Start with the fundamentals before attempting another quiz.")
    


def performance_mode():
    """Display a detailed student performance dashboard."""

    performance = get_performance_summary()

    print("\n========================================")
    print("         EDU MENTOR - PROGRESS")
    print("========================================")

    if performance["total_quizzes"] == 0:
        print("\nNo quiz results found.")
        print("Complete a quiz first to see your progress.")
        return

    print(f"\nTotal Quizzes: {performance['total_quizzes']}")

    print(
        f"Overall Average: "
        f"{performance['average_percentage']:.1f}%"
    )

    print(
        f"Strongest Topic: "
        f"{performance['strongest_topic']}"
    )

    print(
        f"Weakest Topic: "
        f"{performance['weakest_topic']}"
    )

    print("\n========================================")
    print("        TOPIC-WISE PERFORMANCE")
    print("========================================")

    for topic, average in performance["topics"].items():

        if average >= 80:
            level = "Strong"

        elif average >= 60:
            level = "Average"

        else:
            level = "Needs Practice"

        print(
            f"{topic}: "
            f"{average:.1f}% "
            f"({level})"
        )

    weakest_topic = performance["weakest_topic"]
    weakest_score = performance["topics"][weakest_topic]

    recommended_difficulty = recommend_difficulty(
        weakest_topic
    )

    print("\n========================================")
    print("          LEARNING RECOMMENDATION")
    print("========================================")

    print(f"Focus Area: {weakest_topic}")
    print(f"Current Score: {weakest_score:.1f}%")
    print(
        f"Recommended Quiz Difficulty: "
        f"{recommended_difficulty}"
    )

    if weakest_score < 60:
        print(
            "\nRecommendation: Review the fundamentals "
            "and practice more questions."
        )

    elif weakest_score < 80:
        print(
            "\nRecommendation: Continue practicing "
            "and attempt another quiz."
        )

    else:
        print(
            "\nRecommendation: Your performance is strong. "
            "Try a harder challenge."
        )



def study_plan_mode(language):
    """Generate a personalized study plan based on performance."""

    performance = get_performance_summary()

    print("\n================================")
    print("       PERSONALIZED STUDY PLAN")
    print("================================")

    if performance["total_quizzes"] == 0:
        print("\nNo quiz results found.")
        print("Complete a quiz first so EduMentor can analyze your performance.")
        return

    weakest_topic = performance["weakest_topic"]

    weakest_score = performance["topics"][weakest_topic]

    print(f"\nWeakest Topic: {weakest_topic}")
    print(f"Current Performance: {weakest_score:.1f}%")

    print("\nGenerating your personalized study plan...")

    plan = generate_study_plan(
        weakest_topic,
        weakest_score,
        language
    )

    print("\n================================")
    print("          YOUR STUDY PLAN")
    print("================================\n")

    print(plan)



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
    print("6. My Performance")
    print("7. Exit")


def main():
    print("================================")
    print("       Welcome to EduMentor")
    print("================================")
    print("Your bilingual AI learning assistant.")

    language = choose_language()

    print(f"\nLanguage selected: {language}")

    while True:
        show_menu()

        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            ask_question(language)

        elif choice == "2":
            explain_topic(language)

        elif choice == "3":
            quiz_mode(language)

        elif choice == "4":
            print("\nSummarization mode will be implemented soon.")

        elif choice == "5":
            study_plan_mode(language)
        

        elif choice == "6":
            performance_mode()

        elif choice == "7":
            print("\nThank you for using EduMentor AI!")
            break

        else:
            print("\nInvalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()