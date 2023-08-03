import re

def clean_date(input):

    """
Turns input such as '2 weeks' or '5 days' into tuple of the form (Amount, 'W' or 'D')
Can also be used to check correct shape of input string

Parameters:
input (str): wanted timeframe expressed in natural language

Returns:
(tuple): (int, 'W') or (int, 'D')
If transformation not possible, return False

"""

    input = input.lower()

    digits = re.findall(r'\b\d+\b', input)
    if len(digits) != 1:
        return False

    if input.endswith(' week') or input.endswith(' weeks') or input.endswith(' w'):
        return int(digits[0]), 'W'
    if input.endswith(' day') or input.endswith(' days') or input.endswith(' d'):
        return int(digits[0]), 'D'
    
    return False

def reformat_date(input):

    """
Turn tuple of the form (Amount, 'W' or 'D') into natural language timeframe (such as '2 weeks' or '5 days')

Parameters:
input (tuple): (int, 'W') or (int, 'D')

Returns:
formatted (str):  timeframe expressed in natural language

"""

    if input[1] == 'W':
        formatted = f'{input[0]} ' + 'week'
    elif input[1] == 'D':
        formatted = f'{input[0]} ' + 'day'
        
    if input[0] > 1:
        formatted = formatted + 's'
    
    return formatted


def valid_persons(data, persons):

    """
Check if specified persons are column headers of data.

Parameters:
persons (list): list of strings (names)
data (pandas DataFrame): contains processed data from .csv

Returns:
(bool)

"""
    if data.columns.isin(persons).any(): return True
    else:
        print('The specified Person(s) do not exist in the database!')
        return False
    
def valid_date(data, date):

    """
Check if specified date is an index of data.

Parameters:
date (np.datetime64)
data (pandas DataFrame): contains processed data from .csv

Returns:
(bool)

"""

    if date in data.index: return True
    else: return False

def valid_file(string):

    """
Check if specified string is of correct shape (ends with .csv).

Parameters:
string (str): filename

Returns:
(bool)

"""

    if not string.endswith('.csv'):
        print("Your file needs to be of the type .csv")
        return False
    else:
        return True