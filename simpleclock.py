from tkinter import * 
from tkinter.ttk import *
  
#Importing strftime function to 
#Retrieve system's time 
from time import strftime 
  
#Creating tkinter window 
root = Tk() 
root.title('Clock') 
  
#This function is used to  
#Display time on the label 
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
  
#Styling the label widget so that clock 
#Will look more attractive 
lbl = Label(root, font = ('arial', 45, 'bold'), 
            background = 'purple', 
            foreground = 'white') 
  
#Placing clock at the centre 
#Of the tkinter window 
lbl.pack(anchor = 'center') 
time() 
  
mainloop() 
