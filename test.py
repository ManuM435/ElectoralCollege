import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
from utils.csv_readers import population_reader, electors_reader


# Test with the file named 2024_dataset.csv
dict24 = electors_reader('2024_dataset.csv')
print(dict24)

