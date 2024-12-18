import matplotlib.pyplot as plt

# Data
x = [0, 1, 2, 3, 4, 5]  # X-axis values
y = [0, 1, 4, 9, 16, 25]  # Y-axis values (y = x^2)

# Create a figure and axis object
plt.figure(figsize=(8, 6))

# Plot the data
plt.plot(x, y, label="y = x^2", color='blue', marker='o')

# Add title and labels
plt.title("Simple Line Plot", fontsize=14)
plt.xlabel("X-Axis", fontsize=12)
plt.ylabel("Y-Axis", fontsize=12)

# Add a grid for better visibility
plt.grid(True)

# Add a legend to the plot
plt.legend()

# Show the plot
plt.show()
