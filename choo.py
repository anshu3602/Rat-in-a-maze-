from tkinter import*
from tkinter.ttk import *
#This variable is used to determine if the user wants to use the auto atic mode or the manual mode.
cho=0
#Defining this function because python doesnt allow assignments in buttons.
def ad(ass):
    
    ass=ass+1
    
    global cho
    
    cho=ass
    
    return ass
#Displaying a window asking which mode user wants.
def ch():
    
    roo=Tk()

    Label(roo,text="Click this button for Automatic mode ").grid()

    Button(roo,text = "Automatic", command = lambda: [roo.destroy(),ad(cho)]).grid(row=0, column=1, pady=10)

    Label(roo,text="Click this button for Manual control ").grid(row=1,column=0)

    Button(roo,text = "Manual", command = lambda: roo.destroy()).grid(row=1, column=1, pady=10)

    mainloop()

retu=ch()
