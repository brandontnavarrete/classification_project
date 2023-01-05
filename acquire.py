import os
import pandas as pd 
import numpy as np

import re

from sklearn.model_selection import train_test_split
import sklearn.preprocessing

import env


###############

# setting connectiong to sequel server using env
def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


##################
 
# acquiring telco data using a different function

def get_telco_data(get_connection):
    filename = "telco_id.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    
    else:
        
    # read the SQL query into a dataframe
        df = pd.read_sql(
    
        '''
        select * from customers
        join contract_types
        using (contract_type_id)
        join internet_service_types
        using (internet_service_type_id)
        join payment_types
        using (payment_type_id)
        ''', get_connection('telco_churn'))

     # Drop duplicate columns
        df.drop(columns=['payment_type_id', 'internet_service_type_id', 
                         'contract_type_id'], inplace=True)
       
    # Drop null values stored as whitespace    
        df['total_charges'] = df['total_charges'].str.strip()
        
        df = df[df.total_charges != '']
        
    # Convert to correct datatype
        df['total_charges'] = df.total_charges.astype(float)
    
        
        
        
    # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

    # Return the dataframe to the calling code
    return df 

######## train, validate, test split ############


def split_data(df):
    ''' 
    splits data frame and returns a train, validate, 
    and test data frame stratified on churn 
    '''
    
    # split df into train_validate and test
    train_validate, test = train_test_split(df,test_size =.2, 
                                             random_state = 42,
                                             stratify = df.churn_Yes)
    
    # split train_validate into train and validate
    train, validate = train_test_split(train_validate,
                                      test_size = .3,
                                      random_state = 42,
                                      stratify = train_validate.churn_Yes)
                                            
    # reset index for train validate and test
    train.reset_index(drop=True, inplace=True)
    validate.reset_index(drop=True, inplace=True)
    test.reset_index(drop=True, inplace=True)
    
    return train, validate, test