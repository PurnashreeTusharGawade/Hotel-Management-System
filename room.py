from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Rooms_Win:

    def __init__(self,root):
        self.root = root
        self.root.title("Reservations")
        self.root.geometry("1307x550+210+219")

        # ============title============
        lbl_title = Label(self.root, text="ADD ROOM DETAILS", font=("times new roman", 20, "bold"), bg="black",
                          fg="gold")
        lbl_title.place(x=0, y=0, width=1307, height=50)

        # ==========logo===============
        img2 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\logo.jpg").resize((50, 50))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2)
        lblimg.place(x=0, y=0, width=50, height=50)

        # ===========label frame================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Add new room",
                                    font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=490, height=350)

        lbl_roomNo = Label(labelframeleft, text="Room Number", padx=10, pady=6)
        lbl_roomNo.grid(row=0, column=0, sticky=W)
        self.var_roomno = StringVar()
        entry_roomNo = Entry(labelframeleft, textvariable=self.var_roomno, width=20)
        entry_roomNo.grid(row=0, column=1, sticky=W)

        lbl_floor = Label(labelframeleft, text="Floor", padx=10, pady=6)
        lbl_floor.grid(row=1, column=0, sticky=W)
        self.var_floor=StringVar()
        entry_floor = Entry(labelframeleft,textvariable=self.var_floor,width=20)
        entry_floor.grid(row=1, column=1, sticky=W)

        lbl_roomType = Label(labelframeleft, text="Room Type", padx=10, pady=6)
        lbl_roomType.grid(row=2, column=0, sticky=W)
        self.var_roomtype = StringVar()
        combo_roomtype = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, width=17, state="readonly")
        combo_roomtype["value"] = ("Single", "Double", "Suite", "Deluxe")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=2, column=1, sticky=W)

        lbl_price = Label(labelframeleft, text="Price", padx=10, pady=6)
        lbl_price.grid(row=3, column=0, sticky=W)
        self.var_price = StringVar()
        entry_price = Entry(labelframeleft, textvariable=self.var_price, width=20)
        entry_price.grid(row=3, column=1, sticky=W)

        lbl_capacity = Label(labelframeleft, text="Room Capacity", padx=10, pady=6)
        lbl_capacity.grid(row=4, column=0, sticky=W)
        self.var_capacity = StringVar()
        entry_capacity = Entry(labelframeleft, textvariable=self.var_capacity, width=20)
        entry_capacity.grid(row=4, column=1, sticky=W)



        # =============buttons===========
        btn_frame = Frame(labelframeleft, bd=0)
        btn_frame.place(x=10, y=200, width=400, height=90)

        btnAdd = Button(btn_frame, text="Add", font=("times new roman", 13, "bold"), bg="black",command=self.add_data,
                        fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnAdd.grid(row=1, column=0, padx=5, pady=5)

        btnUpdate = Button(btn_frame, text="Update", font=("times new roman", 13, "bold"), command=self.update,
                           bg="black", fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnUpdate.grid(row=1, column=1, padx=5, pady=5)

        btnDelete = Button(btn_frame, text="Delete", font=("times new roman", 13, "bold"),command=self.deleteRoom,
                           bg="black", fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnDelete.grid(row=1, column=2, padx=5, pady=5)

        btnReset = Button(btn_frame, text="Reset", font=("times new roman", 13, "bold"), bg="black", command=self.reset,
                          fg="white", bd=1, relief=RIDGE, width=8, cursor="hand1")
        btnReset.grid(row=1, column=3, padx=5, pady=5)

        #========table frame============
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show room details",
                                 font=("times new roman", 12, "bold"))
        table_frame.place(x=510, y=50, width=600, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(table_frame, column=("roomno", "floor", "roomtype","price","capacity"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("price", text="Price")
        self.room_table.heading("capacity", text="Capacity")

        self.room_table["show"] = "headings"

        self.room_table.column("roomno", width=80)
        self.room_table.column("floor", width=80)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("price", width=80)
        self.room_table.column("capacity", width=80)


        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Piyu2003$",database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s)",(self.var_roomno.get(),
                                                                                        self.var_floor.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_price.get(),
                                                                                        self.var_capacity.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room details added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning",f"Something went wrong:{str(es)}",parent=self.root)



    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        self.var_roomno.set(row[0]),
        self.var_floor.set(row[1]),
        self.var_roomtype.set(row[2]),
        self.var_price.set(row[3]),
        self.var_capacity.set(row[4]),

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter floor", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",
                                           database="hotel_management")
            my_cursor = conn.cursor()

            my_cursor.execute(
                "update room set floor=%s, roomType=%s, price=%s, capacity=%s where roomno=%s",
                (
                    self.var_floor.get(),
                    self.var_roomtype.get(),
                    self.var_price.get(),
                    self.var_capacity.get(),
                    self.var_roomno.get()
                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details has been updated successfully", parent=self.root)

    def deleteRoom(self):
        deleteRoom = messagebox.askyesno("Hotel Management System","Do you want to delete this room?",parent=self.root)
        if deleteRoom>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Piyu2003$",database="hotel_management")
            my_cursor = conn.cursor()
            query = "delete from room where roomno=%s"
            value = (self.var_roomno.get(),)
            my_cursor.execute(query, value)
            self.var_floor.set(""),
            self.var_roomtype.set(""),
            self.var_roomno.set(""),
            self.var_price.set(""),
            self.var_capacity.set("")

        else:
            if not deleteRoom:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set(""),
        #self.var_roomtype.set(""),
        self.var_roomno.set(""),
        self.var_price.set(""),
        self.var_capacity.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Rooms_Win(root)
    root.mainloop()