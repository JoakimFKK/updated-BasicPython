import tkinter as tk

def convert(celcius_input):
    try:
        celcius = float(celcius_input)
    except TypeError:
        result_label.config(text="Invalid")

window = tk.Tk()
window.resizable(width=False, height=False)

input_frame = tk.Frame(master=window)
input_frame.pack(
    side=tk.LEFT,
    padx=5,
    pady=5,
    )

output_frame = tk.Frame(master=window)
output_frame.pack(side=tk.LEFT,
    padx=5,
    pady=5
    )

# Output frame widgets.
celcius_txt = tk.Entry(master=input_frame)
celcius_txt.grid(row=0,column=1)

result_label = tk.Label(master=output_frame)
result_label.grid(row=1, column=1)
# float(celcius) * (9 / 5) + 32
convert_button = tk.Button(
    master=output_frame,
    command=convert(celcius_txt),
    text="Convert"
    )
convert_button.grid(row=0, column=2)

# Input frame widgets
celcius_label = tk.Label(master=input_frame, text="Celcius")
celcius_label.grid(row=0, column=0)


window.mainloop()