from tkinter import*
from tkinter.ttk import *
def a(L):
    
    root=Tk()

    wall= PhotoImage(file= r"C:\Users\ANSHU\Pictures\Saved Pictures\wall.png")

    tile= PhotoImage(file= r"C:\Users\ANSHU\Pictures\Saved Pictures\tile.png")

    rat= PhotoImage(file= r"C:\Users\ANSHU\Pictures\Saved Pictures\rat.png")

    cheese= PhotoImage(file= r"C:\Users\ANSHU\Pictures\Saved Pictures\cheese.png")
    
    las= PhotoImage(file= r"C:\Users\ANSHU\Pictures\Saved Pictures\las.png")

    inde=-1

    ind2=-1

    for i,j in enumerate (L):

        ind2+=1
        for k in j:

            inde=inde+1

            if k==0:
                 Button(root,text ='Click Me!', image=wall).grid(row=ind2,column=inde)

            if k==1:
                 Button(root,text='Click Me!', image=tile).grid(row=ind2,column=inde)
                 
            if k==2:
                Button(root,text='Click Me!', image=rat).grid(row=ind2,column=inde)

            if k==4:
                Button(root,text='Click Me!', image=cheese).grid(row=ind2,column=inde)

            if k==5:
                Button(root,text='Click Me!', image=las).grid(row=ind2,column=inde)
                
        inde=-1
    class Test():
        
       def __init__(self):

           self.button1 = Button(root, text = "Next Step", command = lambda: root.destroy())
           
           self.button1.grid(row=11,column=20)
           
    b=Test()
    mainloop()
