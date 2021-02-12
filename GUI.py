#%%
'''import tkinter as tk
from tkinter import filedialog
import PIL
from PIL import Image, ImageTk
#import main as bg

root = tk.Tk()

def UploadAction(event=None):
    img = filedialog.askopenfilename()
    image = PIL.Image.open(img)
    print('Selected:', img)
  

#root = tk.Tk()
button = tk.Button(root, text='Select an image', command=UploadAction)
button.pack()
#root.after(20, UploadAction)
#bg.background(img)
root.mainloop()'''

# %%
'''import main as bg   
from tkinter import *
from tkinter.ttk import *
    
class GUI ():
        
    def create widgets(self):
            #....
        
    def create_panel2(self):
            #create buttons
        panel1 = ...
        btn1 = Button(panel1, text="yyyyy", command=bg.progA)
        btn1.pack() 
        
    def create_panel2(self):
            #create buttons
        panel2 = ...
        btn2 = Button(panel1, text="yyyyy", command=bg.progB)
        btn2.pack() 
    
All_Entries = []
    
window = Tk()
D=GUI(window)
window.mainloop()
runprogram1 = bg.progX()
runprogram2 = bg.probY(x, y, z)

    
#%%

from tkinter import *

from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("parrot.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("200x120")
root.mainloop()'''


# %%
'''
from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import PIL
import os
from tkinter import filedialog

root = Tk()
root.title("Zahlenerfassung")
root.geometry("500x400")
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
def create(): command=os.system("start "+"pepsi.txt")
#def click():
    # Get the file
   # file = askopenfilename(initialdir='C:/Users/%s')
    # Split the filepath to get the directory
#  directory = os.path.split(file)[0]
#   print(directory)

def click():
     image_file_location = filedialog.askopenfilename(initialdir="C:/Users/%s")
     image = ImageTk.PhotoImage(file=image_file_location)
     canvas.create_image(50, 50, image=image, anchor=NW)

button1 = Button(topFrame, text="Bild auswerten", fg="red")
button2 = Button(bottomFrame, text="Erstelle ein Bild", fg="blue", command=lambda: create())
button3 = Button(bottomFrame, text="Lade dein Bild hoch", fg="blue", command=lambda: click())

canvas = Canvas(width=200, height=200)
canvas.pack(expand=NO, fill=NONE)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

one = Label(root, text="", fg="white")
one.pack(fill=BOTH, expand=TRUE)
root.mainloop()'''

#%%
from tkinter import *
from tkinter import filedialog
import main as bg

def get_file_path():
    # Open and return file path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
    l1 = Label(window, text = "File path: " + file_path).pack()
    return l1

window = Tk()
# Creating a button to search the file
b1 = Button(window, text = "Open File", command = get_file_path).pack()
b2 = Button(window, text= "Submit", command= bg.background(b1)).pack()
#bg.background()

window.mainloop()

# %%
'''import PySimpleGUI as sg

sg.SetOptions(background_color = 'LightBlue',
            element_background_color = 'LightBlue',
            text_element_background_color = 'LightBlue',
              font= ('Calibri', 14, 'bold'))  
dirname, filename = os.path.split(os.path.abspath(__file__))
'''
# %%
