import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Parameters for synthetic data
num_students = 395
grades = np.random.randint(0, 21, size=(num_students, 3))  # Grades between 0 and 20 for G1, G2, G3
ages = np.random.randint(15, 23, size=num_students)  # Ages between 15 and 22
sex = np.random.choice(['M', 'F'], size=num_students)  # Randomly assign gender
address = np.random.choice(['U', 'R'], size=num_students)  # Urban or Rural
famsize = np.random.choice(['GT3', 'LE3'], size=num_students)  # Family size
Medu = np.random.randint(0, 5, size=num_students)  # Mother's education (0-4)
Fedu = np.random.randint(0, 5, size=num_students)  # Father's education (0-4)
absences = np.random.randint(0, 76, size=num_students)  # Absences between 0 and 75

# Create a DataFrame
data = pd.DataFrame({
    'Student ID': range(1, num_students + 1),
    'sex': sex,
    'age': ages,
    'address': address,
    'famsize': famsize,
    'Medu': Medu,
    'Fedu': Fedu,
    'absences': absences,
    'G1': grades[:, 0],
    'G2': grades[:, 1],
    'G3': grades[:, 2]
})

# Display the first few rows of the dataset
print(data.head())

# Visualization 1: Average Grades by Gender
plt.figure(figsize=(12, 6))
data_melted = data.melt(id_vars=['sex'], value_vars=['G1', 'G2', 'G3'], 
                         var_name='Grade', value_name='Score')
sns.barplot(x='Grade', y='Score', hue='sex', data=data_melted, ci=None)
plt.title('Average Grades by Gender')
plt.ylabel('Average Score')
plt.xlabel('Grade')
plt.ylim(0, 20)  # Assuming grades are out of 20
plt.show()

# Visualization 2: Scores Distribution for Each Grade
plt.figure(figsize=(12, 6))
sns.histplot(data=data, x='G3', bins=10, kde=True, color='blue', label='Final Grade (G3)', alpha=0.5)
sns.histplot(data=data, x='G2', bins=10, kde=True, color='green', label='Second Period Grade (G2)', alpha=0.5)
sns.histplot(data=data, x='G1', bins=10, kde=True, color='orange', label='First Period Grade (G1)', alpha=0.5)
plt.title('Score Distribution by Grade')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.legend()
plt.xlim(0, 20)
plt.show()

# Visualization 3: Box Plot of Grades by Gender
plt.figure(figsize=(12, 6))
data_melted_box = data.melt(id_vars=['sex'], value_vars=['G1', 'G2', 'G3'], 
                              var_name='Grade', value_name='Score')
sns.boxplot(x='Grade', y='Score', data=data_melted_box, hue='sex', dodge=True)
plt.title('Box Plot of Grades by Gender')
plt.ylabel('Score')
plt.xlabel('Grade')
plt.ylim(0, 20)
plt.show()
