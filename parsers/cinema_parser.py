from bs4 import BeautifulSoup
import requests
from config import CINEMA_URL

def get_film_by_name(title):
    try:
        response = requests.get(CINEMA_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    films = []

    for film_block in soup.find_all("a", class_="base-movie-main-info_link__YwtP1"):
        film_title = film_block.find("span", class_="desktop-list-main-info_mainTitle__8IBrD")
        film_description = film_block.find("span", class_="desktop-list-main-info_truncatedText__IMQRP")
        film_year = film_block.find("span", class_="desktop-list-main-info_secondaryText__M_aus")

        if not film_title:
            continue

        # Сравниваем названия
        if title.lower() in film_title.text.strip().lower():
            film_info = {
                "title": film_title.text.strip(),
                "description": film_description.text.strip() if film_description else "Описание отсутствует",
                "year": film_year.text.strip() if film_year else "Год не указан"
            }
            films.append(film_info)

    return films  # Возвращаем список фильмов
