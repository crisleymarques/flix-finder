from enum import Enum
from datetime import datetime

class SeriesOrMovie(str, Enum):
    series = "TV series"
    movie = "Movie"


class AgeRating(str, Enum):
    G = "General Audiences"
    PG = "Parental Guidance Suggested"
    PG_13 = "Parents Strongly Cautioned"
    R = "Restricted"
    NC_17 = "Adults Only"


class Genre(str, Enum):
    action = "Action"
    adventure = "Adventure"
    comedy = "Comedy"
    drama = "Drama"
    fantasy = "Fantasy"
    science_fiction = "Science Fiction"
    horror = "Horror"
    romance = "Romance"
    animation = "Animation"
    crime = "Crime"
    documentary = "Documentary"
    suspense = "Suspense"
    musical = "Musical"
    mystery = "Mystery"
    war = "War"
    western = "Western"
    thriller = "Thriller"
    history = "History"
    sport = "Sport"
    talk_show = "Talk Show"
    reality_show = "Reality Show"
    superhero = "Superhero"


def create_decades_enum():
    current_year = datetime.now().year
    start_year = current_year - (current_year % 10)
    items = {f'{str(i)}': str(i) for i in range(start_year, 1900, -10)}
    return Enum('Decades', items)

Decades = create_decades_enum()
