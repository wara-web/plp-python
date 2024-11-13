#import libraries, pandas,matploitlib and numPy

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read the dataset
data = pd.read_csv('/Users/techgenics/Desktop/PLP/Python/week7/plp.csv')

#understanding nthe dataset columns
print(data.columns)
#view the first 10 records    
print(data.head(10))

#brief description of the dataset

data.describe()

# Check for missing values
print(data.isnull().sum())

# Basic information about the dataset
print(data.info())

# Summary statistics
print(data.describe())

# Check the distribution of target classes
print(data['LoginAttempts'].value_counts())



