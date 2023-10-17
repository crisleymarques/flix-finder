import os
import openai
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def get_prompt(movie_description):
    return f"Me diga um filme de {movie_description.genre} da década de {movie_description.decade} similar à {movie_description.movie_reference}"