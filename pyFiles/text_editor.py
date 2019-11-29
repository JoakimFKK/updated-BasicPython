import tkinter as tk
from tkinter import filedialog

# functions
def clear_text_box():
    """Clear all text in the text box"""
    text_box.delete(1.0, tk.END)
    window.title("Simple text editor")

def open_file():
    """Open a file for editing."""
    filepath = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath: return
    clear_text_box()
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_box.insert(tk.END, text)
    window.title(f"Simple text editor - {filepath}")

def save_file_as():
    """Save the current file as a new file."""
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text file", "*.txt")],
    )
    if not filepath: return

    with open(filepath, "w") as output_file:
        text = text_box.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple text editor - {filepath}")

    

# 1
window = tk.Tk()
window.title("Simple text editor")
window.geometry("800x400")

# 2
button_frame = tk.Frame(
    master = window,
    width = 50,
    relief = tk.GROOVE,
    borderwidth = 2
    )
button_frame.pack(
    side = tk.LEFT,
    fill = tk.Y
    )
# 3
text_frame = tk.Frame(
    master = window,
    relief = tk.GROOVE,
    borderwidth = 2
    )
text_frame.pack(
    side = tk.LEFT,
    fill = tk.BOTH,
    expand = True
    )

# 4
open_button = tk.Button(
    master=button_frame,
    text = "Open",
    command=open_file
    )
open_button.pack(
    fill = tk.X,
    padx = 5,
    pady = 5
    )

save_as_button = tk.Button(
    master=button_frame,
    text="Save as...",
    command=save_file_as,
    )
save_as_button.pack(
    fill = tk.X,
    padx = 5,
    pady = 5
    )

clear_button = tk.Button(
    master=button_frame,
    text="Clear",
    command = clear_text_box
    )
clear_button.pack(
    fill = tk.X,
    padx = 5,
    pady = 5
    )

text_box = tk.Text(master=text_frame)
text_box.pack(
    fill=tk.BOTH,
    expand=True
    )

window.mainloop()