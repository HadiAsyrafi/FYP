# -*- coding: utf-8 -*-
import nltk

class highlighter(object):

	def __init__ (self, txt = 'None'):
		self.txt = txt
		

	def highlight(self):

		sentences = nltk.tokenize.sent_tokenize(self.txt)
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
		self.keywords = []
		for sentence_idx in range(len(sentences)):
			s = sentences[sentence_idx]
			for (term, _) in entity_interactions[sentence_idx]:
			    self.keywords.append(term)
