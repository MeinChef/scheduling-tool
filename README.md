# scipy_project
### Goal
scheduling_tool.py is a program for dealing with finding an optimal timeslot that fits the availability of a specified amount of people.
### Motivation
We wanted to create a tool that made it easier to find timeslots that fit the majority of a group, for example when planning a holiday, since it can be a bit tedious to check all contraints and limitations by hand.
Now, you could:
- ask every one to enter the dates that fit them in a .csv you make available (mind the structure!)
- and use our tool to plan trips considering several constraints
    - customizable starting date
    - customizable participants: not everone in the database is considered
    - "Necessary to be included in planning": if there is no timeframe, that fits everyone, our program will give the next best one. But some people are necessary for the trip to happen (i.e. because they are hosting or designated drivers), so specify them in this step.
### Structure
Contained in the repo are:
- Files containing functions used in scheduling_tool.py
    - tools.py
    - get_input.py
- Data folder: 
    - Containts premade .csv for trying the tool
[...]

### Functionality
- Input / Optional custom .csv to be loaded (must be in \data folder):
    - Columns: people or names to be used
    - Index: Dates to be considered for scheduling
    - Data: weighting integer (0-2), 0: person X is not available, 1: person X is avaiable, 2: day fits person X best

    Example csv:
    |          | Person 1 | Person 2|
    | -------- | ------- | ------- |
    | 01.01.1970 | 0 | 1 |
    | 02.01.1970 | 1 | 0 |
    | 03.01.1970 | 2 | 2 |

- User adjustments possible:
    - People(.csv columns) to be considered in planning
    - People that must necessarily be available in that timeframe (Function: i.e. hosting)
    - Length of timeframe to be found
    - Optional startdate

- Output: timeframe best fitting for given  constraints, people participating as a
tuple


## Getting started
### Prerequisites
A working python environment with:
- pandas 
- numpy
### Installation
Clone the repo
```bash
git clone ___
```
## Usage 
- add your own csv in data folder if wanted

Execute in working directory:
```bash
python scheduling_tool.py
```
[add usage examples - possible user adjustments
- own csv
- premade csv
- choosing necessary people
- constraint violation vs. timeframe found]
## Authors and Contact

