# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 22:05:32 2019

@author: Junaid
"""

import wikipediaapi

class Wiki:
    
    def __init__(self):
        self.wiki = wikipediaapi.Wikipedia('en')
    
    def get_wiki_data(self, search_string):
        wiki_obj = self.wiki.page(search_string)
        ret_text_dict = {}
        if(self._check_exist(wiki_obj)):
            ret_text_dict[search_string] = wiki_obj.text
        else:
            ret_text_dict = self._get_suggestions(wiki_obj)
        
        return ret_text_dict
    
    def _get_suggestions(self, wiki_obj):
        '''
            This helps to get top 2 suggestions
        '''
        suggestions_list = list(wiki_obj.links.keys())
        text_dict = {}
        for suggestion in suggestions_list:
            if(suggestion.find(wiki_obj.title)>-1):
                new_obj = self.wiki.page(suggestion)
                text_dict[suggestion] = new_obj.text
        return text_dict
    
    
    def _check_exist(self, wiki_obj):
        if(len(wiki_obj.text) <= 0):
            return False
        return True
        
####################

#fetcher = Wiki()
#text = fetcher.get_wiki_data("Jack Faust")
