import requests
import json
import sys
import urllib.parse

#Основная функция
def main():
    #Проверка передачи аргумента
    if len(sys.argv) < 2:
        print("Использование: python wikisearch.py <запрос>")
        print("Пример: python wikisearch.py 'Дрифт'")
        sys.exit(1)
    
    #Достаем запрос из аргумента
    search_term = " ".join(sys.argv[1:])

    #Формируем Url-запрос
    encoded_term = urllib.parse.quote(search_term)
    
    url = f"https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=true&explaintext=true&titles={encoded_term}"

    #Заголовок для запроса
    headers = {
        'User-Agent': 'MyBot/1.0'
    }

    #Отправка Get-запроса
    try:
        response = requests.get(url, headers = headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        sys.exit(1)

    #Парсим Json-ответ
    data = response.json()

    #Извлекаем ответ
    pages = data.get('query', {}).get('pages', {})

    for page_id in pages:
        page = pages[page_id]
        if page_id == -1:
            print(f"Статья '{search_term}' не найдена.")
        else:
            title = page.get('title', 'Без названия')
            extract = page.get('extract', 'Нет описания')
            print(f"== {title} ==\n")
            print(extract[:500] + "...")
        break

#Проверка
if __name__ == "__main__":
    main()    