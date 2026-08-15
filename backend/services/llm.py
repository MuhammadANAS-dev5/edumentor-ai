import os

from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from .env
load_dotenv()


API_KEY = os.getenv("DASHSCOPE_API_KEY")

BASE_URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"

MODEL = "qwen-plus"


def generate_response(prompt):
    """
    Send the student's prompt to Alibaba Cloud Model Studio
    and return the Qwen model's response.
    """

    if not API_KEY:
        return "Error: DASHSCOPE_API_KEY is not configured."

    client = OpenAI(
        api_key=API_KEY,
        base_url=BASE_URL
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are EduMentor AI, a helpful educational tutor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content