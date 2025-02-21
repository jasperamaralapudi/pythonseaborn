import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset("iris")

# Create a KDE plot
sns.kdeplot(x="sepal_width", y="sepal_length", hue="species", data=iris, fill=True, palette="viridis")

# Customize the plot
plt.title("KDE Plot of Sepal Width vs Sepal Length (Colored by Species)")
plt.xlabel("Sepal Width")
plt.ylabel("Sepal Length")
plt.legend(title="Species")
plt.show()