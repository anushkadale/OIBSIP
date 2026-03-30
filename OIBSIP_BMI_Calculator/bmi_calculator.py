import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "#3498db"
        elif bmi < 24.9:
            category = "Normal weight"
            color = "#2ecc71"
        elif bmi < 29.9:
            category = "Overweight"
            color = "#f39c12"
        else:
            category = "Obese"
            color = "#e74c3c"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}",
            fg=color
        )

    except:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")


def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")


# Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("420x420")
root.config(bg="#1e272e")


# Title
title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Helvetica", 22, "bold"),
    bg="#1e272e",
    fg="#f5f6fa"
)
title_label.pack(pady=20)


# Weight
weight_label = tk.Label(
    root,
    text="Enter Weight (kg)",
    font=("Arial", 12),
    bg="#1e272e",
    fg="white"
)
weight_label.pack()

weight_entry = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center"
)
weight_entry.pack(pady=5)


# Height
height_label = tk.Label(
    root,
    text="Enter Height (meters)",
    font=("Arial", 12),
    bg="#1e272e",
    fg="white"
)
height_label.pack()

height_entry = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center"
)
height_entry.pack(pady=5)


# Buttons
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial", 12, "bold"),
    bg="#00cec9",
    fg="white",
    padx=10,
    pady=5,
    command=calculate_bmi
)
calculate_button.pack(pady=15)


clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 11),
    bg="#d63031",
    fg="white",
    command=clear_fields
)
clear_button.pack()


# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#1e272e"
)
result_label.pack(pady=25)


root.mainloop()