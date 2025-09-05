from openai import OpenAI
import os

key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

ingregent = []


def callChef(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-nano", messages=prompt, max_tokens=20
    )
    print("Here is the recipe I found for you:")
    print(response.choices[0].message.content)


def updatePrompt(ingregent):
    prompt = [
        {
            "role": "system",
            "content": "your are an expert shef which know all the receipe from the italian and india you take the input for the user and then which receipe is good, heathy on the basis of these thing and also tasty the user provide the ingredients as a list",
        },
        {
            "role": "user",
            "content": f" Ingredients: {', '.join(ingregent)}",
        },
    ]
    return prompt


while True:
    userInput = input(
        "Enter the ingreadient or type end to start makeing the recipe:- "
    )

    if userInput.lower() == "end":
        print(f"i have these ingredient {ingregent} what can i make with this")
        prompt = updatePrompt(ingregent)
        callChef(prompt)
        # print(prompt)

        break
    ingregent.append(userInput)
