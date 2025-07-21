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
