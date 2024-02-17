from prompts import INITIAL_PROMPT, QUIT
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv(".env")

USER_INPUT = ''

def is_game_ended(user_input: str):
    return user_input.lower() == 'q'

CHAT = [
    {
        "role": "system",
        "content": INITIAL_PROMPT
    }
]

NEXT_PROMPT = '''
Welcome! Before starting some quick notes:
1. You can exit the game at any time by using 'q'
2. Write all your inputs in a single line
3. You can modify the course of the game by writing between parentheses. Ex, '(make a plot twist)'.

Let's the fun begin!
==================================================================================================
'''

print(NEXT_PROMPT)

client = OpenAI()

while not is_game_ended(USER_INPUT):
    completion = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=CHAT
    )
    NEXT_PROMPT = completion.choices[0].message.content
    CHAT.append({
        "role": "assistant",
        "content": NEXT_PROMPT
    })

    print(f'{NEXT_PROMPT}\n\n{QUIT}')

    USER_INPUT = input()
    CHAT.append({
        "role": "user",
        "content": USER_INPUT
    })

print('Thanks for playing!')




