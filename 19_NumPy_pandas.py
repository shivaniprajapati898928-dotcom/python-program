# Write a program to create a NumPy 2D array, compute row-wise and column wise sums, and convert it to a Pandas DataFrame for further processing (e.g., normalization). 

import numpy as np
import pandas as pd

# Step 1: Create a 2D NumPy array
array = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original NumPy Array:")
print(array)

# Step 2: Compute row-wise and column-wise sums
row_sum = np.sum(array, axis=1)   # Sum across columns
col_sum = np.sum(array, axis=0)   # Sum across rows

print("\nRow-wise Sums:", row_sum)
print("Column-wise Sums:", col_sum)

# Step 3: Convert NumPy array to Pandas DataFrame
df = pd.DataFrame(array, columns=['A', 'B', 'C'])
print("\nDataFrame:")
print(df)

# Step 4: Normalize the DataFrame (values between 0 and 1)
normalized_df = (df - df.min()) / (df.max() - df.min())

print("\nNormalized DataFrame:")
print(normalized_df)
