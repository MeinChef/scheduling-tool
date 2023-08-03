import pandas as pd
import numpy as np
import get_input as gi
import tools

def solve(data, necessary, persons, startdate = np.datetime64('2023-08-01'), length = 6, interval = 'D'):
    """
[Beschreibung]

Parameters:
data (pandas DataFrame): contains processed data from .csv
necessary (list): list of names (people who NEED be available)
persons (list): list of names (people who SHOULD be available)
startdate (np.datetime64): custom or preset earliest startdate for the timeframe
length (int) = custom or preset length of timeframe
daterange (str) = custom ('D'/'W') or preset ('D') quantifier for length (Day/ Week)

Returns:
[Output]

"""

    delta = np.timedelta64(length - 1, interval)
    # the -1 because e.g. 07-01 + 6 days = 07-07, was 7 Tage sind, und nicht 6, wie wir eigentlich wollten

        
    data = data[persons]

    df_results = pd.DataFrame(columns = ['date', 'count', 'weight', 'people'])
    df_results['count'] = pd.to_numeric(df_results['count'])
    df_results['weight'] = pd.to_numeric(df_results['weight'])
    
    for i in np.arange(np.datetime64(startdate), np.datetime64(data.index[-1] - delta, 'D'), dtype = 'datetime64[D]'):
        
        counter = 0
        weight = 0
        people = []

        for person in persons:
            if data[person][i :i + delta].product() != 0:
                counter += 1
                people.append(person)
                weight += data[person][i :i + delta].product()
            
         
        if all(item in people for item in necessary) and counter != 0:
            if counter == len(persons):
                # we actually found solutions fitting to the query
                df_results = df_results._append({'date': i, 'count': counter, 'weight': weight, 'people': people}, ignore_index = True)
            
            else:
                # we didn't find solutions for the query, but we're keeping track of all possibilities - and will return the one with the highest value
                df_results = df_results._append({'date': i, 'count': counter, 'weight': weight, 'people': people}, ignore_index = True)

    return df_results.nlargest(3, ['count', 'weight'])
            

        



if __name__ == "__main__":

    data, file = gi.transform_and_load()
    
    print(f"Hello! I am a scheduling tool made to find a timeframe that fits all people specified in the following.\n\rMy search is based on {file}. Let us begin!\n\r")
    
    persons, necessary, time, startdate = gi.get_constraints(data)

    solution = solve(data,  necessary, persons = persons, length = time[0], interval = time[1])
    print()


    while time[0] >= 0:
        if not solution.empty:
            if len(solution['people'].iloc[0]) < len(persons):
                print("I wasn't able to find a solution tht includes everyone. Here is the best timeframe I was able to find: ")
            if len(solution['people'].iloc[0]) > 1:
                print(f"From the {solution['date'].iloc[0]} on, there are {solution['count'].iloc[0]} people free for {tools.reformat_date(time)}.\n\rThese people are: {solution['people'].iloc[0]}\n\r")
                print(f"Here\'s also up to 3 best fitting solutions:")
                print(solution[['date', 'count', 'people']])
            else:
                print(f"From the {solution['date'].iloc[0]} on, there is {solution['count'].iloc[0]} person free for {tools.reformat_date(time)}.\n\rThis person is: {solution['people'].iloc[0]}\n\r")
                print(f"Here\'s also up to 3 best fitting solutions:")
                print(solution[['date', 'count', 'people']])
            break       

        else:
            print("There is no solution with your constraints.\n\r")
            re_run = input("Should I re-run the search with a smaller time window (Enter to skip)? ")
            if re_run:
                time =  list(time)
                time[0] = time[0]-1
                print(f"Trying with {tools.reformat_date(time)}")
                solution = solve(data, necessary, persons, length = time[0], interval = time[1])

            else: break

    ###############TODO#######################
    

    # comments

    
    
    # From grading pdf:
        # docstrings for all functions
        # There are instructions for the intended usage of the project
    
    # maybe:

        # include where constraint conflict is in "There is no solution with your constraints." - difficult, rejected
        

    # done
        # ! get different output, if solutions can't give a definite solution
        # ! fix output, that it outputs "6 Days" instead of (6, 'D')
        # ! fix default value of startdate not working
        #! fix bugs in get_input.py (while loop where date gets asked for (wrong format))
        # print persons that are avaliable to choose from
        # rename 'availabiltiy' column to something meaningful
        # solver does not necessarily inlcude 'Who should be the one I need to include in the planning'
        # solver skips necessary if typed wrong 1 time
        # show available timeframe
        # rewrite: Who should be the one I need to include in the planning?
        # solver must include specified persons (as in A and B must be there, C,D,E not necessarily) [DONE]
        # solver does not necessarily inlcude all [DoNE]
        # load own csv?
        #cursed !Do you want to input user data (Enter to skip)? 
        # timeframe input allow currencly for '8 weekyetts' or '5 dayyoinks'
        # load own csv: proper pandas convert check 
        # you can specify needed > total - bad!
        # refine how mny ppl do you want to add for ambiguity
        # give mulitple possible time frames - per default 3
        # sort dataframe by weight
        # weight values and implement function to actually work with them
        # Maybe: option of giving shorter timeframe from startdate






    ##########################################
