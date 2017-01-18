import requests
import re

from datetime import date
from bs4 import BeautifulSoup                                     


def fetch_afisha_page():
    req = requests.get('http://www.afisha.ru/msk/schedule_cinema/')
    if req.status_code == requests.codes.ok:
        return req.content


def parse_afisha_list(raw_html):
    mass_info = []                                    
    soup = BeautifulSoup(raw_html, 'html.parser')
    for film in soup.find_all('div', class_='object s-votes-hover-area collapsed'):
        mass_info.append({
            'name': film.find('h3', class_='usetags').string,
            'count': len(film.find('tbody'))
        })
    return mass_info
        
    
def fetch_movie_info(movie_title):
    params = {
        'first': 'yes',
        'kp_query': '{} {}'.format(movie_title, date.today().year),
    }
    
    req = requests.get('https://www.kinopoisk.ru/index.php', params=params)

    soup = BeautifulSoup(req.content, 'html.parser')
    rating = soup.select('.rating_ball')
    if rating:
        rating = float(rating[0].text)
    
    rating_count = soup.select('.ratingCount')
    if rating_count:
        rating_count = ''.join(re.findall('[0-9]+', rating_count[0].text))    

    return [('rating', rating), ('rating_count', rating_count)]


def output_movies_to_console(movies):
    print('|название|оценка|etc|') # Напечатать в виде таблиы
    print('|--------|------|---|')
    for cinema in movies:
        code
        print('*'*70)


if __name__ == '__main__':
    movies = parse_afisha_list(fetch_afisha_page())
    print(movies)
    
    for movie in movies:
        movie.update(fetch_movie_info(movie['name']))
        
    #output_movies_to_consol(movies)
