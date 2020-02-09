from tkinter import *
root = Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
miImagen=PhotoImage(file='lakitu.png')
miLabel = Label(miFrame, image=miImagen).place(x=120, y=120)

root.mainloop()