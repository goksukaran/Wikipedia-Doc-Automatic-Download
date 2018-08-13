'''
Created on 6 Aug 2018

@author: goksukara
'''
import pandas as pd
from PreprocessingClass import PreprocessingFunctions,Cleanupper 

for chunck_df in pd.read_csv('corpus.csv',dtype={'Name':'str',"Text":"str"}, chunksize=5,header=0):
    dataprocesing=PreprocessingFunctions(chunck_df)
    #dataprocesing.cleanup(Cleanupper())
    print(dataprocesing.processed_data)
    dataprocesing.save()
    