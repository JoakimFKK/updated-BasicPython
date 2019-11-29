import easygui as gui

### Valg af fil (.txt i dette tilfælde)
def one():
    result = gui.fileopenbox("Select a file you filthy animal", "FileOpener :)", "*.txt")
    print(result) # Returnere full path til filen der er blevet vist

# ### Pænere måde at gøre forrige eksempel på.
def two():
    result = gui.fileopenbox(title="Open a file, nerd...", default="*.txt")
    print(result)

# ### Spørger om du har lyst til at overwrite den valgte fil. Den gør intet uden yderlige kode.
def three():
    result = gui.filesavebox(title="Overwrite a file, nerd...", default="*.txt")
    print(result)

# ### Valg af mappe
def four():
    result = gui.diropenbox(title="Select a folder, nerd...")
    print(result) # Returnere full path til mappen

