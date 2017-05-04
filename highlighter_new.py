# -*- coding: utf-8 -*-
import nltk

HTML_TEMPLATE = """<html>
    <head>
        <title>%s</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    </head>
    <body>%s</body>
</html>"""


txt = '''The Lazarus effect refers to semiconductor detectors; when these are used in harsh radiation environments, defects begin to appear in the semiconductor crystal lattice as atoms become displaced because of the interaction with the high-energy traversing particles. These defects, in the form of both lattice vacancies and atoms at interstitial sites, have the effect of temporarily trapping the electrons and holes which are created when ionizing particles pass through the detector. Since it is these electrons and holes which drifting under an electric field produce a signal announcing the passage of a particle, when large amounts of defects are produced, detector signal can be strongly reduced leading to an unusable (dead) detector.
Radiation damage produced by relativistic lead ions from the SPS beam hitting a silicon microstrip detector of the NA50 experiment at CERN.'''

sentences = nltk.tokenize.sent_tokenize(txt)
tokens = [nltk.tokenize.word_tokenize(s) for s in sentences]
pos_tagged_tokens = [nltk.pos_tag(t) for t in tokens]

entity_interactions = []

for sentence in pos_tagged_tokens:

        all_entity_chunks = []
        previous_pos = None
        current_entity_chunk = []

        for (token, pos) in sentence:

            if pos == previous_pos and pos.startswith('NN'):
                current_entity_chunk.append(token)
            elif pos.startswith('NN'):
                if current_entity_chunk != []:
                    all_entity_chunks.append((' '.join(current_entity_chunk),
                            pos))
                current_entity_chunk = [token]

            previous_pos = pos

        if len(all_entity_chunks) > 1:
            entity_interactions.append(all_entity_chunks)
        else:
            entity_interactions.append([])

assert len(entity_interactions) == len(sentences)

markup = []
for sentence_idx in range(len(sentences)):
	s = sentences[sentence_idx]
        for (term, _) in entity_interactions[sentence_idx]:
            s = s.replace(term, '<strong>%s</strong>' % (term, ))
        markup += [s]

html = HTML_TEMPLATE % ('News' + ' Interactions', 
                            ' '.join(markup),)

f = open('news.html', 'w')
f.write(html.encode('utf-8'))
f.close()
