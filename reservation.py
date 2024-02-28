from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Booking_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Rooms")
        self.root.geometry("1307x550+210+219")

        #========variables=============
        self.var_resID=StringVar()
        x = random.randint(7000, 9999)
        self.var_resID.set(str(x))


        self.var_custID=StringVar()
        self.var_roomtype = StringVar()
        self.var_roomno = StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()

        # ============title============
        lbl_title = Label(self.root, text="ROOM BOOKING", font=("times new roman", 20, "bold"), bg="black",fg="gold")
        lbl_title.place(x=0, y=0, width=1307, height=50)
        # ==========logo===============
        img2 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\logo.jpg").resize((50, 50))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2)
        lblimg.place(x=0, y=0, width=50, height=50)
        # ===========label frame================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details",font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # =========labels================================================
        reservation_id = Label(labelframeleft, text="Reservation ID",padx=10, pady=6)
        reservation_id.grid(row=0, column=0, sticky=W)
        entry_resid = Entry(labelframeleft,textvariable=self.var_resID, width=20,state="readonly")
        entry_resid.grid(row=0, column=1,sticky=W)

        lbl_custid = Label(labelframeleft, text="Customer ID", padx=10, pady=6)
        lbl_custid.grid(row=1, column=0, sticky=W)
        entry_custid = Entry(labelframeleft, textvariable=self.var_custID, width=29)
        entry_custid.grid(row=1, column=1)

        room_type = Label(labelframeleft, text="Room Type", padx=10, pady=6)
        room_type.grid(row=2, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select distinct roomType from room")
        rtype = my_cursor.fetchall()

        combo_roomtype = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, width=27, state="readonly")
        combo_roomtype["value"] = rtype
        combo_roomtype.current(0)
        combo_roomtype.grid(row=2, column=1)
        combo_roomtype.bind("<<ComboboxSelected>>", self.fetch_room_numbers)

        room_available = Label(labelframeleft, text="Room Number", padx=10, pady=6)
        room_available.grid(row=3, column=0, sticky=W)

        self.combo_roomno = ttk.Combobox(labelframeleft, textvariable=self.var_roomno, width=27, state="readonly")
        self.combo_roomno.grid(row=3, column=1)
        self.fetch_room_numbers()

        checkin_date = Label(labelframeleft, text="Check-in Date", padx=10, pady=6)
        checkin_date.grid(row=4, column=0, sticky=W)
        entry_checkin = Entry(labelframeleft, textvariable=self.var_checkin, width=29)
        entry_checkin.grid(row=4, column=1)

        checkout_date = Label(labelframeleft, text="Check-out Date", padx=10, pady=6)
        checkout_date.grid(row=5, column=0, sticky=W)
        entry_checkout = Entry(labelframeleft, textvariable=self.var_checkout, width=29)
        entry_checkout.grid(row=5, column=1)

        #========image============
        img1 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\hotel5.jpg").resize((300,200))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1)
        lblimg.place(x=995, y=60, width=300, height=200)


        # =============buttons===========
        btn_frame = Frame(labelframeleft, bd=0)
        btn_frame.place(x=10, y=350, width=400, height=90)

        btnFetch = Button(labelframeleft, text="Fetch data", command=self.fetch_cust,font=("times new roman", 8, "bold"), bg="black",
                          fg="gold", bd=1, relief=RIDGE, width=9, cursor="hand1")
        btnFetch.place(x=295, y=37)

        btnAdd = Button(btn_frame, text="Add", font=("times new roman", 13, "bold"),command=self.add_data, bg="black",fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnAdd.grid(row=1, column=0, padx=5, pady=5)

        btnUpdate = Button(btn_frame, text="Update", font=("times new roman", 13, "bold"), command=self.update,bg="black", fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnUpdate.grid(row=1, column=1, padx=5, pady=5)

        btnDelete = Button(btn_frame, text="Delete", font=("times new roman", 13, "bold"), command=self.deleteRoom,bg="black", fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnDelete.grid(row=1, column=2, padx=5, pady=5)

        btnReset = Button(btn_frame, text="Reset", font=("times new roman", 13, "bold"), bg="black", command=self.reset,fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnReset.grid(row=1, column=3, padx=5, pady=5)

        #============table frame===============
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details",font=("times new roman", 12, "bold"))
        table_frame.place(x=440, y=260, width=860, height=280)

        lbl_searchBy = Label(table_frame, text="Search By:", font=("times new roman", 11, "bold"), bg="brown", fg="white",padx=1, pady=1)
        lbl_searchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()

        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, width=15,font=("times new roman", 11, "bold"), state="readonly")
        combo_search["value"] = ("Reservation ID","Customer ID", "Room No")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.text_search = StringVar()
        txtSearch = Entry(table_frame, textvariable=self.text_search, font=("times new roman", 11, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(table_frame, text="Search",font=("times new roman", 11, "bold"), command=self.search,
                           bg="black", fg="white", width=10, cursor="hand1")
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(table_frame, text="Show All", font=("times new roman", 11, "bold"), command=self.fetch_data,bg="black", fg="white", width=10, cursor="hand1")
        btnShowAll.grid(row=0, column=4, padx=2)

        # ========================show table========================
        res_table = Frame(table_frame, bd=2, relief=RIDGE)
        res_table.place(x=4, y=50, width=847, height=200)

        scroll_x = ttk.Scrollbar(res_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(res_table, orient=VERTICAL)

        self.reservations_table = ttk.Treeview(res_table, column=(
        "resID", "custID", "roomType", "roomNo", "checkin", "checkout","no_of_days"), xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.reservations_table.xview)
        scroll_y.config(command=self.reservations_table.yview)

        self.reservations_table.heading("resID", text="Reservation ID")
        self.reservations_table.heading("custID", text="Customer ID")
        self.reservations_table.heading("roomType", text="Room Type")
        self.reservations_table.heading("roomNo", text="Room Number")
        self.reservations_table.heading("checkin", text="Check-in")
        self.reservations_table.heading("checkout", text="Check-out")
        self.reservations_table.heading("no_of_days", text="Number of Days")

        self.reservations_table["show"] = "headings"

        self.reservations_table.column("resID", width=80)
        self.reservations_table.column("custID", width=70)
        self.reservations_table.column("roomType", width=100)
        self.reservations_table.column("roomNo", width=80)
        self.reservations_table.column("checkin", width=110)
        self.reservations_table.column("checkout", width=110)
        self.reservations_table.pack(fill=BOTH, expand=1)

        self.reservations_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def get_cursor(self,event=""):
        cursor_row = self.reservations_table.focus()
        content = self.reservations_table.item(cursor_row)
        row = content["values"]

        self.var_resID.set(row[0]),
        self.var_custID.set(row[1]),
        self.var_roomtype.set(row[2]),
        self.var_roomno.set(row[3]),
        self.var_checkin.set(row[4]),
        self.var_checkout.set(row[5])

        self.reservations_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
    def fetch_room_numbers(self, event=None):
        room_type = self.var_roomtype.get()
        if room_type:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                           database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT roomno FROM room WHERE roomType=%s", (room_type,))
            rows = my_cursor.fetchall()
            room_numbers = [row[0] for row in rows]  # Extract room numbers from fetched rows
            self.var_roomno.set("")  # Clear previous selection
            self.combo_roomno["values"] = room_numbers
            conn.close()



    def add_data(self):
        if self.var_custID.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")
                my_cursor = conn.cursor()

                query = "SELECT MAX(check_out) FROM reservation WHERE roomno = %s"
                room_no = self.var_roomno.get()
                my_cursor.execute(query, (room_no,))
                max_checkout_date = my_cursor.fetchone()[0]

                checkin_date = datetime.strptime(self.var_checkin.get(), "%Y-%m-%d").date()
                checkout_date = datetime.strptime(self.var_checkout.get(), "%Y-%m-%d").date()

                if checkout_date>checkin_date:
                    if max_checkout_date is None or checkin_date > max_checkout_date:
                        my_cursor.execute(
                            "INSERT INTO reservation (reservation_id, guest_id, roomType, roomno, check_in, check_out) VALUES (%s, %s, %s, %s, %s, %s)",
                            (self.var_resID.get(), self.var_custID.get(), self.var_roomtype.get(), self.var_roomno.get(),
                             self.var_checkin.get(), self.var_checkout.get()))

                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Room booked", parent=self.root)
                        self.reset()

                    else:
                        messagebox.showerror("Error", "This room is not available", parent=self.root)
                else:
                    messagebox.showerror("Warning", "Invalid check-out date", parent=self.root)

            except Exception as es:
                messagebox.showerror("Warning", f"Something went wrong: {str(es)}", parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from reservation")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.reservations_table.delete(*self.reservations_table.get_children())
            for i in rows:
                self.reservations_table.insert("",END,values=i)
            conn.commit()
            conn.close()
        self.text_search.set("")



    def update(self):
        if self.var_custID.get()=="":
            messagebox.showerror("Error","Please enter phone number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$", database="hotel_management")
            my_cursor = conn.cursor()

            my_cursor.execute(
                "update reservation set guest_id=%s, roomType=%s, roomno=%s, check_in=%s, check_out=%s where reservation_id=%s", (
                    self.var_custID.get(),
                    self.var_roomtype.get(),
                    self.var_roomno.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_resID.get()
                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)
    def deleteRoom(self):
        deleteRoom = messagebox.askyesno("Hotel Management System","Do you want to delete this room?",parent=self.root)
        if deleteRoom>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",database="hotel_management")
            my_cursor = conn.cursor()
            query = "delete from reservation where reservation_id=%s"
            value = (self.var_resID.get(),)
            my_cursor.execute(query, value)
        else:
            if not deleteRoom:
                return

        conn.commit()
        self.fetch_data()
        conn.close()
        self.reset()

    def reset(self):
        x = random.randint(7000, 9999)
        self.var_resID.set(str(x))
        self.var_custID.set(""),
        self.var_roomno.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.text_search.set("")
        self.fetch_data()


    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$", database="hotel_management")
        my_cursor = conn.cursor()

        search_field = self.search_var.get()
        search_value = self.text_search.get()

        if search_field == "Customer ID":
            my_cursor.execute("SELECT * FROM reservation WHERE guest_id LIKE %s", ('%' + search_value + '%',))
        elif search_field == "Room No":
            my_cursor.execute("SELECT * FROM reservation WHERE roomno LIKE %s", ('%' + search_value + '%',))
        elif search_field == "Reservation ID":
            my_cursor.execute("SELECT * FROM reservation WHERE reservation_id LIKE %s", ('%' + search_value + '%',))

        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.reservations_table.delete(*self.reservations_table.get_children())
            for i in rows:
                self.reservations_table.insert("", END, values=i)

        conn.commit()
        conn.close()
    def fetch_cust(self):
        if self.var_custID.get()=="":
            messagebox.showerror("Error","Please enter Customer ID",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                           database="hotel_management")
            my_cursor = conn.cursor()
            query=("SELECT guest_name FROM guest WHERE guest_id=%s")
            value=(self.var_custID.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()


            if row==None:
                messagebox.showerror("Error","Customer ID does not exist",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2,bg="white")
                showDataFrame.place(x=445,y=58,width=400,height=190)
                lblName=Label(showDataFrame,text="Name:",font=("Arial",10,"bold"),bg="white")
                lblName.place(x=0,y=0)
                lbl=Label(showDataFrame,text = row,font=("Arial",10),bg="white")
                lbl.place(x=90,y=0)

                conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                               database="hotel_management")
                my_cursor = conn.cursor()
                query = ("SELECT gender FROM guest WHERE guest_id=%s")
                value = (self.var_custID.get(),)
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
                value = (self.var_custID.get(),)
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
                value = (self.var_custID.get(),)
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
                value = (self.var_custID.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblGender = Label(showDataFrame, text="Address:", font=("Arial", 10, "bold"),bg="white")
                lblGender.place(x=0, y=120)
                lbl5 = Label(showDataFrame, text=row, font=("Arial", 10),bg="white")
                lbl5.place(x=90, y=120)





if __name__ == "__main__":
    root = Tk()
    obj = Booking_Win(root)
    root.mainloop()