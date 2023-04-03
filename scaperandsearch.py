from googleapiclient.discovery import build
import requests;
import json;
import html;
from bs4 import BeautifulSoup as soup;
import urllib.request
import numpy as np


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
    for item in result['items']:
        while x < 1:
            page_content = requests.get(item['link']).content
            soup_page = soup(page_content, 'html.parser')
            lyricpage = soup_page.findAll('div', {"class": "Lyrics__Container-sc-1ynbvzw-5 Dzxov"})
            print(len(lyricpage))
            a=0
            while a < len(lyricpage):
                text = " ".join(lyricpage[a].strings) 
                print(text)
                a+=1

            # third_p = soup_page.find('div', {"class": "Lyrics__Container-sc-1ynbvzw-5 Dzxov"})
            # print(''.join(third_p.find('br').next_siblings))

            x+=1
    i+=2
