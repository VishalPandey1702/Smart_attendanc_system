from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student_detail import Student

class Face_recognisition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system ")
        
        #img1
        # img = Image.open(r"imge1.jpg")
        # img=img.resize((500,130),Image.ANTIALIAS)
        # self.photoimage=ImageTk.PhotoImage(img)
        # f_lable = Label(self.root,image=self.photoimage)
        # f_lable.place(x=1,y=1,width=130,height=500)

        # img3 = Image.open(r"img3.jpg")
        # img3=img3.resize((1530,790),Image.ANTIALIAS)
        # self.photoimage3=ImageTk.PhotoImage(img3)
        # f_lable = Label(self.root,image=self.photoimage3)
        # f_lable.place(x=1,y=0,height=1530,width=790)

        # Button

        btn1 = Button(root,text = 'STUDENT',command=self.student_detail,cursor="hand2",font=("time new rom",15,"bold"),bg="blue",fg="skyblue")
        btn1.place(x=0,y=0,height=150,width=150)
 
        btn2 = Button(root, text = 'Face Dector',cursor="hand2",font=("time new rom",15,"bold"),bg="grey",fg="skyblue")
        btn2.place(x=350,y=0,height=150,width=150)

        btn3 = Button(root, text = 'Attendance',cursor="hand2",font=("time new rom",15,"bold"),bg="grey",fg="skyblue")
        btn3.place(x=700,y=0,height=150,width=150)

        btn4 = Button(root, text = 'Help desk',cursor="hand2",font=("time new rom",15,"bold"),bg="grey",fg="skyblue")
        btn4.place(x=1050,y=0,height=150,width=150)
           
        btn5 = Button(root, text = 'Train data ',cursor="hand2",font=("time new rom",15,"bold"),bg="grey",fg="skyblue")
        btn5.place(x=0,y=160,height=150,width=150)
           
        btn6 = Button(root, text = 'Photos ',cursor="hand2",font=("time new rom",15,"bold"),bg="grey",fg="skyblue")
        btn6.place(x=350,y=160,height=150,width=150)
 
        btn7 = Button(root, text = 'Developer ',cursor="hand2",font=("time new rom",15,"bold"),bg="grey",fg="skyblue")
        btn7.place(x=700,y=160,height=150,width=150)
 
        btn8 = Button(root, text = 'Exit',cursor="hand2",font=("time new rom",15,"bold"),bg="grey",fg="skyblue")
        btn8.place(x=1050,y=160,height=150,width=150)
 


#=================== Function Button ======================

    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)






if __name__ =="__main__":
    root=Tk()
    obj=Face_recognisition_system(root)
    root.mainloop()