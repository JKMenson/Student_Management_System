from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student():
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System ")
        self.root.geometry("1300x700+0+0")

        title = Label(self.root,text= "Student Management System",bd=9,relief=GROOVE,font=("times new roman",50,"bold"),bg="yellow", fg="red")
        title.pack(side=TOP,fill=X)

        # ==========AllVariables============
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()


        #==========ManageFrame============
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Manage_Frame.place(x=20,y=100,width=450,height=595)

        m_title = Label(Manage_Frame,text="Manage Student",bg="yellow",fg="black",font=("times new roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,padx=30,pady=20)

        lbl_roll = Label(Manage_Frame,text="Roll No",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,padx=20,pady=5,sticky="w")
        txt_roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,padx=5,pady=5,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        txt_name = Entry(Manage_Frame,textvariable=self.name_var, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        txt_email = Entry(Manage_Frame,textvariable=self.email_var, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, padx=20, pady=5, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",16,"bold"),state="readonly")
        combo_gender['values'] = ("male","female","other")
        combo_gender.grid(row=4,column=1,padx=5, pady=5, sticky="w")

        lbl_contact = Label(Manage_Frame, text="Contact", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, padx=20, pady=5, sticky="w")
        txt_contact = Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, padx=20, pady=5, sticky="w")
        txt_dob = Entry(Manage_Frame,textvariable=self.dob_var, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, padx=20, pady=20, sticky="w")
        self.txt_address = Text(Manage_Frame, width=20,height=4,font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        self.txt_address.grid(row=7, column=1, padx=5, pady=10, sticky="w")

        #==============buttonframe============
        btn_frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg="black")
        btn_frame.place(x=15, y=525, width=410)

        Addbtn = Button(btn_frame,text="Add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(btn_frame,text="Update",width=10,command=self.update).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn = Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn = Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        # ==========DetailsFrame============
        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        Details_Frame.place(x=500, y=100, width=780, height=595)

        lbl_search = Label(Details_Frame,text="Search By",bg="blue",fg="white", font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        combo_search = ttk.Combobox(Details_Frame,textvariable=self.search_by,font=("times new roman", 13, "bold"),width=10,state="readonly")
        combo_search['values'] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=5, sticky="w")
        txt_search = Entry(Details_Frame,textvariable=self.search_txt, font=("times new roman", 10, "bold"), width=20,bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, padx=20, pady=5, sticky="w")

        searchbtn = Button(Details_Frame, text="Search", width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        searchbtn = Button(Details_Frame, text="Show All", width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        # ==========TableFrame============
        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=750, height=500)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,column=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("Address",text="Address")

        self.Student_table['show'] = 'headings'
        self.Student_table.column('roll',width=80)
        self.Student_table.column('name',width=100)
        self.Student_table.column('email',width=100)
        self.Student_table.column('gender',width=80)
        self.Student_table.column('contact',width=100)
        self.Student_table.column('dob',width=100)
        self.Student_table.column('Address',width=150)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_student(self):
        if self.Roll_No_var.get()== "" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are required to fill")
        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="studentMgtSystem")
            cur = con.cursor()
            cur.execute("Insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_address.get('1.0',END)
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record has been inserted successfully")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentMgtSystem")
        cur = con.cursor()
        cur.execute("Select * from students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                   self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def get_cursor(self,ev):
       cursor_row = self.Student_table.focus()
       contents = self.Student_table.item(cursor_row)
       row = contents['values']
       self.Roll_No_var.set(row[0])
       self.name_var.set(row[1])
       self.email_var.set(row[2])
       self.gender_var.set(row[3])
       self.contact_var.set(row[4])
       self.dob_var.set(row[5])
       self.txt_address.delete("1.0",END)
       self.txt_address.insert(END,row[6])

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.dob_var.set(""),
        self.txt_address.delete("1.0",END)

    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentMgtSystem")
        cur = con.cursor()
        cur.execute("Update students set name = %s, email = %s, gender = %s, contact = %s, dob = %s, address = %s where roll_no = %s",(
                    self.name_var.get(),
                    self.email_var.get(),
                    self.gender_var.get(),
                    self.contact_var.get(),
                    self.dob_var.get(),
                    self.txt_address.get('1.0', END),
                    self.Roll_No_var.get()
                    ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Record has been update successfully")

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentMgtSystem")
        cur = con.cursor()
        cur.execute("Delete from students where roll_no = %s",self.Roll_No_var.get())

        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentMgtSystem")
        cur = con.cursor()
        cur.execute("Select * from students where " +str(self.search_by.get()) +" Like '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()


root=Tk()
obj=Student(root)
root.mainloop()
