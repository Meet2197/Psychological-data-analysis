import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data into a pandas DataFrame
df3 = pd.read_excel('C:/Users/User/Downloads/DATA_WORK.xlsx')

# Replace 'Non administratif' with 0 and 'Administratif' with 1
df3['POSTE'] = df3['POSTE'].replace({'Non administratif': 0, 'Administratif': 1})
df3['Genre'] = df3['Genre'].replace({'Homme': 0, 'Femme': 1})

# Explicitly set the column type to integer if desired
df3['POSTE'] = df3['POSTE'].astype(int)

# Display the updated DataFrame
print(df3)

# Extract relevant data and drop any rows with missing values
data = df3[['POSTE', 'SCORE_TOTAL_détresse_psychologique_au_travail']].dropna()

# Perform a t-test to compare the means of the two groups
group1 = data[data['POSTE'] == 0]['SCORE_TOTAL_détresse_psychologique_au_travail']
group2 = data[data['POSTE'] == 1]['SCORE_TOTAL_détresse_psychologique_au_travail']

t_stat, p_value = stats.ttest_ind(group1, group2)

print(f"T-statistic: {t_stat}, P-value: {p_value}")

# Generate a box plot to visualize the distribution
plt.figure(figsize=(10, 6))
sns.boxplot(x='POSTE', y='SCORE_TOTAL_détresse_psychologique_au_travail', data=data)
plt.xlabel('POSTE (0 = Non administratif, 1 = Administratif)')
plt.ylabel('SCORE_TOTAL_détresse_psychologique_au_travail')
plt.title('Distribution of Psychological Distress Scores by POSTE')
plt.show()

# Generate a bar plot to show the mean scores with error bars
plt.figure(figsize=(10, 6))
sns.barplot(x='POSTE', y='SCORE_TOTAL_détresse_psychologique_au_travail', data=data, ci='sd')
plt.xlabel('POSTE (0 = Non administratif, 1 = Administratif)')
plt.ylabel('Mean SCORE_TOTAL_détresse_psychologique_au_travail')
plt.title('Mean Psychological Distress Scores by POSTE with Standard Deviation')
plt.show()


# Extract relevant data and drop any rows with missing values
data = df3[['Secteur_métier', 'Genre', 'Age', 'SCORE_TOTAL_détresse_psychologique_au_travail']].dropna()

# Check the unique values in 'Secteur_métier' to understand the categories
print(data['Secteur_métier'].unique())

# Perform a t-test to compare the means of psychological distress scores between different 'Secteur_métier' groups
unique_secteurs = data['Secteur_métier'].unique()
for i in range(len(unique_secteurs)):
    for j in range(i + 1, len(unique_secteurs)):
        group1 = data[data['Secteur_métier'] == unique_secteurs[i]]['SCORE_TOTAL_détresse_psychologique_au_travail']
        group2 = data[data['Secteur_métier'] == unique_secteurs[j]]['SCORE_TOTAL_détresse_psychologique_au_travail']
        t_stat, p_value = stats.ttest_ind(group1, group2)
        print(f"Comparing {unique_secteurs[i]} and {unique_secteurs[j]}: T-statistic = {t_stat}, P-value = {p_value}")

# Generate a box plot to visualize the distribution by 'Secteur_métier' and 'Genre'
plt.figure(figsize=(12, 8))
sns.boxplot(x='Secteur_métier', y='SCORE_TOTAL_détresse_psychologique_au_travail', hue='Genre', data=data)
plt.xlabel('Secteur_métier')
plt.ylabel('SCORE_TOTAL_détresse_psychologique_au_travail')
plt.title('Distribution of Psychological Distress Scores by Secteur Metier and Genre')
plt.xticks(rotation=45)

# Add custom annotation inside the plot
plt.text(x=0.5, y=max(data['SCORE_TOTAL_détresse_psychologique_au_travail']),
         s='Note: Homme = 0, Femme = 1',
         horizontalalignment='center', fontsize=12, color='black',
         bbox=dict(facecolor='white', alpha=0.5))

plt.legend(title='Genre', loc='upper right', labels=['Homme', 'Femme'])
plt.show()

# Generate a scatter plot to show the relationship between 'Age' and psychological distress scores by 'Secteur_métier' and 'Genre'
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Age', y='SCORE_TOTAL_détresse_psychologique_au_travail', hue='Secteur_métier', style='Genre', data=data)
plt.xlabel('Age')
plt.ylabel('SCORE_TOTAL_détresse_psychologique_au_travail')
plt.title('Psychological Distress Scores by Age, Secteur Metier, and Genre')
plt.show()


# Create a results table to store t-test results
results = []

# Perform a t-test to compare the means of psychological distress scores between different 'Secteur_métier' groups
unique_secteurs = data['Secteur_métier'].unique()
for i in range(len(unique_secteurs)):
    for j in range(i + 1, len(unique_secteurs)):
        group1 = data[data['Secteur_métier'] == unique_secteurs[i]]['SCORE_TOTAL_détresse_psychologique_au_travail']
        group2 = data[data['Secteur_métier'] == unique_secteurs[j]]['SCORE_TOTAL_détresse_psychologique_au_travail']
        t_stat, p_value = stats.ttest_ind(group1, group2)
        results.append({
            'Secteur_métier_1': unique_secteurs[i],
            'Secteur_métier_2': unique_secteurs[j],
            'T-statistic': t_stat,
            'P-value': p_value
        })

# Convert the results to a DataFrame
results_df = pd.DataFrame(results)

# Display the results table
print(results_df)

# Check if the column exists
if 'Secteur_métier' in df3.columns:
    # Calculate the frequency of each unique value in the Secteur_métier column
    secteur_freq = df3['Secteur_métier'].value_counts()
    print(secteur_freq)
else:
    print("The 'Secteur_métier' column does not exist in the dataframe.")

# Perform ANOVA if the columns exist
if 'Secteur_métier' in df3.columns and 'SCORE_Epuisement_professionnel ' in df3.columns:
    anova_result = stats.f_oneway(*[df3[df3['Secteur_métier'] == secteur]['SCORE_Epuisement_professionnel '] for secteur in df3['Secteur_métier'].unique()])
    print(anova_result)
else:
    print("Required columns for ANOVA do not exist in the dataframe.")

# Plot boxplot for the numerical variable across different Secteur_métier groups if columns exist
if 'Secteur_métier' in df3.columns and 'SCORE_Epuisement_professionnel ' in df3.columns:
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Secteur_métier', y='SCORE_Epuisement_professionnel ', data=df3)
    plt.title('Boxplot of SCORE_Epuisement_professionnel by Secteur_métier')
    plt.xlabel('Secteur_métier')
    plt.ylabel('SCORE_Epuisement_professionnel')
    plt.xticks(rotation=90, fontsize=6)
    plt.show()
else:
    print("Required columns for plotting do not exist in the dataframe.")
# ADSM - Arts - Danse - Spectacle- Musique,  Ins-Acc : Insertion - Accompagnement , Aéronautique - Spacial : Aer-Sp , Médical - Santé - Hôpital - Soins : MSHS ,
# Enseignement - Education - Universitaire : EEU , BTP , Administration - Secretariat - Assistant : ASA,  Banque - Assurance - Finance : BAF,
# Social - Service à la personne - Aide à la personne : SSPAP , Secteur public - Administration  : SPA, Transport - logistique : TL,
# Commerce - Distribution - Vente - E commerce : CDVEC, Psychologue ( santé mentale / physique) : Psycho
