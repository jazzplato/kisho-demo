import os
import sys
import csv
import requests

DIR_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_DATA = os.path.join(DIR_BASE, "data")
FILE_CSV_MOVIES = os.path.join(DIR_DATA, "movies.csv")
URL_MOVIES = "http://localhost:8000/movies/"

with open(FILE_CSV_MOVIES, "r") as f:
    movies = csv.DictReader(f)
    count = 1
    for movie in movies:
        url = URL_MOVIES
        body = {
            'title': movie.get('title'),
            'year': movie.get('year'),
        }
        res = requests.post(url, data=body)
        print('\r{0}'.format(count), end='')
        count += 1