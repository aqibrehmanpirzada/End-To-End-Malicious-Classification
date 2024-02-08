import pandas as pd
import os
from pathlib import Path
from sklearn.model_selection import train_test_split

# Define the path to the external data directory
path = Path('/media/aqib/Software/My Boys Team Projects/project week 1/End-To-End-Malicious-Classification/data/raw_data')
# Function to load datasets
def load_data():
    spam_df = pd.read_csv(path / 'features-domain_Spam.csv')
    phishing_df = pd.read_csv(path / 'features-domain_phishing.csv')
    malware_df = pd.read_csv(path / 'features-domain_Malware.csv')
    benign_df = pd.read_csv(path / 'features_domain_benign_csv.csv')
    return spam_df, phishing_df, malware_df, benign_df

# Function to preprocess datasets
def preprocess_data(spam_df, phishing_df, malware_df, benign_df):
    # Example preprocessing steps:
    # - Encode categorical variables
    # - Fill or drop missing values
    # - Feature scaling
    # - Feature selection or extraction
    # This is a placeholder for actual preprocessing logic
    # Combine all datasets and add a 'label' column
    spam_df['label'] = 'spam'
    phishing_df['label'] = 'phishing'
    malware_df['label'] = 'malware'
    benign_df['label'] = 'benign'
    
    full_df = pd.concat([spam_df, phishing_df, malware_df, benign_df], ignore_index=True)
    return full_df





if __name__ == '__main__':
    # Load the data
    spam_df, phishing_df, malware_df, benign_df = load_data()
    
    # Preprocess the data
    full_df = preprocess_data(spam_df, phishing_df, malware_df, benign_df)
    
    # Split the data
    # X_train, X_test, y_train, y_test = split_data(full_df)
    
    # Save the processed data
    PROCESSED_DATA_PATH = Path('/media/aqib/Software/My Boys Team Projects/project week 1/End-To-End-Malicious-Classification/data/processed_data')
    # os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    full_df.to_csv(PROCESSED_DATA_PATH/'dataset.csv')
    # X_train.to_csv(PROCESSED_DATA_PATH / 'X_train.csv', index=False)
    # X_test.to_csv(PROCESSED_DATA_PATH / 'X_test.csv', index=False)
    # y_train.to_csv(PROCESSED_DATA_PATH / 'y_train.csv', index=False)
    # y_test.to_csv(PROCESSED_DATA_PATH / 'y_test.csv', index=False)
