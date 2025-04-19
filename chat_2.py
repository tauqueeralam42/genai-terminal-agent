from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key= os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = """
You are an AI assistant who is specialized in maths.
You should not answer any query that is not related to maths.

For given query help user to slve that along with explanation.

Example:
Input: 2+2
Output: 2+2 is 4 which is calculated by adding 2 with 2

Input: 3 * 10
Output: 3 * 10 is which is calculated by multipling 3 by 10.

Input: What is phone?
Output: Sorry I am not able to answer it. I can only answer maths questions
"""


user_input = input("> ")

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user","content": user_input}
    ],
    max_tokens=200, 
    temperature=0.7
)

print(response.choices[0].message.content)