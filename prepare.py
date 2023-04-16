import pandas as pd 
import env
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from sklearn.model_selection import train_test_split
import os
import acquire
from sklearn.impute import SimpleImputer

def split_data(df, target):
    '''
    Takes in the titanic dataframe and return train, validate, test subset dataframes
    '''
    
    
    train, test = train_test_split(df,
                                   test_size=.2, 
                                   random_state=123, 
                                   stratify=df[target]
                                   )
    train, validate = train_test_split(train, 
                                       test_size=.25, 
                                       random_state=123, 
                                       stratify=train[target]
                                       )
    
    return train, validate, test



def prep_telco(data):
    data = data.drop(columns = ['payment_type_id', 'internet_service_type_id',
                     'contract_type_id','Unnamed: 0'])
    the_columns = data.select_dtypes('object').columns

    the_columns = the_columns.drop(['customer_id', 'total_charges'])
    dummy = pd.get_dummies(data, columns = the_columns, drop_first=True)
    return dummy 



def prep_titanic(raw_titanic_df):
    titanic = acquire.get_titanic_data() 
    titanic = titanic.drop(columns=['passenger_id','class','embarked','deck'])
    dummy = pd.get_dummies(titanic[['sex', 'embark_town']], drop_first=True)
    titanic = pd.concat([titanic, dummy], axis=1)
    titanic = titanic.drop(columns=['sex', 'embark_town'])
    return titanic

def prep_iris(iris_df):
    iris_df = iris_df.rename(columns={"species_name": "species"})
    iris_df = iris_df.drop(columns=['Unnamed: 0','species_id','measurement_id'])
    dummy_df = pd.get_dummies(iris_df[['species']])
    iris_df = pd.concat([iris_df,dummy_df], axis=1)
    return iris_df