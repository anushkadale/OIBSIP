import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


def generate_password():

    length = int(length_entry.get())

    characters = ""

    if var_letters.get():
        characters += string.ascii_letters

    if var_numbers.get():
        characters += string.digits

    if var_symbols.get():
        characters += string.punctuation


    if characters == "":
        messagebox.showwarning("Warning", "Select at least one option")
        return


    password = ''.join(random.choice(characters) for i in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate password first")
        return

    pyperclip.copy(password)
    messagebox.showinfo("Success", "Password copied to clipboard!")


# GUI window

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.config(bg="#1e272e")


title = tk.Label(root,
                 text="🔐 Password Generator",
                 font=("Arial", 18, "bold"),
                 fg="white",
                 bg="#1e272e")

title.pack(pady=10)


length_label = tk.Label(root,
                        text="Password Length:",
                        fg="white",
                        bg="#1e272e")

length_label.pack()


length_entry = tk.Entry(root)
length_entry.pack(pady=5)


var_letters = tk.IntVar()
var_numbers = tk.IntVar()
var_symbols = tk.IntVar()


letters_check = tk.Checkbutton(root,
                               text="Include Letters",
                               variable=var_letters,
                               bg="#1e272e",
                               fg="white")

letters_check.pack()


numbers_check = tk.Checkbutton(root,
                               text="Include Numbers",
                               variable=var_numbers,
                               bg="#1e272e",
                               fg="white")

numbers_check.pack()


symbols_check = tk.Checkbutton(root,
                               text="Include Symbols",
                               variable=var_symbols,
                               bg="#1e272e",
                               fg="white")

symbols_check.pack()


generate_btn = tk.Button(root,
                         text="Generate Password",
                         command=generate_password,
                         bg="#05c46b",
                         fg="white",
                         font=("Arial", 12))

generate_btn.pack(pady=10)


password_entry = tk.Entry(root,
                          font=("Arial", 14),
                          justify="center")

password_entry.pack(pady=10)


copy_btn = tk.Button(root,
                     text="Copy Password",
                     command=copy_password,
                     bg="#ffa801",
                     fg="white",
                     font=("Arial", 12))

copy_btn.pack()


root.mainloop()