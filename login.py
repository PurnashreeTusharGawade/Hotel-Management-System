from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from hotel import HotelManagementSystem

def main():
    win=Tk()
    app=login_win(win)
    win.mainloop()
class login_win:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1523x780+0+0")

        self.bg = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\login-bg.jpg").resize((1523, 780))
        self.bg = ImageTk.PhotoImage(self.bg)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root,bg="#011F5B")
        frame.place(x=580, y=130,width=340, height=500)

        img1 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\profile.png")
        img1 = img1.resize((90,90))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg="#011F5B",borderwidth=0)
        lblimg1.place(x=700,y=165,width=90,height=90)

        get_str = Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="#FCF75E",bg="#011F5B")
        get_str.place(x=95,y=120)

        #labels
        username_lbl = Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="#011F5B")
        username_lbl.place(x=50,y=175)

        self.txtuser=Entry(frame,font=("times new roman",12))
        self.txtuser.place(x=50,y=207,width=240)

        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="#011F5B")
        password_lbl.place(x=50, y=245)

        self.txtpass = Entry(frame,show="*",font=("times new roman", 12))
        self.txtpass.place(x=50, y=277, width=240)

        #buttons
        loginBtn = Button(frame,text="Login", command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RAISED,fg="white",bg="#C51E3A",cursor="hand2")
        loginBtn.place(x=115,y=330,width=100,height=30)

        registerBtn = Button(frame, text="Sign Up",command=self.signup_win, font=("times new roman", 10, "bold"),bd=0, fg="white",activeforeground="white",activebackground="#011F5B",
                          bg="#011F5B",cursor="hand2")
        registerBtn.place(x=115, y=370, width=100, height=30)

        registerBtn = Button(frame, text="Forgot Password", command=self.forgot_password_window, font=("times new roman", 10, "bold"), bd=0,
                             fg="white", activeforeground="white", activebackground="#011F5B",
                             bg="#011F5B", cursor="hand2")
        registerBtn.place(x=115, y=400, width=100, height=30)

    def reset_password(self):
        if self.combo_secQ.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.sa_entry.get()=="":
            messagebox.showerror("Error", "Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                           database="hotel_management")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM signup WHERE email=%s and secq=%s and seca=%s")
            value = (self.txtuser.get(),self.combo_secQ.get(),self.sa_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query = ("UPDATE signup SET password=%s WHERE email=%s")
                value = (self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been reset!",parent=self.root2)
                self.root2.destroy()


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                           database="hotel_management")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM signup WHERE email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x500+580+130")

                lbl = Label(self.root2,text="Forgot Password",font=("times new roman", 20, "bold"),fg="red",bg="white")
                lbl.place(x=0, y=10, relwidth=1)

                securityq = Label(self.root2, text="Security Question", font=("times new roman", 14, "bold"),
                                  bg="aliceblue")
                securityq.place(x=50, y=80)

                self.combo_secQ = ttk.Combobox(self.root2, font=("times new roman", 14),
                                               state="readonly")
                self.combo_secQ["values"] = ("Select", "Your birth place", "Your favourite food", "Your pet name")
                self.combo_secQ.place(x=50, y=110, width=250)
                self.combo_secQ.current(0)

                securityans = Label(self.root2, text="Security Answer", font=("times new roman", 14, "bold"),
                                    bg="aliceblue")
                securityans.place(x=50, y=150)
                self.sa_entry = Entry(self.root2, font=("times new roman", 14))
                self.sa_entry.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 14, "bold"),
                                    bg="aliceblue")
                new_password.place(x=50, y=220)
                self.txt_newpass = Entry(self.root2, font=("times new roman", 14),show="*")
                self.txt_newpass.place(x=50, y=250, width=250)

                resetbtn = Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman", 14),fg="white",bg="green")
                resetbtn.place(x=130,y=290,width=80)




    def signup_win(self):
        self.new_win = Toplevel(self.root)
        self.app = Register_win(self.new_win)
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","Please enter all fields")

        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                           database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from signup where email=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                self.new_win = Toplevel(self.root)
                self.app = HotelManagementSystem(self.new_win)

            conn.commit()
            conn.close()
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
        lblimg1 = Label(frame,image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=7, y=250, width=450, height=300)

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
        loginBtn = Button(leftframe, text="Login",command=self.return_login, font=("times new roman", 13, "bold"), bd=0, fg="blue",
                             activeforeground="blue", activebackground="aliceblue",
                             bg="aliceblue", cursor="hand2")
        loginBtn.place(x=370, y=460, width=100, height=30)

    def signup(self):
        if self.var_name.get() == "" or self.var_email.get() == "" or self.var_secQ.get() == "Select":
            messagebox.showerror("Error", "Please enter all fields",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Passwords do not match",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                           database="hotel_management")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM signup WHERE email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row != None:
                messagebox.showerror("Error", "User already exists, please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into signup values(%s,%s,%s,%s,%s)", (self.var_name.get(),
                                                                                self.var_email.get(),
                                                                                self.var_secQ.get(),
                                                                                self.var_secA.get(),
                                                                                self.var_pass.get(),
                                                                                ))

                messagebox.showinfo("Success", "Sign Up successful!",parent=self.root)
                # Clear the entry fields
                self.var_name.set("")
                self.var_email.set("")
                self.var_secQ.set("")
                self.var_secA.set("")
                self.var_pass.set("")
                self.var_confpass.set("")
            conn.commit()
            conn.close()
    def return_login(self):
        self.root.destroy()





if __name__ == "__main__":
    main()