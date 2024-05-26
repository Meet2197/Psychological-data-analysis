import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the Excel file
df = pd.read_excel('C:/Users/User/Downloads/work.xlsx')

# Function to calculate p-values using .loc to avoid chained assignment
def calculate_pvalues(df):
    df = df.dropna()._get_numeric_data()
    pvalues = pd.DataFrame(data=np.zeros((df.shape[1], df.shape[1])),
                           columns=df.columns,
                           index=df.columns)
    for row in df.columns:
        for col in df.columns:
            pvalues.loc[row, col] = pearsonr(df[row], df[col])[1]
    return pvalues

# Calculate the correlation matrix and p-values
corr = df.corr()
pvalues = calculate_pvalues(df)

# Create a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=False, fmt=".2f",
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

# Reduce the size of the tick labels
ax.set_xticklabels(ax.get_xticklabels(), fontsize=8)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=8)

# Annotate the lower triangle with p-values and stars for significance
for i in range(len(corr)):
    for j in range(i):
        p = pvalues.iloc[i, j]
        text = f'{corr.iloc[i, j]:.2f}'
        if p < 0.05:
            text += '*'
        ax.text(j + 0.5, i + 0.5, text, ha='center', va='center', color='black', fontsize=7)

plt.show()
