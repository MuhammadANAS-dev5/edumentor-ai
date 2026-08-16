import json
import os


DATA_FILE = "data/performance.json"


def load_performance():
    """Load previous quiz results from the JSON file."""

    if not os.path.exists(DATA_FILE):
        return {"quizzes": []}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return {"quizzes": []}


def save_quiz_result(topic, difficulty, score, total_questions):
    """Save one quiz result to the performance file."""

    data = load_performance()

    percentage = (score / total_questions) * 100

    result = {
        "topic": topic,
        "difficulty": difficulty,
        "score": score,
        "total_questions": total_questions,
        "percentage": round(percentage, 1)
    }

    data["quizzes"].append(result)

    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return result

def get_performance_summary():
    """Calculate detailed performance statistics."""

    data = load_performance()
    quizzes = data.get("quizzes", [])

    if not quizzes:
        return {
            "total_quizzes": 0,
            "average_percentage": 0,
            "topics": {},
            "weakest_topic": None,
            "strongest_topic": None
        }

    topic_scores = {}

    for quiz in quizzes:
        topic = quiz["topic"]
        percentage = quiz["percentage"]

        if topic not in topic_scores:
            topic_scores[topic] = []

        topic_scores[topic].append(percentage)

    topic_averages = {}

    for topic, scores in topic_scores.items():
        topic_averages[topic] = sum(scores) / len(scores)

    average_percentage = sum(
        quiz["percentage"] for quiz in quizzes
    ) / len(quizzes)

    weakest_topic = min(
        topic_averages,
        key=lambda topic: topic_averages[topic]
    )

    strongest_topic = max(
        topic_averages,
        key=lambda topic: topic_averages[topic]
    )

    return {
        "total_quizzes": len(quizzes),
        "average_percentage": round(average_percentage, 1),
        "topics": topic_averages,
        "weakest_topic": weakest_topic,
        "strongest_topic": strongest_topic
    }


def recommend_difficulty(topic):
    """Recommend quiz difficulty based on previous performance."""

    data = load_performance()
    quizzes = data.get("quizzes", [])

    topic_scores = []

    for quiz in quizzes:
        if quiz["topic"].lower() == topic.lower():
            topic_scores.append(quiz["percentage"])

    # No previous attempts for this topic
    if not topic_scores:
        return "Easy"

    average_score = sum(topic_scores) / len(topic_scores)

    if average_score < 60:
        return "Easy"

    elif average_score < 80:
        return "Medium"

    else:
        return "Hard"