from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Register_win:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1523x780+0+0")
        self.root.configure(background="#011F5B")

        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_secQ = StringVar()
        self.var_secA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        frame = Frame(self.root, bg="white",relief=RAISED,bd=3)
        frame.place(x=200, y=100, width=1100, height=600)

        img1 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\signup.png")
        img1 = img1.resize((450,300))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=200, y=220, width=450, height=300)

        leftframe = Frame(frame, bg="aliceblue")
        leftframe.place(x=450, y=0, width=640, height=590)

        title_lbl = Label(leftframe, text="SIGN UP", font=("times new roman", 25, "bold"), fg="#011F5B",bg="aliceblue")
        title_lbl.place(x=10, y=10)

        #labels
        name = Label(leftframe, text="Name",font=("times new roman", 14, "bold"), bg="aliceblue")
        name.place(x=50,y=100)
        self.name_entry = Entry(leftframe,textvariable=self.var_name, font=("times new roman", 14))
        self.name_entry.place(x=230, y=100, width=240)

        email = Label(leftframe, text="Email Id", font=("times new roman", 14, "bold"), bg="aliceblue")
        email.place(x=50, y=150)
        self.email_entry = Entry(leftframe,textvariable=self.var_email, font=("times new roman", 14))
        self.email_entry.place(x=230, y=150, width=240)

        securityq = Label(leftframe, text="Security Question", font=("times new roman", 14, "bold"), bg="aliceblue")
        securityq.place(x=50, y=200)

        self.combo_secQ=ttk.Combobox(leftframe,font=("times new roman", 14),textvariable=self.var_secQ,state="readonly")
        self.combo_secQ["values"]=("Select","Your birth place","Your favourite food","Your pet name")
        self.combo_secQ.place(x=230, y=200,width=240)
        self.combo_secQ.current(0)

        securityans = Label(leftframe, text="Security Answer", font=("times new roman", 14, "bold"), bg="aliceblue")
        securityans.place(x=50, y=250)
        self.sa_entry = Entry(leftframe,textvariable=self.var_secA,font=("times new roman", 14))
        self.sa_entry.place(x=230, y=250, width=240)

        pwd = Label(leftframe, text="Password", font=("times new roman", 14, "bold"), bg="aliceblue")
        pwd.place(x=50, y=300)
        self.pwd_entry = Entry(leftframe, textvariable=self.var_pass,font=("times new roman", 14),show="*")
        self.pwd_entry.place(x=230, y=300, width=240)

        confirm = Label(leftframe, text="Confirm Password", font=("times new roman", 14, "bold"), bg="aliceblue")
        confirm.place(x=50, y=350)
        self.confirm_entry = Entry(leftframe, textvariable=self.var_confpass,font=("times new roman", 14),show="*")
        self.confirm_entry.place(x=230, y=350, width=240)

        #buttons
        signupBtn = Button(leftframe, text="Sign Up", font=("times new roman", 15, "bold"), bd=3, command=self.signup,
                          relief=RAISED, fg="white", bg="#C51E3A", cursor="hand2")
        signupBtn.place(x=370, y=400, width=100, height=30)

        logintxt = Label(leftframe, text="Already have an account?", font=("times new roman", 13), bg="aliceblue")
        logintxt.place(x=175, y=461)
        loginBtn = Button(leftframe, text="Login", font=("times new roman", 13, "bold"), bd=0, fg="blue",
                             activeforeground="blue", activebackground="aliceblue",
                             bg="aliceblue", cursor="hand2")
        loginBtn.place(x=370, y=460, width=100, height=30)

    def signup(self):
        if self.var_name.get()=="" or self.var_email.get()=="" or self.var_secQ.get()=="Select":
            messagebox.showerror("Error", "Please enter all fields")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error", "Passwords do not match")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                           database="management")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM signup WHERE email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exists, please try another email")
            else:
                my_cursor.execute("insert into signup values(%s,%s,%s,%s,%s)",(self.var_name.get(),
                                                                               self.var_email.get(),
                                                                               self.var_secQ.get(),
                                                                               self.var_secA.get(),
                                                                               self.var_pass.get(),
                                                                               ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Signup successful!")
                self.var_name.set("")
                self.var_email.set("")
                self.var_secQ.set("")
                self.var_secA.set("")
                self.var_pass.set("")
                self.var_confpass.set("")

if __name__ == "__main__":
    root = Tk()
    app=Register_win(root)
    root.mainloop()