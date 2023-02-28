from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("student ")

    # Variable defining 

        self.var_dep=StringVar()    
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_adddress=StringVar()
        self.var_teacher=StringVar()
        self.var_photo = StringVar()


        main_frame = Frame(bd=4)
        main_frame.place(x=50,y=50,width=1480,height=800)

#left lable frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student detail",font=("times new roman",35,"bold"))
        left_frame.place(x=10,y=10,height=730,width=700)

    #current course
        current_course_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current course information ",font=("times new roman",18,"bold"))
        current_course_frame.place(x=12,y=70,height=140,width=690)

        #department

        department_lable = Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        department_lable.grid(row=0,column=0,padx=2,pady=10)

        department_cmbo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly")
        department_cmbo["values"]=("Select Department","CSE","ME","CIVIL","EC","EE")
        department_cmbo.current(0)
        department_cmbo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course

        course_lable = Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_lable.grid(row=0,column=2,padx=2,pady=10)

        course_cmbo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",11,"bold"),state="readonly")
        course_cmbo["values"]=("Select course","FW","Direct")
        course_cmbo.current(0)
        course_cmbo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year

        year_lable = Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_lable.grid(row=2,column=0,padx=2,pady=10)

        year_cmbo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly")
        year_cmbo["values"]=("Select year","1st","2nd","3rd","4th")
        year_cmbo.current(0)
        year_cmbo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_lable = Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_lable.grid(row=2,column=2,padx=2,pady=10)

        semester_cmbo = ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",11,"bold"),state="readonly")
        semester_cmbo["values"]=("Select semester","1","2","3","4","5","6","7","8")
        semester_cmbo.current(0)
        semester_cmbo.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        
    #student detail
        class_student_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student information ",font=("times new roman",18,"bold"))
        class_student_frame.place(x=12,y=200,height=500,width=690)

        #student id

        student_id_lable = Label(class_student_frame,text="Student id.",font=("times new roman",13,"bold"),bg="white")
        student_id_lable.grid(row=0,column=0,padx=2,pady=10)
        
        student_id_entry = ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",11,"bold"))
        student_id_entry.grid(row=0,column=1,sticky=W)

        #student name

        student_name_lable = Label(class_student_frame,text="Student Nmae",font=("times new roman",13,"bold"),bg="white")
        student_name_lable.grid(row=0,column=2,padx=2,pady=10)
        
        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_name,width=35,font=("times new roman",11,"bold"))
        student_name_entry.grid(row=0,column=3,sticky=W)
        
        # class division 
        
        student_class_division_lable = Label(class_student_frame,text="class division",font=("times new roman",13,"bold"),bg="white")
        student_class_division_lable.grid(row=1,column=0,padx=2,pady=10)
        
        student_class_division_entry = ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",11,"bold"))
        student_class_division_entry.grid(row=1,column=1,sticky=W)

        #student roll no

        student_rollno_lable = Label(class_student_frame,text="Roll No.",font=("times new roman",13,"bold"),bg="white")
        student_rollno_lable.grid(row=1,column=2,padx=2,pady=10)
        
        student_rollno_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",11,"bold"))
        student_rollno_entry.grid(row=1,column=3,sticky=W)
        
        

        #Gender
        student_class_division_lable = Label(class_student_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        student_class_division_lable.grid(row=2,column=0,padx=2,pady=10)
        
        semester_cmbo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",11,"bold"),state="readonly")
        semester_cmbo["values"]=("Select gender","male","female","other")
        semester_cmbo.current(0)
        semester_cmbo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        
        #BOD

        student_dob_lable = Label(class_student_frame,text="DOB",font=("times new roman",13,"bold"),bg="white")
        student_dob_lable.grid(row=2,column=2,padx=2,pady=10)
        
        student_dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",11,"bold"))
        student_dob_entry.grid(row=2,column=3,sticky=W)
        
        #email

        student_email_lable = Label(class_student_frame,text="Email",font=("times new roman",13,"bold"),bg="white")
        student_email_lable.grid(row=3,column=0,padx=2,pady=10)
        
        student_email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",11,"bold"))
        student_email_entry.grid(row=3,column=1,sticky=W)

        #phone no 

        student_phone_lable = Label(class_student_frame,text="Phone",font=("times new roman",13,"bold"),bg="white")
        student_phone_lable.grid(row=3,column=2,padx=2,pady=10)
        
        student_phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",11,"bold"))
        student_phone_entry.grid(row=3,column=3,sticky=W)

        #address

        student_address_lable = Label(class_student_frame,text="Address",font=("times new roman",13,"bold"),bg="white")
        student_address_lable.grid(row=4,column=0,padx=2,pady=10)
        
        student_address_entry = ttk.Entry(class_student_frame,textvariable=self.var_adddress,width=20,font=("times new roman",11,"bold"))
        student_address_entry.grid(row=4,column=1,sticky=W)

        #teacher name

        student_teacher_lable = Label(class_student_frame,text="Teacher Name",font=("times new roman",13,"bold"),bg="white")
        student_teacher_lable.grid(row=4,column=2,padx=2,pady=10)
        
        student_teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",11,"bold"))
        student_teacher_entry.grid(row=4,column=3,sticky=W)

        
        # Radio button
        self.var_radio1=StringVar()
        radio_sample_button = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value=YES)
        radio_sample_button.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radio_sample_button = ttk.Radiobutton(class_student_frame,variable=self.var_radio2,text="No photo sample",value=NO)
        radio_sample_button.grid(row=6,column=1)
        # Button Frame

        button_frame = Frame(class_student_frame,bd=2,bg="white",relief=RIDGE)
        button_frame.place(x=0,y=300,width=680,height=70)

        save_button = Button(button_frame,command=self.add_data,text="Save",width=17,bd=2,bg="blue",fg="white",font=("times new roman",13,"bold"))
        save_button.grid(row=0,column=0)

        update_button = Button(button_frame,command=self.update_data,text="Update",width=17,bd=2,bg="blue",fg="white",font=("times new roman",13,"bold"))
        update_button.grid(row=0,column=1)


        delete_button = Button(button_frame,text="Delete",width=17,bd=2,bg="blue",fg="white",font=("times new roman",13,"bold"))
        delete_button.grid(row=0,column=2)

        reset_button = Button(button_frame,text="Reset",width=17,bd=2,bg="blue",fg="white",font=("times new roman",13,"bold"))
        reset_button.grid(row=0,column=3)

        button_frame1 = Frame(class_student_frame,bd=2,bg="white",relief=RIDGE)
        button_frame1.place(x=0,y=330,width=680,height=38)

        photo_sample_button = Button(button_frame1,text="Take Photo Sample",width=35,bd=2,bg="blue",fg="white",font=("times new roman",13,"bold"))
        photo_sample_button.grid(row=0,column=0)


        photo_sample_button = Button(button_frame1,text="Update Photo Sample",width=35,bd=2,bg="blue",fg="white",font=("times new roman",13,"bold"))
        photo_sample_button.grid(row=0,column=1)


      




