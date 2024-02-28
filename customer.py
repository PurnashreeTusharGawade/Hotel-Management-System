from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Cust_Win:

    def __init__(self,root):
        self.root = root
        self.root.title("Customer")
        self.root.geometry("1307x550+210+219")

        # ==========variables==============
        self.var_id = StringVar()
        x = random.randint(1000,7000)
        self.var_id.set(str(x))

        self.var_cust_name = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()

    #============title============
        lbl_title = Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1307,height=50)
#==========logo===============
        img2 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\logo.jpg").resize((50,50))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root,image=self.photoimg2)
        lblimg.place(x=0,y=0,width=50,height=50)
        #===========label frame================================
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer details",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #=========labels================================================
        lbl_custid = Label(labelframeleft,text="Customer ID",padx=10,pady=6)
        lbl_custid.grid(row=0,column=0,sticky=W)
        entry_custid = Entry(labelframeleft,textvariable=self.var_id,width=29,state="readonly")
        entry_custid.grid(row=0,column=1)

        lbl_cname = Label(labelframeleft,text="Customer Name",padx=10,pady=6)
        lbl_cname.grid(row=1,column=0,sticky=W)
        entry_cname = Entry(labelframeleft,textvariable=self.var_cust_name,width=29)
        entry_cname.grid(row=1,column=1)

        lbl_custphone = Label(labelframeleft,text="Phone Number",padx=10,pady=6)
        lbl_custphone.grid(row=2,column=0,sticky=W)
        entry_custphone = Entry(labelframeleft,textvariable=self.var_phone,width=29)
        entry_custphone.grid(row=2,column=1)

        lbl_custemail = Label(labelframeleft,text="Email",padx=10,pady=6)
        lbl_custemail.grid(row=3,column=0,sticky=W)
        entry_custemail = Entry(labelframeleft,textvariable=self.var_email,width=29)
        entry_custemail.grid(row=3,column=1)

        #=====gender===============================================
        lbl_custgender = Label(labelframeleft,text="Gender",padx=10,pady=6)
        lbl_custgender.grid(row=4,column=0,sticky=W)
        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender,width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1)

        #=======nationality=========
        lbl_cnationality = Label(labelframeleft,text="Nationality",padx=10,pady=6)
        lbl_cnationality.grid(row=5,column=0,sticky=W)
        combo_nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality,width=27,state="readonly")
        combo_nationality["value"]=("Indian","American","British")
        combo_nationality.current(0)
        combo_nationality.grid(row=5,column=1)


        lbl_addr = Label(labelframeleft,text="Address",padx=10,pady=6)
        lbl_addr.grid(row=6,column=0,sticky=W)
        entry_addr = Entry(labelframeleft,textvariable=self.var_address,width=29)
        entry_addr.grid(row=6,column=1)

        #=================btn frame================================================================
        btn_frame = Frame(labelframeleft,bd=0)
        btn_frame.place(x=10,y=400,width=400,height=47)

        btnAdd = Button(btn_frame,text="Add",command=self.add_data,font=("times new roman",13,"bold"),bg="black",fg="white",bd=1,relief=RIDGE,width=8,cursor="hand1")
        btnAdd.grid(row=0,column=0,padx=5,pady=5)

        btnUpdate = Button(btn_frame,text="Update",command=self.update,font=("times new roman",13,"bold"),bg="black",fg="white",bd=1,relief=RIDGE,width=8,cursor="hand1")
        btnUpdate.grid(row=0,column=1,padx=5,pady=5)

        btnDelete = Button(btn_frame, text="Delete", command=self.deleteCust, font=("times new roman", 13, "bold"),bg="black", fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnDelete.grid(row=0, column=2, padx=5, pady=5)

        btnReset = Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",13,"bold"),bg="black",fg="white",bd=1,relief=RIDGE,width=8,cursor="hand1")
        btnReset.grid(row=0,column=3,padx=5,pady=5)

        #======================table frame========================
        table_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="View details",font=("times new roman",12,"bold"))
        table_frame.place(x=440,y=50,width=860,height=490)

        lbl_searchBy = Label(table_frame,text="Search By:",font=("times new roman",11,"bold"),bg="brown",fg="white",padx=1,pady=1)
        lbl_searchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_search = ttk.Combobox(table_frame,textvariable=self.search_var,width=15,font=("times new roman",11,"bold"),state="readonly")
        combo_search["value"]=("Mobile","Id")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.text_search=StringVar()
        txtSearch = Entry(table_frame,textvariable=self.text_search,font=("times new roman",11,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch = Button(table_frame,text="Search",command=self.search,font=("times new roman",11,"bold"),bg="black",fg="white",width=10,cursor="hand1")
        btnSearch.grid(row=0,column=3,padx=2)

        btnShowAll = Button(table_frame,text="Show All",command=self.fetch_data,font=("times new roman",11,"bold"),bg="black",fg="white",width=10,cursor="hand1")
        btnShowAll.grid(row=0,column=4,padx=2)

        #========================show table========================
        details_table = Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=4,y=50,width=847,height=350)

        scroll_x = ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table,column=("id","name","phone","email","gender","nationality","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("id",text="Customer ID")
        self.Cust_Details_Table.heading("name",text="Customer Name")
        self.Cust_Details_Table.heading("phone",text="Phone Number")
        self.Cust_Details_Table.heading("email",text="Email id")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("id",width=50)
        self.Cust_Details_Table.column("name",width=110)
        self.Cust_Details_Table.column("phone",width=100)
        self.Cust_Details_Table.column("email",width=120)
        self.Cust_Details_Table.column("gender",width=50)
        self.Cust_Details_Table.column("nationality",width=80)
        self.Cust_Details_Table.column("address",width=150)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_data(self):
        if self.var_phone.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Piyu2003$",database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into guest values(%s,%s,%s,%s,%s,%s,%s)", (self.var_id.get(),
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from guest")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
            conn.close()
    def get_cursor(self,event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_id.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_phone.set(row[2]),
        self.var_email.set(row[3]),
        self.var_gender.set(row[4]),
        self.var_nationality.set(row[5]),
        self.var_address.set(row[6])
    def update(self):
        if self.var_phone.get()=="":
            messagebox.showerror("Error","Please enter phone number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$", database="hotel_management")
            my_cursor = conn.cursor()

            my_cursor.execute(
                "update guest set guest_name=%s, phone=%s, email=%s, gender=%s, nationality=%s, address=%s where guest_id=%s", (
                    self.var_cust_name.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_nationality.get(),
                    self.var_address.get(),
                    self.var_id.get()
                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)

    def deleteCust(self):
        deleteCust = messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
        if deleteCust:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",database="hotel_management")
            my_cursor = conn.cursor()
            query = "delete from guest where guest_id=%s"
            value = (self.var_id.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
            self.reset()
    def reset(self):
        self.var_cust_name.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_id.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$", database="hotel_management")
        my_cursor = conn.cursor()

        search_field = self.search_var.get()
        search_value = self.text_search.get()

        if search_field == "Mobile":
            my_cursor.execute("SELECT * FROM guest WHERE phone LIKE %s", ('%' + search_value + '%',))
        elif search_field == "Id":
            my_cursor.execute("SELECT * FROM guest WHERE guest_id LIKE %s", ('%' + search_value + '%',))

        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)

        conn.commit()
        conn.close()
if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()