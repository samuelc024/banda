from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width="300", height="150")

miFrame.pack()

raiz.title("BANDA")

raiz.resizable(0,0)

raiz.geometry("800x600")

raiz.config(bg="lightpink")

raiz.config(bd=15)

raiz.config(relief="groove")

miLabel=Label(miFrame, text="HORA DE GENERAR TU BANDA")

miLabel.config(bg="lightblue")

miLabel.config(width="32", height="5")

miLabel.config(bd=35)

miLabel.config(relief="groove")

miLabel.place(x=0 ,y=0)

raiz.mainloop()
