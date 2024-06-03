import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

df3 = pd.read_excel('C:/Users/User/Downloads/DATA_WORK.xlsx')

# Logistic regression:
# Select the necessary columns for the regression analysis
df_reg = df3[['SCORE_harcèlement_au_travail', 'Score_total_justice_organisationnelle', 'Score_justice_procédurale', 'Score_justice_interpersonnelle']]

# Display the first few rows of the selected columns
print(df_reg.head())


# Define the dependent variable (y) and independent variables (X)
y = df3['SCORE_harcèlement_au_travail']
X = df3[['Score_total_justice_organisationnelle', 'Score_justice_procédurale', 'Score_justice_interpersonnelle']]

# Add a constant to the independent variables matrix
X = sm.add_constant(X)

# Perform the regression analysis
model = sm.OLS(y, X).fit()

# Display the regression results
print(model.summary())

# Plot boxplot for the numerical variable across different Secteur_métier groups if columns exist
if 'Secteur_métier' in df3.columns and 'SCORE_Epuisement_professionnel ' in df3.columns:
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Secteur_métier', y='SCORE_Epuisement_professionnel ', data=df3)
    plt.title('Boxplot of SCORE_Epuisement_professionnel by Secteur_métier')
    plt.xlabel('Secteur_métier')
    plt.ylabel('SCORE_Epuisement_professionnel')
    plt.xticks(rotation=90, fontsize=8)  # Reduce the font size to 8
    plt.show()
else:
    print("Required columns for plotting do not exist in the dataframe.")


# Assuming the inspected columns might have trailing spaces or special characters
df_reg2 = df3[['SCORE_Epuisement_professionnel ', 'SCORE_TOTAL_Engagement_au_travail', 'optimisme', 'scoresoutiensocial']]

# Drop any rows with missing values in the selected columns
df_reg2 = df_reg2.dropna()

# Define the dependent variable (y) and independent variables (X)
y = df_reg2['SCORE_Epuisement_professionnel ']
X = df_reg2[['SCORE_TOTAL_Engagement_au_travail', 'optimisme', 'scoresoutiensocial']]

# Add a constant to the independent variables matrix
X = sm.add_constant(X)

# Perform the regression analysis
model2 = sm.OLS(y, X).fit()

# Display the regression results
print(model2.summary())

# Extract summary information from the model summary
summary_df = model.summary2().tables[1]

# Convert the summary information into a DataFrame
summary_df = pd.DataFrame(summary_df)

# Save the summary DataFrame to an Excel file
output_file_path = 'C:/Users/User/Downloads/Regression_Results.xlsx'
summary_df.to_excel(output_file_path, index=False)

print(f"Regression results saved to {output_file_path}")