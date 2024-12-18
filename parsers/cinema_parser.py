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

    soup = BeautifulSoup(response.text)
    films = []

    for film_block in soup.find_all("div", class_="movieItem_info"):
        film_title = film_block.find("a", class_="movieItem_title")
        film_description = film_block.find("span", class_="movieItem_genres")
        film_year = film_block.find("span", class_="movieItem_year")

        if not film_title:
            continue

        if title.lower() in film_title.text.strip().lower():
            film_info = {
                "title": film_title.text.strip(),
                "description": film_description.text.strip() if film_description else "Описание отсутствует",
                "year": film_year.text.strip() if film_year else "Год не указан"
            }
            films.append(film_info)

    return films

def get_three_films():
    try:
        response = requests.get(CINEMA_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return []

    soup = BeautifulSoup(response.text)
    films = []

    for film_block in soup.find_all("div", class_="movieItem_info")[:3]:
        film_title = film_block.find("a", class_="movieItem_title")
        film_description = film_block.find("span", class_="movieItem_genres")
        film_year = film_block.find("span", class_="movieItem_year")

        if film_title:
            films.append({
                "title": film_title.text.strip(),
                "description": film_description.text.strip() if film_description else "Описание отсутствует",
                "year": film_year.text.strip() if film_year else "Год не указан"
            })

    return films

def get_films_by_genre(genre):
    try:
        response = requests.get(CINEMA_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return []

    soup = BeautifulSoup(response.text)
    films = []

    for film_block in soup.find_all("div", class_="movieItem_info"):
        film_title = film_block.find("a", class_="movieItem_title")
        film_description = film_block.find("span", class_="movieItem_genres")
        film_year = film_block.find("span", class_="movieItem_year")

        if not film_title or not film_description:
            continue

        if genre.lower() in film_description.text.strip().lower():
            films.append({
                "title": film_title.text.strip(),
                "description": film_description.text.strip(),
                "year": film_year.text.strip() if film_year else "Год не указан"
            })

    return films[:3]

