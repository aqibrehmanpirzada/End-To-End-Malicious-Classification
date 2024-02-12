import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data =  pd.read_excel('data/processed_data/cleaned_data.xlsx')
# print(data.info())

# Histogram
def plot_histogram(data, feature):
    plt.figure(figsize=(8, 6))
    sns.histplot(data[feature], bins=20, kde=True)
    plt.title(f'Histogram of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()

# Bar Chart
def plot_bar_chart(data, feature):
    plt.figure(figsize=(10, 6))
    sns.countplot(data[feature])
    plt.title(f'Bar Chart of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Scatter Plot
def plot_scatter(data, feature1, feature2):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=feature1, y=feature2, data=data)
    plt.title(f'Scatter Plot of {feature1} vs {feature2}')
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.show()

# Box Plot
def plot_box(data, feature, by):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=by, y=feature, data=data)
    plt.title(f'Box Plot of {feature} by {by}')
    plt.xlabel(by)
    plt.ylabel(feature)
    plt.xticks(rotation=45)
    plt.show()

# Correlation Heatmap
def plot_correlation_heatmap(data):
    plt.figure(figsize=(12, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.show()

# Pie Chart
def plot_pie_chart(data, feature):
    plt.figure(figsize=(8, 8))
    data[feature].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title(f'Pie Chart of {feature}')
    plt.ylabel('')
    plt.show()

# Time Series Plot
def plot_time_series(data, time_feature, numeric_feature):
    plt.figure(figsize=(12, 6))
    data.set_index(time_feature)[numeric_feature].plot()
    plt.title(f'Time Series Plot of {numeric_feature} over {time_feature}')
    plt.xlabel(time_feature)
    plt.ylabel(numeric_feature)
    plt.show()


# Custom Visualization (e.g., domain name patterns)
def plot_custom(data):
    # Your custom visualization code here
    pass
# def scatter_plot(data, col1, col2):
#     plt.figure(figsize=(12, 6))
#     sns.scatterplot(data=data, x=col1, y=col2)
#     plt.title(f"The Scatter Plot of {col1} and {col2}")
#     plt.xlabel(col1)
#     plt.ylabel(col2)
#     plt.show()

# Example Usage:
print(plot_bar_chart(data, 'Country'))
# plot_scatter(data, 'Domain_Age', 'Page_Rank')
# plot_box(data, 'Page_Rank', 'label')
# plot_correlation_heatmap(data)
# plot_pie_chart(data, 'label')
# plot_time_series(data, 'Creation_Date_Time', 'Page_Rank')
# plot_custom(data)
