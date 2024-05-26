import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import kruskal

# Read your data into a pandas DataFrame
df = pd.read_excel('C:/Users/User/Downloads/work.xlsx')

# Calculate basic descriptive statistics
descriptive_stats = df.describe().transpose()

# Calculate mode for each column
modes = df.mode().iloc[0]

# Add mode to the descriptive statistics
descriptive_stats['mode'] = modes

# Calculate standard error of the mean (SEM)
descriptive_stats['sem'] = descriptive_stats['std'] / np.sqrt(descriptive_stats['count'])

# Calculate interquartile range (IQR)
descriptive_stats['iqr'] = descriptive_stats['75%'] - descriptive_stats['25%']

# Create a DataFrame to hold the calculated statistics
desc_stats = descriptive_stats[['mean', '50%', 'mode', 'std', 'sem', 'iqr']].rename(columns={'50%': 'median'})

# Display the descriptive statistics
print("Descriptive Statistics:")
print(desc_stats)

# Plot the descriptive statistics
plt.figure(figsize=(15, 10))
desc_stats.plot(kind='bar')
plt.title('Descriptive Statistics for Each Numeric Column')
plt.xlabel('Variables')
plt.ylabel('Values')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Statistics')
plt.tight_layout()
plt.show()

# Create a violin plot for descriptive statistics
plt.figure(figsize=(15, 10))
sns.violinplot(data=df, inner='quartile')
plt.title('Graphique en boîte pour les statistiques descriptives')
plt.xticks(rotation=90)
plt.show()

grouping_variable = df.columns[1]  # Change this if you want to group by a different column

# Prepare a DataFrame to hold Kruskal-Wallis test results
kruskal_results = []

# Conduct the Kruskal-Wallis test for each numeric column
for column in df.select_dtypes(include=[np.number]).columns:
    groups = [df[column][df[grouping_variable] == level] for level in df[grouping_variable].unique()]
    stat, p_value = kruskal(*groups)
    kruskal_results.append({'Variable': column, 'Kruskal-Wallis statistiques': stat, 'p-value': p_value})

# Convert the results to a DataFrame
kruskal_results_df = pd.DataFrame(kruskal_results)

# Display the Kruskal-Wallis test results
print("Kruskal-Wallis Test Results:")
print(kruskal_results_df)

# Create box plots for each numeric column, grouped by the categorical variable
plt.figure(figsize=(15, 10))
sns.boxplot(data=df, orient="h")
plt.title('Graphique en boîte pour les statistiques descriptives')
plt.xticks(rotation=90)
plt.show()

# Create box plots for each numeric column, grouped by the categorical variable
plt.figure(figsize=(15, 10))
for column in df.select_dtypes(include=[np.number]).columns:
    plt.figure()
    sns.boxplot(x=grouping_variable, y=column, data=df)
    plt.title(f'Box Plot of {column} Grouped by {grouping_variable}')
    plt.xlabel(grouping_variable)
    plt.ylabel(column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()