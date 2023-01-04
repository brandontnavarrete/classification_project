from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import pandas as pd
import os


def prep_telco(df):
    
    df = df.drop_duplicates()
    
    dummy_df = pd.get_dummies(df[[
     'gender',
     'partner',
     'dependents',
     'phone_service',
     'multiple_lines',
     'online_security',
     'online_backup',
     'device_protection',
     'tech_support',
     'streaming_tv',
     'streaming_movies',
     'paperless_billing',
     'churn',
     'contract_type',
     'internet_service_type',
     'payment_type']], dummy_na=False, drop_first = True )
    
    df = pd.concat([df, dummy_df], axis=1)  
    
    df = df.drop([
     'gender',
     'partner',
     'dependents',
     'phone_service',
     'multiple_lines',
     'online_security',
     'online_backup',
     'device_protection',
     'tech_support',
     'streaming_tv',
     'streaming_movies',
     'paperless_billing',
     'churn',
     'contract_type',
     'internet_service_type',
     'payment_type'],axis = 1)
    
    return df