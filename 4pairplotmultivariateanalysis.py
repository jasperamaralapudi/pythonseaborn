import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset("iris")

# Create a pair plot
sns.pairplot(iris, hue="species", palette="Set2")

# Add title
plt.suptitle("Pair Plot of Iris Dataset (Colored by Species)", y=1.02)
plt.show()