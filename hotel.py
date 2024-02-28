from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Rooms_Win
from reservation import Booking_Win
from invoice import Invoice_Win
from restaurant import Restaurant_Win

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1525x780+0+0")
        self.create_main_window()

    def create_main_window(self):
        # ================img1=======================
        img1 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\hotel1.jpg").resize((1525, 900))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=5, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1525, height=140)

        # =================logo===================
        img2 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\logo.jpg").resize((200, 140))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=5, relief=RIDGE)
        lblimg.place(x=0, y=0, width=200, height=140)

        # =================title========================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), bg="black",
                          fg="gold")
        lbl_title.place(x=0, y=140, width=1525, height=50)

        # ===================mainframe========================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1525, height=585)

        # ====================menu============================
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold")
        lbl_menu.place(x=0, y=0, width=205)

        # ====================buttons frame=============================
        btn_frame = Frame(main_frame, bd=3, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=205, height=214)

        cust_button = Button(btn_frame, text="CUSTOMERS", command=self.cust_details,
                             font=("times new roman", 13, "bold"), bg="black", fg="white", bd=1, relief=RIDGE, width=19,
                             cursor="hand1", pady=2)
        cust_button.grid(row=0, column=0)

        room_button = Button(btn_frame, text="RESERVATIONS", command=self.room_booking, font=("times new roman", 13, "bold"), bg="black", fg="white",
                             bd=1, relief=RIDGE, width=19, cursor="hand1", pady=3)
        room_button.grid(row=1, column=0)

        rooms_button = Button(btn_frame, text="ROOMS",command=self.room_details, font=("times new roman", 13, "bold"), bg="black", fg="white",
                                bd=1, relief=RIDGE, width=19, cursor="hand1", pady=3)
        rooms_button.grid(row=2, column=0)

        restaurant_button = Button(btn_frame, text="RESTAURANT", font=("times new roman", 13, "bold"),command=self.restaurant_details, bg="black", fg="white",
                               bd=1, relief=RIDGE, width=19, cursor="hand1", pady=3)
        restaurant_button.grid(row=3, column=0)

        invoice_button = Button(btn_frame, text="INVOICE", font=("times new roman", 13, "bold"), bg="black", command=self.invoice_details,
                                   fg="white",bd=1, relief=RIDGE, width=19, cursor="hand1", pady=3)
        invoice_button.grid(row=4, column=0)



        logout_button = Button(btn_frame, text="LOGOUT", font=("times new roman", 13, "bold"), bg="black", fg="white",
                               bd=1, relief=RIDGE, width=19, cursor="hand1", pady=3, command=self.logout,
                               )
        logout_button.grid(row=5, column=0)

        # ==================right side image=========================
        img3 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\hotel2.jpg").resize((1307, 580))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=208, y=0, width=1307, height=580)

        # ==================down images============================
        img4 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\hotel3.jpg").resize((205, 155))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=250, width=205, height=155)

        img5 = Image.open(r"D:\Piyu\CMRIT\mini project\HotelManagement\images\hotel4.jpg").resize((205, 250))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=370, width=205, height=205)


    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def room_booking(self):
        self.new_window = Toplevel(self.root)
        self.app = Booking_Win(self.new_window)

    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Rooms_Win(self.new_window)


    def restaurant_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Restaurant_Win(self.new_window)

    def invoice_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Invoice_Win(self.new_window)

    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
