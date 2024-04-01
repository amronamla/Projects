import pandas as pd

# Read census data from CSV file into a DataFrame
census = pd.read_csv('census_data.csv', index_col=0)

# Display the first 5 rows of the DataFrame
print(census.head(5))

# Display the data types of each column
print(census.dtypes)

# Display unique values in the 'birth_year' column
print(census['birth_year'].unique())

# Replace 'missing' values in 'birth_year' column with 1967
census['birth_year'] = census['birth_year'].replace(['missing'], 1967)

# Display unique values in the 'birth_year' column after replacement
print(census['birth_year'].unique())

# Convert 'birth_year' column to integer data type
census['birth_year'] = census['birth_year'].astype("int")

# Display data types after conversion
print(census.dtypes)

# Print the mean of the 'birth_year' column
print(census['birth_year'].mean())

# Convert 'higher_tax' column to an ordered categorical type
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)

# Display unique values in the 'higher_tax' column after conversion
print(census['higher_tax'].unique())

# Convert 'higher_tax' column to numeric codes
census['higher_tax'] = census['higher_tax'].astype('category').cat.codes

# Print the median of the 'higher_tax' column
print(census['higher_tax'].median())

# Create dummy variables for the 'marital_status' column
census = pd.get_dummies(census, columns=['marital_status'])

# Display the first 5 rows of the DataFrame after dummy encoding
print(census.head())
