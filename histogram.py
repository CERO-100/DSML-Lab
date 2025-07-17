import matplotlib.pyplot as plt
import numpy as np
# Sample data
data =np.random.randn(1000)

# Create histogram
plt.hist(data, bins=17, color='green', edgecolor='black')

# Add labels and title
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.title('Histogram')

# Show plot
plt.show()
