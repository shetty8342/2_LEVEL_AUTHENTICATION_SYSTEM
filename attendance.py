from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("15300x790+0+0")
        self.root.title("face Recognition System")
        
        #first image

        img=Image.open(r"images\students.jpg")
        img=img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #second_image

        img1=Image.open(r"images\student1.jpg")
        img1=img1.resize((500,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

if __name__=="__main__" :
    root=Tk()
    obj=Attendance(root)
    root.mainloop()