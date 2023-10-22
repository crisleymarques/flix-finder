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

def get_prompt(movie_description):
    prompt = f"""
    Sua tarefa é gerar uma recomendação de um filme ou série de TV para um usuário de uma 
    aplicação.
    
    Recomende um filme do gênero: {movie_description.genre}, 
    com data de lançamento entre {movie_description.decade} e {movie_description.decade + 9}, 
    que possua características similares à {movie_description.movie_reference}.

    Sua resposta deve conter o nome do filme ou série de TV, o ano de lançamento e uma breve 
    descrição sobre ele contendo no máximo 200 caracteres.

    ---

    Explicação da Recomendação:

    {movie_description.movie_reference} é um filme {movie_description.genre} lançado em {movie_description.decade}.
    Acredito que este filme seja uma excelente recomendação para você, pois compartilha características similares com {movie_description.movie_reference}.
    Ele é conhecido por {descrição_do_filme_aqui}.

    ---

    Por que eu recomendei este filme?

    Esta recomendação foi feita com base em análises de similaridade entre os atributos de {movie_description.movie_reference} e outros filmes no mesmo gênero e década de lançamento. Acredito que você irá apreciar as semelhanças entre essas obras.

    ---

    Curiosidade sobre {movie_description.movie_reference}:

    Aqui está uma curiosidade interessante sobre o filme {movie_description.movie_reference}:
    {curiosidade_sobre_o_filme_aqui}.

    ---

    Outra recomendação:

    Além disso, se você gostou de {movie_description.movie_reference}, recomendo também o filme {outro_filme_similar} lançado em {ano_do_outro_filme}.
    Ele possui uma atmosfera semelhante e tenho certeza de que você vai apreciar.

    ---

    Aproveite a recomendação e divirta-se assistindo!

    """
    return prompt
