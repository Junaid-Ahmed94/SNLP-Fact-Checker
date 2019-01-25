# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:20:16 2018
@author: HP
"""

from nltk import ne_chunk, pos_tag, word_tokenize, ne_chunk_sents, sent_tokenize
from nltk.tree import Tree

class ProcessTriplets():
   
    def process_entities(self, txt):
        chunks = self._get_chunks(txt)
        continuous_chunk = []
        for chunk in chunks:
            continuous_chunk.extend(self._extract_entity_names(chunk))
        return continuous_chunk

    def _get_chunks(self, txt):
        chunks = ne_chunk_sents(self._get_pos_tags(txt), binary=True)
        return chunks
    
    def _get_pos_tags(self, txt):
        token_words = self._get_tokens(txt)
        tags = [pos_tag(word) for word in token_words]
        return tags
    
    def _get_sent_tokens(self, txt):
        sentence = sent_tokenize(txt)
        return sentence
    
    def _get_tokens(self, txt):
        token_sent = self._get_sent_tokens(txt)
        tokens = [word_tokenize(sentence) for sentence in token_sent]
        return tokens
    
    def _extract_entity_names(self, t):
        entity_names = []
        if hasattr(t, 'label') and t.label:
            if t.label() == 'NE':
                entity_names.append(' '.join([child[0] for child in t]))
            else:
                for child in t:
                    entity_names.extend(self._extract_entity_names(child))
        return entity_names
