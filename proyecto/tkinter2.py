from tkinter import *
raiz=Tk()
miFrame = Frame(raiz, width=800, height=500)
miFrame.pack()
#campos de texto
cuadroUsername=Entry(miFrame)
cuadroUsername.grid(row=0, column=1, padx=25, pady=10)
cuadroEmail=Entry(miFrame)
cuadroEmail.grid(row=1, column=1, padx=25, pady=10)
cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=2, column=1, padx=25, pady=10)
cuadroPassword.config(show="*", justify="center")
#etiquetas
usernameLabel = Label(miFrame, text='Username:')
usernameLabel.grid(row=0, column=0, sticky=W, padx=25, pady=10)
emailLabel = Label(miFrame, text='Email:')
emailLabel.grid(row=1, column=0, sticky=W, padx=25, pady=10)
passwordLabel = Label(miFrame, text='Password:')
passwordLabel.grid(row=2, column=0, sticky=W, padx=25, pady=10)

raiz.mainloop()