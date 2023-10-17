from fastapi import FastAPI
from model import *
from data_models import *

flixfinder = FastAPI()

@flixfinder.get("/")
def home():
  return "Welcome to FlixFinder!"

@flixfinder.post("/chat")
def send_prompt(movie_description: MovieDescription):
  prompt = get_prompt(movie_description)
  print(prompt, flush=True)

  return get_completion(prompt)