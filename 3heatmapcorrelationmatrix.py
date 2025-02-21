import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

# Create a heatmap
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")

# Customize the plot
plt.title("Passenger Count Heatmap (Year vs Month)")
plt.xlabel("Year")
plt.ylabel("Month")
plt.show()