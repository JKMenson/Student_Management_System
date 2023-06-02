from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    userEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)
    
def connect_database():
    if emailEntry.get() == "" or userEntry.get() == "" or passwordEntry.get() == "" or confirmEntry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required!")
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror("Error", "Password Mismatched!")
    elif check.get() == 0:
        messagebox.showerror("Error", "Please Accept Terms & Conditions")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="")
            myCursor = conn.cursor()
            query = "create database if not exists userData"
            myCursor.execute(query)
            query = "use userData"
            myCursor.execute(query)
            query = "CREATE TABLE IF NOT EXISTS userTable(id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, email VARCHAR(50), username VARCHAR(100), password VARCHAR(30))"
            myCursor.execute(query)
            
            query = "SELECT * FROM userTable WHERE username = %s"
            myCursor.execute(query, (userEntry.get()))
            row = myCursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Username Already exists")
            else:
                query = "INSERT INTO userTable(email, username, password) VALUES (%s, %s, %s)"
                myCursor.execute(query, (emailEntry.get(), userEntry.get(), passwordEntry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration is Successful")
                clear()
                signup_window.destroy()
                import login
                
        except pymysql.Error as e:
            messagebox.showerror("Error", "Database Connectivity Issue, Please Try Again!")
   
def loginPage():
    signup_window.destroy()
    import login
    
signup_window=Tk()
signup_window.title("Signup Page")
signup_window.resizable(0,0)


background = ImageTk.PhotoImage(file="student.jpg")
bgLabel = Label(signup_window,image=background)
bgLabel.grid()

signFrame = Frame(signup_window,bg="white")
signFrame.place(x=554,y=100)
heading = Label(signFrame,text="CREATE AN ACCOUNT",font=("times new roman",18,"bold"),bg="white",fg="firebrick1")
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel = Label(signFrame,text="Email",font=("times new roman",12,"bold"),bg="white",fg="firebrick1")
emailLabel.grid(row=1,column=0,padx=25,sticky="w",pady=(10,0))
emailEntry = Entry(signFrame,width=25,font=("times new roman",16,"bold"),fg="white",bg="firebrick1")
emailEntry.grid(row=2,column=0,sticky="w",padx=25)


userLabel = Label(signFrame,text="Username",font=("times new roman",12,"bold"),bg="white",fg="firebrick1")
userLabel.grid(row=3,column=0,padx=25,sticky="w",pady=(10,0))
userEntry = Entry(signFrame,width=25,font=("times new roman",16,"bold"),fg="white",bg="firebrick1")
userEntry.grid(row=4,column=0,sticky="w",padx=25)


passwordLabel = Label(signFrame,text="Password",font=("times new roman",12,"bold"),bg="white",fg="firebrick1")
passwordLabel.grid(row=5,column=0,padx=25,sticky="w",pady=(10,0))
passwordEntry = Entry(signFrame,width=25,font=("times new roman",16,"bold"),fg="white",bg="firebrick1")
passwordEntry.grid(row=6,column=0,sticky="w",padx=25)


confirmLabel = Label(signFrame,text="Confirm Password",font=("times new roman",12,"bold"),bg="white",fg="firebrick1")
confirmLabel.grid(row=7,column=0,padx=25,sticky="w",pady=(10,0))
confirmEntry = Entry(signFrame,width=25,font=("times new roman",16,"bold"),fg="white",bg="firebrick1")
confirmEntry.grid(row=8,column=0,sticky="w",padx=25)

check=IntVar()
terms = Checkbutton(signFrame,text="I agree to the Terms & Conditions",font=("times new roman",12,"bold"),bg="white",fg="firebrick1",activeforeground="firebrick1",cursor="hand2",variable=check)
terms.grid(row=9,column=0,pady=10,padx=15)

signupButton = Button(signFrame,text="Sign Up",font=("Open Sans", 16,"bold")
                     ,fg="white",bg="firebrick1",activebackground="firebrick1",activeforeground="white",cursor="hand2",bd=0,width=21,command=connect_database)
signupButton.grid(row=10,column=0,padx=22)


loginLabel = Label(signFrame,text="Do you have an account?",font=("times new roman",12,"bold"),fg="firebrick",bg="white")
loginLabel.grid(row=11,column=0,padx=20,pady=10,sticky="w")

loginButton = Button(signFrame,text="Login",font=("Open Sans",12,"bold underline")
                     ,fg="blue",bg="white",activebackground="white",activeforeground="blue",cursor="hand2",bd=0,command=loginPage)
loginButton.place(x=195,y=400)


signup_window.mainloop()