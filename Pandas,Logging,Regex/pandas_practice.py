import pandas as pd

# Creating DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Reshaping Data
melted_df = pd.melt(df1)
reshaped_df = pd.pivot(df1, columns='A', values='B')

# Change layout, sorting, reindexing, renaming
sorted_df = df1.sort_values('A')
renamed_df = df1.rename(columns={'A': 'Year'})
reindexed_df = df1.reset_index()

# Append rows and columns of DataFrames
df2 = pd.DataFrame({'A': [10, 11, 12], 'B': [13, 14, 15], 'C': [16, 17, 18]})
appended_rows = pd.concat([df1, df2])
appended_columns = pd.concat([df1, df2], axis=1)

# Summarize Data
count_values = df1['A'].value_counts()
data_shape = df1.shape
distinct_values = df1['A'].nunique()
df1_summary = df1.describe()

# Make New Columns
df1['Area'] = df1['B'] * df1['C']
df1['Volume'] = df1['B'] * df1['C'] * df1['A']

# Combine Data Sets
df3 = pd.DataFrame({'A': [1, 2, 3], 'D': ['T', 'F', 'D']})
df4 = pd.DataFrame({'A': [2, 3, 4], 'D': ['F', 'D', 'T']})
inner_join = pd.merge(df3, df4, how='inner', on='A')
left_join = pd.merge(df3, df4, how='left', on='A')
right_join = pd.merge(df3, df4, how='right', on='A')
outer_join = pd.merge(df3, df4, how='outer', on='A')

# Print the results
print("Original DataFrame:")
print(df1)

print("\nMelted DataFrame:")
print(melted_df)

print("\nReshaped DataFrame:")
print(reshaped_df)

print("\nSorted DataFrame:")
print(sorted_df)

print("\nRenamed DataFrame:")
print(renamed_df)

print("\nReindexed DataFrame:")
print(reindexed_df)

print("\nAppended Rows:")
print(appended_rows)

print("\nAppended Columns:")
print(appended_columns)

print("\nCount Values:")
print(count_values)

print("\nData Shape:")
print(data_shape)

print("\nDistinct Values:")
print(distinct_values)

print("\nDataFrame Summary:")
print(df1_summary)

print("\nNew Columns:")
print(df1)

print("\nInner Join:")
print(inner_join)

print("\nLeft Join:")
print(left_join)

print("\nRight Join:")
print(right_join)

print("\nOuter Join:")
print(outer_join)




import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50],
    'z': [100, 200, 300, 400, 500]
})

# Plot a histogram for each column
df.plot.hist()
plt.show()

# Plot a scatter plot
df.plot.scatter(x='x', y='y')
plt.show()