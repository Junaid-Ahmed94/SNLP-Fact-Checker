# -*- coding: utf-8 -*-

###########################################################
# This is the Main file for controlling all the operations
###########################################################

from FileUtils import FileOperations
from PreProcessing import ProcessTriplets
from WikipediaFetcher import Wiki


def has_match(page, title):
    if(page.find(title) > -1):
        return True
    return False

def check_match(page_dict, title, text_string):
    for page in list(page_dict.keys()):
        if(page.find(title) > -1):
            if(has_match(page_dict[page], text_string)):
                return True
    return False

def check_fact(extracts):
    total_pages = 0
    total_occurances = 0 
    
    wikifetcher = Wiki()
    
    for extract in extracts:
        page_dict = wikifetcher.get_wiki_data(extract)
        for ext in extracts:
            if(ext != extract):
                if(check_match(page_dict, extract, ext)):
                    total_occurances += 1
                total_pages += 1
    return total_occurances/(total_pages+0.000000001)



#########################################
# This Part Controls the Train.tsv file
#########################################

#file_path = r"C:\Users\HP\Desktop\University Paderborn\SNLP\miniproject\train.tsv"
#df = ReadOperations.read_file(file_path)
#
#triplet_processer = ProcessTriplets()
#
#fact_ids = df['FactID']
#facts = df['Fact_Statement']
#fact_real = df['True/False']
#
#count_same = 0
#for idx, fact in enumerate(facts):
#    extracts = triplet_processer.process_entities(fact)
#    probability = check_fact(extracts)
#    return_prob = 0
#    if(probability >= 0.5):
#        return_prob = 1
#    if (fact_real[idx] == return_prob):
#        count_same += 1
#    print(str(return_prob) + "  " + str(fact_real[idx]))
#
#print ("\n\nThe Total Count for True Fact is: \n\n " + str(count_same))

#########################################
# This Part Controls the Test.tsv file
#########################################

file_path = r"C:\Users\HP\Desktop\University Paderborn\SNLP\miniproject\test.tsv"
df = FileOperations.read_file(file_path)

triplet_processer = ProcessTriplets()

fact_dict = {}

for index, fact in df.iterrows():
    #print(row['FactID'])
    extracts = triplet_processer.process_entities(fact['Fact_Statement'])
    probability = check_fact(extracts)
    return_prob = 0.0
    if(probability >= 0.5):
        return_prob = 1.0
    fact_dict[fact['FactID']] = return_prob

FileOperations.write_results(fact_dict)
