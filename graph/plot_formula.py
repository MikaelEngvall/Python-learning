import numpy as np
import matplotlib.pyplot as plt

# Define the formula y = x^2 - 3x + 2
def formula(x):
    return x**2 - 3*x + 2

# Generate x values (e.g., from -10 to 10)
x = np.linspace(-10, 10, 500)  # 500 points between -10 and 10
y = formula(x)

# Plot the formula
plt.figure(figsize=(8, 6))  # Set figure size
plt.plot(x, y, label=r"$y = x^2 - 3x + 2$", color='blue', linewidth=2)

# Add labels, title, and grid
plt.title("Graph of the Formula", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.axhline(0, color='black',linewidth=0.8, linestyle="--")  # Add x-axis
plt.axvline(0, color='black',linewidth=0.8, linestyle="--")  # Add y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)

# Show the plot
plt.show()
