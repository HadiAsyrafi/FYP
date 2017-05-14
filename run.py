# -*- coding: utf-8 -*-

# web scraper

'''from web_scraper import web_scraper

scraper = web_scraper(site = 'Kedah')

txt = scraper.txt

print txt'''

# lang detector

"""from lang_detector import lang_detect

txt = open('Short Stories/malay.txt', 'r').read()

lang = lang_detect(txt)

#print lang.text

print lang.detect_language()"""

# highlighter

'''from highlighter import highlighter

txt = open('Short Stories/english.txt', 'r').read()

hg = highlighter(txt)

print hg.txt

hg.highlight()'''

# summariser

'''from summariser import *

txt = open('Short Stories/english2.txt', 'r').read()

summ = summariser(txt, len(txt)/50)

output = summ.summarize()

print '\n\n'

for data in output['top_n_summary']:
	print data

print '\n\nDivider\n\n'

for data in output['mean_scored_summary']:
	print data'''


# sentiment analysis

from sentiment import *

txt = open('Review/the help review.txt', 'r').read()

txt = """I must admit when I saw the preview for "Inglorious Basterds" I gave myself big expectations. THIS FILM DID NOT Disappoint.

Rarely when I watch a movie with such high-expectations do I have those expectations met or exceeded; this film did that and more. Even more rarely do I clap at the end of a movie, this I and everyone else in the theater did.

I have to say I am a little biased towards Quentin, I grew up with "Pulp Fiction." I watched it when I was 12 and it is still my favorite and most influential film.

However, since then Quentin has not really lived up to his billing. His style was getting a little predictable instead of familiar, the quality honestly wasn't there (I never watched Jackie Brown, and then there's Grindhouse). That is until "Inglorious Basterds." What Quentin did was exactly what was needed for the war genre, a spaghetti western feel that could only be done by Tarantino or Sergio Leone, but seeing how Leone is dead, Tarantino's the self appointed guy on this masterpiece.

So let's look at the movie which I won't give away. The writing was spot on, a beautiful transition between using not one but four different languages in this movie. Not to mention this movie was set up in the classic Tarantino mold, great scenes of rich meaningful dialog and sudden shocking action.

The acting was superb!! Christopher Waltz deserves an Oscar, seriously. I don't say that often, but honestly the man should get one for this movie, he spoke every language in this movie, and delivered with such amazing touch and poise. He stole the show in a movie that everybody was amazingly impressive.

I have no problem building this movie up, because this movie is the best film I've seen all year, and probably all of next year. Quite frankly the more I think about it, this movie may crack my top films of all time, and is Quentin's best movie since "Pulp Fiction." Take it from me, watch this film. I loved it doesn't do this movie enough justice.

I watched it yesterday and I'm still blown away. Thank you Quentin from the bottom of my heart for you making this movie. You're back on top again buddy. I can't say enough for "Inglorious Basterds!"  
"""

splitter = Splitter()
postagger = POSTagger()

splitted_sentences = splitter.split(txt)
pos_tagged_sentences = postagger.pos_tag(splitted_sentences)

dicttagger = DictionaryTagger(['dicts/positive.yml', 'dicts/negative.yml', 'dicts/inc.yml', 'dicts/dec.yml', 'dicts/inv.yml'])

dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)

print sentiment_score(dict_tagged_sentences)
