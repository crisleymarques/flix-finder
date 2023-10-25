from enum import Enum
from datetime import datetime

class AgeRating(str, Enum):
    livre = "Livre"
    dez_anos = "10 Anos"
    doze_anos = "12 Anos"
    quatorze_anos = "14 Anos"
    dezesseis_anos = "16 Anos"
    dezoito_anos = "18 Anos"


class Genre(str, Enum):
    acao = "Ação"
    aventura = "Aventura"
    comedia = "Comédia"
    drama = "Drama"
    fantasia = "Fantasia"
    ficcao_cientifica = "Ficção Científica"
    terror = "Terror"
    romance = "Romance"
    animacao = "Animação"
    crime = "Crime"
    documentario = "Documentário"
    suspense = "Suspense"
    musical = "Musical"
    misterio = "Mistério"
    guerra = "Guerra"
    western = "Western"


def create_decades_enum():
    current_year = datetime.now().year
    start_year = current_year - (current_year % 10)
    items = {f'{str(i)}': str(i) for i in range(start_year, 1900, -10)}
    return Enum('Decades', items)

Decades = create_decades_enum()
