from prompts.dnd import INITIAL_PROMPT, WELCOME_PROMPT
from dynamic import game_development
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv(".env")

game_development(INITIAL_PROMPT, WELCOME_PROMPT, OpenAI())
