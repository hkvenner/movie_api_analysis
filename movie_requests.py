import csv
import requests
import numpy as np
import pandas as pd

from keys import api_key

oscar_winners = pd.read_csv("oscar_winners.csv")

for id in oscar_winners['IMDB'].iteritems():
    print(id[1])


title = "Happy Feet"
#res = requests.get("http://www.omdbapi.com/?apikey={}&/?t=Happy+Feet".format(api_key))
#res = requests.get('http://www.omdbapi.com/?apikey='+api_key+'&i='+title).json()

#print(res)

