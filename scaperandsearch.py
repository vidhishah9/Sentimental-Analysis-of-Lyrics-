from googleapiclient.discovery import build
import requests;
from bs4 import BeautifulSoup as soup;
import numpy as np
import rpy2 
from rpy2 import robjects
from rpy2.robjects.packages import importr


print("Enter the link")
urluser = input()
page_content = requests.get(urluser).content
soup_page = soup(page_content, 'html.parser')
artists = soup_page.findAll('a', {"class": "artist"})
songs = soup_page.findAll('span', {"class": "song"})
songsarr = []
artistsarr = []
for artist in artists:
    songsarr.append(artist.get_text().strip())
for song in songs:
    artistsarr.append(song.get_text().strip())

# npsongsarr = np.array(songsarr)
# npartistarr = np.array(artistsarr)
del artistsarr[1::2]
# print(len(artistsarr))
combinedarr = []
i = 0
a=0
while i < len(artistsarr):
    if(a%2==0):
        combinedarr.insert(a, artistsarr[i])
        i+=1
    a+=1
i =0 
a=0
while i < len(songsarr):
    if(a%2!=0):
        combinedarr.insert(a, songsarr[i])
        i+=1
    a+=1

print(combinedarr)

API_KEY = "AIzaSyAEmC6cs0DvRZPI5rBjaXWOEH30z7oaWAI"
resource = build("customsearch", 'v1', developerKey=API_KEY).cse()

i = 0
# while i < len(combinedarr):
while i < 1:
    query = combinedarr[i] + " " + combinedarr[i+1]
    print(query)
    result = resource.list(q=query, cx='b4587532947334d8a').execute()
    # result = resource.list(q='Ebony Ivory Paul McCartney Stevie Wonder', cx='b4587532947334d8a').execute()
    x= 0
    original = ""
    for item in result['items']:
        while x < 1:
            page_content = requests.get(item['link']).content
            soup_page = soup(page_content, 'html.parser')
            lyricpage = soup_page.findAll('div', {"class": "Lyrics__Container-sc-1ynbvzw-5 Dzxov"})
            print(len(lyricpage))
            a=0
            while a < len(lyricpage):
                text = " ".join(lyricpage[a].strings) 
                original+=text
                a+=1
            print(original)

            x+=1
    i+=2

import rpy2.robjects.packages as rpackages
from rpy2.robjects import r
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
import pandas as pd
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

from rpy2.robjects.conversion import localconverter


# Install and import the 'syuzhet' package
utils = rpackages.importr('utils')
utils.install_packages('syuzhet')
syuzhet = importr('syuzhet')

song_lyrics = "Rising up, back on the street Did my time, took my chances Went the distance, now I'm back on my feet Just a man and his will to survive So many times, it happens too fast You trade your passion for glory Don't lose your grip on the dreams of the past You must fight just to keep them alive "
s_v = syuzhet.get_sentences(song_lyrics)
poa_word_v = syuzhet.get_tokens(song_lyrics, pattern = "\\W")
syuzhet_vector = syuzhet.get_sentiment(poa_word_v, method = "syuzhet")


pandas2ri.activate()
pd_df = pd.DataFrame(syuzhet_vector)

base = importr('base')
with localconverter(ro.default_converter + pandas2ri.converter):
  df_summary = base.summary(pd_df)
  mean = pd_df.mean()

print(float(mean))