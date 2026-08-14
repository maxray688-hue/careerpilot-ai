from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Create NVIDIA client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("NVIDIA_API_KEY")
)


def ask_ai(prompt: str):
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content