import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset("tips")

# Create a box plot
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips)

# Add annotations
plt.title("Total Bill Distribution by Day and Gender")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.legend(title="Gender")
plt.show()