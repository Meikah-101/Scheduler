import pandas as pd
import numpy as np 
import random
import csv

file = pd.read_csv('') #enter name of cvs file of schedule into ''
new_schedule = pd.DataFrame(columns=['dates', 'names'])
date_column = file['dates']
names_column = file['names'] 

names_column_list = list(names_column)
names_column_str = ','.join(map(str,names_column_list))
replace_nan = names_column_str.replace('nan,', '') #removes nan values from list of names 
names_column_nowhite = replace_nan.strip() 
names_column_split = names_column_nowhite.split(",")


with open('') as f: #enter name of text file with names inside ''
    namesfile = f.read()
names_nowhite = namesfile.replace(" ", "")
names_not_found = names_nowhite.split(",")
new_names_set = set(names_not_found).difference(names_column_split) # finds the names that are not found in the original schedule
new_names_list = list(new_names_set)
new_names_random = random.sample(new_names_list, len(new_names_list))
name_counter = 0


for index, row in file.iterrows():
    if pd.isna(row.iloc[1]):
        date = row.iloc[0]
        name = new_names_random[name_counter]
        name_counter = name_counter +1 # iterates through new_names_random 
        
        data = {'dates': [date], 'names': [name]}
        new_entry = pd.DataFrame(data=data) #creates new pandas dataframe
        new_schedule = new_schedule.append(new_entry)
        

    else:
        new_schedule = new_schedule.append(row) #adds data from orginal csv schedule if nan values are absent 
        

new_schedule.to_csv('new_sch.csv' , index = False , columns = ['dates', 'names']) #creates new csv with the new data 
