# SCT_02.py
# Task 2: Video Game Sales Data - Cleaning & EDA

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set display options
pd.set_option('display.max_columns', None)

# Load the dataset
data_path = os.path.join('..', 'data', 'vgsales.csv')
df = pd.read_csv(data_path)

# Basic info
print(" Dataset Shape:", df.shape)
print("\n Column Names:\n", df.columns.tolist())
print("\n Missing Values:\n", df.isnull().sum())
print("\n Data Types:\n", df.dtypes)
print("\n Sample Rows:\n", df.sample(5))

# Data Cleaning
# 1. Remove rows with missing Year or Publisher
df_cleaned = df.dropna(subset=['Year', 'Publisher'])

# 2. Convert Year to integer (some values are floats like 2006.0)
df_cleaned.loc[:, 'Year'] = df_cleaned['Year'].astype('int')

# 3. Reset index after dropping rows
df_cleaned.reset_index(drop=True, inplace=True)

# 4. Summary after cleaning
print("\nCleaned Data Shape:", df_cleaned.shape)
print("Missing Values After Cleaning:\n", df_cleaned.isnull().sum())
print("Year Range:", df_cleaned['Year'].min(), "-", df_cleaned['Year'].max())

# Objective 1: Most Successful Genres per Region

# Grouping by Genre and summing regional sales
genre_region_sales = df.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()

# Optional: sort genres by total global sales for cleaner display
genre_region_sales = genre_region_sales.sort_values(by='NA_Sales', ascending=False)

# Plotting heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(genre_region_sales, annot=True, fmt=".2f", cmap="YlGnBu")
plt.title('Regional Sales by Genre (in Millions)')
plt.xlabel('Region')
plt.ylabel('Genre')
plt.tight_layout()
plt.show()

# Objective 2: Platform Popularity Over Time

# Group by publisher and sum the global sales
top_publishers = df_cleaned.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x=top_publishers.values, y=top_publishers.index, hue=top_publishers.index, palette='viridis', legend=False)
# sns.barplot(x=top_publishers.values, y=top_publishers.index, palette='viridis')
plt.title('Top 10 Publishers by Global Sales')
plt.xlabel('Total Global Sales (in millions)')
plt.ylabel('Publisher')
plt.tight_layout()
plt.show()

# Objective 3: Top 5 Platforms by Global Sales

# Group by platform and sum global sales
top_platforms = df_cleaned.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(5)

# Plotting
plt.figure(figsize=(8, 5))
# sns.barplot(x=top_platforms.index, y=top_platforms.values, palette='coolwarm')
sns.barplot(x=top_platforms.index, y=top_platforms.values, hue=top_platforms.index, palette='coolwarm', legend=False)
plt.title('Top 5 Platforms by Global Sales')
plt.xlabel('Platform')
plt.ylabel('Total Global Sales (in millions)')
plt.tight_layout()
plt.show()
