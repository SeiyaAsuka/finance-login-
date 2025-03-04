# MIT License
#
# Copyright (c) 2025 Seiya Genda
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import tkinter as tk
from tkinter import messagebox
import csv
import os

CSV_FILE = "name_list.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "NUID", "Password"])


def validate_login(first_name, last_name, nuid, password):
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row == [first_name, last_name, nuid, password]:
                return True
    return False


def register_user(first_name, last_name, nuid, password):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([first_name, last_name, nuid, password])


def open_chapter_selection():
    chapter_window = tk.Toplevel(root)
    chapter_window.title("Chapter Selection")
    chapter_window.geometry("600x400")

    tk.Label(chapter_window, text="Select a Chapter", font=("Arial", 14)).pack(pady=10)

    valid_chapters = [str(i) for i in range(2, 15) if i != 11]
    for chapter in valid_chapters:
        tk.Button(chapter_window, text=f"Chapter {chapter}",
                  command=lambda c=chapter: messagebox.showinfo("Selected", f"Chapter {c} Selected")).pack(pady=3)


def register_screen():
    register_window = tk.Toplevel(root)
    register_window.title("New User Registration")
    register_window.geometry("500x500")

    tk.Label(register_window, text="Register New User", font=("Arial", 14)).pack(pady=10)

    tk.Label(register_window, text="First Name").pack()
    entry_first = tk.Entry(register_window)
    entry_first.pack()

    tk.Label(register_window, text="Last Name").pack()
    entry_last = tk.Entry(register_window)
    entry_last.pack()

    tk.Label(register_window, text="NUID").pack()
    entry_nuid = tk.Entry(register_window)
    entry_nuid.pack()

    tk.Label(register_window, text="Password").pack()
    entry_password = tk.Entry(register_window, show="*")
    entry_password.pack()

    def register_action():
        first_name = entry_first.get()
        last_name = entry_last.get()
        nuid = entry_nuid.get()
        password = entry_password.get()

        if not all([first_name, last_name, nuid, password]):
            messagebox.showerror("Error", "All fields are required!")
            return

        register_user(first_name, last_name, nuid, password)
        messagebox.showinfo("Success", "User registered successfully!")
        register_window.destroy()
        open_chapter_selection()

    tk.Button(register_window, text="Register", bg="#FFD700", command=register_action).pack(pady=10)


def login_screen():
    root.configure(bg="#2E3B4E")

    frame = tk.Frame(root, bg="#3E4A5A", bd=3, relief="ridge")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Login", font=("Arial", 16, "bold"), fg="#FFD700", bg="#3E4A5A").pack(pady=10)

    tk.Label(frame, text="First Name:", fg="white", bg="#3E4A5A").pack()
    entry_first = tk.Entry(frame)
    entry_first.pack()

    tk.Label(frame, text="Last Name:", fg="white", bg="#3E4A5A").pack()
    entry_last = tk.Entry(frame)
    entry_last.pack()

    tk.Label(frame, text="NUID:", fg="white", bg="#3E4A5A").pack()
    entry_nuid = tk.Entry(frame)
    entry_nuid.pack()

    tk.Label(frame, text="Password:", fg="white", bg="#3E4A5A").pack()
    entry_password = tk.Entry(frame, show="*")
    entry_password.pack()

    def login_action():
        first_name = entry_first.get()
        last_name = entry_last.get()
        nuid = entry_nuid.get()
        password = entry_password.get()

        if validate_login(first_name, last_name, nuid, password):
            messagebox.showinfo("Login Success", "Welcome!")
            open_chapter_selection()
        else:
            messagebox.showwarning("Login Failed", "User not found. Please register.")

    tk.Button(frame, text="Login", bg="#FFD700", fg="black", command=login_action).pack(pady=5)
    tk.Button(frame, text="Click Here For First Time ", bg="#2E8B57", fg="white", command=register_screen).pack(pady=5)

root = tk.Tk()
root.title("User Login")
root.geometry("500x400")

login_screen()

root.mainloop()
