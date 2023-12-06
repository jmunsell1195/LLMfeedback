from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())

SYSTEM = "You are a helpful AI assistant who has been tasked with grading student essays. You should always be honest, fair, and thorough. Always provide a score. If you are unsure, give your best attempt while remaining honest, fair, and thorough"

def test_wrapper(text: str) -> str:
    """Dummy function to test imports and integration"""
    return text.upper()

client = OpenAI()

def gpt_wrapper(prompt:str, system: str = SYSTEM, return_raw:bool = False, model: str = "gpt-4-1106-preview") -> str:
  response = client.chat.completions.create(
  model = model,
  messages=[
    {"role": "system", "content": system},
    {"role": "user", "content": prompt}
  ]
  )
  if return_raw:
    return response
  else:
    return response.choices[0].message.content



