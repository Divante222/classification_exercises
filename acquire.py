import pandas as pd 
import env
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

import os



# Make a function named get_titanic_data that returns the titanic data from the codeup 
# data science database as a pandas data frame. Obtain your data from the Codeup Data Science Database.    
    
    
def new_titanic_data(SQL_query, url):
    '''
    this function will:
    - take in a SQL_query 
    -create a connection url to mySQL
    -return a df of the given query from the titanic_db
    
    '''
    url= f'mysql+pymysql://{env.username}:{env.password}@{env.hostname}/titanic_db'
    return pd.read_sql(SQL_query,url)    
    
    
    
    
def get_titanic_data(filename = "titanic.csv"):
    '''
    this function will:
    -check local directory for csv file
        return if exists
    if csv doesn't exist
    if csv doesnt exist:
        - create a df of the SQL_query
        write df to csv
    output titanic df
    
    '''

    SQL_query = '''select * from passengers'''
    filename = "titanic.csv"
    directory = '/Users/divante/codeup-data-science/classification_exercises/'
    url= f'mysql+pymysql://{env.username}:{env.password}@{env.hostname}/titanic_db'

    if os.path.exists(directory + filename):
        df = pd.read_csv(filename)
        return df
    else:
        df= new_titanic_data(SQL_query, url)
        df.to_csv(filename)
        return df
    
    




# Make a function named get_iris_data that returns the data from the iris_db on the 
# codeup data science database as a pandas data frame. The returned data frame should 
# include the actual name of the species in addition to the species_ids. 
# Obtain your data from the Codeup Data Science Database.



    
def new_iris_data(SQL_query, url):
    '''
    this function will:
    - take in a SQL_query 
    -create a connection url to mySQL
    -return a df of the given query from the iris_db
    
    '''
    
    url= f'mysql+pymysql://{env.username}:{env.password}@{env.hostname}/iris_db'
    return pd.read_sql(SQL_query,url)    
        

    
def get_iris_data(filename = "iris.csv"):

    '''
    this function will:
    -check local directory for csv file
        return if exists
    if csv doesn't exist
    if csv doesnt exist:
        - create a df of the SQL_query
        write df to csv
    output iris_db df
    
    '''
    SQL_query = '''select * from measurements
    join species using(species_id);
    ;'''    
    url= f'mysql+pymysql://{env.username}:{env.password}@{env.hostname}/iris_db'
    filename = "iris_db.csv"

    directory = '/Users/divante/codeup-data-science/classification_exercises/'
    if os.path.exists(directory + filename):
        df = pd.read_csv(filename)
        return df
    else:
        df = new_iris_data(SQL_query, url)
        df.to_csv(filename)
        return df
    




# Make a function named get_telco_data that returns the data from the telco_churn database in SQL. 
# In your SQL, be sure to join contract_types, internet_service_types, payment_types tables with 
# the customers table, so that the resulting dataframe contains all the contract, payment, 
# and internet service options. Obtain your data from the Codeup Data Science Database.


def new_telco_data(SQL_query, url):
    '''
    this function will:
    - take in a SQL_query 
    -create a connection url to mySQL
    -return a df of the given query from the telco_churn
    
    '''
    url= f'mysql+pymysql://{env.username}:{env.password}@{env.hostname}/telco_churn'
    return pd.read_sql(SQL_query,url)    
        

    
def get_telco_data(filename = "telco_churn.csv"):
    '''
    this function will:
    -check local directory for csv file
        return if exists
    if csv doesn't exist
    if csv doesnt exist:
        - create a df of the SQL_query
        write df to csv
    output telco_churn df
    
    '''
    SQL_query = '''
    select *
    from customers
    join contract_types using(contract_type_id)
    join internet_service_types using(internet_service_type_id)
    join payment_types using(payment_type_id)
    ;
    '''    
    directory = '/Users/divante/codeup-data-science/classification_exercises/'
    filename = 'telco_churn.csv'
    url= f'mysql+pymysql://{env.username}:{env.password}@{env.hostname}/telco_churn'
    if os.path.exists(directory + filename):
        df = pd.read_csv(filename)
        return df
    else:
        df = new_telco_data(SQL_query, url)
        df.to_csv(filename)
        return df
    



# from pydataset import data


# # In a jupyter notebook, classification_exercises.ipynb, use a python module 
# # (pydata or seaborn datasets) containing datasets as a source from the iris data. 
# # Create a pandas dataframe, df_iris, from this data.
# df = data('iris')

# # print the first 3 rows
# df.head(3)
# # print the number of rows and columns (shape)
# df.shape

# # print the column names
# df.columns

# # print the data type of each column
# df.info()


# # print the summary statistics for each of the numeric variables
# df.describe()


# from pydataset import data
# # Read the data from this google sheet into a dataframe, df_google.

# df = pd.read_clipboard()



# # print the first 3 rows
# df.head()
# # print the number of rows and columns
# df.shape

# # print the column names
# df.columns
# # print the data type of each column
# df.info()
# # print the summary statistics for each of the numeric variables
# df.describe

# # print the unique values for each of your categorical variables
# print(df.Embarked.value_counts())
# print(df.Sex.value_counts())
# print(df.Cabin.value_counts())
# print(df.Ticket.value_counts())





# # Download the previous exercise's file into an excel (File → Download → Microsoft Excel). 
# # Read the downloaded file into a dataframe named df_excel.
# df = pd.read_excel('train.xlsx')

# # assign the first 100 rows to a new dataframe, df_excel_sample
# df_excel_sample = df.head()
# # print the number of rows of your original dataframe
# df.shape[0]

# # print the first 5 column names
# df.columns[0:5]
# # print the column names that have a data type of object
# df.columns[[3,4,8,10,11]]


# # compute the range for each of the numeric variables.
# range_of_PassengerId = df.PassengerId.max() - df.PassengerId.min()
# range_of_Survived = df.Survived.max() - df.Survived.min()
# range_of_Pclass = df.Pclass.max() - df.Pclass.min()
# range_of_Age = df.Age.max() - df.Age.min()
# range_of_SibSp = df.SibSp.max() - df.SibSp.min()
# range_of_Parch = df.Parch.max() - df.Parch.min()
# range_of_Fare = df.Fare.max() - df.Fare.min()


# print(df.columns)
# df.info()
# print(range_of_Fare)


# # Once you've got your get_titanic_data, get_iris_data, and get_telco_data functions written, 
# # now it's time to add caching to them. To do this, edit the beginning of the function to check 
# # for the local filename of telco.csv, titanic.csv, or iris.csv. If they exist, use the .csv file. 
# # If the file doesn't exist, then produce the SQL and pandas necessary to create a dataframe, 
# # then write the dataframe to a .csv file with the appropriate name.
# os.getcwd()