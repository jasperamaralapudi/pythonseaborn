import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset("tips")

# Create a FacetGrid
g = sns.FacetGrid(tips, col="time", row="smoker", hue="sex")
g.map(sns.scatterplot, "total_bill", "tip")

# Add titles and legends
g.add_legend()
g.set_axis_labels("Total Bill ($)", "Tip ($)")
plt.suptitle("Total Bill vs Tip (Faceted by Time and Smoker)", y=1.02)
plt.show()