# SNLP Fact Checker

## Team Members
  1. Junaid Ahmed - 6852164
  2. Salman Khalid - 6844233

### Introduction:
The basic idea of this project is to check a given fact against Wikipedia. 

### Installation:
Install following tools to run this project,
  <br />1- wikipedia-api
  <br />2- NLTK (punkt, words, max_ne_chunker, averaged_preceptron_tagger)
  <br />3- pandas

### Run:
To run this project, Simply execute Fact_Checker.py file. And pass the given **test.tsv** file. (Do update the Test file path in code)

### Procedure:
1. NER on Fetched Data
  <br />After reading data from file, do tokenization on the fetch data using NLTK's word_tokenizer then perform pos tagging. Using
  <bold>ne_chunk_sents<bold/> we extract continuous Name entities.

2. Fetching data from Wikipedia
  <br />We fetch wiki pages against all the fetched NEs, and if these exist a NE for which no wiki page was found, we fetch all the suggestions
  against this NE.

3. Check for NE occurences
  <br />Lets assume a sentence from which we get 3 NEs (A, B, C), first we check occurence of NE-'A' in the other NEs wiki pages, then we repeat
  the same check for the other NE wiki pages, i.e, occurence of NE-'A' in B and C wiki pages and so on.
  <br /><br />We consider multiple occurences of NE in a single wiki pages as one, so total occurences means total number of pages where we found this
  NE.

4. Calculate Probability
<br />**total_occurances/(total_pages+0.000000001)** using this equation, if we get probability higher or equal to 0.5, this fact is correct.

### Examples:
Following are some True and False facts other than test/train sets.
#### True Facts:
Arthur Conan Doyle's birth place is Edinburgh, United Kingdom.
<br />Asif Ali Zardari was the President of Pakistan.
<br />Italy is located in the middle of the Mediterranean Sea.
<br />Johnny Depp played the title character in Tim Burton's film Edward Scissorhands.
<br />Sundar Pichai is the CEO of Google.
#### False Facts:
Winston Churchill suffer from narcolepsy.
<br />Justin Trudeau taught snowboarding.
<br />Elvis Presley was a natural blond.
<br />Mark Wahlberg was a rapper.
<br />Leighton Meester was born in prison.
