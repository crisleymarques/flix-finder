from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from data_models import *
from model import get_prompt, get_completion

flixfinder = FastAPI()

# disable cors
flixfinder.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@flixfinder.get("/")
def home():
    return "Welcome to FlixFinder!"

@flixfinder.post("/chat")
def send_prompt(
    series_or_movie: SeriesOrMovie,
    genre: Genre,
    decade: Decades,
    age_rating: AgeRating,
    positive_reference: str, 
    negative_reference: str
):
    prompt = get_prompt(series_or_movie, genre, decade, age_rating, positive_reference, negative_reference)
    print(prompt, flush=True)
    return get_completion(prompt)
