from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from password_generator import password

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #first_image
        img=Image.open(r"images\dormakaba-Blog-Post-pictures-_-1024-x-683-83-3550001707.jpg")
        img=img.resize((510,150),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=150)

        #second_image
        img1=Image.open(r"images\face_recognition_3_4x-2811321631.jpg")
        img1=img1.resize((510,150),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=510,height=150)

        #third_image
        img2=Image.open(r"images\facial-recognition-328945941.jpg")
        img2=img2.resize((510,150),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1020,y=0,width=510,height=150)
        
        #bg_image
        img3=Image.open(r"images\ss.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1530,height=710)  

        title_lbl=Label(bg_img,text="2 LEVEL AUTHENTICATION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #student Details_Button
        img4=Image.open(r"images\student.jpg")
        img4=img4.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=90,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=250,width=200,height=40)

        #Detect face button
        img5=Image.open(r"images\facedetector.jpg")
        img5=img5.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=90,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detection",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=250,width=200,height=40)
        
        #Attendance face button
        img6=Image.open(r"images\attendance.jpg")
        img6=img6.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
        b1.place(x=850,y=90,width=200,height=200)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=850,y=250,width=200,height=40)

        #Help face button
        img7=Image.open(r"images\help.jpg")
        img7=img7.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1200,y=90,width=200,height=200)

        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1200,y=250,width=200,height=40)

        # Train Face Button
        img8=Image.open(r"images\AI-model.jpg")
        img8=img8.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=380,width=200,height=200)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=550,width=200,height=40)

        #   Photo face Button
        img9=Image.open(r"images\TrainFace.jpg")
        img9=img9.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=200,height=200)

        b1_1=Button(bg_img,text="Train Face",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=550,width=200,height=40)

        #Password Generator Button
        img10=Image.open(r"images\PasswordGenerator.jpg")
        img10=img10.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.password_generator)
        b1.place(x=850,y=380,width=200,height=200)

        b1_1=Button(bg_img,text="Password Generator",cursor="hand2",command=self.password_generator,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=850,y=550,width=200,height=40)

        #Exit Face Button
        img11=Image.open(r"images\Exit.jpg")
        img11=img11.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1200,y=380,width=200,height=200)

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1200,y=550,width=200,height=40)
 
    #===============================function buttons===========================

    def open_img(self):
         os.startfile("data")

    def student_details(self):
          self.new_window=Toplevel(self.root)
          self.app=Student(self.new_window)       
        
    def train_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Train(self.new_window)        

    def face_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Face_Recognition(self.new_window)     

    def password_generator(self):
         self.new_window=Toplevel(self.root)
         self.app=password(self.new_window)    

if __name__=="__main__" :
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()