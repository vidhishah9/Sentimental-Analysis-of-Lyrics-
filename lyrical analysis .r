library(syuzhet)

song_lyrics <- "
So long, I've been looking too hard
I've been waiting too long
Sometimes I don't know what I will find
I only know it's a matter of time
When you love someone
When you love someone
It feels so right, so warm and true
I need to know if you feel it too
Maybe I'm wrong
Won't you tell me if I'm coming on too strong?
This heart of mine has been hurt before
This time I want to be sure
I've been waiting for a girl like you to come into my life
I've been waiting for a girl like you, your a love that will survive
I've been waiting for someone new to make me feel alive
Yeah, waiting for a girl like you to come into my life
You're so good
When we make love it's understood
It's more than a touch or a word can say
Only in dreams could it be this way
When you love someone
Yeah, I really love someone
Now, I know it's right
From the moment I wake up 'til deep in the night
There's nowhere on earth that I'd rather be than holding you tenderly
I've been waiting for a girl like you to come into my life
I've been waiting for a girl like you, your a love that will survive
I've been waiting for someone new to make me feel alive
Yeah, waiting for a girl like you to come into my life
I've been waiting, waiting for you, ooh
Ooh, I've been waiting
(Waiting) I've been waiting, yeah
(I've been waiting for a girl like you, I've been waiting)
Won't you come into my life?
Ah
"
s_v <- get_sentences(song_lyrics)

poa_word_v <- get_tokens(song_lyrics, pattern = "\\W")

syuzhet_vector <- get_sentiment(poa_word_v, method = "syuzhet")

# nrc_vector <- get_sentiment(poa_word_v, method = "nrc")

# afinn_vector <- get_sentiment(poa_word_v, method = "afinn")

# bing_vector <- get_sentiment(poa_word_v, method = "bing")

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
