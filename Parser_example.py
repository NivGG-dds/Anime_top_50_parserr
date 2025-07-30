# импорт неообходимых модулей
import requests
from bs4 import BeautifulSoup

# url сайта
url = 'https://site.yummyani.me/catalog/top'

# Получение HTML-страницы
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

# Поиск элементов с названиями и рейтингами
titles = soup.find_all('a', class_='anime-title')
ratings = soup.find_all('span', 'main-rating materiable')

# делаем цикл для воспроизведения полученной информации
for i in range(1, 51):

    title = titles[i].text.strip()
    rating = ratings[i].text.strip()
    href = titles[i].get('href')

    print(f'Номер в топе: {i} Аниме - {title} с рейтингом - {rating}    ссылка на аниме - https://site.yummyani.me{href}')
