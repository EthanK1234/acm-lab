from openrouter import OpenRouter
from dotenv import load_dotenv
import os

load_dotenv()

# model 1
with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:
    response = client.chat.send(
        model="deepseek/deepseek-v4.1-flash-20261017",
        messages=[
            {"role": "user", "content": "What is the hardest major?"}
        ],
    )

print(response.choices[0].message.content)


# model 2
with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:
    response = client.chat.send(
        model="anthropic/claude-sonnet-5.5",
        messages=[
            {"role": "user", "content": "What is the easiest major?"}
        ],
    )

print(response.choices[0].message.content)