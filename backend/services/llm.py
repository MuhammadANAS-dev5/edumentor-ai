import os

from dotenv import load_dotenv


# Load variables from the .env file
load_dotenv()


def generate_response(prompt):
    """
    Generate a response from the configured language model.

    The real LLM API will be connected later.
    """

    api_key = os.getenv("DASHSCOPE_API_KEY")

    if not api_key:
        return (
            "[DEVELOPMENT MODE]\n"
            "No AI API key is configured yet.\n\n"
            f"Prompt received:\n{prompt}"
        )

    # Real AI API integration will be added here later.
    return "[AI API CONNECTION WILL BE ADDED HERE]"