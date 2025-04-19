from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

result = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user","content": "Hey, How are you? Tauqueer this side",
        }
    ],
)

print(result.choices[0].message.content)



# Zero Shot Prompting