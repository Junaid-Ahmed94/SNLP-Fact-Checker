# -*- coding: utf-8 -*-

######################################
# Reads file and do all the operations
# necessary to process the fact check
######################################
import pandas as pd

class FileOperations():
    
    @staticmethod
    def read_file(file_path):
        file_data = pd.read_csv(file_path, sep="\t", encoding='latin-1')
        return file_data
    
    @staticmethod
    def write_results(facts):
        fact_uri = "<http://swc2017.aksw.org/task2/dataset/"
        property_uri = "<http://swc2017.aksw.org/hasTruthValue>"
        value_type = "^^<http://www.w3.org/2001/XMLSchema#double> ."
        
        with open('Boolean.ttl', 'a') as results:
            for fact_id in list(facts.keys()):
                results.write(fact_uri+ str(fact_id)+"> "+property_uri+" \""+str(facts[fact_id])+"\""+value_type)
                results.write("\n")
            