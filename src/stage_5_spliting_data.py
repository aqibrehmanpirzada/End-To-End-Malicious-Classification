# Function to split datasets
def split_data(full_df):
    X = full_df.drop('label', axis=1)
    y = full_df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test