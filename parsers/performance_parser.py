from bs4 import BeautifulSoup
import requests
from config import PERFORMANCE_URL

def get_performance_by_title(title):
    try:
        response = requests.get(PERFORMANCE_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return []

    soup = BeautifulSoup(response.text)
    performances = []
    for performance_block in soup.find_all("div", class_="recommendation-item_text-block compilation-tile__text-block"):
        performance_title = performance_block.find("h2", "recommendation-item_title compilation-tile__title")
        performance_description = performance_block.find("a", class_="recommendation-item_venue compilation-tile__venue hover:underline")
        performance_year = performance_block.find("time", class_="recommendation-item_date compilation-tile__date")

        if not performance_title:
            continue

        if title.lower() in performance_title.text.strip().lower():
            performance_info = {
                "title": performance_title.text.strip(),
                "place": performance_description.text.strip() if performance_description else "Место отсутствует",
                "dates": performance_year.text.strip() if performance_year else "Дата не указана"
            }
            performances.append(performance_info)

    return performances

def get_three_performances():
    try:
        response = requests.get(PERFORMANCE_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return []

    soup = BeautifulSoup(response.text)
    performances = []

    for performance_block in soup.find_all("div", class_="recommendation-item_text-block compilation-tile__text-block")[:3]:
        performance_title = performance_block.find("h2", class_="recommendation-item_title compilation-tile__title")
        performance_description = performance_block.find("a", class_="recommendation-item_venue compilation-tile__venue hover:underline")
        performance_year = performance_block.find("time", class_="recommendation-item_date compilation-tile__date")

        if performance_title:
            performances.append({
                "title": performance_title.text.strip(),
                "place": performance_description.text.strip() if performance_description else "Место отсутствует",
                "dates": performance_year.text.strip() if performance_year else "Дата не указана"
            })

    return performances
