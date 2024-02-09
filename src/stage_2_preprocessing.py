import numpy as np  
import pandas as pd
from logger import log
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import os


# subdirectory_path = '../data/processed_data/'
subdirectory_path = 'data/processed_data/'
os.makedirs(subdirectory_path, exist_ok=True)


def drop_unnamed_columns(data):
    unnamed_cols = [col for col in data.columns if col.startswith('Unnamed')]
    data.drop(columns=unnamed_cols, inplace=True)
    log("Dropped 'Unnamed' columns.")
    log(f"Data Columns after dropping unnamed columns: {data.columns.tolist()}")
    return data  # Return the modified DataFrame


def handle_missing_values(data):
    missing_percentages = (data.isnull().sum() / len(data)) * 100
    for col in data.columns:
        missing_percentage = missing_percentages[col]
        if missing_percentage > 5 and missing_percentage <= 30:
            suggestion = f"For column '{col}', {missing_percentage:.2f}% missing values. Consider imputing with mean (numerical) or mode (categorical)."
            log(suggestion)
            print(suggestion)  # Print suggestion on console
        if missing_percentage > 30:
            suggestion = f"For column '{col}', {missing_percentage:.2f}% missing values. Consider using ML-based approaches for handling missing values."
            log(suggestion)
            print(suggestion)  # Print suggestion on console
        if missing_percentage > 0 and missing_percentage <= 5:
            suggestion = f"For column '{col}', {missing_percentage:.2f}% missing values. You may choose to remove rows with missing values."
            log(suggestion)
            print(suggestion)  # Print suggestion on console
        else:
            log(f"No missing values found in column '{col}'.")
    return data
def separate_columns(data):
    
    missing_percentages = (data.isnull().sum() / len(data)) * 100
    
    # Separate columns based on missing percentage
    more_than_5_percent = [col for col, percentage in missing_percentages.items() if percentage > 5]
    less_than_or_equal_to_5_percent = [col for col, percentage in missing_percentages.items() if percentage <= 5]
    
    # Create DataFrames for each group
    more_than_5_percent_df = data[more_than_5_percent]
    less_than_or_equal_to_5_percent_df = data[less_than_or_equal_to_5_percent]
    log("Separate cols on percentage basis")
    return more_than_5_percent_df, less_than_or_equal_to_5_percent_df
def separate_numerical_categorical_cols(data):
    numerical_cols = data.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = data.select_dtypes(exclude=['number']).columns.tolist()
    return numerical_cols, categorical_cols


def impute_missing_values_with_simple_imputer(data, categorical_cols, numerical_cols):
    # Impute missing values for numerical columns using mean strategy
    numerical_imputer = SimpleImputer(strategy='mean')
    data[numerical_cols] = numerical_imputer.fit_transform(data[numerical_cols])
    
    # Impute missing values for categorical columns using most frequent strategy
    categorical_imputer = SimpleImputer(strategy='most_frequent')
    data[categorical_cols] = categorical_imputer.fit_transform(data[categorical_cols])
    log("The Imputer has been trained for its working of Imputation")
    data.to_excel(subdirectory_path + 'cleaned_data.xlsx', index=False)
    log("The Data has successfully been saved to the Data directory")
    return data

if __name__ == "__main__":
    file_path = 'data/processed_data/dataset.csv' 
    data = pd.read_csv(file_path,low_memory=False)
    data = drop_unnamed_columns(data)
    # data = handle_missing_values(data)
    more_than_5_percent_df, less_than_or_equal_to_5_percent_df = separate_columns(data)
    numerical_cols, categorical_cols =  separate_numerical_categorical_cols(data)
    # print(f"Numerical columns{numerical_cols} \n Categorical columns{categorical_cols}")
    imputed_data = impute_missing_values_with_simple_imputer(data, categorical_cols, numerical_cols)
    # print(imputed_data.isnull().sum())
    # print("Columns with more than 5% missing values:")
    # print(more_than_5_percent_df.columns.tolist())
    # print(data[more_than_5_percent_df].info())
    # print("\nColumns with 5% or less missing values:")
    # print(less_than_or_equal_to_5_percent_df.columns.tolist())