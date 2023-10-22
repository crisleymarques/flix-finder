from fastapi import FastAPI
from data_models import MovieDescription
from model import get_prompt, get_completion

flixfinder = FastAPI()

@flixfinder.get("/")
def home():
    return "Welcome to FlixFinder!"

@flixfinder.post("/chat")
def send_prompt(movie_description: MovieDescription):
    prompt = get_prompt(movie_description)
    print(prompt, flush=True)
    return get_completion(prompt)
