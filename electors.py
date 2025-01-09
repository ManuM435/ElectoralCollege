import numpy as np
import pandas as pd
from utils.csv_readers import population_reader, electors_reader
import math
from colorama import Style, Fore
from typing import List, Tuple, Dict, Any, Union, Optional

def allocate_house_seats(states_number: int, populations: Tuple[int]) -> List[int]:
    """
    Allocate the 435 House seats among the states based on their populations using the method of equal proportions.

    Args:
        states_number (int): The number of states.
        populations (Tuple[int]): A tuple of state populations.

    Returns:
        List[int]: A list of House seats allocated to each state.
    """
    # Start with 1 seat for each state
    seats = [1] * states_number

    # Priority values for each state
    priority_values = [pop / math.sqrt(seats[i] * (seats[i] + 1)) for i, pop in enumerate(populations)]

    # Assign the remaining 435 - states_number seats
    total_seats = 435
    remaining_seats = total_seats - states_number

    for _ in range(remaining_seats):
        # Find the state with the highest priority value
        max_index = priority_values.index(max(priority_values))

        # Assign one more seat to that state
        seats[max_index] += 1

        # Recalculate the priority value for that state
        priority_values[max_index] = populations[max_index] / math.sqrt(seats[max_index] * (seats[max_index] + 1))

    return seats

def calculate_electors(states_number: int, populations: Tuple[int]) -> List[int]:
    """ Calculates the electors (House Reps + Senators) for each state based on the population.

    Args:
        states_number (int): The number of states in the Union
        populations (Tuple[int]): A tuple of state populations

    Returns:
        List[int]: A list of electors allocated to each state, ordered by the same index as the populations 
        such that the ith element of the populations tuple corresponds to the ith element of the returned list
    """

# Example usage:
states_population = (1000000, 5000000, 10000000, 2000000)  # Example populations for 4 states
states_number = len(states_population)
house_seats = allocate_house_seats(states_number, states_population)
print(house_seats)  # Output: House seat allocations
