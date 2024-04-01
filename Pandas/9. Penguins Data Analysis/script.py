# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Set numpy print options for better readability
np.set_printoptions(suppress=True, precision=1)

# Read the penguins dataset from a CSV file
penguins = pd.read_csv('penguins.csv')

# Display the first few rows of the dataset
print(penguins.head())

# Scatter plot of flipper length vs. body mass
plt.scatter(penguins.flipper_length_mm, penguins.body_mass_g)
plt.show()

# Calculate the covariance matrix for flipper length and body mass
covariance_mat = np.cov(penguins.flipper_length_mm, penguins.body_mass_g)
print("covariance matrix: ")
print(covariance_mat)

# Print the specific covariance value between flipper length and body mass
print("covariance: ", covariance_mat[1][0])

# Calculate Pearson correlation coefficient and p-value
correlation, p = pearsonr(penguins.flipper_length_mm, penguins.body_mass_g)
print("correlation: ", correlation)
