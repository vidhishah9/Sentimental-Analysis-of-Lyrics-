library(syuzhet)


song_lyrics <- "

Rising up, back on the street Did my time, took my chances Went the distance, now I'm back on my feet Just a man and his will to survive So many times, it happens too fast You trade your passion for glory Don't lose your grip on the dreams of the past You must fight just to keep them alive


"
s_v <- get_sentences(song_lyrics)

poa_word_v <- get_tokens(song_lyrics, pattern = "\\W")

syuzhet_vector <- get_sentiment(poa_word_v, method = "syuzhet")

nrc_vector <- get_sentiment(poa_word_v, method = "nrc")

afinn_vector <- get_sentiment(poa_word_v, method = "afinn")

bing_vector <- get_sentiment(poa_word_v, method = "bing")

sign(head(syuzhet_vector))

# sign(head(bing_vector))

# sign(head(afinn_vector))

# sign(head(nrc_vector))

sum(syuzhet_vector)

mean(syuzhet_vector)

# sum(bing_vector)

# mean(bing_vector)

# sum(afinn_vector)

# mean(afinn_vector)

# sum(nrc_vector)

# mean(nrc_vector)





# # Load the reticulate package
# library(reticulate)

# # Create a Python environment using virtualenvwrapper
# virtualenvwrapper::mkvirtualenv("myenv")
# use_virtualenv("myenv")

# # Install the necessary Python packages using pip
# py_install(c("google-api-python-client", "requests", "beautifulsoup4"))

# # Load the Python packages into R
# google_api_python_client <- import("googleapiclient.discovery")
# requests <- import("requests")
# soup <- import("bs4", as = "soup")
# np <- import("numpy")

# # Define the Python code as a string
# python_code <- "
# print('Enter the link')
# urluser = input()
# page_content = requests.get(urluser).content
# soup_page = soup(page_content, 'html.parser')
# artists = soup_page.findAll('a', {'class': 'artist'})
# songs = soup_page.findAll('span', {'class': 'song'})
# songsarr = []
# artistsarr = []
# for artist in artists:
#     songsarr.append(artist.get_text().strip())
# for song in songs:
#     artistsarr.append(song.get_text().strip())
# del artistsarr[1::2]
# combinedarr = []
# i = 0
# a = 0
# while i < len(artistsarr):
#     if a % 2 == 0:
#         combinedarr.insert(a, artistsarr[i])
#         i += 1
#     a += 1
# i = 0
# a = 0
# while i < len(songsarr):
#     if a % 2 != 0:
#         combinedarr.insert(a, songsarr[i])
#         i += 1
#     a += 1
# API_KEY = 'YOUR_API_KEY_HERE'
# resource = google_api_python_client.build('customsearch', 'v1', developerKey=API_KEY).cse()
# i = 0
# while i < len(combinedarr):
#     query = combinedarr[i] + ' ' + combinedarr[i+1]
#     result = resource.list(q=query, cx='b4587532947334d8a').execute()
#     x = 0
#     for item in result['items']:
#         while x < 1:
#             page_content = requests.get(item['link']).content
#             soup_page = soup(page_content, 'html.parser')
#             lyricpage = soup_page.findAll('div', {'class': 'Lyrics__Container-sc-1ynbvzw-5 Dzxov'})
#             print(len(lyricpage))
#             a = 0
#             while a < len(lyricpage):
#                 text = ' '.join(lyricpage[a].strings) 
#                 print(text)
#                 a += 1
#             x += 1
#     i += 2
# "

# # Run the Python code using the py_run_string function from reticulate
# py_run_string(python_code)
