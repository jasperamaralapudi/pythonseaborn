import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset("iris")
iris_numeric = iris.drop("species", axis=1)  # Remove non-numeric column

# Create a clustermap
sns.clustermap(iris_numeric, cmap="coolwarm", standard_scale=1, figsize=(8, 6))

# Add title
plt.suptitle("Clustermap of Iris Dataset (Standardized)", y=1.02)
plt.show()