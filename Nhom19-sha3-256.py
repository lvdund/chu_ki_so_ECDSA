# Nhom 19 - Demo SHA3 256
import hashlib
import tkinter as tk
from tkinter import ttk

# Generate root instance
root = tk.Tk()
root.title("Nhom 19 - Demo SHA3 256")
root.geometry("500x80")


def execute():
    str = message.get()
    hash_sha3_256 = hashlib.new("sha3_256", str.encode())
    label_hash.configure(text=f"Hashed message: {hash_sha3_256.hexdigest()}")


# UI
label_hello = ttk.Label(master=root)
label_hello.configure(text='Enter message')
label_hello.place(x=10, y=10)

message = tk.StringVar()
entry_message = ttk.Entry(master=root)
entry_message.configure(textvariable=message)
entry_message.place(x=100, y=10)

button_execute = ttk.Button(master=root)
button_execute.configure(text="Hash with SHA3 256", command=execute)
button_execute.place(x=230, y=10)

label_hash = ttk.Label(master=root)
label_hash.configure(text='Please input message to hash')
label_hash.place(x=10, y=40)

root.mainloop()
