from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import random 



class password:
    def __init__(self,root):
        self.root=root
        self.root.geometry("15300x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="Password Generator",font=("times new roman",35,"bold"),bg="lightblue",fg="red") 
        title_lbl.place(x=0,y=0,width=1530,height=790)

        img_top=Image.open(r"images\facenew1.jpg")
        img_top=img_top.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=790)
        

        b1_1=Button(f_lbl,text="Generate new password",cursor="hand2",command=self.new_password,font=("times new roman",18,"bold"),bg="darkblue",fg="yellow")
        b1_1.place(x=610,y=620,width=300,height=40)
    
    def new_password(password):
        lower="abcdefghijklmnopqrstuvwxyz"
        upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers="0123456789"
        symbols="~!@#$%^&*()."
    
        string=lower+upper+numbers+symbols
        length=16
        password="".join(random.sample(string,length))

        messagebox.showinfo("Your new password is: ",password)

if __name__=="__main__" :
    root=Tk()
    obj=password(root)
    root.mainloop()