#!/usr/bin/python
from __future__ import division
"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# size of enron_data
print(len(enron_data))

# number of features
print(len(enron_data.values()[0]))

# number of poi
count = 0
for i in enron_data.values():
    if i['poi'] == True:
        count += 1
print(count)

# Total value of stock belonging to James Prentice
print(enron_data['PRENTICE JAMES']['total_stock_value'])

#Emails from Wesley Colwell to poi
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

# Value of Stock options exercised by Skilling
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

# How many 'NaN' for total payments and % of total
count = 0
for i in enron_data.values():
    if i['total_payments'] == 'NaN':
        count += 1
print(count)
print(count/len(enron_data)*100)

# How many POIs have total payments as 'NaN'
count = 0
for i in enron_data.values():
    if i['total_payments'] == 'NaN' and i['poi'] == True:
        count += 1
print(count)
print(count/len(enron_data)*100)

# for k in enron_data:
#     print enron_data[k]['long_term_incentive']