# right lable 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",35,"bold"))
        right_frame.place(x=730,y=10,height=730,width=700)


        # Searching 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",text="Search System",font=("times new roman",20,"bold"))
        search_frame.place(x=12,y=70,height=70,width=680)


        search_lable = Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="white")
        search_lable.grid(row=0,column=0,padx=2,pady=10)

        search_cmbo = ttk.Combobox(search_frame,font=("times new roman",9,"bold"),state="readonly")
        search_cmbo["values"]=("Select","Roll No","Phone No")
        search_cmbo.current(0)
        search_cmbo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry = ttk.Entry(search_frame,width=20,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,sticky=W,padx=10,pady=2)
        
        search_button = Button(search_frame,text="Search",width=10,bd=2,bg="blue",fg="white",font=("times new roman",13,"bold"))
        search_button.grid(row=0,column=3,padx=10,pady=2,sticky=W)

        show_all_button = Button(search_frame,text="Show_all",width=10,bd=2,bg="blue",fg="white",font=("times new roman",13,"bold"))
        show_all_button.grid(row=0,column=4,padx=10,pady=2,sticky=W)
        
        
        # TabeFrame     

        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=12,y=150,height=150,width=680)

        scroll_X = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("dep","cor","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_X.set,yscrollcommand=scroll_Y.set)

        scroll_X.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)

        scroll_X.config(command=self.student_table.xview) #for configration with the table 
        scroll_Y.config(command=self.student_table.yview)  # same for the y 

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("cor",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",tex="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")

        self.student_table.column("dep",width=100)
        self.student_table.column("cor",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
  

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ====================== function def ============================


    def add_data (self):
        if self.var_dep.get()=="Select Department" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_adddress.get()=="" or self.var_gender.get()=="Select gender":
            messagebox.showerror("error","All Fill Is Requir",parent=self.root)
        else:
           
            conn=mysql.connector.connect(host="localhost",username="root",password="123321",database="attendence")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_adddress.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Sucess","Student detail sucessefully saved",parent=self.root)
  
  
  
# ======================= fetching the data =============================

    def fetch_data (self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123321",database="attendence")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!= 0 :
            self.student_table.delete(*self.student_table.get_children())

            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()

# ================================= Get Cursor =============================

    def get_cursor(self,event=""):
        cursor_focus= self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_adddress.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


# ========  Updatwe function  =============================
    def update_data(self):
        if self.var_dep=="Select Department" or self.var_adddress=="":
            messagebox.showerror("Error","all details are required",parent=self.root)
        else:
            update = messagebox.askyesno("Update","Do you want to update or not",parent=self.root)
            if update>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="123321",database="attendence")
                my_cursor = conn.cursor()
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Student id=%s,Name=%s,Division=%s,Roll Number=%s,Gender=%s,DOb=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo Sample=%s,where Student id=%s",(
                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                            self.var_adddress.get(),
                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                            self.var_id.get()))
            else:
                if not update:
                    return
            messagebox.showinfo("update","student dat sucessufully updated",parent=self.root)
            conn.commit()
            self.fetch_data()
            conn.close()
