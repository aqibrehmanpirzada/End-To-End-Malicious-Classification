import pandas as pd
import ast
from sklearn.preprocessing import LabelEncoder
class DataProcessor:
    def __init__(self):
        self.df = None

    def read_excel_file(self, file_path):
        self.df = pd.read_excel(file_path)

    def remove_ids_and_sum(self, row):
        row_dict = ast.literal_eval(row)
        values = [value for value in row_dict.values()]
        return sum(values)

    def preprocess_data(self):
        self.df['distance_from_bad_words'] = self.df['distance_from_bad_words'].apply(self.remove_ids_and_sum)
        self.df['Domain_Age'] = pd.to_timedelta(self.df['Domain_Age'])
        self.df['Domain_Age_in_days'] = self.df['Domain_Age'].dt.days
        self.df['Creation_Date_Time'] = pd.to_datetime(self.df['Creation_Date_Time'].replace('0', pd.NaT), errors='coerce')
        self.df['Creation_year'] = self.df['Creation_Date_Time'].dt.year
        self.df['Creation_month'] = self.df['Creation_Date_Time'].dt.month
        self.df['Creation_day'] = self.df['Creation_Date_Time'].dt.day
        self.df['Creation_hour'] = self.df['Creation_Date_Time'].dt.hour
        self.df['Creation_minute'] = self.df['Creation_Date_Time'].dt.minute
        self.df['Creation_second'] = self.df['Creation_Date_Time'].dt.second
        self.df = self.df.drop(columns=['oc_8', 'hex_32', 'Page_Rank', 'hex_8', 'dec_8','oc_32','dec_32','Domain_Age','Domain_Name','3gram','2gram','1gram','len','Creation_Date_Time',
                      'char_distribution','Emails','Registrar','Registrant_Name','typos','Organization'], axis=1)
        self.df = self.df.dropna()

    def label_encode_categorical(self, columns):
        label_encoder = LabelEncoder()
        for col in columns:
            if col in self.df.columns:
                self.df[col] = label_encoder.fit_transform(self.df[col])

    def analyze_data(self):
        categorical_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        numerical_cols = self.df.select_dtypes(include=['int64', 'float64']).columns.tolist()

        for col in categorical_cols:
            unique_values = self.df[col].nunique()
            print(f"Column '{col}' has '{unique_values}' unique values.")

        for col in numerical_cols:
            unique_values = self.df[col].nunique()
            print(f"Column '{col}' has '{unique_values}' unique values.")
    
    def display_latest_data(self, num_rows=5):
        print(self.df.head(num_rows))

    def map_labels(self, label_mapping):
        self.df['label'] = self.df['label'].map(label_mapping)


if __name__ == "__main__":
    processor = DataProcessor()
    processor.read_excel_file('data/processed_data/cleaned_data.xlsx')
    processor.preprocess_data()
    processor.label_encode_categorical(['sld',
     'Country',
     'State',
     'obfuscate_at_sign',
     'shortened',
     'longest_word',
     'Name_Server_Count',
     'tld']) # Specify the categorical columns you want to encode
    processor.analyze_data()
    processor.display_latest_data()
    processor.map_labels({'spam': 0, 'phishing': 1, 'malware': 2, 'benign': 3})  # Map labels
    processor.display_latest_data()  # Display the latest data after label mapping
