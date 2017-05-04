# -*- coding: utf-8 -*-
import sys

try:
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print '[!] You need to install nltk (http://nltk.org/index.html)'



#----------------------------------------------------------------------
def _calculate_languages_ratios(text):
    """
    Calculate probability of given text to be written in several languages and
    return a dictionary that looks like {'french': 2, 'spanish': 4, 'english': 0}
    
    @param text: Text whose language want to be detected
    @type text: str
    
    @return: Dictionary with languages and unique stopwords seen in analyzed text
    @rtype: dict
    """

    languages_ratios = {}

    '''
    nltk.wordpunct_tokenize() splits all punctuations into separate tokens
    
    >>> wordpunct_tokenize("That's thirty minutes away. I'll be there in ten.")
    ['That', "'", 's', 'thirty', 'minutes', 'away', '.', 'I', "'", 'll', 'be', 'there', 'in', 'ten', '.']
    '''

    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    # Compute per language included in nltk number of unique stopwords appearing in analyzed text
    for language in stopwords.fileids():
    # [danish, dutch, english, finnish, french, german, hungarian, italian, kazakh, norwegian, portuguese, russian, spanish, swedish, turkish]

        stopwords_set = set(stopwords.words(language))
	'''stops=[]
	for item in stopwords.words(language):
		stops.extend(wordpunct_tokenize(item))
		stopwords_set = set(stops)'''

        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements) # language "score"

    return languages_ratios


#----------------------------------------------------------------------
def detect_language(text):
    """
    Calculate probability of given text to be written in several languages and
    return the highest scored.
    
    It uses a stopwords based approach, counting how many unique stopwords
    are seen in analyzed text.
    
    @param text: Text whose language want to be detected
    @type text: str
    
    @return: Most scored language guessed
    @rtype: str
    """

    ratios = _calculate_languages_ratios(text)

    print ratios

    most_rated_language = max(ratios, key=ratios.get)

    return most_rated_language



if __name__=='__main__':

    text = '''
    Asielzoekerscentra worden jaarlijks geconfronteerd met vermissingen van AMA (Alleenstaande Minderjarige Asielzoekers) jongens en meisjes. Volgens vele Asielzoekers centra worden er veelal meisjes vermist. In 1990 zouden er 3 per jaar mysterieus verdwijnen en in de jaren daaropvolgend zijn dat er tientallen geworden. Langzaam begint de groepsleiding te begrijpen, hoe dit zoal in zijn werk gaat, maar ervaren een bureaucratische muur waar met geen mogelijkheid verandering in gebracht kan worden. Het schrijnende is dat de groepsleiding hier dagelijks mee te maken krijgen maar verzuipen in de tekortgeschoten protocollen. Het is dan ook verontrustend dat het asielzoekersbeleid niet verantwoord versterkt wordt, zodat deze kwetsbare groep kinderen buiten de mazen van de wet vallen.
 
De vele artikelen die hierover zijn geschreven, geven aan, dat het om een weldoordacht netwerk gaat. Dit begint al in de landen van oorsprong waar ze de meisjes ronselen. Ze worden verkracht of bedreigd dat hun dierbaren worden vermoord. Kansloos als ze zijn en volgepropt met kortzichtige moralen door hun omgeving, vinden ze geen mogelijkheid om uit de handen van de pooiers te blijven. Wanneer ze eenmaal afhankelijk zijn van de pooier, krijgen ze een paspoort om bijvoorbeeld naar Nederland te vluchten. Ze weten niet, dat zelfs het AZC niet veilig is en de begeleiding kan niets doen om de verdwijningen te voorkomen. De meisjes hebben een telefoonnummer, dat moeten ze bellen want anders gebeurt er waar ze zo bang voor zijn. Er zijn meisjes die het telefoonnummer zijn kwijtgeraakt en daardoor in een psychiatrische inrichting terecht zijn gekomen. Een niet te onderschatten angst waardoor het heel lastig is om ze te helpen. Soms lopen de meisjes zelf weg maar vaak worden ze ontvoerd, gezien het feit dat ze alles hebben achtergelaten, ook al is dat niet veel.
 
Dit netwerk zit diepgeworteld in vele legale instanties, men moet dan denken aan ambassades, ministerie van Justitie, vliegtuigmaatschappijen en politie (vreemdelingen- en zedenpolitie). Vele honderden meisjes en een aantal jongens zijn verdwenen en er lijkt geen einde aan te komen. Alle verontruste berichten vanuit alle hoeken en instanties, verontrusten niet genoeg om tot een verbetering van het systeem te komen.
    '''

    language = detect_language(text)

    print language

