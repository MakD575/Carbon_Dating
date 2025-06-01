import tkinter as tk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_age():
    try:
        ratio = float(entry.get())

        if not 0 < ratio <= 1:
            messagebox.showerror("Invalid Input", "The ratio must be a number between 0 and 1.")
            return

        half_life = 5730  # years
        decay_constant = math.log(2) / half_life

        age = -math.log(ratio) / decay_constant
        result_label.config(text=f"Estimated Age: {age:.2f} years")

        times = np.linspace(0, 50000, 500)
        ratios = np.exp(-decay_constant * times)

        plt.figure(figsize=(8, 5))
        plt.plot(times, ratios, label="C-14 Decay Curve", color="blue")
        plt.axhline(y=ratio, color="red", linestyle="--", label=f"Input Ratio = {ratio}")
        plt.axvline(x=age, color="green", linestyle="--", label=f"Estimated Age ≈ {age:.0f} yrs")

        plt.scatter([age], [ratio], color="black", zorder=5)
        plt.title("Carbon-14 Decay Over Time")
        plt.xlabel("Years")
        plt.ylabel("C-14/C-12 Ratio")
        plt.ylim(0, 1.05)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Carbon Dating Calculator")
root.geometry("350x200")
root.resizable(False, False)

# Input label and entry
label = tk.Label(root, text="Enter C-14/C-12 ratio (0 < ratio ≤ 1):")
label.pack(pady=10)

entry = tk.Entry(root, width=20, justify='center')
entry.pack()

# Calculate button
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start GUI event loop
root.mainloop()