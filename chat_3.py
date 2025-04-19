from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key= os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


system_prompt = """
You are an AI assistant who is expert in breaking down complex problems and then resolve the user query.

For the given user input, analyse the input and break down the problem step by step.
At least think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for several times and then return an output with explanation and then finally you validate the output as well before giving final result.

Follow the steps in sequence that is "analyse", "think", "result", "validate" and finally "output".

Rules:
1. Follow the strict json output as per Output schema.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query

Output Format: { "step": "string", "content": "string" }

Example:
Input: What is 2 + 2.
Output: { step: "analyse", content: "Alright! The user is intersted in maths query and he is asking a basic arthermatic operation" }
Output: { step: "think", content: "To perform the addition i must go from left to right and add all the operands" }
Output: { step: "result", content: "2 + 2 = 4 and that is calculated by adding all numbers" }
Output: { step: "validate", content: "seems like 4 is correct ans for 2 + 2" }
Output: { step: "output", content: "4" }
"""



messages = [
    { "role": "system", "content": system_prompt },
]

user_input = input("> ")
messages.append({ "role": "user", "content": user_input })

while True:
        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            response_format={"type": "json_object"},
            messages=messages,
            max_tokens=200, 
            temperature=0.7
        )


        parsed_response = json.loads(response.choices[0].message.content)
        messages.append({ "role": "assistant", "content": json.dumps(parsed_response) })

        if parsed_response.get("step") != "output":
            print(f"🧠: {parsed_response.get('content')}")
            continue
    
        print(f"🤖: {parsed_response.get('content')}")
        break
