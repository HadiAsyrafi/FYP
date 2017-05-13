# -*- coding: utf-8 -*-
import json
import nltk
import numpy

txt = '''The winter of my seventh grade year, my alcoholic mother entered a psychiatric unit for an attempted suicide. Mom survived, but I would never forget visiting her at the ward or the complete confusion I felt about her attempt to end her life. Today I realize that this experience greatly influenced my professional ambition as well as my personal identity. While early on my professional ambitions were aimed towards the mental health field, later experiences have redirected me towards a career in academia.

I come from a small, economically depressed town in Northern Wisconson. Many people in this former mining town do not graduate high school and for them college is an idealistic concept, not a reality. Neither of my parents attended college. Feelings of being trapped in a stagnant environment permeated my mind, and yet I knew I had to graduate high school; I had to get out. Although most of my friends and family did not understand my ambitions, I knew I wanted to make a difference and used their doubt as motivation to press through. Four days after I graduated high school, I joined the U.S. Army.

The 4 years I spent in the Army cultivated a deep-seated passion for serving society. While in the Army, I had the great honor to serve with several men and women who, like me, fought to make a difference in the world. During my tour of duty, I witnessed several shipmates suffer from various mental aliments. Driven by a commitment to serve and a desire to understand the foundations of psychological illness, I decided to return to school to study psychology.

In order to pay for school and continue being active in the community, I enlisted in the Texas Army National Guard as a Medic. Due to the increased deployment schedule and demands placed on all branches of the military after September 11, my attendance in school has necessarily come second to my commitment to the military. There are various semesters where, due to this demand, I attended school less than full time. Despite taking a long time and the difficulty in carving separate time for school with such occupational requirements, I remained persistent aiming towards attending school as my schedule would allow. My military commitment ends this July and will no longer complicate my academic pursuits.

In college, as I became more politically engaged, my interest began to gravitate more towards political science. The interest in serving and understanding people has never changed, yet I realized I could make a greater difference doing something for which I have a deeper passion, political science. Pursuing dual degrees in both Psychology and Political Science, I was provided an opportunity to complete a thesis in Psychology with Dr. Sheryl Carol a Professor in Social Psychology at the University of Texas (UT) This fall I will complete an additional thesis as a McNair Scholar with Dr. Ken Chambers, Associate Professor in Latin American studies in the UT Political Science Department.

As an undergraduate, I was privileged to gain extensive research experience working in a research lab with Dr. Carol. During the three years I worked in her lab, I aided in designing a study, writing an Institutional Review Board (IRB) application, running participants through both pilot and regular studies, coding data, and analyzing said data, with these experiences culminating in my honors thesis. This thesis, entitled Self-Esteem and Need-to-Belong as predictors of implicit stereotypic explanatory bias, focuses on the relationship between levels (high and low) of self-esteem and an individual’s need to belong in a group, and how they predict whether an individual will tend to explain stereotype-inconsistent behavior. Participating in such a large study from start to finish has validated my interest in academic research as a profession.

This fall I will embark on writing an additional honors thesis in political science. While the precise topic of my thesis is undecided, I am particularly interested in Mexico and its development towards a more democratic government. Minoring in Spanish, I have read various pieces of literature from Mexico and have come to respect Mexico and Latin American culture and society. I look forward to conducting this research as it will have a more qualitative tilt than my thesis in psychology, therefore granting an additional understanding of research methodology.

My present decision to switch from social psychology to political science is further related to a study abroad course sponsored by the European Union with Dr. Samuel Mitchell, an Associate Professor in the Political Science Department at UT. Professor Mitchell obtained a grant to take a class of students to Belgium in order to study the EU. This course revealed a direct correlation between what I had studied in the classroom with the real world. After spending several weeks studying the EU, its history and present movement towards integration, the class flew to Brussels where we met with officials and proceeded to learn firsthand how the EU functioned.

My interest in attending the University of Rochester in particular, relates to my first semester at OU and the opportunity to take an introductory course in statistics with the now retired Dr. Larry Miller. Through the combination of a genuine appreciation and knack for statistics and with his encouragement, I proceeded to take his advanced statistics class as well as the first graduate level statistics course at OU. I continued my statistical training by completing the second graduate statistics course on model comparisons with Dr. Roger Johnson, a Professor in the Psychology Department. The model comparison course was not only the most challenging course I have taken as an undergraduate, but the most important. As the sole undergraduate in the course and only college algebra under my belt, I felt quite intimidated. Yet, the rigors of the class compelled me to expand my thinking and learn to overcome any insecurities and deficits in my education. The effort paid off as I earned not only an ‘A’ in the course, but also won the T.O.P.S. (Top Outstanding Psychology Student) award in statistics. This award is given to the top undergraduate student with a demonstrated history of success in statistics.

My statistical training in psychology orientates me toward a more quantitative graduate experience. Due to the University of Rochester’s reputation for an extensive use of statistics in political science research, I would make a good addition to your fall class. While attending the University of Rochester, I would like to study international relations or comparative politics while in graduate school. I find the research of Dr.’s Hein Goemans and Gretchen Helmke intriguing and would like the opportunity to learn more about it through the Graduate Visitation program.

Participation in the University of Rochester’s Graduate School Visitation Program would allow me to learn more about the Department of Political Science to further see if my interests align with those in the department. Additionally, my attendance would allow the Political Science department to make a more accurate determination on how well I would fit in to the program than from solely my graduate school application. Attending the University of Rochester with its focus on quantitative training, would not only allow me to utilize the skills and knowledge I gained as an undergraduate, but also would expand this foundation to better prepare me to conduct research in a manner I find fascinating.

From attending S.E.R.E. (Survival/POW training) in the military and making it through a model comparisons course as an undergraduate, I have rarely shied away from a challenge. I thrive on difficult tasks as I enjoy systematically developing solutions to problems. Attending the University of Rochester would more than likely prove a challenge, but there is no doubt in my mind that I would not only succeed but enable me to offer a unique set of experiences to fellow members of the incoming graduate class. '''

'''#print txt.split(".")

sentences = nltk.tokenize.sent_tokenize(txt)
#print sentences

tokens = [nltk.tokenize.word_tokenize(s) for s in sentences]
#print tokens

pos_tagged_tokens = [nltk.pos_tag(t) for t in tokens]
#print pos_tagged_tokens

#for chunk in nltk.ne_chunk_sents(pos_tagged_tokens, binary=True):
    #print(chunk)'''


N = 130  # Number of words to consider
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

 
