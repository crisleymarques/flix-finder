import openai

openai.api_key  = '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'


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