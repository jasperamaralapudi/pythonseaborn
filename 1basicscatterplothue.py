import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset("tips")

# Create a scatter plot
sns.scatterplot(x="total_bill", y="tip", hue="sex", style="time", data=tips)

# Customize the plot
plt.title("Total Bill vs Tip (Colored by Gender and Meal Time)")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.legend(title="Gender")
plt.show()