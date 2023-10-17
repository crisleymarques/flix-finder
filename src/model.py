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
    prompt = f"""
    Sua tarefa é gerar uma recomendação de um filme ou série de TV para um usuário de uma 
    aplicação.
    
    Recomende um filme do gênero: {movie_description.genre}, 
    com data de lançamento entre {movie_description.decade} e {movie_description.decade + 9}, 
    que possua características similares à {movie_description.movie_reference}.

    Sua resposta deve conter o nome do filme ou série de TV, o ano de lançamento e uma breve 
    descrição sobre ele contendo no máximo 200 caracteres.
    """
    return prompt