import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
from colorama import Style, Fore
from typing import List, Tuple, Dict, Any, Union, Optional
from utils.csv_readers import population_reader, electors_reader


# Test with the file named 2024_dataset.csv
dict24 = electors_reader('2024_dataset.csv')
true_data24 = {'AL': 9, 'AK': 3, 'AZ': 11, 'AR': 6, 'CA': 54, 'CO': 10, 'CT': 7, 'DE': 3, 'DC': 3, 'FL': 30, 'GA': 16, 'HI': 4, 'ID': 4, 'IL': 19, 'IN': 11, 'IA': 6, 'KS': 6, 'KY': 8, 'LA': 8, 'ME': 4, 'MD': 10, 'MA': 11, 'MI': 15, 'MN': 10, 'MS': 6, 'MO': 10, 'MT': 4, 'NE': 5, 'NV': 6, 'NH': 4, 'NJ': 14, 'NM': 5, 'NY': 28, 'NC': 16, 'ND': 3, 'OH': 17, 'OK': 7, 'OR': 8, 'PA': 19, 'RI': 4, 'SC': 9, 'SD': 3, 'TN': 11, 'TX': 40, 'UT': 6, 'VT': 3, 'VA': 13, 'WA': 12, 'WV': 4, 'WI': 10, 'WY': 3}

assert dict24 == true_data24, Style.BRIGHT + Fore.RED + f'Error!\nOur Data was {dict24} while\nTrue Data is {true_data24}' + Style.RESET_ALL

print(Style.BRIGHT + Fore.GREEN + 'Tests passed!' + Style.RESET_ALL)