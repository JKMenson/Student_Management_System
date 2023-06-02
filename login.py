from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

#Functionality Part

def createAccount():
    login_window.destroy()
    import signUp
   
def forgetPassword():
    def changePassword():
        if userEntry.get()==""  or newpasswordEntry.get()=="" or confirmpassEntry.get()=="":
            messagebox.showerror("Error","All Fields Are Required!",parent=window)
        elif newpasswordEntry.get()!=confirmpassEntry.get():
            messagebox.showerror("Error","Password and Confirm Password are not Matched",parent=window)
        else:
            conn = pymysql.connect(host="localhost", user="root", password="",database="userData")
            myCursor = conn.cursor() 
            
            query = "SELECT * FROM userTable WHERE username = %s"
            myCursor.execute(query, (userEntry.get()))
            row = myCursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Incorrect Username",parent=window)
            else:
                query = "update userTable set password=%s where username = %s"
                myCursor.execute(query,(newpasswordEntry.get(),userEntry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Password is reset,please login with new password",parent=window)
                window.destroy()
                 
    window = Toplevel()
    window.title("Change Password")
    
    bgPicture = ImageTk.PhotoImage(file="background.jpg")
    bgLabel = Label(window,image=bgPicture)
    bgLabel.grid()
    
    heading = Label(window,text="RESET PASSWORD",font=("times new roman",20,"bold"),bg="white",fg="magenta2")
    heading.place(x=480,y=60)
    
    userLabel = Label(window,text="Username",font=("times new roman",20,"bold"),bg="white",fg="orchid1")
    userLabel.place(x=470,y=130)
    
    userEntry = Entry(window,width=25,font=("times new roman",11,"bold"),bd=0,fg="orchid1")
    userEntry.place(x=470,y=160)
     
    frame1 = Frame(window,width=250,height=2,bg="orchid1")
    frame1.place(x=470,y=180)
    
    
    newpasswordLabel = Label(window,text="New Password",font=("times new roman",20,"bold"),bg="white",fg="orchid1")
    newpasswordLabel.place(x=470,y=210)
    
    newpasswordEntry = Entry(window,width=25,font=("times new roman",11,"bold"),bd=0,fg="orchid1")
    newpasswordEntry.place(x=470,y=240)
    
        
    frame1 = Frame(window,width=250,height=2,bg="orchid1")
    frame1.place(x=470,y=260)
    
    
    
    confirmpassLabel = Label(window,text="Confirm Password",font=("times new roman",20,"bold"),bg="white",fg="orchid1")
    confirmpassLabel.place(x=470,y=290)
    
    confirmpassEntry = Entry(window,width=35,font=("times new roman",11,"bold"),bd=0,fg="orchid1")
    confirmpassEntry.place(x=470,y=320)
    
    frame1 = Frame(window,width=250,height=2,bg="orchid1")
    frame1.place(x=470,y=340)
    
    
    
    submitButton = Button(window, text="Submit",width=25
                          ,font=("times new roman",11,"bold"),bd=0,bg="orchid1",fg="white", activebackground="orchid1",activeforeground="white",command=changePassword)
    submitButton.place(x=470,y=390)
    
    window.mainloop()
def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required!")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="")
            myCursor = conn.cursor()
            query = "use userData"
            myCursor.execute(query)
            query = "SELECT * FROM userTable WHERE username = %s AND password = %s"
            myCursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
            row = myCursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                messagebox.showinfo("Welcome", "Login is successful")
                login_window.destroy()
                import student
        except pymysql.Error as e:
            messagebox.showerror("Error", "Connection is not established, please try again!")
            conn.close()

        
        
def hide():
    openeye.config(file="closeye.png")
    passwordEntry.config(show="*")
    eyeButton.config(command = show)
    
def show():
    openeye.config(file="openeye.png")
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
     
     
def user_enter(event):
    if usernameEntry.get()=="Username":
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=="Password":
        passwordEntry.delete(0,END)

#GUI PARTI
login_window=Tk()
login_window.geometry("990x660+50+50")
login_window.resizable(0,0)
login_window.title("Login Page")
bgImage = ImageTk.PhotoImage(file="student.jpg")
bgLabel = Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading = Label(login_window,text="USER LOGIN",font=("times new roman",20,"bold"),bg="white",fg="firebrick1")
heading.place(x=620,y=120)

usernameEntry = Entry(login_window,width=25,font=("times new roman",11,"bold"),bd=0,fg="firebrick1")
usernameEntry.place(x=590,y=200)

usernameEntry.insert(0,"Username")
usernameEntry.bind("<FocusIn>",user_enter)

frame1 = Frame(login_window,width=250,height=2,bg="firebrick1")
frame1.place(x=580,y=222)


passwordEntry = Entry(login_window,width=25,font=("times new roman",11,"bold"),bd=0,fg="firebrick1")
passwordEntry.place(x=590,y=260)

passwordEntry.insert(0,"Password")
passwordEntry.bind("<FocusIn>",password_enter)

frame2 = Frame(login_window,width=250,height=2,bg="firebrick1")
frame2.place(x=580,y=282)

openeye = PhotoImage(file="openeye.png")
eyeButton = Button(login_window,image=openeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=hide)
eyeButton.place(x=800,y=255)

forgetButton = Button(login_window,text="Forgot Password",bd=0,bg="white",activebackground="white",cursor="hand2",font=("times new roman",11,"bold"),fg="firebrick1",activeforeground="firebrick1",command=forgetPassword)
forgetButton.place(x=715,y=295)

loginButton = Button(login_window,text="Login",font=("Open Sans", 16,"bold")
                     ,fg="white",bg="firebrick1",activebackground="firebrick1",activeforeground="white",cursor="hand2",bd=0,width=19,command=login)
loginButton.place(x=578,y=350)

orLabel = Label(login_window,text="----------------- OR ----------------",font=("Open Sans",14),fg="firebrick",bg="white")
orLabel.place(x=583,y=400)

fbLogo = PhotoImage(file="facebook.png")
fbLabel = Label(login_window,image=fbLogo,bg="white")
fbLabel.place(x=640,y=440)

googleLogo = PhotoImage(file="google.png")
googleLabel = Label(login_window,image=googleLogo,bg="white")
googleLabel.place(x=690,y=440)

twitterLogo = PhotoImage(file="twitter.png")
twitterLabel = Label(login_window,image=twitterLogo,bg="white")
twitterLabel.place(x=740,y=440)


signUpLabel = Label(login_window,text="Don't have an account?",font=("Open Sans",10),fg="firebrick",bg="white")
signUpLabel.place(x=590,y=500)

newAccountButton = Button(login_window,text="Create Account",font=("Open Sans",10,"bold underline")
                     ,fg="blue",bg="white",activebackground="white",activeforeground="blue",cursor="hand2",bd=0,command=createAccount)
newAccountButton.place(x=727,y=500)

login_window.mainloop()
