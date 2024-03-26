import tkinter as tk

from tkinter import ttk, filedialog
from components.data_generator import generate_data, save_data_to_excel

def on_submit():
  print(entry.get())

def on_save():
  num_data = int(entry.get())
  data = generate_data(num_data)
  wb = save_data_to_excel(data)

  file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                           filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
  if file_path:
    wb.save(file_path)
    print(f"Data saved to {file_path}")

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")

label = ttk.Label(root, text="Enter something: ")
label.pack(pady=10)

entry = ttk.Entry(root)
entry.pack()

submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

save_button = ttk.Button(root, text="Save to Excel", command=on_save)
save_button.pack(pady=10)

root.mainloop()