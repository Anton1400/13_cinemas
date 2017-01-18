import requests
from bs4 import BeautifulSoup                                     


def fetch_afisha_page():
    return requests.get('http://www.afisha.ru/msk/schedule_cinema/').text


def parse_afisha_list(raw_html):
    mass_info = []                                    
    soup = BeautifulSoup(raw_html, 'html.parser')
    for film in soup.find_all('div', class_='object s-votes-hover-area collapsed'):
        mass_info.append(dict(name=film.find('h3', class_='usetags').string,
                              count=len(film.find('tbody'))))
    return mass_info
        
    



def fetch_movie_info(movie_title):
    pass


def output_movies_to_console(movies):
    print('|название|оценка|etc|') # Напечатать в виде таблиы
    print('|--------|------|---|')
    for cinema in movies:
        code
        print('*'*70)


if __name__ == '__main__':
    movies = parse_afisha_list(fetch_afisha_page()) # html страница афиши, которую нужно распарсить, информация содержиться в псевдо таблице на сайте афиши
    print(movies)
    
