import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
from colorama import Style, Fore
from typing import List, Tuple, Dict, Any, Union, Optional
from utils.csv_readers import population_reader, electors_reader
from electors import calculate_electors


# Test with the file named 2024_dataset.csv
read_elecs_24 = electors_reader('2024_dataset.csv')
data_elecs_24 = {
    'AL': 9, 'AK': 3, 'AZ': 11, 'AR': 6, 'CA': 54, 'CO': 10, 'CT': 7,
    'DE': 3, 'FL': 30, 'GA': 16, 'HI': 4, 'ID': 4, 'IL': 19,
    'IN': 11, 'IA': 6, 'KS': 6, 'KY': 8, 'LA': 8, 'ME': 4, 'MD': 10,
    'MA': 11, 'MI': 15, 'MN': 10, 'MS': 6, 'MO': 10, 'MT': 4, 'NE': 5,
    'NV': 6, 'NH': 4, 'NJ': 14, 'NM': 5, 'NY': 28, 'NC': 16, 'ND': 3,
    'OH': 17, 'OK': 7, 'OR': 8, 'PA': 19, 'RI': 4, 'SC': 9, 'SD': 3,
    'TN': 11, 'TX': 40, 'UT': 6, 'VT': 3, 'VA': 13, 'WA': 12, 'WV': 4,
    'WI': 10, 'WY': 3
}

read_pops_24 = population_reader('populations.csv')
data_pops_24 = {
    "AL": 5024279, "AK": 733391, "AZ": 7151502, "AR": 3011524, "CA": 39538223, "CO": 5773714, "CT": 3605944,
    "DE": 989948, "FL": 21538187, "GA": 10711908, "HI": 1455271, "ID": 1839106, "IL": 12812508,
    "IN": 6785528, "IA": 3190369, "KS": 2937880, "KY": 4505836, "LA": 4657757, "ME": 1362359, "MD": 6177224,
    "MA": 7029917, "MI": 10077331, "MN": 5706494, "MS": 2961279, "MO": 6154913, "MT": 1084225, "NE": 1961504,
    "NV": 3104614, "NH": 1377529, "NJ": 9288994, "NM": 2117522, "NY": 20201249, "NC": 10439388, "ND": 779094,
    "OH": 11799448, "OK": 3959353, "OR": 4237256, "PA": 13002700, "RI": 1097379, "SC": 5118425, "SD": 886667,
    "TN": 6910840, "TX": 29145505, "UT": 3271616, "VT": 643077, "VA": 8631393, "WA": 7705281, "WV": 1793716,
    "WI": 5893718, "WY": 576851
}

pops_values_24 = tuple(data_pops_24.values())
print(f"The pop values for 24 are {pops_values_24}")
electors_pred_24 = calculate_electors(states_number=50, populations=pops_values_24)

# Tests
assert read_elecs_24 == data_elecs_24, Style.BRIGHT + Fore.RED + f'Error!\nOur Data was {read_elecs_24} while\nTrue Data is {data_elecs_24}' + Style.RESET_ALL
assert read_pops_24 == data_pops_24, Style.BRIGHT + Fore.RED + f'Error!\nOur Data was {read_pops_24} while\nTrue Data is {data_pops_24}' + Style.RESET_ALL

print(Style.BRIGHT + Fore.GREEN + 'Tests passed!' + Style.RESET_ALL)