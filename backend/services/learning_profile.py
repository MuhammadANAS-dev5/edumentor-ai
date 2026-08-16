from services.performance import (
    get_performance_summary,
    recommend_difficulty
)


def build_learning_profile():
    """Build a personalized learning profile from quiz history."""

    performance = get_performance_summary()

    if performance["total_quizzes"] == 0:
        return {
            "has_data": False,
            "total_quizzes": 0,
            "average_percentage": 0,
            "strongest_topic": None,
            "weakest_topic": None,
            "weakest_score": 0,
            "recommended_difficulty": "Easy",
            "learning_status": "No Data"
        }

    weakest_topic = performance["weakest_topic"]
    strongest_topic = performance["strongest_topic"]

    weakest_score = performance["topics"][weakest_topic]

    recommended_difficulty = recommend_difficulty(
        weakest_topic
    )

    if weakest_score < 60:
        learning_status = "Needs Improvement"

    elif weakest_score < 80:
        learning_status = "Developing"

    else:
        learning_status = "Strong"

    return {
        "has_data": True,
        "total_quizzes": performance["total_quizzes"],
        "average_percentage": performance["average_percentage"],
        "strongest_topic": strongest_topic,
        "weakest_topic": weakest_topic,
        "weakest_score": round(weakest_score, 1),
        "recommended_difficulty": recommended_difficulty,
        "learning_status": learning_status
    }