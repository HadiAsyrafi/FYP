# -*- coding: utf-8 -*-
import json
import nltk
import numpy

txt = '''A major change that has occurred in the Western family is an increased incidence in divorce. Whereas in the past, divorce was a relatively rare occurrence, in recent times it has become quite commonplace. This change is borne out clearly in census figures. For example thirty years ago in Australia, only one marriage in ten ended in divorce; nowadays the figure is more than one in three (Australian Bureau of Statistics, 1996: p.45). A consequence of this change has been a substantial increase in the number of single parent families and the attendant problems that this brings (Kilmartin, 1997).

An important issue for sociologists, and indeed for all of society, is why these changes in marital patterns have occurred. In this essay I will seek to critically examine a number of sociological explanations for the 'divorce phenomenon' and also consider the social policy implications that each explanation carries with it. It will be argued that the best explanations are to be found within a broad socio-economic framework.

One type of explanation for rising divorce has focused on changes in laws relating to marriage. For example, Bilton, Bonnett and Jones (1987) argue that increased rates of divorce do not necessarily indicate that families are now more unstable. It is possible, they claim, that there has always been a degree of marital instability. They suggest that changes in the law have been significant, because they have provided unhappily married couples with 'access to a legal solution to pre-existent marital problems' (p.301). Bilton et al. therefore believe that changes in divorce rates can be best explained in terms of changes in the legal system. The problem with this type of explanation however, is that it does not consider why these laws have changed in the first place. It could be argued that reforms to family law, as well as the increased rate of divorce that has accompanied them, are the product of more fundamental changes in society.

Another type of explanation is one that focuses precisely on these broad societal changes. For example, Nicky Hart (cited in Haralambos, 1995) argues that increases in divorce and marital breakdown are the result of economic changes that have affected the family. One example of these changes is the raised material aspirations of families, which Hart suggests has put pressure on both spouses to become wage earners. Women as a result have been forced to become both homemakers and economic providers. According to Hart, the contradiction of these two roles has lead to conflict and this is the main cause of marital breakdown. It would appear that Hart's explanation cannot account for all cases of divorce - for example, marital breakdown is liable to occur in families where only the husband is working. Nevertheless, her approach, which is to relate changes in family relations to broader social forces, would seem to be more probing than one that looks only at legislative change.

The two explanations described above have very different implications for social policy, especially in relation to how the problem of increasing marital instability might be dealt with. Bilton et al. (1995) offer a legal explanation and hence would see the solutions also being determined in this domain. If rises in divorce are thought to be the consequence of liberal divorce laws, the obvious way to stem this rise is to make them less obtainable. This approach, one imagines, would lead to a reduction in divorce statistics; however, it cannot really be held up as a genuine solution to the problems of marital stress and breakdown in society. Indeed it would seem to be a solution directed more at symptoms than addressing fundamental causes. Furthermore, the experience of social workers, working in the area of family welfare suggests that restricting a couple's access to divorce would in some cases serve only to exacerbate existing marital problems (Johnson, 1981). In those cases where violence is involved, the consequences could be tragic. Apart from all this, returning to more restrictive divorce laws seems to be a solution little favoured by Australians. (Harrison, 1990).

Hart (cited in Haralambos, 1995), writing from a Marxist-feminist position, traces marital conflict to changes in the capitalist economic system and their resultant effect on the roles of men and women. It is difficult to know however, how such an analysis might be translated into practical social policies. This is because the Hart program would appear to require in the first place a radical restructuring of the economic system. Whilst this may be desirable for some, it is not achievable in the present political climate. Hart is right however, to suggest that much marital conflict can be linked in some way to the economic circumstances of families. This is borne out in many statistical surveys which show consistently that rates of divorce are higher among socially disadvantaged families (McDonald, 1993). This situation suggests then that social policies need to be geared to providing support and security for these types of families. It is little cause for optimism however, that in recent years governments of all persuasions have shown an increasing reluctance to fund social welfare programs of this kind.

It is difficult to offer a comprehensive explanation for the growing trend of marital breakdown; and it is even more difficult to find solutions that might ameliorate the problems created by it. Clearly though, as I have argued in this essay, the most useful answers are to be found not within a narrow legal framework, but within a broader socio-economic one.

Finally, it is worth pointing out that, whilst we may appear to be living in a time of increased family instability, research suggests that historically, instability may have been the norm rather than the exception. As Bell and Zajdow (1997) point out, in the past, single parent and step families were more common than is assumed - although the disruptive influence then was not divorce, but the premature death of one or both parents. This situation suggests that in studying the modern family, one needs to employ a historical perspective, including the possibility of looking to the past in searching for ways of dealing with problems in the present.'''