# # ================= Reset Funvtion ================
#     def reset_data(self):
#         self.var_dep.set("Select Department"),
#         self.var_course.set(),
#         self.var_year.set(),
#         self.var_sem.set(),
#         self.var_id.set(),
#         self.var_name(),
#         self.var_div.set(),
#         self.var_roll.set(),
#         self.var_gender.set(),
#         self.var_dob.set(),
#         self.var_email.set(),
#         self.var_phone.set(),
#         self.var_adddress.set(),
#         self.var_teacher.set(),
#         self.var_radio1.set()

# ===================== Generate Data Set ===

#     def Generate_data_set(self):
#         if self.var_id=="" or self.var_dep=="Select Department":
#             messagebox.showerror("Error","All entry are required")
#         else:
#             # try:
#             conn=mysql.connector.connect(host="localhost",username="root",password="123321",database="attendence")
#             my_cursor = conn.cursor()
#             my_cursor.execute("select * from student")
#             myresult = my_cursor.fetchall()
#             id = 0 
#             for i in myresult:
#                 id = id +1

#             my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Student id=%s,Name=%s,Division=%s,Roll Number=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where Student_id=%s",(
#                                                                                                                                                                                                                     self.var_dep.get(),
#                                                                                                                                                                                                                     self.var_adddress.get(),
#                                                                                                                                                                                                                     self.var_course.get(),
#                                                                                                                                                                                                                     self.var_div.get(),
#                                                                                                                                                                                                                     self.var_dob.get(),
#                                                                                                                                                                                                                     self.var_div.get(),
#                                                                                                                                                                                                                     self.var_email.get(),
#                                                                                                                                                                                                                     self.var_gender.get(),
#                                                                                                                                                                                                                     self.var_name.get(),
#                                                                                                                                                                                                                     self.var_phone.get(),
#                                                                                                                                                                                                                     self.var_teacher.get(),
#                                                                                                                                                                                                                     self.var_year.get(),
#                                                                                                                                                                                                                     self.var_roll.get(),
#                                                                                                                                                                                                                     self.var_id.get()==id+1
#                                                                                                                                                                                                                     ))
#             conn.commit()
#             self.fetch_data()
#             self.reset_data()
#             conn.close()

# # ================ load Predefind data set =======
#             face_classifire=cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
#             def Face_croped(img):
#                 gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#                 faces=face_classifire.detectMultiScale(gray,1.3,5)

#                 for (x,y,w,h) in faces: 
#                     face_croped=img[y:y+h,x:x+w]
#                     return face_croped
#             cap = cv2.VideoCapture(0)

#             img_id = 0
#             while True:
#                 ret,my_frame=cap.read
#                 if Face_croped(my_frame) is not None:
#                     img_id = img_id+1
#                     face = cv2.resize(Face_croped(my_frame),(450,450))
#                     face = cv2.cvtColor(face,cv2.COLOR_RGB2GRAY)
#                     file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
#                     cv2.imwrite(file_name_path)
#                     cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)

#                     if cv2.waitKey(1)==13 or int(img_id)==100:
#                         break
#             cap.release()
#             cv2.destroyWindow()
#             messagebox.showinfo("result","Generating data set completd")


    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()