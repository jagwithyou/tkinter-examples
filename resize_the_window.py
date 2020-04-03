from tkinter import *
#instantiating the tkinter
root = Tk()

#resize the window
root.geometry("500x500")

#instantiating the  leble of root instance
txtLabel = Label(root, text = "Hello World")
#packing the eble to the root 
txtLabel.pack()
#Showing the root
root.mainloop() 