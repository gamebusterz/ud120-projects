#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    error = list((net_worths - predictions)**2)                 #Calculating the squared errors
    cleaned_data = zip(ages,net_worths, error)                  #zip the three lists into a single list of three-tuples
    cleaned_data = sorted(cleaned_data, key= lambda x: x[2])
    length = int(len(cleaned_data)*0.9)
    cleaned_data = cleaned_data[0:length]
    return cleaned_data
