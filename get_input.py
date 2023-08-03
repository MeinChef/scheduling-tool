import tools 
import numpy as np
import pandas as pd

# basically a function for getting the inputs
# make sure the input is in the correct format

#################################################
# one where the user specifies an "after" date (optional) - done
# one where the user specifies a length of the vacation (13 days, etc) (maybe import the check here as well) - done
#################################################


def load_data(filename):

    """
Loads csv file with name 'filename' into a pandas dataframe.

Data is loaded with consideration to setting index to dates, 
filling empty fields with zeroes and turning all numbers into 
integers.

Parameters:
filename (str): ideally folder/name.csv

Returns:
data (pandas DataFrame): contains processed data from .csv
"""

    data = pd.read_csv(filename, parse_dates = True, index_col = 0)
    data = data.fillna(value = 0)
    data = data.apply(pd.to_numeric, downcast = 'integer')
    return data



def transform_and_load():

    """
Uses load_data(filename) to load a .csv from user input.

Ask whether user wants to use their own .csv or premade.
Asks for filename.
Add path to user input filename, check for valid filename with tools.valid_file
and load data. (Ask for new input when input doesn't work)
Alternatively loads data/vacations.csv.

Parameters:

Returns:
data (pandas DataFrame): contains processed data from .csv
file (str): processed filename as string

"""

    skip = input('Do you want to use a custom .csv (Enter to skip)? ')
    if skip:
        check = False
        while not check:
            file = input("What file do you want to load? ")
            file = 'data/' + file 
            if tools.valid_file(file):
                try:
                    data = load_data(file)
                    return data, file
                except:
                    print("Your file must be a .csv in the data folder of this program")
                    continue

    else:
        file = 'data/vacations_w.csv'
        return load_data(file), file
    

def get_travel_buddies(data):

    print(f"\n\rTravel buddies are:{data.columns.values.tolist()}\n\r")

    check = False
    necessary_num = 0

    # get the number of persons the user wants to add
    while not check:
        length = input('How many Travel Buddies do you want to add to go on vacation? ')
        
        try:
            length = int(length)
        except: 
            print('That\'s not a number, try again!')
            continue
        check = True
    check = False
    while not check:
        necessary_num = input('How many people of those need be present? ')
        
        try:
            necessary_num = int(necessary_num)
            if necessary_num >= length:
                print('That\'s more people than the ones that are planned! Please enter a number smaller than total.')
                continue
        except: 
            print('That\'s not a number, try again!')
            continue
        check = True
    print()

    people = []
    necessary = []
    i = 0
    print('Please add names one after the other:')
    while i < length:
        if i < necessary_num:
            person = input('Who is necessary in the planning ? ')
        else:
            person = input('Who else should be added, who doesn\'t need to be there? ') 
        if tools.valid_persons(data, [person]):
            if person not in people:
                people.append(person)
                if i < necessary_num: necessary.append(person)
                i +=1
            else:
                print('You already named that person!')
    print()

    return necessary, people


def get_timeframe(data):
    print(f"The total timeframe available is: {data.index[0]} to {data.index[-1]}")
    check = False
    while not check:
        daterange = input('For how long should the people be available (Enter to use default (6 days))? ')
        if not daterange:
            daterange = (6, 'D')
            break
        
        if tools.clean_date(daterange):
            daterange = tools.clean_date(daterange)
            check = True
        else:
            print('That\'s not a valid input, try something of the format [int, Day/Week]')
    print()
    
    return daterange


def get_startdate(data):

    check = False
    while not check:
        startdate = input('What is the starting date I should start searching from (Enter to use default)? ')
        if not startdate: 
            startdate = data.index[0]
            break
        try:
            startdate = np.datetime64(startdate)
        except ValueError:
            print('The date should be in the ISO8601 (YYYY-MM-DD) format!')
            continue
        if tools.valid_date(data, startdate):
            check = True
        else:
            print('You specified a date outside of the date-range in the data!')
    print()

    return startdate


def get_constraints(data):
    
    """
Reads user input for constraints.

Possible Options:
Choose whether user wants to pick their own constraints.
If yes:
- Ask for amount of people that should be available 
- Ask for amount of people that NEED be available 
- Ask for length of timeframe to be found
- Ask for custom start date (optional)
- Check all of the above for valid type
If skipped:
- Use presets for testing purposes
(First person from DF need be available, 
All others should be available,
When using default .csv remove 'Alberich',
Timeframe should last 6 days)

Parameters:
data (pandas DataFrame): contains processed data from .csv

Returns:
people (list): list of people that should be available
necessary (list): list of people that MUST be available
daterange (tuple): amount of weeks/days the timeframe should last
startdate (np.datetime64): chosen earliest date of the timeframe

"""


    skip = input('Do you want to specify custom persons and times? (Enter to use defaults) ')
    
    if skip:

        necessary, people = get_travel_buddies(data)

        daterange = get_timeframe(data)

        startdate = get_startdate(data)
                

    else: 
        # default values, if we don't want to actually excecute the programe:
        people = data.columns.values.tolist()
        try: 
            people.remove('Alberich') # because this person is actually never there.
        except: print('Warning: You\'re not working with the default dataframe!')

        necessary = [data.columns[0]]
        daterange = (6, 'D')
        startdate = data.index[0]

    return people, necessary, daterange, startdate