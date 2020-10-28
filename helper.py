"""
helper functions to use
"""
import pandas as pd


def num_nulls(dataframe):
    #return number of null values
    return dataframe.isnull().sum

def date_column(dataframe, column):
    #takes in dataframe and column name
    #converts date column into year, month, day
    dataframe[column] = pd.to_datetime(dataframe[column])
    dataframe['year'] = dataframe[column].year
    dataframe['month'] = dataframe[column].month
    dataframe['day'] = dataframe[column].day
    dataframe.drop(column, axis=1, inplace=True)
    return dataframe