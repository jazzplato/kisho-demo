import csv
import requests
from urllib.parse import urljoin

FILE_CSV_MOVIES = "movies.csv"
URL_MOVIES = "http://localhost:8000/movies/"

with open(FILE_CSV_MOVIES, "r") as f:
    movies = csv.DictReader(f)
    count = 0
    count_diff = 0
    for movie in movies:
        count += 1
        if count == 1:
            continue
        print('\r{0}'.format(count), end='')

        url = urljoin(URL_MOVIES, movie.get('id'))
        res = requests.get(url)
        if res.status_code != 200:
            print("Missing: {}\t: {}".format(movie.get("id"),
                                             movie.get("title")))
            count_diff += 1
            continue
        res_json = res.json()
        if res_json.get("title") != movie.get("title"):
            print("Mismatch: {}\t: {} != {}".format(movie.get("id"),
                                                    movie.get("title"),
                                                    res_json.get("title")))
            continue
