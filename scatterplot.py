import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5,5, 7, 6, 8]
y = [5, 7, 6, 8, 1, 2, 3, 4, 5]

# Create scatter plot
plt.scatter(x, y, color='blue', marker='x')

# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Scatter Plot')

# Show grid and plot
plt.grid(True)
plt.show()
