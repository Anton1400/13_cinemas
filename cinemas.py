import requests
import beautifulsoup4

def fetch_afisha_page():
    return requests.get('http://www.afisha.ru/msk/schedule_cinema/').text


def parse_afisha_list(raw_html):
    pass


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
    
