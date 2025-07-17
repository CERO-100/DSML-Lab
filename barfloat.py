import matplotlib.pyplot as plt

# Sample data: each item is (category, low value, high value)
data = [
    ("A", 2, 5),
    ("B", 4, 9),
    ("C", 1, 6),
    ("D", 7, 10),
    ("E", 2, 5),
    ("F", 4, 9),
    ("G", 1, 6),
    ("H", 7, 10),
]

# Prepare values
categories = [item[0] for item in data]
lows = [item[1] for item in data]
highs = [item[2] for item in data]
heights = [highs[i] - lows[i] for i in range(len(data))]

# Create floating bars
plt.bar(categories, heights, bottom=lows, color="skyblue", edgecolor="black")

# Add labels and title
plt.xlabel("Category")
plt.ylabel("Value Range")
plt.title("Floating Bar Chart (Barfloat)")

# Optionally, add grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.tight_layout()
plt.show()
