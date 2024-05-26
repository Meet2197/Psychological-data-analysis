import pandas as pd
import numpy as np

df = pd.read_excel('C:/Users/User/Downloads/DATA_WORK.xlsx')
# Afficher la structure du DataFrame
df.info()
# statistiques descriptives
df.describe()

# Afficher les premières lignes du DataFrame pour comprendre sa structure
print("Avant la transformation:")
print(df.head())
print(df.columns)

df['Genre'] = df['Genre'].replace({'Femme': 1, 'Homme': 0})

# Imprimer toutes les valeurs de la colonne « Genre ».
print("\nAll values in 'Genre' column:")
print(df['Genre'])

# Imprimer les 3 premières valeurs de la colonne « Genre ».
print("\nLes 3 premières valeurs en 'Genre' column:")
print(df['Genre'].head(3))


# Filter the DataFrame for women in psychological distress
women_distress_df = df[(df['Genre'] == 1) & (df['SCORE_TOTAL_détresse_psychologique_au_travail'] == 1)]

# Count the number of women in psychological distress
num_women_distress = len(women_distress_df)

# Group by sector and count the frequency of women in distress in each sector
sector_distress_freq = women_distress_df.groupby('Secteur_métier').size().reset_index(name='Frequency')

# Display the number of women in psychological distress and the frequency in each sector
print("Number of women in psychological distress:", num_women_distress)
print("\nFrequency of women in psychological distress in each sector:")
print(sector_distress_freq)
