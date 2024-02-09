import pandas as pd
from logger import log

def read_data(file_path):
    try:
        data = pd.read_csv(file_path, low_memory=False)
        log("Data loaded successfully")
        return data
    except Exception as e:
        log(f"Error loading data: {str(e)}")
        return None

def show_data_status(data):
    try:
        log(f"Number of rows: {data.shape[0]}")
        log(f"Number of columns: {data.shape[1]}")
        log("Columns with missing values:")
        missing_cols = data.columns[data.isnull().any()].tolist()
        if missing_cols:
            for col in missing_cols:
                log(f" - {col}: {data[col].isnull().sum()} missing values")
        else:
            log("No missing values found")
        log("Data types:")
        log(data.dtypes)
    except Exception as e:
        log(f"Error showing data status: {str(e)}")

if __name__ == "__main__":
         # Provide the path to your data file
    file_path = 'data/processed_data/dataset.csv' 
    data = read_data(file_path)
    if data is not None:
        show_data_status(data)
