import numpy as np
import pandas as pd

def population_reader(csv_file):
    ''' Given a CSV file with 3 columns separated as follows:
        State Name: str,State Abbreviation: str,Population: int
        This function will return a dictionary with the state abbreviation as the key and the population as the value
    '''
    population = pd.read_csv(csv_file)
    population_dict = dict(zip(population['State Abbreviation'],population['Population']))
    return population_dict

def electors_reader(csv_file):
    ''' Given a CSV file with 3 columns separated as follows:
        State Name: str,State Abbreviation: str,Electors: int
        This function will return a dictionary with the state abbreviation as the key and the electors as the value
    '''
    electors = pd.read_csv(csv_file)
    electors_dict = dict(zip(electors['State Abbreviation'],electors['Electors']))
    return electors_dict