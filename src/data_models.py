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
    items = {f'DEC_{str(i)}': str(i) for i in range(1900, datetime.now().year, 10)}
    return Enum('Decades', items)

Decades = create_decades_enum()