'''#print txt.split(".")

sentences = nltk.tokenize.sent_tokenize(txt)
#print sentences

tokens = [nltk.tokenize.word_tokenize(s) for s in sentences]
#print tokens

pos_tagged_tokens = [nltk.pos_tag(t) for t in tokens]
#print pos_tagged_tokens

#for chunk in nltk.ne_chunk_sents(pos_tagged_tokens, binary=True):
    #print(chunk)'''


N = 200  # Number of words to consider
CLUSTER_THRESHOLD = 5  # Distance between words to consider
TOP_SENTENCES = 5  # Number of sentences to return for a "top n" summary

# Approach taken from "The Automatic Creation of Literature Abstracts" by H.P. Luhn

def _score_sentences(sentences, important_words):
    scores = []
    sentence_idx = -1

    for s in [nltk.tokenize.word_tokenize(s) for s in sentences]:

        sentence_idx += 1
        word_idx = []

        # For each word in the word list...
        for w in important_words:
            try:
                # Compute an index for where any important words occur in the sentence.

                word_idx.append(s.index(w))
            except ValueError, e: # w not in this particular sentence
                pass

        word_idx.sort()

        # It is possible that some sentences may not contain any important words at all.
        if len(word_idx)== 0: continue

        # Using the word index, compute clusters by using a max distance threshold
        # for any two consecutive words.

        clusters = []
        cluster = [word_idx[0]]
        i = 1
        while i < len(word_idx):
            if word_idx[i] - word_idx[i - 1] < CLUSTER_THRESHOLD:
                cluster.append(word_idx[i])
            else:
                clusters.append(cluster[:])
                cluster = [word_idx[i]]
            i += 1
        clusters.append(cluster)

        # Score each cluster. The max score for any given cluster is the score 
        # for the sentence.

        max_cluster_score = 0
        for c in clusters:
            significant_words_in_cluster = len(c)
            total_words_in_cluster = c[-1] - c[0] + 1
            score = 1.0 * significant_words_in_cluster \
                * significant_words_in_cluster / total_words_in_cluster

            if score > max_cluster_score:
                max_cluster_score = score

        scores.append((sentence_idx, score))

    return scores

def summarize(txt):
    sentences = [s for s in nltk.tokenize.sent_tokenize(txt)]
    normalized_sentences = [s.lower() for s in sentences]

    words = [w.lower() for sentence in normalized_sentences for w in
             nltk.tokenize.word_tokenize(sentence)]

    fdist = nltk.FreqDist(words)

    top_n_words = [w[0] for w in fdist.items() 
            if w[0] not in nltk.corpus.stopwords.words('english')][:N]

    scored_sentences = _score_sentences(normalized_sentences, top_n_words)

    # Summarization Approach 1:
    # Filter out nonsignificant sentences by using the average score plus a
    # fraction of the std dev as a filter

    avg = numpy.mean([s[1] for s in scored_sentences])
    std = numpy.std([s[1] for s in scored_sentences])
    mean_scored = [(sent_idx, score) for (sent_idx, score) in scored_sentences
                   if score > avg + 0.5 * std]

    # Summarization Approach 2:
    # Another approach would be to return only the top N ranked sentences

    top_n_scored = sorted(scored_sentences, key=lambda s: s[1])[-TOP_SENTENCES:]
    top_n_scored = sorted(top_n_scored, key=lambda s: s[0])

    # Decorate the post object with summaries

    return dict(top_n_summary=[sentences[idx] for (idx, score) in top_n_scored],
                mean_scored_summary=[sentences[idx] for (idx, score) in mean_scored])


output = summarize(txt)

print '\n\n'

for data in output['top_n_summary']:
	print data

print '\n\nDivider\n\n'

for data in output['mean_scored_summary']:
	print data

 
