import tkinter as tk
from tkinter import messagebox
import pyperclip

def remove_duplicates():
    all_cities = []
    for textbox in input_textboxes:
        cities = [city.split(',')[0].strip().strip('"').title() for city in textbox.get("1.0", tk.END).splitlines()]
        all_cities.extend(cities)
    
    unique_cities = set(all_cities)
    
    # Find duplicates
    duplicates = set([city for city in all_cities if all_cities.count(city) > 1])
    
    # Update text boxes
    textbox_output.delete("1.0", tk.END)
    textbox_output.insert(tk.END, "\n".join(sorted(unique_cities)))
    
    textbox_duplicates.delete("1.0", tk.END)
    textbox_duplicates.insert(tk.END, "\n".join(sorted(duplicates)))
    
    # Update duplicates counter
    duplicates_counter.config(text=f"Total Duplicates: {len(duplicates)}")
    duplicates_count_textbox.delete("1.0", tk.END)
    duplicates_count_textbox.insert(tk.END, str(len(duplicates)))

def show_about():
    messagebox.showinfo("About", "City Duplicate Remover\nVersion 1.0\nBy Your Name")

def clear_all():
    for textbox in input_textboxes:
        textbox.delete("1.0", tk.END)
    textbox_output.delete("1.0", tk.END)
    textbox_duplicates.delete("1.0", tk.END)
    duplicates_count_textbox.delete("1.0", tk.END)
    
    # Clear duplicates counter
    duplicates_counter.config(text="")

def copy_to_clipboard():
    output_text = textbox_output.get("1.0", tk.END)
    pyperclip.copy(output_text)

root = tk.Tk()
root.title("City Duplicate Remover")

# Menu
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)
help_menu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

# Input text boxes
input_textboxes = []
for i in range(1, 5):
    label = tk.Label(root, text=f"City Input Box {i}")
    label.grid(row=i, column=0, padx=10, pady=5)
    
    input_textbox = tk.Text(root, height=10, width=30)
    input_textbox.grid(row=i, column=1, padx=10, pady=5)
    input_textboxes.append(input_textbox)

# Remove duplicates button
remove_duplicates_button = tk.Button(root, text="Remove Duplicates", command=remove_duplicates)
remove_duplicates_button.grid(row=5, column=0, padx=10, pady=10)

# Clear button
clear_button = tk.Button(root, text="Clear All", command=clear_all)
clear_button.grid(row=5, column=1, padx=10, pady=10)

# Copy button
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=5, column=2, padx=10, pady=10)

# Output labels
output_label = tk.Label(root, text="Unique Cities")
output_label.grid(row=0, column=3, padx=10, pady=5)

duplicates_label = tk.Label(root, text="Duplicate Cities")
duplicates_label.grid(row=3, column=3, padx=10, pady=5)

# Output text boxes
textbox_output = tk.Text(root, height=20, width=30)
textbox_output.grid(row=1, column=3, rowspan=2, padx=10, pady=10)

textbox_duplicates = tk.Text(root, height=10, width=30)
textbox_duplicates.grid(row=4, column=3, rowspan=2, padx=10, pady=10)

# Duplicates counter
duplicates_counter = tk.Label(root, text="")
duplicates_counter.grid(row=6, column=3, padx=10, pady=5, sticky=tk.E)

# Duplicates count text box
duplicates_count_textbox = tk.Text(root, height=1, width=10)
duplicates_count_textbox.grid(row=6, column=4, padx=10, pady=5)

root.mainloop()
