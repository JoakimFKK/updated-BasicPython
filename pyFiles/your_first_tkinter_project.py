import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello world!")
greeting.pack()

button = tk.Button()
button["width"] = 25
button["height"] = 5
button["background"] = "blue"
button["text"] = "Click me!"
button["foreground"] = "red"
button.pack()

button_compact = tk.Button(
    text="!em kcilC",
    background="red",
    foreground="blue",
    width=25,
    height=5
)
button_compact.pack()

entry = tk.Entry()
entry.insert(0, "hello")

text_box = tk.Text()
text_box.insert("1.0", "hewwo")
text_box.insert(tk.END, "hewwo")


window.mainloop()