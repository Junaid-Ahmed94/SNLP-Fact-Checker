# SNLP Fact Checker

Introduction:
The basic idea of this project is to check a given fact against wikipedia. 

Installation:
-install following tools to run this project,
  1- wikipediaapi
  2- NLTK 
  3- pandas
  
Run:
To run this project, Simply execute Fact_Checker.py file.

Procedure:
1. NER on Fetch Data
  After reading data from file, perform tokenization on the fetch data using NLTK's word_tokenizer then perform pos tagging. Using ne_chunk_sents we extract continuous Name Ententies.
2. Fetching data from wikipedia
  We fetch wiki pages against all the fetched NEs, and if these exist a NE for which no wiki page was found, we fetch all the suggestions against this NE.
3. Check for NE Occurances
  Lets assume a sentence from which we get 3 NEs (A, B, C), first we check occurance of NE-'A' in the other NEs wiki pages, then we repeat the same check for the other NE wiki pages, i.e, occurance of NE-'A' in B and C wiki pages and so on. 
  
  We consider multiple occurances of NE in a single wiki pages as one, so total occurances means total number of pages where we found this NE.
  
4. Calculate Probability
  " total_occurances/(total_pages+0.000000001) " using this equation, if we get probability higher or equal to 0.5, this fact is correct.
