from game_features.quit import quit
from game_features.save_load import save

def is_game_ended(user_input: str, chat:list):
    if user_input.lower() == 'q':
        quit()
    if user_input.lower() == 's':
        save(chat)
        return True
    return False
        
def append_user_input(chat: list, user_input=None):
    chat.append({
        "role": "user",
        "content": input() if user_input is None else user_input
    })

def game_development(INITIAL_PROMPT, WELCOME_PROMPT, client, user_first=False):

    USER_INPUT = ''
    chat = [
        {
            "role": "system",
            "content": INITIAL_PROMPT
        }
    ]

    next_prompt = WELCOME_PROMPT

    print(next_prompt)

    while not is_game_ended(USER_INPUT, chat):
        if user_first:
            append_user_input(chat)
            user_first = False

        completion = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=chat
        )
        next_prompt = completion.choices[0].message.content
        chat.append({
            "role": "assistant",
            "content": next_prompt
        })

        print(f'\n======\n{next_prompt}\n\n')
        print('Quit: [q]    Save & Quit: [s]')

        USER_INPUT = input()
        append_user_input(chat, USER_INPUT)