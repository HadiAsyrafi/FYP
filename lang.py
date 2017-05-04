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
        stopwords_set = set(stopwords.words(language))
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

    most_rated_language = max(ratios, key=ratios.get)

    return most_rated_language



if __name__=='__main__':

    text = '''
    Er war sanftmütig und freundlich. Seine Augen standen dicht beieinander. Das bedeutete
Hinterlist. Seine Brauen stießen über der Nase zusammen. Das bedeutete Jähzorn. Seine Nase
war lang und spitz. Das bedeutete unstillbare Neugier. Seine Ohrläppchen waren
angewachsen. Das bedeutete Hang zum Verbrechertum. Warum gehst du nicht unter die
Leute?, fragte man ihn. Er besah sich im Spiegel und bemerkte einen grausamen Zug um
seinen Mund. Ich bin kein guter Mensch, sagte er. Er verbohrte sich in seine Bücher. Als er
sie alle ausgelesen hatte, musste er unter die Leute, sich ein neues Buch kaufen gehn.
Hoffentlich gibt es kein Unheil, dachte er und ging unter die Leute. Eine Frau sprach ihn an
und bat ihn, ihr einen Geldschein zu wechseln. Da sie sehr kurzsichtig war, musste sie
mehrmals hin- und zurücktauschen. Der Skorpion dachte an seine Augen, die dicht
beieinander standen, und verzichtete darauf, sein Geld hinterlistig zu verdoppeln. In der
Straßenbahn trat ihm ein Fremder auf die Füße und beschimpfte ihn in einer fremden Sprache.
Der Skorpion dachte an seine zusammengewachsenen Augenbrauen und ließ das Geschimpfe,
das er nicht verstand, als Bitte um Entschuldigung gelten. Er stieg aus und vor ihm lag eine
Brieftasche auf der Straße. Der Skorpion dachte an seine Nase und blickte sich nicht und
drehte sich auch nicht um. In der Buchhandlung fand er ein Buch, das hätte er gern gehabt.
Aber es war zu teuer. Es hätte gut in seine Manteltasche gepasst. Der Skorpion dachte an
seine Ohrläppchen und stellte das Buch ins Regal zurück. Er nahm ein anderes. Als er es
bezahlen wollte, klagte ein Bücherfreund: Das ist das Buch, das ich seit Jahren suche. Jetzt
kauft's mir ein anderer weg. Der Skorpion dachte an den grausamen Zug um seinen Mund und
sagte: Nehmen Sie das Buch. Ich trete zurück. Der Bücherfreund weinte fast. Er presste das
Buch mit beiden Händen an sein Herz und ging davon. Das war ein guter Kunde, sagte der
Buchhändler, aber für Sie ist auch noch was da. Er zog aus dem Regal das Buch, das der
Skorpion so gern gehabt hätte. Der Skorpion winkte ab: Das kann ich mir nicht leisten. -
Doch, Sie können, sagte der Buchhändler, eine Liebe ist der anderen wert. Machen Sie den
Preis. Der Skorpion weinte fast. Er presste das Buch mit beiden Händen fest an sein Herz und,
da er nichts mehr frei hatte, reichte er dem Buchhändler zum Abschied seinen Stachel. Der
Buchhändler drückte den Stachel und fiel tot um.
    '''

    language = detect_language(text)

    print language

