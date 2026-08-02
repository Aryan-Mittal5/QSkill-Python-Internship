import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("students.csv")

# Display first 5 rows
print("Dataset:")
print(df.head())
  
# Basic Information
print("\nDataset Information:")
print(df.info())

# Descriptive Statistics
print("\nStatistics:")
print(df.describe())

# Calculate Average of Math column
average_math = df["Math"].mean()
print("\nAverage Math Marks:", average_math)


# Bar Chart

plt.figure(figsize=(6,4))
plt.bar(df["Name"], df["Math"])
plt.title("Math Marks of Students")
plt.xlabel("Students")
plt.ylabel("Math Marks")
plt.savefig("bar_chart.png")
plt.show()

# Scatter Plot

plt.figure(figsize=(6,4))
plt.scatter(df["Math"], df["Science"])
plt.title("Math vs Science Marks")
plt.xlabel("Math")
plt.ylabel("Science")
plt.savefig("scatter_plot.png")
plt.show()

# Heatmap (Correlation Matrix)

correlation = df[["Math", "Science", "English"]].corr()

plt.figure(figsize=(5,4))
plt.imshow(correlation, cmap="coolwarm", interpolation="nearest")
plt.colorbar()

subjects = ["Math", "Science", "English"]
plt.xticks(range(len(subjects)), subjects)
plt.yticks(range(len(subjects)), subjects)

plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()