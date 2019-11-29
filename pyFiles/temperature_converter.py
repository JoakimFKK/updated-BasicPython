import tkinter as tk

def convert_to_fahrenheit(celcius, digits=3):
    """Convert celcius to fahrenheit and round to whole numbers."""
    fahrenheit = float(celcius) * (9 / 5) + 32
    rounded = round(fahrenheit, digits)
    return rounded

def convert():
    celcius = celcius_entry.get()
    try:
        result = str(convert_to_fahrenheit(celcius))
    except ValueError:
        result = "Invalid"
    result_display.config(text=result)

### Start!
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

input_frame = tk.Frame(master=window)
button_frame = tk.Frame(master=window)
input_frame.pack(side=tk.LEFT, padx=5, pady=5)
button_frame.pack(side=tk.LEFT, padx=5, pady=5)

celcius_label = tk.Label(master = input_frame, text = "Degrees (Celcius):")
celcius_label.grid(row=0, column=0)

celcius_entry = tk.Entry(master=input_frame)
celcius_entry.grid(row=0, column=1)

result_label = tk.Label(master=input_frame, text="Degrees (Fahrenheit):")
result_label.grid(row=1, column=0)

result_display = tk.Label(master=input_frame)
result_display.grid(row=1, column=1)

convert_button = tk.Button(
    master = button_frame,
    text = "Convert",
    command = convert
    )
convert_button.pack(side=tk.LEFT)

window.mainloop()