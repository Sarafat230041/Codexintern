import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set a consistent theme for the plots
sns.set_theme(style="whitegrid", palette="viridis")

# 1. Load the dataset from the URL
URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
df = pd.read_csv(URL)

# Quick health-check to inspect the data
print(f"Shape: {df.shape}\n{df.head()}")

# 2. Core Statistics
target = "median_house_value"
print(f"\n--- Core Statistics for '{target}' ---")
print(f"Average: ${df[target].mean():,.0f}")
print(f"Median : ${df[target].median():,.0f}")
print(f"Std-Dev: ${df[target].std():,.0f}")

# 3. Average price by proximity to ocean
avg_by_ocean = df.groupby("ocean_proximity")[target].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 4))
sns.barplot(x=avg_by_ocean.index, y=avg_by_ocean.values)
plt.title("Ocean Proximity vs. Median House Value")
plt.ylabel("Mean Value ($)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# 4. Overall distribution of median house values
plt.figure(figsize=(10, 6))
sns.histplot(df[target], bins=30, kde=True, color="teal")
plt.title("Distribution of Median House Values")
plt.xlabel("Value ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 5. Rooms vs. Value, color-coded by ocean proximity
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x="total_rooms", y=target,
                 hue="ocean_proximity", alpha=0.5)
plt.title("Total Rooms vs. Median House Value")
plt.xlabel("Total Rooms")
plt.ylabel("Median House Value ($)")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()

# 6. Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Feature Correlations")
plt.tight_layout()
plt.show()