import easygui as gui

breadtext = "Australian say: "
choices = ("Oi", "Oy", "Oi, cunt!")
title = "Top text"

# ### 1 knap.
def one():
    result = gui.msgbox("Bread text", "Title text", "Button text")
    print(result) # Returnere værdien som knappen har

# ### Multiple buttons.
def two():
    choices = ("Wars", "Trek", "Man", "ring Rob Schneider", "Star these nuts, gottem", "\"Stars\"")
    result = gui.buttonbox("Finish the sentence: Star ____", "Choose your destiny", choices)
    print(result) # Returnere værdien som knappen har

# ### Multiple buttons 
def three():
    result = gui.indexbox(breadtext, title, choices)
    print(result) # Returnere index værdien på knappen

# ### En vertikal liste hvor man kan scrolle
def four():
    result = gui.choicebox(breadtext, title, choices)
    print(result) # Returnere værdien

# ### Ligesom choicebox, men kan vælge mere end en værdi
def five():
    result = gui.multchoicebox(breadtext, title, choices)
    print(result) # Returnere værdien som en liste

# ### Textbox med en linje som kan skrives i.
def six():
    result = gui.enterbox(breadtext, title)
    print(result) # Returnere værdien der bliver skrevet

# ### Textbox med en linje som kan skrives i, men al teksten er vist som *
def seven():
    result = gui.passwordbox(breadtext, title)
    print(result) # Returnere værdien som skrevet

# ### Stor textbox med plads til formattering.
def eight():
    result = gui.textbox(breadtext, title)
    print(result) # Returnere værdien som skrevet, med formattering.
