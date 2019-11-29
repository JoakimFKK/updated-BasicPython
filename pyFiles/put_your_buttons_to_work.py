import tkinter as tk

def increase():
    value = int(value_label["text"])
    value_label["text"] = str(value + 1)

def decrease():
    value = int(value_label["text"])
    value_label["text"] = str(value - 1)

window = tk.Tk()

down_button = tk.Button(
    master = window,
    text = "-",
    command = decrease
)

value_label = tk.Label(
    master=window,
    text = "0"
)

up_button = tk.Button(
    master = window,
    text = "+",
    command = increase
)
down_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
value_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
up_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



window.mainloop()
