from googleapiclient.discovery import build
import requests;
from bs4 import BeautifulSoup as soup;
import numpy as np
import rpy2 
from rpy2 import robjects
from rpy2.robjects.packages import importr
import rpy2.robjects.packages as rpackages
from rpy2.robjects import r
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
import pandas as pd
import rpy2.robjects as ro
import re
# from rpy2.robjects.conversion import localconverter
utils = rpackages.importr('utils')
syuzhet = importr('syuzhet')
base = importr('base')

meanstotals = []

def findmean(numb):
    urluser = "https://playback.fm/charts/rnb/" + str(numb)
    page_content = requests.get(urluser).content
    soup_page = soup(page_content, 'html.parser')
    artists = soup_page.findAll('a', {"class": "artist"})
    songs = soup_page.findAll('span', {"class": "song"})
    titles = soup_page.findAll('h1', {"class": "cf large"})
    setnumb = 200
    genreone = "R&B"
    genreset = ""
    for title in titles:
        titleextract = title.get_text().strip()
        print(titleextract)
        if genreone in titleextract:
            genreset = genreone
        print(genreset)
        temp = re.findall(r'\d+', titleextract)
        print(temp[0])
        setnumb = int(temp[0]) * 2
        print(setnumb)

    songsarr = []
    artistsarr = []
    for artist in artists:
        songsarr.append(artist.get_text().strip())
    for song in songs:
        artistsarr.append(song.get_text().strip())

    del artistsarr[1::2]
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
        
    API_KEY = "AIzaSyAEmC6cs0DvRZPI5rBjaXWOEH30z7oaWAI"
    resource = build("customsearch", 'v1', developerKey=API_KEY).cse()
    means = []
    i = 0
    while i < setnumb:
        query = combinedarr[i] + " " + combinedarr[i+1]
        print(query)
        result = resource.list(q=query, cx='b4587532947334d8a').execute()
        x= 0
        original = ""
        if result['searchInformation']['totalResults'] == '0':
            i+=2
            means.append(0)
        else:
            for item in result['items']:
                while x < 1:
                    page_content = requests.get(item['link']).content
                    soup_page = soup(page_content, 'html.parser')
                    lyricpage = soup_page.findAll('div', {"class": "Lyrics__Container-sc-1ynbvzw-5 Dzxov"})
                    if len(lyricpage)==0:
                        x+=1
                        means.append(float(0))
                    else:
                        a=0
                        while a < len(lyricpage):
                            text = " ".join(lyricpage[a].strings) 
                            original+=text
                            a+=1
                        song_lyrics = original
                        poa_word_v = syuzhet.get_tokens(song_lyrics, pattern = "\\W")
                        syuzhet_vector = syuzhet.get_sentiment(poa_word_v, method = "syuzhet")
                        pandas2ri.activate()
                        pd_df = pd.DataFrame(syuzhet_vector)
                        with localconverter(ro.default_converter + pandas2ri.converter):
                            mean = pd_df.mean()
                        means.append(float(mean))
                        original = ""
                        text = ""
                        x+=1
            i+=2
        
        b = 0
        meansum = 0

    while b < len(means):
        meansum = meansum + means[b]
        b = b + 1
    meantot = meansum/(len(means))
    print(meantot)
    print(len(means))
    meanstotals.append(meantot)
    print(meanstotals)

numb = 1980
while(numb<=2021):
    findmean(numb)
    numb=numb + 1

print(meanstotals)