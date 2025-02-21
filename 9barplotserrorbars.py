import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
titanic = sns.load_dataset("titanic")

# Create a bar plot
sns.barplot(x="class", y="fare", hue="sex", data=titanic, ci="sd", palette="coolwarm")

# Customize the plot
plt.title("Average Fare by Class and Gender (with Standard Deviation)")
plt.xlabel("Class")
plt.ylabel("Fare ($)")
plt.legend(title="Gender")
plt.show()