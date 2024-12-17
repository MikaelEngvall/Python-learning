import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify
import tkinter as tk
from tkinter import messagebox


def plot_parametric(x_formula, y_formula):
    """Plot parametric equations for x(t) and y(t)."""
    t = symbols('t')  # Symbolic variable for sympy

    try:
        # Parse x(t) and y(t) formulas
        x_expr = sympify(x_formula)
        y_expr = sympify(y_formula)

        # Convert formulas to numerical functions
        x_func = lambdify(t, x_expr, modules=["numpy"])
        y_func = lambdify(t, y_expr, modules=["numpy"])

        # Generate t values and evaluate x(t) and y(t)
        t_values = np.linspace(0, 2 * np.pi, 1000)  # Parameter range from 0 to 2π
        x_values = x_func(t_values)
        y_values = y_func(t_values)

        # Plot the parametric curve
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, label=f"Parametric Curve", color='red', linewidth=2)

        # Add labels, title, and grid
        plt.title("Parametric Curve", fontsize=16)
        plt.xlabel("x(t)", fontsize=14)
        plt.ylabel("y(t)", fontsize=14)
        plt.axis('equal')  # Equal scaling for x and y axes
        plt.axhline(0, color='black', linewidth=0.8, linestyle="--")  # x-axis
        plt.axvline(0, color='black', linewidth=0.8, linestyle="--")  # y-axis
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend(fontsize=12)

        # Show the plot
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid parametric equations: {e}")


def on_plot_button():
    """Handle the plot button click event."""
    x_formula = x_formula_entry.get()
    y_formula = y_formula_entry.get()

    if x_formula.strip() and y_formula.strip():
        plot_parametric(x_formula, y_formula)
    else:
        messagebox.showwarning("Input Required", "Please enter both x(t) and y(t) formulas.")


# Create the GUI window
root = tk.Tk()
root.title("Parametric Plotter")
root.geometry("450x300")

# Add input fields for x(t) and y(t)
tk.Label(root, text="Enter x(t):", font=("Arial", 12)).pack(pady=5)
x_formula_entry = tk.Entry(root, width=40, font=("Arial", 12))
x_formula_entry.pack(pady=5)

tk.Label(root, text="Enter y(t):", font=("Arial", 12)).pack(pady=5)
y_formula_entry = tk.Entry(root, width=40, font=("Arial", 12))
y_formula_entry.pack(pady=5)

# Add plot button
plot_button = tk.Button(root, text="Plot Parametric Curve", command=on_plot_button, font=("Arial", 12), bg="blue", fg="white")
plot_button.pack(pady=20)

# Run the GUI main loop
root.mainloop()
