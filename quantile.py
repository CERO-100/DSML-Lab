import numpy as np

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Calculate 25th, 50th, and 75th percentiles
q25 = np.quantile(data, 0.25)
q50 = np.quantile(data, 0.50)  # median
q75 = np.quantile(data, 0.75)

print(f"25th percentile: {q25}")
print(f"50th percentile (median): {q50}")
print(f"75th percentile: {q75}")
