import numpy as np
import matplotlib.pyplot as plt

# Data
data = [10, 80, 30, 40, 50, 20, 70, 60, 90, 100]

# Sort data
sorted_data = np.sort(data)

# Calculate percentiles
q25 = np.quantile(sorted_data, 0.25)
q50 = np.quantile(sorted_data, 0.50)
q75 = np.quantile(sorted_data, 0.75)

# Calculate cumulative quantiles
quantiles = np.linspace(0, 1, len(sorted_data))

# Plot
plt.figure(figsize=(8, 5))
plt.plot(quantiles, sorted_data, marker='o', label='Data Quantiles')

# Mark Q1, Q2, Q3
plt.axhline(y=q25, color='red', linestyle='--', label='25th percentile (Q1)')
plt.axhline(y=q50, color='green', linestyle='--', label='50th percentile (Median)')
plt.axhline(y=q75, color='blue', linestyle='--', label='75th percentile (Q3)')

# Labels and title
plt.title('Quantile Plot with 25th, 50th, and 75th Percentiles')
plt.xlabel('Quantiles (0 to 1)')
plt.ylabel('Data Values')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Print percentiles
print(f"25th percentile: {q25}")
print(f"50th percentile (median): {q50}")
print(f"75th percentile: {q75}")

