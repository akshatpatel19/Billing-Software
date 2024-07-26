from tkinter import *
from tkinter import ttk
from tkinter import Tk
import random, os
from tkinter import messagebox
import tempfile
import datetime

class Bill_App:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        # ===============Variables==============
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        z = random.randint(1000, 1000000000)
        self.bill_no.set(z)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()



        # Product Categories list

        self.Category = ["Select Option", "Acessories", "Earphones", "Mobiles"]

        self.SubCatClothing = ["Cables", "Pendrives", "Other"]
        self.pant = ["USB          ", "TYPE C       ", "MICRO USB    "]

        self.price_usb = 200, 250

        self.price_typec = 300

        self.price_microusb = 250

        self.T_shirt = ['Sandisk      ', 'HP           ', 'Sony         ']

        self.price_sandisk = 1500

        self.price_hp = 1800

        self.price_sony = 1700

        self.Shirt = ['HDMI Cable   ', 'OTG          ', 'Cover        ']

        self.price_hdmi = 250

        self.price_otg = 50, 80

        self.price_cover = 250, 315

        #SubCatLifstyle

        self.SubCatLifStyle = ['Boat', 'Realme', 'Oneplus Earphones']

        self.Bath_soap = ['Rockerz 235v2', 'Rockerz 450  ', 'Airdopes 101 ', 'Rockerz 335  ']

        self.price_235v2 = 1200

        self.price_450 = 1400

        self.price_ad101 = 1300

        self.price_335 = 1600

        self.Face_creame = ['Buds Air 2   ', 'Buds Q       ', 'Buds Air Neo  ', 'Buds Wireless']

        self.price_air2 = 3300

        self.price_budsq = 2000

        self.price_airneo = 2500

        self.price_wireless = 1800

        self.Hair_oil = ['Buds         ', 'Buds Z       ', 'Bullets      ']

        self.price_buds = 5000

        self.price_budsz = 3000

        self.price_bullets = 2000

        # SubCatMobiles

        self.SubCatMobiles = ['Iphone', 'Samsung', 'Xiome', 'RealMe', 'Oneplus', 'Oppo']

        self.Iphone = ['Iphone X     ', 'Iphone_11    ', 'Iphone_12    ']

        self.price_ix = 40000

        self.price_i11 = 60000

        self.price_112 = 85000

        self.Samsung = ['Samsung M16  ', 'Samsung M12  ', 'Samsung M21  ']

        self.price_sm16 = 16000

        self.price_sm12 = 12000

        self.price_sm21 = 18000

        self.Xiome = ['Redmi Note 9 ', 'Mi 10i       ', 'Redmi 9 Pro  ']

        self.price_note9 = 11500

        self.price_mi10i = 24000

        self.price_note9pro = 14000

        self.RealMe = ['RealMe 8     ', 'RealMe 8 Pro ', 'RealMe 7 Pro ']

        self.price_rel8 = 16000

        self.price_rel8pro = 18000

        self.price_relpro = 22000

        self.OnePlus = ['OnePlus Nord ', 'OnePlus 9    ', 'OnePlus 9 Pro']

        self.price_onenord = 30000

        self.price_one9 = 55000

        self.price_one9pro = 70000

        self.Oppo = ['Oppo F19 Pro ', 'Reno 6       ', 'Reno 6 Pro   ']

        self.price_f19pro = 21500

        self.price_reno6 = 30000

        self.price_reno6pro = 40000

        # SubCatClothing
        # self.SubCatClothing = ["Pant", "T-Shirt", "Shirt"]
        # self.pant = ["Levis", "Mufti", "Spykar"]
        #
        # self.price_levis = 5000
        #
        # self.price_mufti = 7000
        #
        # self.price_spaykar = 8000
        #
        # self.T_shirt = ['Polo', 'Roadster', 'Jack&Jones']
        #
        # self.price_polo = 1500
        #
        # self.price_Roadster = 1800
        #
        # self.price_JackJones = 1700
        #
        # self.Shirt = ['Peter England', 'Louis Phillipe', 'Park Avenue']
        #
        # self.price_Peter = 2100
        #
        # self.price_Louis = 2700
        #
        # self.price_Park = 1740

        # SubCatLifstyle
        #
        # self.SubCatLifStyle = ['Bath Soap', 'Face Creame', 'Hair Oil']
        #
        # self.Bath_soap = ['LifeBuy', 'Lux', 'Santoor', 'Pearl']
        #
        # self.price_life = 20
        #
        # self.price_lux = 20
        #
        # self.price_santoor = 29
        #
        # self.price_pearl = 30
        #
        # self.Face_creame = ['Fair&Lovely', 'Ponds', 'Olay', 'Garnier']
        #
        # self.price_fair = 20
        #
        # self.price_ponds = 20
        #
        # self.price_olay = 20
        #
        # self.price_garnier = 30
        #
        # self.Hair_oil = ['Parachute', 'Jashmin', 'Bajaj']
        #
        # self.price_para = 25
        #
        # self.price_jashmin = 22
        #
        # self.price_bajaj = 30

        # # SubCatMobiles
        #
        # self.SubCatMobiles = ['Iphone', 'Sumsung', 'Xiome', 'RealMe', 'One+']
        #
        # self.Iphone = ['Iphone X', 'Iphone_11', 'Iphone_12']
        #
        # self.price_ix = 40000
        #
        # self.price_i11 = 60000
        #
        # self.price_112 = 85000
        #
        # self.Samsung = ['Samsung M16', 'Sumsung M12', 'Sumsung M21']
        #
        # self.price_sm16 = 16000
        #
        # self.price_sm12 = 12000
        #
        # self.price_sm21 = 18000
        #
        # self.Xiome = ['Red11', 'Redme-12', 'RedmePro']
        #
        # self.price_r11 = 11000
        #
        # self.price_r12 = 12000
        #
        # self.price_rpro = 9000
        #
        # self.RealMe = ['RealMe 12', 'RealMe 13', 'RealMe Pro']
        #
        # self.price_rel12 = 25000
        #
        # self.price_rel13 = 22000
        #
        # self.price_relpro = 30000
        #
        # self.OnePlus = ['OnePlus1', 'OnePlus2', 'OnePlus3']
        #
        # self.price_one1 = 45000
        #
        # self.price_one12 = 60000
        #
        # self.price_one3 = 45800

        lbl_title=Label(self.root, text="BILLING SOFTWARE BY REIGNING RESOLUTION", font=("times new roman", 35, "bold"), bg="white", fg="red")
        lbl_title.place(x=0, y=0, width=1275, height=45)

        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Main_Frame.place(x=0, y=45, width=1530, height=620)


        #Customer Label Frame
        Cust_Frame = LabelFrame(Main_Frame, text = "Customer", font=("arial", 17, "bold"), bg="white", fg="red")
        Cust_Frame.place(x=10, y=5, width=370, height=160)

        # Mobile No.
        self.lbl_mob = Label(Cust_Frame, text="Mobile No.", font = ("arial", 13, "bold"), bg="white")
        self.lbl_mob.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame, textvariable=self.c_phone, font=("times new roman", 13, "bold"),width=20)
        self.entry_mob.grid(row=0, column=1)

        # Name
        self.lblCustName = Label(Cust_Frame, text="Customer Name", font=('arial', 13, 'bold'), bg="white", bd=4)
        self.lblCustName.grid(row=1, column=0,stick=W, padx=5, pady=2)

        self.txtCustName = ttk.Entry(Cust_Frame,textvariable=self.c_name, font=("arial", 13, "bold"), width=20)
        self.txtCustName.grid(row=1, column=1, stick=W, padx=5, pady=2)

        # Email
        self.lblEmail = Label(Cust_Frame, text="Email", font=('arial', 13, "bold"), bg="white", bd=4)
        self.lblEmail.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.txtEmail = ttk.Entry(Cust_Frame, textvariable=self.c_email, font=("arial", 13, "bold"), width=20)
        self.txtEmail.grid(row=2, column=1, stick=W, padx=5, pady=2)

        # Product Label Frame
        Product_Frame = LabelFrame(Main_Frame, text="Product", font=("times new roman", 17, "bold"), bg="white", fg="red")
        Product_Frame.place(x=400, y=5, width=400, height=160)

        # Category
        self.lblCategory = Label(Product_Frame, text="Select Categories", font=('arial', 13, "bold"), bg="white", bd=4)
        self.lblCategory.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category, font=('arial', 13, "bold"), width=20, state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1, sticky=W, padx=5, pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        # SubCategory
        self.lblSubCategory = Label(Product_Frame, text="Subcategory", font=('arial', 13, "bold"), bg="white", bd=4)
        self.lblSubCategory.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.ComboSubCategory = ttk.Combobox(Product_Frame, font=('arial', 13, "bold"), width=20, state="readonly")
        self.ComboSubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>", self.Product_add)

        # Product Name
        self.lblproduct = Label(Product_Frame, text="Product Name", font=('arial', 13, "bold"), bg="white", bd=4)
        self.lblproduct.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.ComboProduct = ttk.Combobox(Product_Frame,textvariable=self.product, font=('arial', 13, "bold"), width=20, state="readonly")
        self.ComboProduct.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>", self.price)

        # Sub Total Frame
        SubTotal_Frame = LabelFrame(Main_Frame, text="Sub-Total", font=("times new roman", 17, "bold"), bg="white",fg="red")
        SubTotal_Frame.place(x=10, y=200, width=370, height=160)

        # Price
        self.lblPrice = Label(SubTotal_Frame, text="Price", font=('arial', 13, "bold"), bg="white", bd=4)
        self.lblPrice.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.ComboPrice = ttk.Combobox(SubTotal_Frame,state="readonly", textvariable=self.prices, font=('arial', 13, "bold"), width=18,)
        self.ComboPrice.grid(row=0, column=1, sticky=W, padx=5, pady=2)


        #Qty
        self.lblQty = Label(SubTotal_Frame, text="Quantity", font=('arial', 13, "bold"), bg="white", bd=4)
        self.lblQty.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.ComboQty = ttk.Entry(SubTotal_Frame,textvariable=self.qty, font=('arial', 13, "bold"), width=20)
        self.ComboQty.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        #Sub Total
        self.lblSubTotal = Label(SubTotal_Frame, text="Sub Total", font=('arial', 13, "bold"), bg="white", bd=4)
        self.lblSubTotal.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.ComboSubTotal = ttk.Entry(SubTotal_Frame,textvariable=self.sub_total, font=('arial', 13, "bold"), width=20, state="readonly")
        self.ComboSubTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Bill Area Frame

        BillAreaFrame = LabelFrame(Main_Frame, text="Billing", font=("times new roman", 17, "bold"), bg="white", fg="red")
        BillAreaFrame.place(x=820,y=5,width=430,height=355)

        scroll_y=Scrollbar(BillAreaFrame,orient=VERTICAL)
        self.textarea = Text(BillAreaFrame, yscrollcommand=scroll_y.set,bg="white", fg="blue", font=("times new roman",13,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Bill Counter Frame
        BillCount_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=("times new roman", 17, "bold"), bg="white",fg="red")
        BillCount_Frame.place(x=400, y=200, width=400, height=160)


        self.lblSubTotal = Label(BillCount_Frame, text="Sub Total", font=('arial', 13, "bold"), bg="white", bd=4)
        self.lblSubTotal.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.EntrySubTotal = ttk.Entry(BillCount_Frame,textvariable=self.sub_total, font=('arial', 13, "bold"), width=20,state="readonly")
        self.EntrySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_tax = Label(BillCount_Frame, text="Gov Tax", font=('arial', 13, "bold"), bg="white", bd=4)
        self.lbl_tax.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.tax_tax = ttk.Entry(BillCount_Frame,textvariable=self.tax_input, font=('arial', 13, "bold"), width=20,state="readonly")
        self.tax_tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblAmountTotal = Label(BillCount_Frame, text="Grand Total", font=('arial', 13, "bold"), bg="white", bd=4)
        self.lblAmountTotal.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.txtAmountTotal = ttk.Entry(BillCount_Frame,textvariable=self.total, font=('arial', 13, "bold"), width=20,state="readonly")
        self.txtAmountTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Toolbar Frame
        Toolbar_Frame = LabelFrame(Main_Frame, text="Tool Bar", font=("times new roman", 17, "bold"), bg="white", fg="red")
        Toolbar_Frame.place(x=10, y=395, width=1275, height=125)

        self.BtnAddToCart = Button(Toolbar_Frame, command=self.AddItem, height=2, text="Add To Cart", font=('arial', 17, 'bold'), bg="orangered", fg="white",width=13, cursor="hand2")
        self.BtnAddToCart.grid(row=0, column=0, padx=8)

        self.Btngenerate_bill = Button(Toolbar_Frame, command=self.gen_bill, height=2, text="Generate Bill", font=('arial', 17, 'bold'),bg="orangered", fg="white",width=13, cursor="hand2")
        self.Btngenerate_bill.grid(row=0, column=1,padx=8)

        self.BtnSave = Button(Toolbar_Frame, command=self.save_bill, height=2, text="Save Bill", font=('arial', 17, 'bold'),bg="orangered", fg="white",width=13, cursor="hand2")
        self.BtnSave.grid(row=0, column=2,padx=8)

        self.BtnPrint = Button(Toolbar_Frame, command=self.printbill, height=2, text="Print", font=('arial', 17, 'bold'),bg="orangered", fg="white",width=13, cursor="hand2")
        self.BtnPrint.grid(row=0, column=3,padx=8)

        self.BtnClear = Button(Toolbar_Frame, command=self.clear, height=2, text="Clear", font=('arial', 17, 'bold'),bg="orangered", fg="white",width=13, cursor="hand2")
        self.BtnClear.grid(row=0, column=4,padx=8)

        self.BtnExit = Button(Toolbar_Frame, command=self.root.destroy, height=2, text="Exit", font=('arial', 17, 'bold'),bg="orangered", fg="white",width=13, cursor="hand2")
        self.BtnExit.grid(row=0, column=5,padx=8)

        # Bill Search Frame
        Search_Frame = LabelFrame(Main_Frame, text="Bill Search", font=("times new roman", 17, "bold"), bg="white",fg="red")
        Search_Frame.place(x=10, y=530, width=500, height=65)

        self.lblSearchBill = Label(Search_Frame, text="Search Bill", font=('arial', 13, "bold"), bg="white", bd=4)
        self.lblSearchBill.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.txtSearchBill = ttk.Entry(Search_Frame, textvariable=self.search_bill, font=('arial', 13, "bold"), width=20)
        self.txtSearchBill.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.BtnSearch = Button(Search_Frame, command=self.findbill, text="Search", font=('arial', 8, 'bold'), bg="orangered", fg="white", width=13, cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)
        self.welcome()

        self.l = []
    # =====================================Function Declaration=================================

    def AddItem(self):

        Tax = 1
        self.n = self.prices.get()
        self.m = self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror(("Error", "Please Select the Product Name"))
        else:
            self.textarea.insert(END, f"\n {self.product.get()}\t\t{self.qty.get()}\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) + (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) + (self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror(("Error", "Please Add Product to Cart"))

        else:
            text = self.textarea.get(10.0, (15.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text)
            self.textarea.insert(END, "\n========================================")
            self.textarea.insert(END, f"\n Sub Total:\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax Total:\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Grand Total:\t\t{self.total.get()}")
            self.textarea.insert(END, "\n========================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill", "Do You Want To Save the Bill")
        if op>0:
            self.bill_data = self.textarea.get(1.0, END)
            f1=open('Bills/'+str(self.bill_no.get())+".txt", 'w')
            savedmessage = messagebox.showinfo("Bill Saved", "Bill Has Been Saved Successfully")
            f1.write(self.bill_data)
            f1.close()

    def printbill(self):
        q = self.textarea.get(1.0, "end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename, 'w').write(q)
        os.startfile(filename, "print")

    def findbill(self):
        found = "no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1 = open(f'Bills/{i}', 'r')
                self.textarea.delete(1.0, END)
                for d in f1:
                    self.textarea.insert(END, d)
                f1.close()
                found = "yes"
        if found == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0, END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x = random.randint(1000, 1000000000)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()


    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, f"\t           REIGNING RESOLUTION")
        self.textarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END, f"\n Customer Email:{self.c_email.get()}")
        # x = time.strftime('%H:%M:%S %p')
        y = datetime.datetime.now()
        self.textarea.insert(END, f"\n Time: {y}")

        self.textarea.insert(END, "\n========================================")
        self.textarea.insert(END, f"\n PRODUCTS\t\tQTY\tPRICE")
        self.textarea.insert(END, "\n========================================\n")




    def Categories(self, event=""):
        if self.Combo_Category.get()=="Acessories":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Earphones":
            self.ComboSubCategory.config(value=self.SubCatLifStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    def Product_add(self, event=""):
        if self.ComboSubCategory.get()=="Cables":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Pendrives":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Other":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=='Boat':
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=='Realme':
            self.ComboProduct.config(value=self.Face_creame)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=='Oneplus Earphones':
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=='Iphone':
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=='Samsung':
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=='Xiome':
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=='RealMe':
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=='Oneplus':
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=='Oppo':
            self.ComboProduct.config(value=self.Oppo)
            self.ComboProduct.current(0)

    def price(self, event=""):
        if self.ComboProduct.get()=="USB          ":
            self.ComboPrice.config(value=self.price_usb)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "TYPE C       ":
            self.ComboPrice.config(value=self.price_typec)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "MICRO USB    ":
            self.ComboPrice.config(value=self.price_microusb)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Sandisk      ":
            self.ComboPrice.config(value=self.price_sandisk)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "HP           ":
            self.ComboPrice.config(value=self.price_hp)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Sony         ":
            self.ComboPrice.config(value=self.price_sony)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "HDMI Cable   ":
            self.ComboPrice.config(value=self.price_hdmi)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "OTG          ":
            self.ComboPrice.config(value=self.price_otg)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Cover        ":
            self.ComboPrice.config(value=self.price_cover)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Rockerz 235v2":
            self.ComboPrice.config(value=self.price_235v2)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Rockerz 450  ":
            self.ComboPrice.config(value=self.price_450)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Airdopes 101 ":
            self.ComboPrice.config(value=self.price_ad101)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Rockerz 335  ":
            self.ComboPrice.config(value=self.price_335)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Buds Air 2   ":
            self.ComboPrice.config(value=self.price_air2)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Buds Q       ":
            self.ComboPrice.config(value=self.price_budsq)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Buds Air Neo ":
            self.ComboPrice.config(value=self.price_airneo)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Buds Wireless":
            self.ComboPrice.config(value=self.price_wireless)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Buds         ":
            self.ComboPrice.config(value=self.price_buds)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Buds Z       ":
            self.ComboPrice.config(value=self.price_budsz)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Bullets      ":
            self.ComboPrice.config(value=self.price_bullets)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Iphone X     ":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Iphone_11    ":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Iphone_12    ":
            self.ComboPrice.config(value=self.price_112)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Samsung M16  ":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Samsung M12  ":
            self.ComboPrice.config(value=self.price_sm12)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Samsung M21  ":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Redmi Note 9 ":
            self.ComboPrice.config(value=self.price_note9)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Mi 10i       ":
            self.ComboPrice.config(value=self.price_mi10i)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Redmi 9 Pro  ":
            self.ComboPrice.config(value=self.price_note9pro)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "RealMe 8     ":
            self.ComboPrice.config(value=self.price_rel8)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "RealMe 8 Pro ":
            self.ComboPrice.config(value=self.price_rel8pro)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "RealMe 7 Pro ":
            self.ComboPrice.config(value=self.price_relpro)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "OnePlus Nord ":
            self.ComboPrice.config(value=self.price_onenord)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "OnePlus 9    ":
            self.ComboPrice.config(value=self.price_one9)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "OnePlus 9 Pro":
            self.ComboPrice.config(value=self.price_one9pro)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Oppo F19 Pro ":
            self.ComboPrice.config(value=self.price_f19pro)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Reno 6       ":
            self.ComboPrice.config(value=self.price_reno6)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get() == "Reno 6 Pro   ":
            self.ComboPrice.config(value=self.price_reno6pro)
            self.ComboPrice.current(0)
            self.qty.set(1)


if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()

    # #Image1
    # img = Image.open("Images/reigning.jpeg")
    # img = img.resize((500, 130), Image.ANTIALIAS)
    # self.photoimg = ImageTk.PhotoImage(img)

    # lbl_img = Label(self.root,image=self.photoimg)
    # lbl_img.place(x=0, y=0, width=450, height=130)

    # # Image2
    # img_1 = Image.open("Images/background.jpeg")
    # img_1 = img_1.resize((500, 130), Image.ANTIALIAS)
    # self.photoimg_1 = ImageTk.PhotoImage(img_1)

    # lbl_img_1 = Label(self.root,image=self.photoimg_1)
    # lbl_img_1.place(x=450, y=0, width=450, height=130)

    # # Image3
    # img_2 = Image.open("Images/123.jpg")
    # img_2 = img_2.resize((500, 130), Image.ANTIALIAS)
    # self.photoimg_2 = ImageTk.PhotoImage(img_2)

    # lbl_img_2 = Label(self.root,image=self.photoimg_2)
    # lbl_img_2.place(x=900, y=0, width=450, height=130)


