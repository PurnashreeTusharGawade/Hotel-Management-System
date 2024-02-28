from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Restaurant_Win:

    def __init__(self,root):
        self.root = root
        self.root.title("Restaurant")
        self.root.geometry("1307x550+210+219")

        # ==========variables==============
        self.var_orderid = StringVar()
        x = random.randint(100,999)
        self.var_orderid.set(str(x))

        self.var_custid = StringVar()
        self.var_category = StringVar()
        self.var_amount = StringVar()

    #============title============
        lbl_title = Label(self.root,text="RESTAURANT DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1307,height=50)
    #==========logo===============

        img2 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\logo.jpg").resize((50,50))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root,image=self.photoimg2)
        lblimg.place(x=0,y=0,width=50,height=50)
        #===========label frame================================
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
        labelframeleft.place(x=17,y=70,width=425,height=210)

        #=========labels================================================
        lbl_orderid = Label(labelframeleft, text="Order ID", padx=10, pady=6)
        lbl_orderid.grid(row=0, column=0, sticky=W)
        entry_ordID = Entry(labelframeleft, textvariable=self.var_orderid, width=29,state="readonly")
        entry_ordID.grid(row=0, column=1)

        lbl_custid = Label(labelframeleft,text="Customer ID",padx=10,pady=6)
        lbl_custid.grid(row=1,column=0,sticky=W)
        entry_custid = Entry(labelframeleft,textvariable=self.var_custid,width=29)
        entry_custid.grid(row=1,column=1)

        btnFetch = Button(labelframeleft, text="Fetch data", command=self.fetch_cust,
                          font=("times new roman", 8, "bold"), bg="black",
                          fg="white", bd=1, relief=RIDGE, width=9, cursor="hand1")
        btnFetch.grid(row=1,column=2)



        lbl_category = Label(labelframeleft, text="Meal Category", padx=10, pady=6)
        lbl_category.grid(row=3, column=0, sticky=W)
        self.combo_item = ttk.Combobox(labelframeleft, textvariable=self.var_category, width=26, state="readonly")
        self.combo_item["value"] = ("Breakfast", "Lunch", "Dinner")
        self.combo_item.grid(row=3, column=1, sticky=W)
        self.combo_item.bind("<<ComboboxSelected>>", self.update_amount)

        lbl_amount = Label(labelframeleft, text="Amount", padx=10, pady=6)
        lbl_amount.grid(row=4, column=0, sticky=W)
        entry_amount = Entry(labelframeleft, textvariable=self.var_amount, width=29,state="readonly")
        entry_amount.grid(row=4, column=1)
        self.update_amount(None)

        #=================btn frame================================================================
        btn_frame = Frame(labelframeleft,bd=0)
        btn_frame.place(x=10,y=160,width=400,height=47)

        btnAdd = Button(btn_frame,text="Add",command=self.add_data,font=("times new roman",13,"bold"),bg="black",fg="white",bd=1,relief=RIDGE,width=8,cursor="hand1")
        btnAdd.grid(row=0,column=0,padx=5,pady=5)

        btnUpdate = Button(btn_frame,text="Update",command=self.update,font=("times new roman",13,"bold"),bg="black",fg="white",bd=1,relief=RIDGE,width=8,cursor="hand1")
        btnUpdate.grid(row=0,column=1,padx=5,pady=5)

        btnDelete = Button(btn_frame, text="Delete",command=self.delete_data, font=("times new roman", 13, "bold"),bg="black", fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnDelete.grid(row=0, column=2, padx=5, pady=5)

        btnReset = Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",13,"bold"),bg="black",fg="white",bd=1,relief=RIDGE,width=8,cursor="hand1")
        btnReset.grid(row=0,column=3,padx=5,pady=5)

        #image

        img1 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\buffet.jpg")
        img1 = img1.resize((420, 240))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root,image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=19, y=290, width=420, height=240)

        #table
        table_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="View details",font=("times new roman",12,"bold"))
        table_frame.place(x=450,y=270,width=840,height=270)

        lbl_searchBy = Label(table_frame,text="Search By:",font=("times new roman",11,"bold"),bg="brown",fg="white",padx=1,pady=1)
        lbl_searchBy.grid(row=0,column=0,sticky=W,padx=5,pady=3)

        self.search_var=StringVar()

        combo_search = ttk.Combobox(table_frame,textvariable=self.search_var,width=15,font=("times new roman",11,"bold"),state="readonly")
        combo_search["value"]=("Order ID","Customer ID")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.text_search=StringVar()

        txtSearch = Entry(table_frame,textvariable=self.text_search,font=("times new roman",11,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch = Button(table_frame,text="Search",command=self.search, font=("times new roman",9,"bold"),bg="black",fg="white",width=10,cursor="hand1")
        btnSearch.grid(row=0,column=3,padx=2)

        btnShowAll = Button(table_frame,text="Show All",command=self.fetch_data,font=("times new roman",9,"bold"),bg="black",fg="white",width=10,cursor="hand1")
        btnShowAll.grid(row=0,column=4,padx=2)

        #========================show table========================
        details_table = Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=4,y=50,width=828,height=200)

        scroll_x = ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Restaurant_Table = ttk.Treeview(details_table,column=("ordID","custID","category","amt"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Restaurant_Table.xview)
        scroll_y.config(command=self.Restaurant_Table.yview)

        self.Restaurant_Table.heading("ordID",text="Order ID")
        self.Restaurant_Table.heading("custID",text="Customer ID")
        self.Restaurant_Table.heading("category",text="Meal Category")
        self.Restaurant_Table.heading("amt",text="Amount")

        self.Restaurant_Table["show"] = "headings"

        self.Restaurant_Table.column("ordID",width=60)
        self.Restaurant_Table.column("custID",width=60)
        self.Restaurant_Table.column("category",width=90)
        self.Restaurant_Table.column("amt",width=60)

        self.Restaurant_Table.pack(fill=BOTH,expand=1)
        self.Restaurant_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def update_amount(self,event):
        selected_item = self.var_category.get()
        if selected_item == "Breakfast":
            self.var_amount.set(300)
        elif selected_item == "Lunch":
            self.var_amount.set(600)
        elif selected_item == "Dinner":
            self.var_amount.set(700)

    def get_cursor(self, event=""):
        cursor_row = self.Restaurant_Table.focus()
        content = self.Restaurant_Table.item(cursor_row)
        row = content["values"]

        self.var_orderid.set(row[0]),
        self.var_custid.set(row[1]),
        self.var_category.set(row[2]),
        self.var_amount.set(row[3])

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                       database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from restaurant")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Restaurant_Table.delete(*self.Restaurant_Table.get_children())
            for i in rows:
                self.Restaurant_Table.insert("", END, values=i)
            conn.commit()
            conn.close()

    def add_data(self):
        if self.var_custid.get()=="" or self.var_category.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Piyu2003$",database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into restaurant values(%s,%s,%s,%s)", (self.var_orderid.get(),
                                                                                        self.var_custid.get(),
                                                                                        self.var_category.get(),
                                                                                        self.var_amount.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Restaurant details have been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning",f"Something went wrong:{str(es)}",parent=self.root)
            self.reset()

    def reset(self):
        self.var_custid.set(""),
        self.var_category.set(""),
        self.var_amount.set(""),
        self.text_search.set(""),
        x = random.randint(100, 999)
        self.var_orderid.set(str(x))

    def update(self):
        if self.var_custid.get()=="" or self.var_category.get()=="":
            messagebox.showerror("Error","Please enter all fields",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$", database="hotel_management")
            my_cursor = conn.cursor()

            my_cursor.execute(
                "update restaurant set guest_id=%s, meal_category=%s, amount=%s where order_id=%s", (
                    self.var_custid.get(),
                    self.var_category.get(),
                    self.var_amount.get(),
                    self.var_orderid.get()
                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Restaurant details has been updated successfully",parent=self.root)
            self.reset()

    def delete_data(self):
        delete_check = messagebox.askyesno("Hotel Management System","Do you want to delete this record?",parent=self.root)
        if delete_check:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",database="hotel_management")
            my_cursor = conn.cursor()
            query = "delete from restaurant where order_id=%s"
            value = (self.var_orderid.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
            self.reset()
    
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$", database="hotel_management")
        my_cursor = conn.cursor()

        search_field = self.search_var.get()
        search_value = self.text_search.get()

        if search_field == "Order ID":
            my_cursor.execute("SELECT * FROM restaurant WHERE order_id LIKE %s", ('%' + search_value + '%',))
        elif search_field == "Customer ID":
            my_cursor.execute("SELECT * FROM restaurant WHERE guest_id LIKE %s", ('%' + search_value + '%',))

        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.Restaurant_Table.delete(*self.Restaurant_Table.get_children())
            for i in rows:
                self.Restaurant_Table.insert("", END, values=i)

        conn.commit()
        conn.close()
    def fetch_cust(self):
        if self.var_custid.get()=="":
            messagebox.showerror("Error","Please enter Customer ID",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                           database="hotel_management")
            my_cursor = conn.cursor()
            query=("SELECT guest_name FROM guest WHERE guest_id=%s")
            value=(self.var_custid.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Customer ID does not exist",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2,bg="white")
                showDataFrame.place(x=445,y=68,width=400,height=190)
                lblName=Label(showDataFrame,text="Name:",font=("Arial",10,"bold"),bg="white")
                lblName.place(x=0,y=0)
                lbl=Label(showDataFrame,text = row,font=("Arial",10),bg="white")
                lbl.place(x=90,y=0)

                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")
                my_cursor = conn.cursor()
                query = ("SELECT gender FROM guest WHERE guest_id=%s")
                value = (self.var_custid.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblGender = Label(showDataFrame, text="Gender:", font=("Arial", 10, "bold"),bg="white")
                lblGender.place(x=0, y=30)
                lbl2 = Label(showDataFrame, text=row, font=("Arial", 10),bg="white")
                lbl2.place(x=90, y=30)

                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")
                my_cursor = conn.cursor()
                query = ("SELECT email FROM guest WHERE guest_id=%s")
                value = (self.var_custid.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblEmail = Label(showDataFrame, text="Email:", font=("Arial", 10, "bold"),bg="white")
                lblEmail.place(x=0, y=60)
                lbl3 = Label(showDataFrame, text=row, font=("Arial", 10),bg="white")
                lbl3.place(x=90, y=60)

                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")
                my_cursor = conn.cursor()
                query = ("SELECT nationality FROM guest WHERE guest_id=%s")
                value = (self.var_custid.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblNationality = Label(showDataFrame, text="Nationality:", font=("Arial", 10, "bold"),bg="white")
                lblNationality.place(x=0, y=90)
                lbl4 = Label(showDataFrame, text=row, font=("Arial", 10),bg="white")
                lbl4.place(x=90, y=90)

                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")
                my_cursor = conn.cursor()
                query = ("SELECT address FROM guest WHERE guest_id=%s")
                value = (self.var_custid.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblGender = Label(showDataFrame, text="Address:", font=("Arial", 10, "bold"),bg="white")
                lblGender.place(x=0, y=120)
                lbl5 = Label(showDataFrame, text=row, font=("Arial", 10),bg="white")
                lbl5.place(x=90, y=120)

if __name__ == "__main__":
    root = Tk()
    obj = Restaurant_Win(root)
    root.mainloop()