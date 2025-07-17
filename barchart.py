import matplotlib.pyplot as plt

# Sample data
categories = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
values = [10, 15, 7, 12, 5]

# Create bar chart
plt.bar(categories, values, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Fruit')
plt.ylabel('Quantity')
plt.title('Fruit Quantity Bar Chart')

# Show plot
plt.show()
