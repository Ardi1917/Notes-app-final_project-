import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Add Notes")
root.geometry("600x600")
root.resizable(0, 0)

root.columnconfigure(0, weight=4)
root.columnconfigure(1, weight=4)
root.columnconfigure(2, weight=4)
root.columnconfigure(3, weight=4)
root.columnconfigure(4, weight=4)

def add_note():
    note = entry.get()
    if note:
        listbox.insert(tk.END, note)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Note cannot be empty!")

def delete_note():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a note to delete!")

def edit_note():
    try:
        selected = listbox.curselection()
        new_note = entry.get()
        if new_note:
            listbox.delete(selected)
            listbox.insert(selected, new_note)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter text to edit!")
    except:
        messagebox.showwarning("Warning", "Select a note to edit!")


entry = tk.Entry(root, width=40)
entry.grid(row=1, column=2, padx=20, pady=20)

add_btn = tk.Button(root, text="Add Note", width=10, command=add_note, bg='darkgreen',
    fg='white')
add_btn.grid(row=4, column=1, padx=15, pady=15)

edit_btn = tk.Button(root, text="Edit Note", width=10, command=edit_note, bg='Gold',
    fg='white')
edit_btn.grid(row=4, column=3, padx=15, pady=15)

delete_btn = tk.Button(root, text="Delete Note", width=10, command=delete_note, bg='crimson',
    fg='white')
delete_btn.grid(row=4, column=2, padx=15, pady=15)

listbox = tk.Listbox(root, width=50, height=10,)
listbox.grid(row=8, column=2, padx=15, pady=15)


root.mainloop()
