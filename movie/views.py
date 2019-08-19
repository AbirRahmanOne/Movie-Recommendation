from django.shortcuts import render
from django.views.generic import TemplateView
from decouple import config

import requests as rq
import json


class movie_recommend(TemplateView):
    template_name = "movie/index.html"

    def __init__(self):
        self.movie_name = ''
        self.data = {}

    def get(self, request):
        return render(request, 'movie/index.html', {'data': self.data})

    def post(self, request):
        # self.data = {'Dangal': {'Year': '2016', 'Genre': ['Action', ' Biography', ' Drama', ' Sport'], 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTQ4MzQzMzM2Nl5BMl5BanBnXkFtZTgwMTQ1NzU3MDI@._V1_SX300.jpg', 'imdbRating': '8.4', 'imdbVotes': 12.6072, 'BoxOffice': 12.382287, 'Rotten_Tomatoes': '88%', 'Link': 'https://www.youtube-nocookie.com/embed/x_7YlGv9u1g'}, 'Rang De Basanti': {'Year': '2006', 'Genre': ['Comedy', ' Drama'], 'Poster': 'https://m.media-amazon.com/images/M/MV5BM2I3OGU1YmQtNjIyOC00OGYzLWFkOTgtOGIyMDVlNmE2M2VmXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_SX300.jpg', 'imdbRating': '8.2', 'imdbVotes': 10.1468, 'BoxOffice': 'N/A', 'Link': 'https://www.youtube-nocookie.com/embed/QHhnhqxB4E8'}, 'Dil Chahta Hai': {
        #    'Year': '2001', 'Genre': ['Comedy', ' Drama', ' Romance'], 'Poster': 'https://m.media-amazon.com/images/M/MV5BMzcxOWU3ZTAtZmYwYS00MzJmLWI1MmEtYmJlOTFjYTAxMWUwXkEyXkFqcGdeQXVyODk1MzE5NDA@._V1_SX300.jpg', 'imdbRating': '8.2', 'imdbVotes': 6.1216, 'BoxOffice': 'N/A', 'Link': 'https://www.youtube-nocookie.com/embed/m13b25V0B10'}, 'Ghajini': {'Year': '2008', 'Genre': ['Action', ' Drama', ' Mystery', ' Thriller'], 'Poster': 'https://m.media-amazon.com/images/M/MV5BMjU4N2ZlYTktNTFlNy00OGZmLWEwZWQtZDllMjk1MzhiZDEzXkEyXkFqcGdeQXVyODE0NjUxNzY@._V1_SX300.jpg', 'imdbRating': '7.3', 'imdbVotes': 5.2343, 'BoxOffice': 2.411071, 'Rotten_Tomatoes': '50%', 'Link': 'https://www.youtube-nocookie.com/embed/_I0xx8Oj3Ww'}}
        self.movie_name = request.POST['search']
        if self.movie_name != '':
            try:
                self.data = get_sorted_recommendations(
                    self.movie_name.split(','))
                # pass
            except:
                pass
        return render(request, 'movie/index.html', {'data': self.data})


def get_movies_from_tastedive(a):
    baseurl = config('baseurl1')
    d = {'q': a, 'limit': 5,
         'k': config('apikey_movie'), 'verbose': 1}
    x = json.loads(rq.get(baseurl, params=d).text)
    return x


def extract_movie_titles(a):
    x = []
    for i in a['Similar']['Results']:
        x.append([i['Name'], i['yUrl']])
    return x


def get_related_titles(a):
    y = []
    for i in a:
        x = extract_movie_titles(get_movies_from_tastedive(i))
        for j in x:
            if j not in y:
                y.append(j)
    return y


def get_movie_data(a):
    baseurl = config('baseurl2')
    d = {'t': a[0], 'r': 'json', 'apikey': config('apikey_moviedetail2')}
    x = json.loads(rq.get(baseurl, params=d).text)
    data = {'Year': x['Year'], 'Genre': x['Genre'].split(',')[:4], 'Poster': x['Poster'], 'imdbRating': x['imdbRating'], 'imdbVotes': float(
        x['imdbVotes'].replace(',', ''))/10000, 'Link': a[1], 'Type': x['Type']}
    for k in x['Ratings']:
        if k['Source'] == 'Rotten Tomatoes':
            data['Rotten_Tomatoes'] = k['Value']
            break
    try:
        data['BoxOffice'] = float(x['BoxOffice'][1:].replace(',', ''))/1000000
    except:
        data['BoxOffice'] = 'N/A'
        pass
    try:
        data['Total_Season'] = x['totalSeasons']
    except:
        pass
    return data


def get_sorted_recommendations(a):
    x = get_related_titles(a)
    result = {}
    for i in x:
        try:
            result[i[0]] = get_movie_data(i)
        except:
            pass
    b = sorted(result, key=lambda x: (
        float(result[x]['imdbRating']), float(result[x]['imdbVotes'])), reverse=True)
    res = {}
    for i in b:
        res[i] = result[i]
    return res
