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


def get_prompt(series_or_movie, genre, decade, age_rating, positive_reference, negative_reference):
    prompt = f"""
    Your task is to generate a personalized {series_or_movie} recommendation for an application user.

    Recommend a {series_or_movie} in the {genre} genre,
    released between {decade.value} and {int(decade.value) + 9},
    with an age rating of {age_rating},
    that has similar characteristics to {positive_reference} 
    and it is not similar to {negative_reference}.

    Your response should include the name of the {series_or_movie}, the release year, and a brief
    description of it, containing a maximum of 200 characters.

    Explain why you would recommend this {series_or_movie} to the user, justifying
    the reasons that led to the choice, given the context of the recommendation.

    Additionally, share an interesting fact about the recommended {series_or_movie}.

    """
    return prompt
