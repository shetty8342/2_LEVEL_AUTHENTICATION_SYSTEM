img_top=Image.open(r"images\face1.jpg")
        img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)
        
        # Button

        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="green",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open(r"images\facenew.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)