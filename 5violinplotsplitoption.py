import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset("tips")

# Create a violin plot
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True, palette="pastel")

# Customize the plot
plt.title("Total Bill Distribution by Day and Gender")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.legend(title="Gender")
plt.show()