import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os, stat



root = tk.Tk()

root.title("JPG-1024")#name of program

canvas1 = tk.Canvas(root, width = 300, height = 350, bg = 'azure3', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


export_file_path = StringVar(root, 'Mypath') #Default save location: must be changed

def getPNG (): #Choosing file to convert
    global im1
    
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
    
browseButton_PNG = tk.Button(text="      Import File     ", command=getPNG, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_PNG)

def convertToJPG (): #converts to jpg
    global im1

    
    im2 = im1.crop((0,0,1024,1024)) #This is optional: It crops the picture to 1024*1024 pixels
    #im2 = im1.resize((1024,1024)) #This is also optional: It resizes the picture to 1024*1024 pixels


    
    export_file_name = getImageName(im1.filename) 
    mypath = export_file_path.get()+export_file_name+'.jpg' #this includes the path + the imported filename + extension
    
    try:
        im2.save(mypath)
    except:
        messagebox.showerror("ERROR", "Cannot access path!")



def getImageName(file_location):
    filename = file_location.split('/')[-1]
    filename = filename.split('.')
    
    return filename[0]


def changePath (): #Saving path changer
    temp = filedialog.askdirectory()
    temp = temp + '/'
    export_file_path.set(temp) 


path_button = tk.Button(text="      Change save path     ", command=changePath, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 300, window=path_button)


saveAsButton_JPG = tk.Button(text='Convert and resize', command=convertToJPG, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_JPG)


def on_closing(): #optional: "While exiting do this"
    
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)



root.mainloop() #tkinter loop for the interface
