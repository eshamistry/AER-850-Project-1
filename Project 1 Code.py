# Step 1
import pandas as pd

df = pd.read_csv("Project 1 Data.csv")


# Step 2
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


groups = df.groupby('Step')
   
 
fig = plt.figure(num = 1, figsize = (18, 18))
ax = fig.add_subplot(111, projection='3d')

colors = {1: 'r', 2: 'g', 3: 'b', 4: 'yellow', 5: 'c', 6: 'm', 7: 'orange', 8: 'pink', 9: 'tan', 10: 'sienna', 11: 'purple', 12: 'springgreen', 13: 'skyblue'}

for Step, group_data in groups:
    ax.scatter(group_data['X'], group_data['Y'], group_data['Z'], c=colors[Step], label=Step, marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot Based on Groups')
ax.legend()
plt.show()


stats = groups['X', 'Y', 'Z'].agg(['mean', 'std', 'count'])


plt.figure(num = 2, figsize = (12, 6))
for column in ['X', 'Y', 'Z']:
    plt.scatter(stats.index, stats[column]['mean'], label=column)

plt.xlabel('Step')
plt.ylabel('Mean Value')
plt.title('Mean Values of X, Y, and Z by Step')
plt.legend()
plt.grid(True)
plt.show()


plt.figure(num = 3, figsize = (12, 6))
for column in ['X', 'Y', 'Z']:
    plt.plot(stats.index, stats[column]['std'], label=column)

plt.xlabel('Step')
plt.ylabel('Standard Value')
plt.title('Standard Values of X, Y, and Z by Step')
plt.legend()
plt.grid(True)
plt.show()


plt.figure(num = 4, figsize = (12, 6))
for column in ['X', 'Y', 'Z']:
    plt.scatter(stats.index, stats[column]['count'], label=column)

plt.xlabel('Step')
plt.ylabel('Count Value')
plt.title('Count Values of X, Y, and Z by Step')
plt.legend()
plt.grid(True)
plt.show()


# Step 3
import seaborn as sns

correlations = []

for name, group in groups:
    correlation_matrix = group[['X', 'Y', 'Z']].corr(method='pearson')
    correlations.append((name, correlation_matrix))

for step, matrix in correlations:
    print(f"Step {step}:")
    print(matrix)
    print()
    
num_subplots = len(correlations)
cols = 2  # Number of columns in the subplot grid
rows = (num_subplots + cols - 1) // cols  # Calculate the number of rows needed

plt.figure(figsize=(40, 60))
for i, (step, matrix) in enumerate(correlations, 1):
    plt.subplot(rows, cols, i)
    sns.heatmap(matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title(f'Correlation Matrix for Step {step}')

plt.tight_layout()  # Adjust subplot layout
plt.show()


