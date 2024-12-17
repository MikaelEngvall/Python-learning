import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify

# Function to dynamically input and plot a formula
def plot_custom_formula():
    x = symbols('x')  # Symbolic variable for sympy

    # Prompt the user to input a formula
    formula_input = input("Enter a formula in terms of x (e.g., x**2 - 3*x + 2): ")

    try:
        # Parse the formula
        formula = sympify(formula_input)
        print(f"The formula you entered: {formula}")

        # Convert the formula to a numerical function
        formula_func = lambdify(x, formula, modules=["numpy"])

        # Generate x values and evaluate y values
        x_values = np.linspace(-10, 10, 500)  # 500 points from -10 to 10
        y_values = formula_func(x_values)

        # Plot the formula
        plt.figure(figsize=(8, 6))  # Set figure size
        plt.plot(x_values, y_values, label=f"$y = {formula}$", color='blue', linewidth=2)

        # Add labels, title, and grid
        plt.title("Graph of the Formula", fontsize=16)
        plt.xlabel("x", fontsize=14)
        plt.ylabel("y", fontsize=14)
        plt.axhline(0, color='black', linewidth=0.8, linestyle="--")  # Add x-axis
        plt.axvline(0, color='black', linewidth=0.8, linestyle="--")  # Add y-axis
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend(fontsize=12)

        # Show the plot
        plt.show()
    except Exception as e:
        print(f"Error: {e}. Please enter a valid formula in terms of x.")

# Run the function
plot_custom_formula()
