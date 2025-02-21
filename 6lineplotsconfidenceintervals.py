import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
fmri = sns.load_dataset("fmri")

# Create a line plot
sns.lineplot(x="timepoint", y="signal", hue="region", style="event", data=fmri, ci=95)

# Customize the plot
plt.title("FMRI Signal Over Time (by Region and Event)")
plt.xlabel("Timepoint")
plt.ylabel("Signal")
plt.legend(title="Region/Event")
plt.show()