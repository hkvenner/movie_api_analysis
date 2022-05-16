import csv
import requests
import numpy as np
import pandas as pd

from keys import api_key

oscar_winners = pd.read_csv("oscar_winners.csv")
all_movie_rows = []
header = ['Movie Title', 'Runtime', 'Genre', 'Award Wins', 'Award Nominations', 'Box Office', 'Director', 'Plot', 'DVD']

#this loop gets the movie info from the IMDB API using the movie ids in the input spreadsheet
for id in oscar_winners['IMDB'].iteritems():
    data = requests.get('http://www.omdbapi.com/?apikey='+api_key+'&i='+id[1]).json()
    row = []
    row.append(data['Title'])
    row.append(int(data['Runtime'].split()[0]))
    row.append(data['Genre'])
    row.append(int(data['Awards'].split()[3]))
    row.append(int(data['Awards'].split()[6]))
    row.append(int(data['BoxOffice'][1:].replace(',','')))
    #Additional columns for Exceeds Expectations
    row.append(data['Director'])
    row.append(data['Plot'])
    row.append(data['DVD'])
    all_movie_rows.append(row)

with open("movies.csv",'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for movie in all_movie_rows:
        writer.writerow(movie)
