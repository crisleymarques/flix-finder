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
        temperature=0,
    )
    return response.choices[0].message["content"]

def get_prompt(genre, decade, age_rating, movie_reference):
    prompt = f"""
    Sua tarefa é gerar uma recomendação de um filme ou série de TV para um usuário de uma 
    aplicação.
    
    Recomende um filme do gênero: {genre}, 
    com data de lançamento entre {decade} e {decade + 9},
    com classificação indicativa: {age_rating},
    que possua características similares à {movie_reference}.

    Sua resposta deve conter o nome do filme ou série de TV, o ano de lançamento e uma breve 
    descrição sobre ele contendo no máximo 200 caracteres.

    Explique o porquê você recomendaria este filme ou série de TV para o usuário, justificando
    os motivos que levaram a escolha deste filme ou série de TV, dado o contexto da recomendação.

    Em seguida, diga uma curiosidade sobre o filme ou série de TV que você recomendou.

    """
    return prompt
