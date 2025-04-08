import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st
# Importing the dataset
df = pd.read_csv("railway.csv")
# Checking the dimensions of the dataset
#print(df.shape)
# Listing the columns of the dataset
#print(df.columns)
# Viewing the first five rows of the dataset
#print(df.head())
# Viewing the last five rows of the dataset
#print(df.tail())
# Viewing all the information about the dataset
# print(df.info())
# Viewing all the information about the dataset
#print(df.info())
# Descriptive statistics of the dataset
#print(df.describe())
# Checking for missing values in the dataset and their total count
#print(df.isnull().sum())
# Viewing the maximum values in the dataset
#print(df.max())
# Viewing the minimum values in the dataset
#print(df.min())
# Viewing the median values in the dataset
#print(df.median())
# Viewing the mean values in the dataset
#print(df.mean())
# Viewing the mode values in the dataset
#print(df.mode())
# Counting non-null values in each column
#print(df.count())
'''
# Select the numerical column
price = df["Price"]

# Calculate statistics
mean_price = price.mean()
median_price = price.median()
mode_price = price.mode().tolist()
max_price = price.max()
min_price = price.min()
count_price = price.count()

# Display results
print("Mean Price:", mean_price)
print("Median Price:", median_price)
print("Mode Price:", mode_price)
print("Max Price:", max_price)
print("Min Price:", min_price)
print("Count:", count_price)
'''

# Cleaning the dataset by dropping rows with missing values
#print(df.dropna(inplace=True))

'''
print("Objective 1: Average Ticket Price by Departure Station (Ranked)")
average_price_by_station = df.groupby('Departure Station')['Price'].mean().sort_values(ascending=False)
print(average_price_by_station)
print("\n")
'''
'''
# Objective 2: Identify outliers in ticket prices using the IQR method
print("Objective 2: Outliers in Ticket Prices (IQR Method)")
Q1 = np.percentile(df['Price'], 25)
Q3 = np.percentile(df['Price'], 75)
IQR = Q3 - Q1
outliers = df[(df['Price'] < (Q1 - 1.5 * IQR)) | (df['Price'] > (Q3 + 1.5 * IQR))]
print(outliers[['Departure Station', 'Arrival Destination', 'Price']])
print("\n")
'''

'''
# Objective 3: Analyze the percentage of delayed journeys by reason for delay
print("Objective 3: Percentage of Delayed Journeys by Reason")
delayed_journeys = df[df['Journey Status'] == 'Delayed']
delay_reason_counts = delayed_journeys['Reason for Delay'].value_counts(normalize=True) * 100
print(delay_reason_counts)
print("\n")


# Objective 4: Compare the average ticket price for different ticket classes
print("Objective 4: Average Ticket Price by Ticket Class")
average_price_by_class = df.groupby('Ticket Class')['Price'].mean()
print(average_price_by_class)


# Optional: Bar plot
average_price_by_class.plot(kind='bar', title='Average Ticket Price by Class', color='skyblue')
plt.xlabel('Ticket Class')
plt.ylabel('Average Price')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(df['Price'], kde=False, bins=30, color='skyblue')
plt.title('Histogram of Ticket Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()




# Objective 5: Analyze the distribution of payment methods
print("Objective 5: Distribution of Payment Methods")
payment_method_distribution = df['Payment Method'].value_counts(normalize=True) * 100
print(payment_method_distribution)


# 2. Bar Plot – Average ticket price by class
plt.figure(figsize=(6, 4))
sns.barplot(x='Ticket Class', y='Price', data=df, estimator=np.mean, palette='muted')
plt.title('Average Ticket Price by Class')
plt.ylabel('Average Price')
plt.tight_layout()
plt.show()

# 4. Violin Plot – Ticket price distribution by class
plt.figure(figsize=(6, 4))
sns.violinplot(x='Ticket Class', y='Price', data=df, palette='Set2')
plt.title('Violin Plot of Price by Ticket Class')
plt.tight_layout()
plt.show()

# 5. Count Plot – Frequency of ticket classes
plt.figure(figsize=(6, 4))
sns.countplot(x='Ticket Class', data=df, palette='pastel')
plt.title('Count of Ticket Classes')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
'''

# 6. KDE Plot – Density of ticket prices
plt.figure(figsize=(8, 4))
sns.kdeplot(df['Price'], shade=True, color='purple')
plt.title('KDE Plot of Ticket Prices')
plt.xlabel('Price')
plt.tight_layout()
plt.show()













































































