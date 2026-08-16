from services.tutor import tutor
from services.quiz import generate_quiz
from services.performance import (
    save_quiz_result,
    get_performance_summary,
    recommend_difficulty
)
from services.study_plan import generate_study_plan
from services.remediation import generate_remediation
from services.learning_profile import build_learning_profile


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
    """Run an interactive AI tutoring conversation with memory."""

    print("\n================================")
    print("          AI TUTOR")
    print("================================")

    print("\nYou can ask EduMentor anything about your studies.")
    print("EduMentor will remember the current conversation.")
    print("Type 'exit' to return to the main menu.")

    conversation_history = []

    while True:

        question = input("\nYour question: ").strip()

        if not question:
            print("Please enter a question.")
            continue

        if question.lower() == "exit":
            print("\nReturning to the main menu...")
            break

        print("\nEduMentor is thinking...\n")

        try:
            response = tutor(
                question,
                language,
                conversation_history
            )

            print("================================")
            print("          EDU MENTOR")
            print("================================")

            print(response)

            # Store the student's message.
            conversation_history.append({
                "role": "Student",
                "content": question
            })

            # Store the AI response.
            conversation_history.append({
                "role": "EduMentor",
                "content": response
            })

        except Exception as error:
            print("\nUnable to generate a response.")
            print(f"Error: {error}")

        print("\n--------------------------------")
        print("You can ask another question.")
        print("Type 'exit' to return to the main menu.")


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

            print(
        f"Explanation: "
        f"{question_data['explanation']}"
    )

        else:
            print(
        f"Incorrect. Correct answer: "
        f"{correct_answer}"
    )

            print(
        f"Explanation: "
        f"{question_data['explanation']}"
    )

            print("\nGenerating personalized feedback...")

        remediation = generate_remediation(
            question_data["question"],
            answer,
            correct_answer,
            question_data["explanation"],
            language
    )

        print("\n================================")
        print("       AI LEARNING FEEDBACK")
        print("================================")

        print(remediation)

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
    """Display a personalized AI-generated study plan."""

    print("\n========================================")
    print("          AI STUDY PLAN")
    print("========================================")

    print("\nAnalyzing your learning profile...")

    result = generate_study_plan(language)

    if not result["success"]:
        print("\nUnable to generate a study plan.")
        print(result["message"])
        return

    print("\n========================================")
    print("       YOUR PERSONALIZED PLAN")
    print("========================================")

    print(result["plan"])



def learning_profile_mode():
    """Display the student's personalized learning profile."""

    profile = build_learning_profile()

    print("\n========================================")
    print("          AI LEARNING PROFILE")
    print("========================================")

    if not profile["has_data"]:
        print("\nNo learning history available yet.")
        print("Complete a quiz to build your profile.")
        return

    print(f"\nLearning Status: {profile['learning_status']}")

    print(
        f"Total Quizzes: "
        f"{profile['total_quizzes']}"
    )

    print(
        f"Overall Average: "
        f"{profile['average_percentage']:.1f}%"
    )

    print(
        f"Strongest Topic: "
        f"{profile['strongest_topic']}"
    )

    print(
        f"Weakest Topic: "
        f"{profile['weakest_topic']}"
    )

    print(
        f"Weakest Topic Score: "
        f"{profile['weakest_score']:.1f}%"
    )

    print(
        f"Recommended Difficulty: "
        f"{profile['recommended_difficulty']}"
    )

    print("\n========================================")
    print("             NEXT ACTION")
    print("========================================")

    print(
        f"Focus your next study session on "
        f"{profile['weakest_topic']}."
    )
    
    article = (
    "an"
    if profile["recommended_difficulty"] == "Easy"
    else "a"
)    

    print(
        f"Start with {article} "
        f"{profile['recommended_difficulty']} quiz "
        f"and review the topic afterward."
    ) 


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
    print("7. Learning Profile")
    print("8. Exit")


def main():
    print("================================")
    print("       Welcome to EduMentor")
    print("================================")
    print("Your bilingual AI learning assistant.")

    language = choose_language()

    print(f"\nLanguage selected: {language}")

    while True:
        show_menu()

        choice = input("\nChoose an option (1-8): ").strip()

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
            learning_profile_mode()

        elif choice == "8":
            print("\nThank you for using EduMentor AI!")
            break

        else:
            print("\nInvalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()