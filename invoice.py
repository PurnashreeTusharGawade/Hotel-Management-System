from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Invoice_Win:

    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant")
        self.root.geometry("1307x550+210+219")

        # ==========variables==============
        self.var_reservationID = StringVar()


        # ============title============
        lbl_title = Label(self.root, text="INVOICE", font=("times new roman", 20, "bold"), bg="black",
                          fg="gold")
        lbl_title.place(x=0, y=0, width=1307, height=50)
        # ==========logo===============
        img2 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\logo.jpg").resize((50, 50))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2)
        lblimg.place(x=0, y=0, width=50, height=50)
        # ===========label frame================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, font=("times new roman", 12, "bold"))
        labelframeleft.place(x=17, y=70, width=425, height=210)

        # =========labels================================================
        lbl_resID = Label(labelframeleft, text="Reservation ID",font=("times new roman", 13, "bold"), padx=10, pady=10)
        lbl_resID.place(x=10,y=20)
        entry_resID = Entry(labelframeleft, textvariable=self.var_reservationID,font=("times new roman", 12), width=29)
        entry_resID.place(x=150,y=29)


        # =================btn frame================================================================
        btn_frame = Frame(labelframeleft, bd=0)
        btn_frame.place(x=100, y=120, width=200, height=47)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("times new roman", 13, "bold"), bg="black",
                        fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnAdd.grid(row=0, column=0, padx=5, pady=5)


        btnDelete = Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman", 13, "bold"),
                           bg="black", fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnDelete.grid(row=0, column=2, padx=5, pady=5)


        # image
        img1 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\receipt.png")
        img1 = img1.resize((240, 240))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root,image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=19, y=290, width=420, height=240)

        # table
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details",
                                 font=("times new roman", 12, "bold"))
        table_frame.place(x=450, y=60, width=840, height=470)

        lbl_searchBy = Label(table_frame, text="Search By:", font=("times new roman", 11, "bold"), bg="brown",
                             fg="white", padx=1, pady=1)
        lbl_searchBy.grid(row=0, column=0, sticky=W, padx=5, pady=3)

        self.search_var = StringVar()

        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, width=15,
                                    font=("times new roman", 11, "bold"), state="readonly")
        combo_search["value"] = ("Reservation ID",)
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.text_search = StringVar()

        txtSearch = Entry(table_frame, textvariable=self.text_search, font=("times new roman", 11, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnGenerate = Button(table_frame, text="Generate Bill",command=self.generate, font=("times new roman", 9, "bold"),
                           bg="black", fg="white", width=15, cursor="hand1")
        btnGenerate.grid(row=0, column=3, padx=5)


        # ========================show table========================
        invoice_table = Frame(table_frame, bd=2, relief=RIDGE)
        invoice_table.place(x=4, y=50, width=828, height=390)

        scroll_x = ttk.Scrollbar(invoice_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(invoice_table, orient=VERTICAL)

        self.invoice_table = ttk.Treeview(invoice_table, column=("resID", "custID", "roomno", "checkin", "checkout","foodbill","roombill","total"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.invoice_table.xview)
        scroll_y.config(command=self.invoice_table.yview)

        self.invoice_table.heading("resID", text="Reservation ID")
        self.invoice_table.heading("custID", text="Customer ID")
        self.invoice_table.heading("roomno", text="Room Number")
        self.invoice_table.heading("checkin", text="Check-in")
        self.invoice_table.heading("checkout", text="Check-out")
        self.invoice_table.heading("foodbill", text="Restaurant Bill")
        self.invoice_table.heading("roombill", text="Room Bill")
        self.invoice_table.heading("total", text="Total")


        self.invoice_table["show"] = "headings"

        self.invoice_table.column("resID", width=90)
        self.invoice_table.column("custID", width=90)
        self.invoice_table.column("roomno", width=80)
        self.invoice_table.column("checkin", width=100)
        self.invoice_table.column("checkout", width=100)
        self.invoice_table.column("foodbill", width=90)
        self.invoice_table.column("roombill", width=90)
        self.invoice_table.column("total", width=80)


        self.invoice_table.pack(fill=BOTH, expand=1)
        self.invoice_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                       database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from invoice")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.invoice_table.delete(*self.invoice_table.get_children())
            for i in rows:
                self.invoice_table.insert("", END, values=i)
            conn.commit()
            conn.close()

    def add_data(self):
        if self.var_reservationID.get() == "":
            messagebox.showerror("Error", "Please enter Reservation ID")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")
                my_cursor = conn.cursor()

                query = '''
                    SELECT r.reservation_id, r.guest_id, r.roomno, r.check_in, r.check_out, rs.FoodBill, r.no_of_days * ro.price AS roomPrice
                    FROM reservation AS r
                    JOIN (SELECT guest_id, SUM(amount) AS FoodBill FROM restaurant GROUP BY guest_id) AS rs ON r.guest_id = rs.guest_id
                    JOIN room AS ro ON r.roomno = ro.roomno
                    WHERE r.reservation_id = %s
                '''

                value = (self.var_reservationID.get(),)
                my_cursor.execute(query, value)
                rows = my_cursor.fetchone()

                if rows!=None:
                    reservation_id = rows[0]
                    guest_id = rows[1]
                    roomno = rows[2]
                    check_in = rows[3]
                    check_out = rows[4]
                    food_bill = rows[5]
                    room_price = rows[6]

                    query2 = "INSERT INTO invoice(reservation_id,guest_id,roomno,check_in,check_out,foodbill,roombill) values(%s,%s,%s,%s,%s,%s,%s)"
                    values2 = (reservation_id,guest_id,roomno,check_in,check_out,food_bill,room_price)
                    my_cursor.execute(query2,values2)
                    messagebox.showinfo("Success", "Invoice details have been added", parent=self.root)

                else:
                    query = '''
                        SELECT r.reservation_id, r.guest_id, r.roomno, r.check_in, r.check_out, r.no_of_days * ro.price AS roomPrice
                        FROM reservation r
                        JOIN room ro ON r.roomno = ro.roomno
                        WHERE r.reservation_id = %s;
                    '''
                    value=(self.var_reservationID.get(),)
                    my_cursor.execute(query,value)
                    rows = my_cursor.fetchone()
                    reservation_id = rows[0]
                    guest_id = rows[1]
                    roomno = rows[2]
                    check_in = rows[3]
                    check_out = rows[4]
                    food_bill = 0
                    room_price = rows[5]
                    query2 = "INSERT INTO invoice(reservation_id,guest_id,roomno,check_in,check_out,foodbill,roombill) values(%s,%s,%s,%s,%s,%s,%s)"
                    values2 = (reservation_id, guest_id, roomno, check_in, check_out, food_bill, room_price)
                    my_cursor.execute(query2, values2)
                    messagebox.showinfo("Success", "Invoice details have been added", parent=self.root)
                conn.commit()
                conn.close()

            except Exception as es:
                    messagebox.showerror("Warning", f"Something went wrong: {str(es)}", parent=self.root)

        self.fetch_data()
        self.reset()

    def reset(self):
        self.var_reservationID.set(""),




    def delete_data(self):
        delete_check = messagebox.askyesno("Hotel Management System", "Do you want to delete this record?",
                                           parent=self.root)
        if delete_check:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                           database="hotel_management")
            my_cursor = conn.cursor()
            query = "delete from invoice where reservation_id=%s"
            value = (self.var_reservationID.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
            self.reset()

    def generate(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                       database="hotel_management")
        my_cursor = conn.cursor()

        search_field = self.search_var.get()
        search_value = self.text_search.get()


        if search_field == "Reservation ID":
            my_cursor.execute("SELECT * FROM details WHERE reservation_id = %s", (search_value,))

            rows = my_cursor.fetchone()


            if rows!=None:
                self.root2 = Toplevel()
                self.root2.title("Generate invoice")
                self.root2.geometry("800x200+670+380")
                lbl = Label(self.root2, text="Invoice", font=("times new roman", 20, "bold"), fg="black", bg="white")
                lbl.place(x=0, y=10, relwidth=1)
                self.view_table = Frame(self.root2, bd=2, relief=RIDGE)
                self.view_table.place(x=4, y=90, width=790, height=90)

                self.view_table = ttk.Treeview(self.view_table, column=("resID", "custID", "custname", "total"))

                self.view_table.heading("resID", text="Reservation ID")
                self.view_table.heading("custID", text="Customer ID")
                self.view_table.heading("custname", text="Customer Name")
                self.view_table.heading("total", text="Total")

                self.view_table["show"] = "headings"

                self.view_table.column("resID", width=90)
                self.view_table.column("custID", width=90)
                self.view_table.column("custname",width=80)
                self.view_table.column("total", width=80)

                self.view_table.pack(fill=BOTH, expand=1)
                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")

                self.view_table.delete(*self.view_table.get_children())

                self.view_table.insert("", END, values=rows)
                conn.commit()
                conn.close()
            else:
                messagebox.showerror("Error", "Please enter valid reservation id", parent=self.root)



    def get_cursor(self,event=""):
        cursor_row = self.invoice_table.focus()
        content = self.invoice_table.item(cursor_row)
        row = content["values"]
        self.var_reservationID.set(row[0])


"""    def fetch_cust(self):
        if self.var_custid.get() == "":
            messagebox.showerror("Error", "Please enter Customer ID", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                           database="hotel_management")
            my_cursor = conn.cursor()
            query = ("SELECT guest_name FROM guest WHERE guest_id=%s")
            value = (self.var_custid.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Customer ID does not exist", parent=self.root)
            else:
                conn.commit()
                conn.close()
                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2, bg="white")
                showDataFrame.place(x=445, y=68, width=400, height=190)
                lblName = Label(showDataFrame, text="Name:", font=("Arial", 10, "bold"), bg="white")
                lblName.place(x=0, y=0)
                lbl = Label(showDataFrame, text=row, font=("Arial", 10), bg="white")
                lbl.place(x=90, y=0)

                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")
                my_cursor = conn.cursor()
                query = ("SELECT gender FROM guest WHERE guest_id=%s")
                value = (self.var_custid.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblGender = Label(showDataFrame, text="Gender:", font=("Arial", 10, "bold"), bg="white")
                lblGender.place(x=0, y=30)
                lbl2 = Label(showDataFrame, text=row, font=("Arial", 10), bg="white")
                lbl2.place(x=90, y=30)

                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")
                my_cursor = conn.cursor()
                query = ("SELECT email FROM guest WHERE guest_id=%s")
                value = (self.var_custid.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblEmail = Label(showDataFrame, text="Email:", font=("Arial", 10, "bold"), bg="white")
                lblEmail.place(x=0, y=60)
                lbl3 = Label(showDataFrame, text=row, font=("Arial", 10), bg="white")
                lbl3.place(x=90, y=60)

                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")
                my_cursor = conn.cursor()
                query = ("SELECT nationality FROM guest WHERE guest_id=%s")
                value = (self.var_custid.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblNationality = Label(showDataFrame, text="Nationality:", font=("Arial", 10, "bold"), bg="white")
                lblNationality.place(x=0, y=90)
                lbl4 = Label(showDataFrame, text=row, font=("Arial", 10), bg="white")
                lbl4.place(x=90, y=90)

                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")
                my_cursor = conn.cursor()
                query = ("SELECT address FROM guest WHERE guest_id=%s")
                value = (self.var_custid.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblGender = Label(showDataFrame, text="Address:", font=("Arial", 10, "bold"), bg="white")
                lblGender.place(x=0, y=120)
                lbl5 = Label(showDataFrame, text=row, font=("Arial", 10), bg="white")
                lbl5.place(x=90, y=120)
"""

if __name__ == "__main__":
    root = Tk()
    obj = Invoice_Win(root)
    root.mainloop()