# Data Analysis with Pandas, NumPy, and Seaborn
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
This project contains a series of scripts for performing data analysis using Python libraries such as Pandas, NumPy, Seaborn, Matplotlib, and Scipy. The scripts load data from an Excel file, perform various data manipulations, and generate descriptive statistics and visualizations.

## Prerequisites
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
Before you begin, ensure you have the following installed:

- Python 3.x
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scipy
- OpenPyXL (for reading Excel files)

You can install these packages using pip:

```bash
pip install pandas numpy seaborn matplotlib scipy openpyxl
```bash


Usage 
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
Loading Data
The script reads data from an Excel file located at local/DATA_WORK.xlsx. Modify the path in the script if your file is located elsewhere.

# Data Exploration and Transformation
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
1. Display the structure of the DataFrame:

```bash
df.info()
```bash

2. Generate descriptive statistics:

```bash
df.describe()
```bash

3. Display the first few rows of the DataFrame:

```bash
print("Avant la transformation:")
print(df.head())
print(df.columns)
```bash

4. Convert the 'Genre' column values to numeric:

```bash
df['Genre'] = df['Genre'].replace({'Femme': 1, 'Homme': 0})
```bash

5. Filter data for women in psychological distress:

```bash
women_distress_df = df[(df['Genre'] == 1) & (df['SCORE_TOTAL_détresse_psychologique_au_travail'] == 1)]
```bash

6. Group by sector and count the frequency:

```bash
sector_distress_freq = women_distress_df.groupby('Secteur_métier').size().reset_index(name='Frequency')
```bash

# Statistical Analysis and Visualization :
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------

1. Calculate correlation matrix and p-values:

```bash
corr = df.corr()
pvalues = calculate_pvalues(df)
```bash

2. Create a heatmap of the correlation matrix with p-values:

```bash
sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=False, fmt=".2f", linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
```bash

3. Display descriptive statistics including mode, SEM, and IQR:

```bash
print("Descriptive Statistics:")
print(desc_stats)
```bash

4. Generate bar and violin plots for descriptive statistics:

```bash
desc_stats.plot(kind='bar')
sns.violinplot(data=df, inner='quartile')
```bash

5. Perform Kruskal-Wallis tests:

```bash
kruskal_results_df = pd.DataFrame(kruskal_results)
```bash

6. Create box plots grouped by a categorical variable:

```bash
sns.boxplot(data=df, orient="h")
```bash

# Example Outputs:
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
Descriptive statistics for each numeric column.
Frequency of women in psychological distress in each sector.
Heatmap showing correlation matrix with significance stars.
Bar plots, violin plots, and box plots for various statistics.

# License :
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgements:
--------------------------------------------------------------------------------------------------------------------------------------------
This project uses data analysis libraries such as Pandas, NumPy, Seaborn, Matplotlib, and Scipy. Special thanks to the open-source community for providing these tools.
