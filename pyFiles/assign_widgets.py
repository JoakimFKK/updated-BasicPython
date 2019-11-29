import tkinter as tk

window = tk.Tk()
frame_a = tk.Frame()
frame_b = tk.Frame()

text_a = tk.Label(text="I'm in Frame A", master=frame_a)
text_b = tk.Label(text="I'm in Frame B", master=frame_b)
text_a.pack()
text_b.pack()
frame_b.pack()
frame_a.pack()

window.mainloop()