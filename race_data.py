import pandas as pd
import numpy as np

#####  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  #####
## !!! My csv file is not named the same as yours !!!

traffic_data_to_load = "Traffic_Violations (1).csv"

traffic_data = pd.read_csv(traffic_data_to_load)



## Choose only the rows that were tiketed for cellphone use and 
## contributed to an accident.

cell_phone_accidents = traffic_data[(traffic_data['Charge'] == '21-1124.2(d2)') & (traffic_data['Contributed To Accident'] == 'Yes')]
cell_phone_data = traffic_data[(traffic_data['Charge'] == '21-1124.2(d2)')]

## Overview of which gender is cited for cell phone use
## can easily addapt to look at race
male_violations = len(cell_phone_data[(cell_phone_data['Gender'] == 'M')])
female_violations = len(cell_phone_data[(cell_phone_data['Gender'] == 'F')])
gender_summary_df = pd.DataFrame({'Gender': ['Male', 'Female'], 'Violations': [male_violations, female_violations], 
                          'Percentage of Total':[round(male_violations/len(cell_phone_data)*100,3), round(female_violations/len(cell_phone_data)*100,3)]})


## Drop needless columns
cleaned_cell_phone = cell_phone_accidents.drop(columns = ['VehicleType', 'Fatal', 'HAZMAT', 'Commercial Vehicle', 'Work Zone', 'Alcohol', 'Driver City', 'Agency', 'Driver State', 'State', 'Commercial License', 'Year', 'Make', 'Accident', 'Article', 'Belts', 'Arrest Type', 'DL State', 'Color', 'Model', 'Description'])


## Count the number of violations per race ##
race_asian = len(cleaned_cell_phone[(cleaned_cell_phone['Race'] == 'ASIAN')])
race_native_am = len(cleaned_cell_phone[(cleaned_cell_phone['Race'] == 'NATIVE AMERICAN')])
race_white = len(cleaned_cell_phone[(cleaned_cell_phone['Race'] == 'WHITE')])
race_black = len(cleaned_cell_phone[(cleaned_cell_phone['Race'] == 'BLACK')])
race_hispanic = len(cleaned_cell_phone[(cleaned_cell_phone['Race'] == 'HISPANIC')])
race_other = len(cleaned_cell_phone[(cleaned_cell_phone['Race'] == 'OTHER')])

## Create DataFrame that compares the 
## percentage of violations with the percentage of the population.
## This shows which groups may be over/under ticketed.
race_summary_df = pd.DataFrame({'Race': ['Asian', 'Native American', 'White', 'Black', 'Hispanic', 'Other'], 
                        'Violations': [race_asian, race_native_am, race_white, race_black, race_hispanic, race_other], 
                       'Percent of Violations': [round(race_asian/102*100,3), round(race_native_am/102*100,3), round(race_white/102*100,3), round(race_black/102*100,3), round(race_hispanic/102*100,3), round(race_other/102*100,3)  ],
                       'Percent of Population': [4.8, 0.9, 72.4, 12.6, 16.3, 6.2]})
## There are some number plugged un there instead of programatically inserted.
## This shoud change.



## The Dataframes to analyze:                    

#race_summary_df
#gender_summary_df