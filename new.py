import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Read your data into a pandas DataFrame
# Replace 'your_data.xlsx' with the path to your data file
df = pd.read_excel('C:/Users/User/Downloads/work.xlsx')

X = df.drop(columns=[df.columns[1], df.columns[7]])  # Drop columns at positions 1 and 7
y_harassment = df[df.columns[1]]  # Assuming the target column for harassment is at position 1
y_distress = df[df.columns[7]]  # Assuming the target column for distress is at position 7

# Split the data into training and testing sets for harassment
X_train_harassment, X_test_harassment, y_train_harassment, y_test_harassment = train_test_split(X, y_harassment, test_size=0.2, random_state=42)

# Train the Gradient Boosting classifier for harassment
gb_classifier_harassment = GradientBoostingClassifier()
gb_classifier_harassment.fit(X_train_harassment, y_train_harassment)

# Split the data into training and testing sets for distress
X_train_distress, X_test_distress, y_train_distress, y_test_distress = train_test_split(X, y_distress, test_size=0.2, random_state=42)

# Train the Gradient Boosting classifier for distress
gb_classifier_distress = GradientBoostingClassifier()
gb_classifier_distress.fit(X_train_distress, y_train_distress)

# Predictions for harassment
harassment_predictions = gb_classifier_harassment.predict(X_test_harassment)

# Predictions for distress
distress_predictions = gb_classifier_distress.predict(X_test_distress)

# Evaluate the performance for harassment
harassment_accuracy = accuracy_score(y_test_harassment, harassment_predictions)

# Evaluate the performance for distress
distress_accuracy = accuracy_score(y_test_distress, distress_predictions)

print("Accuracy for harassment:", harassment_accuracy)
print("Accuracy for distress:", distress_accuracy)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Create a heatmap of the correlation matrix (showing only lower triangle)
plt.figure(figsize=(10, 8))
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", mask=mask, annot_kws={"size": 8})
plt.title('Heatmap of Pearson Correlation Coefficient Matrix (Lower Triangle)')
plt.show()

# Extract the lower triangle of the correlation matrix
lower_triangle = correlation_matrix.where(np.tril(np.ones(correlation_matrix.shape), k=-1).astype(np.bool))

# Convert the lower triangle into a DataFrame
correlation_table = lower_triangle.stack().reset_index()
correlation_table.columns = ['Variable 1', 'Variable 2', 'Correlation']

# Display the correlation table
print("Correlation Table:")
print(correlation_table)