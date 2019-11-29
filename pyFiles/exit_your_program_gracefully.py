import easygui as gui

input_path = gui.fileopenbox(
    title="Choose a file, nerd...",
    default="*.pdf"
)
if input_path is None:
    exit()
else:
    print(input_path)