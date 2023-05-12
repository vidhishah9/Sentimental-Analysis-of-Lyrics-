library(syuzhet)


song_lyrics <- "

[Intro]

[Verse 1: Roger Waters & David Gilmour]
We don't need no education
We don't need no thought control
No dark sarcasm in the classroom
Teacher, leave them kids alone
Hey! Teacher! Leave them kids alone!

[Chorus: Roger Waters & David Gilmour]
All in all, it's just another brick in the wall
All in all, you're just another brick in the wall


[Verse 2: Islington Green School Students]
We don't need no education
We don't need no thought control
No dark sarcasm in the classroom
Teachers, leave them kids alone
Hey! Teacher! Leave us kids alone!

[Chorus: Islington Green School Students]
All in all, you're just another brick in the wall
All in all, you're just another brick in the wall

[Guitar Solo]

[Outro: Roger Waters]
Wrong, do it again! (*Children playing*)
Wrong, do it again!
If you don't eat your meat, you can't have any pudding!
(Wrong, do it again!)
How can you have any pudding if you don't eat your meat?
(Wrong, do it again!)
You! Yes! You behind the bike sheds! Stand still, laddie!
(If you don't eat your meat, you can't have any pudding!
How can you have any pudding if you don't eat your meat?)
(You! Yes! You behind the bike sheds! Stand still, laddie!)
*Children playing*
*Phone beeping sound*

"
s_v <- get_sentences(song_lyrics)

poa_word_v <- get_tokens(song_lyrics, pattern = "\\W")

syuzhet_vector <- get_sentiment(poa_word_v, method = "syuzhet")

nrc_vector <- get_sentiment(poa_word_v, method = "nrc")

afinn_vector <- get_sentiment(poa_word_v, method = "afinn")

bing_vector <- get_sentiment(poa_word_v, method = "bing")

head(syuzhet_vector)

sign(head(bing_vector))

sign(head(afinn_vector))

sign(head(nrc_vector))

sum(syuzhet_vector)

mean(syuzhet_vector)

# sum(bing_vector)

# mean(bing_vector)

# sum(afinn_vector)

# mean(afinn_vector)

# sum(nrc_vector)

# mean(nrc_vector)

