from tkinter import *

class BillingApp:
    def __init__(self,root):
        self.root = root
        # self.root.geometry('1300x700+0+0')
        self.root.minsize(1300,700)
        self.root.maxsize(1300,700)
        self.root.title("Billing Software")
        
        bg_color = "#074463"
        title = Label(self.root,text='Billing Software',fg='white',font=("times new roman",30,'bold'),bd=12,bg=bg_color,relief=GROOVE,pady=2).pack(fill=X)
        
        #===================================Variables=====================================================================
        
        self.C_Name = StringVar()
        self.C_Phn = IntVar()
        self.C_Bill = IntVar()
        
        self.Bath_Soap = IntVar()
        self.Face_Cream = IntVar()
        self.Face_Wash = IntVar()
        self.Hair_Spray = IntVar()
        self.Hair_Gel = IntVar()
        self.Body_Loshan = IntVar()
        
        self.Rice = IntVar()
        self.Food_Oil = IntVar()
        self.Daal = IntVar()
        self.Wheat = IntVar()
        self.Sugar = IntVar()
        self.Tea = IntVar()
        
        self.Seven_Up = IntVar()
        self.Pepsi = IntVar()
        self.Dew = IntVar()
        self.Fanta = IntVar()
        self.Pakola = IntVar()
        self.Diet_Juice = IntVar()         
        
        self.Total_Cosmetic_Price = IntVar()
        self.Total_Grocery_Price = IntVar()
        self.Total_Cold_Drink_Price = IntVar()
        
        self.Cosmetic_Tax = IntVar()
        self.Grocery_Tax = IntVar()
        self.Cold_Drink_Tax = IntVar()
        
        #================================Customer_Details==============================================
        
        F1 = LabelFrame(self.root,text='Customer Details',font=('times new roman',15,'bold'),bd=8,bg=bg_color,fg='gold')
        F1.place(x=0,y=75,relwidth=1)
        
        C_Name_Label = Label(F1,text='Customer Name',font=('times new roman',18,'bold'),fg='White',bg=bg_color)
        C_Name_Label.grid(row=0,column=0,padx=20,pady=5)
        C_Name_Entry = Entry(F1,textvariable=self.C_Name,font=('tiems new roman',12,'bold'),bg='white',fg='black')
        C_Name_Entry.grid(row=0,column=1,pady=5)
        
        C_Phn_Label = Label(F1,text='Phone Number',font=('times new roman',18,'bold'),fg='White',bg=bg_color)
        C_Phn_Label.grid(row=0,column=2,padx=20,pady=5)
        C_Phn_Entry = Entry(F1,textvariable=self.C_Phn,font=('tiems new roman',12,'bold'),bg='white',fg='black')
        C_Phn_Entry.grid(row=0,column=3,pady=5)
        
        C_Bill_Label = Label(F1,text='Bill No.',font=('times new roman',18,'bold'),fg='White',bg=bg_color)
        C_Bill_Label.grid(row=0,column=4,padx=20,pady=5)
        C_Bill_Entry = Entry(F1,textvariable=self.C_Bill,font=('tiems new roman',12,'bold'),bg='white',fg='black',width=20)
        C_Bill_Entry.grid(row=0,column=5,pady=5)
        C_Bill_Btn = Button(F1,text='Search',font=('times new roman',12,'bold'),bd=5,fg='black',bg='grey',width=15)
        C_Bill_Btn.grid(row=0,column=6,padx=20,pady=5)
        
        #===========================================================================================
        
        F2 = LabelFrame(self.root,text='Cosmetics',font=('times new roman',12,'bold'),bd=15,bg=bg_color,fg='gold')
        F2.place(x=0,y=160,relwidth=0.25)
        
        Bath_Soap_Label = Label(F2,text='Bath Soap',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Bath_Soap_Label.grid(row=0,column=0,padx=12,pady=5)
        Bath_Soap_Entry = Entry(F2,textvariable=self.Bath_Soap,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Bath_Soap_Entry.grid(row=0,column=1,pady=12)
        
        Face_Cream_Label = Label(F2,text='Face Cream',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Face_Cream_Label.grid(row=1,column=0,padx=12,pady=5)
        Face_Cream_Entry = Entry(F2,textvariable=self.Face_Cream,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Face_Cream_Entry.grid(row=1,column=1,pady=12)
        
        Face_Wash_Label = Label(F2,text='Face Wash',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Face_Wash_Label.grid(row=2,column=0,padx=12,pady=5)
        Face_Wash_Entry = Entry(F2,textvariable=self.Face_Wash,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Face_Wash_Entry.grid(row=2,column=1,pady=12)
        
        Hair_Spray_Label = Label(F2,text='Hair Spray',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Hair_Spray_Label.grid(row=3,column=0,padx=12,pady=5)
        Hair_Spray_Entry = Entry(F2,textvariable=self.Hair_Spray,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Hair_Spray_Entry.grid(row=3,column=1,pady=12)
        
        Hair_Gel_Label = Label(F2,text='Hair Gel',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Hair_Gel_Label.grid(row=4,column=0,padx=12,pady=5)
        Hair_Gel_Entry = Entry(F2,textvariable=self.Hair_Gel,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Hair_Gel_Entry.grid(row=4,column=1,pady=12)
        
        Body_Loshan_Label = Label(F2,text='Body Loshan',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Body_Loshan_Label.grid(row=5,column=0,padx=12,pady=5)
        Body_Loshan_Entry = Entry(F2,textvariable=self.Body_Loshan,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Body_Loshan_Entry.grid(row=5,column=1,pady=12)
        
        #===================================Grocery========================================================
        
        F3 = LabelFrame(self.root,text='Grocery',font=('times new roman',12,'bold'),bd=15,bg=bg_color,fg='gold')
        F3.place(relx=0.25,y=160,relwidth=0.25)
        
        Rice_Label = Label(F3,text='Rice',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Rice_Label.grid(row=0,column=0,padx=12,pady=5)
        Rice_Entry = Entry(F3,textvariable=self.Rice,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Rice_Entry.grid(row=0,column=1,pady=12)
        
        Food_Oil_Label = Label(F3,text='Food Oil',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Food_Oil_Label.grid(row=1,column=0,padx=12,pady=5)
        Food_Oil_Entry = Entry(F3,textvariable=self.Food_Oil,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Food_Oil_Entry.grid(row=1,column=1,pady=12)
        
        Daal_Label = Label(F3,text='Daal',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Daal_Label.grid(row=2,column=0,padx=12,pady=5)
        Daal_Entry = Entry(F3,textvariable=self.Daal,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Daal_Entry.grid(row=2,column=1,pady=12)
        
        Wheat_Label = Label(F3,text='Wheat',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Wheat_Label.grid(row=3,column=0,padx=12,pady=5)
        Wheat_Entry = Entry(F3,textvariable=self.Wheat,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Wheat_Entry.grid(row=3,column=1,pady=12)
        
        Sugar_Label = Label(F3,text='Sugar',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Sugar_Label.grid(row=4,column=0,padx=12,pady=5)
        Sugar_Entry = Entry(F3,textvariable=self.Sugar,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Sugar_Entry.grid(row=4,column=1,pady=12)
        
        Tea_Label = Label(F3,text='Tea',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Tea_Label.grid(row=5,column=0,padx=12,pady=5)
        Tea_Entry = Entry(F3,textvariable=self.Tea,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Tea_Entry.grid(row=5,column=1,pady=12)
        
        #===================================Cold Drinks========================================================
        
        F4 = LabelFrame(self.root,text='Cold Drinks',font=('times new roman',12,'bold'),bd=15,bg=bg_color,fg='gold')
        F4.place(relx=0.5,y=160,relwidth=0.25)
        
        Seven_up_Label = Label(F4,text='7 Up',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Seven_up_Label.grid(row=0,column=0,padx=12,pady=5)
        Seven_up_Entry = Entry(F4,textvariable=self.Seven_Up,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Seven_up_Entry.grid(row=0,column=1,pady=12)
        
        Pepsi_Label = Label(F4,text='Pepsi',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Pepsi_Label.grid(row=1,column=0,padx=12,pady=5)
        Pepsi_Entry = Entry(F4,textvariable=self.Pepsi,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Pepsi_Entry.grid(row=1,column=1,pady=12)
        
        Dew_Label = Label(F4,text='Dew',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Dew_Label.grid(row=2,column=0,padx=12,pady=5)
        Dew_Entry = Entry(F4,textvariable=self.Dew,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Dew_Entry.grid(row=2,column=1,pady=12)
        
        Fanta_Label = Label(F4,text='Fanta',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Fanta_Label.grid(row=3,column=0,padx=12,pady=5)
        Fanta_Entry = Entry(F4,textvariable=self.Fanta,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Fanta_Entry.grid(row=3,column=1,pady=12)
        
        Pakola_Label = Label(F4,text='Pakola',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Pakola_Label.grid(row=4,column=0,padx=12,pady=5)
        Pakola_Entry = Entry(F4,textvariable=self.Pakola,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Pakola_Entry.grid(row=4,column=1,pady=12)
        
        Diet_Juice_Label = Label(F4,text='Diet Juice',font=('times new roman',12,'bold'),fg='white',bg=bg_color)
        Diet_Juice_Label.grid(row=5,column=0,padx=12,pady=5)
        Diet_Juice_Entry = Entry(F4,textvariable=self.Diet_Juice,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Diet_Juice_Entry.grid(row=5,column=1,pady=12)
        
        #==============================Bill======================================================================
        
        F6 = LabelFrame(self.root,bg='white',bd=10,relief=GROOVE)
        F6.place(relx=0.75,y=160, relwidth=0.25,height=365)
        label = Label(F6,text='Bill Area',font=('',12,'bold'),bd=5,relief=GROOVE)
        label.pack(fill=X)
        scrol_y = Scrollbar(F6,orient=VERTICAL)
        self.txtarea=Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #==============================Billing Area========================================================================
        
        F5 = LabelFrame(self.root,text='Billing Area',font=('times new roman',12,'bold'),bd=15,bg=bg_color,fg='gold')
        F5.place(x=0,y=530,relwidth=1)
        
        Total_Cosmetic_Price_Label = Label(F5,text='Total Cosmetic Price',font=('times new roman',12,'bold'),bg=bg_color,fg='White')
        Total_Cosmetic_Price_Label.grid(row=0,column=0,padx=25,pady=8)
        Total_Cosmetic_Price_Entry = Entry(F5,textvariable=self.Total_Cosmetic_Price,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Total_Cosmetic_Price_Entry.grid(row=0,column=1,pady=8)
        
        Total_Grocery_Price_Label = Label(F5,text='Total Grocery Price',font=('times new roman',12,'bold'),bg=bg_color,fg='White')
        Total_Grocery_Price_Label.grid(row=1,column=0,pady=8)
        Total_Grocery_Price_Entry = Entry(F5,textvariable=self.Total_Grocery_Price,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Total_Grocery_Price_Entry.grid(row=1,column=1,pady=8)
        
        Total_Cold_Drink_Label = Label(F5,text='Total Cold Drink Price',font=('times new roman',12,'bold'),bg=bg_color,fg='White')
        Total_Cold_Drink_Label.grid(row=2,column=0,pady=8)
        Total_Cold_Drink_Entry = Entry(F5,textvariable=self.Total_Cold_Drink_Price,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Total_Cold_Drink_Entry.grid(row=2,column=1,pady=8)
        
        Cosmetic_Tax_Label = Label(F5,text='Cosmetic Tax',font=('times new roman',12,'bold'),bg=bg_color,fg='White')
        Cosmetic_Tax_Label.grid(row=0,column=3,padx=25,pady=8)
        Cosmetic_Tax_Entry = Entry(F5,textvariable=self.Cosmetic_Tax,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Cosmetic_Tax_Entry.grid(row=0,column=4,pady=8)
        
        Grocery_Tax_Label = Label(F5,text='Grocery Tax',font=('times new roman',12,'bold'),bg=bg_color,fg='White')
        Grocery_Tax_Label.grid(row=1,column=3,pady=8)
        Grocery_Tax_Entry = Entry(F5,textvariable=self.Grocery_Tax,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Grocery_Tax_Entry.grid(row=1,column=4,pady=8)
        
        Cold_Drink_Tax_Label = Label(F5,text='Cold Drink Tax',font=('times new roman',12,'bold'),bg=bg_color,fg='White')
        Cold_Drink_Tax_Label.grid(row=2,column=3,pady=8)
        Cold_Drink_Tax_Entry = Entry(F5,textvariable=self.Cold_Drink_Tax,font=('times new roman',12,'bold'),bd=5,fg='black',bg='white')
        Cold_Drink_Tax_Entry.grid(row=2,column=4,pady=8)
        
        #==========================Button Frame===============================================================
        
        Btn_Frame = Frame(F5,bg='White',bd=10,relief=GROOVE)
        Btn_Frame.place(x=700,y=8,height=125,width=560)
        
        Total_btn = Button(Btn_Frame,text='Total',command=self.Total,font=('',12,'bold'),height=3,width=10,bg='grey',fg='white',bd=5)
        Total_btn.grid(pady=12,padx=10,row=0,column=0)
        
        Generate_Bill_Btn = Button(Btn_Frame,command=self.Bill_Area,text='Generate Bill',font=('',12,'bold'),height=3,width=10,bg='grey',fg='white',bd=5)
        Generate_Bill_Btn.grid(pady=10,padx=10,row=0,column=1)
        
        Clear_btn = Button(Btn_Frame,text='Clear',font=('',12,'bold'),height=3,width=10,bg='grey',fg='white',bd=5)
        Clear_btn.grid(pady=12,padx=10,row=0,column=2)
        
        Exit_btn = Button(Btn_Frame,text='Exit',font=('',12,'bold'),height=3,width=10,bg='grey',fg='white',bd=5)
        Exit_btn.grid(pady=12,padx=10,row=0,column=3)
        
        self.Welcome_Area()
               
    def Total(self):
        self.Bath_Soap_Price = self.Bath_Soap.get()*40
        self.Face_Cream_Price = self.Face_Cream.get()*40
        self.Face_Wash_Price = self.Face_Wash.get()*40
        self.Hair_Spray_Price = self.Hair_Spray.get()*40
        self.Hair_Gel_Price = self.Hair_Gel.get()*40
        self.Body_Loshan_Price = self.Body_Loshan.get()*40
        
        self.Total_Cosmetic_Price.set(
                                (self.Bath_Soap_Price)+
                                (self.Face_Cream_Price)+
                                (self.Face_Wash_Price)+
                                (self.Hair_Spray_Price)+
                                (self.Hair_Gel_Price)+
                                (self.Body_Loshan_Price)
        )
        self.Rice_Price = self.Rice.get()*40
        self.Food_Oil_Price = self.Food_Oil.get()*40
        self.Daal_Price = self.Daal.get()*40
        self.Wheat_Price = self.Wheat.get()*40
        self.Sugar_Price = self.Sugar.get()*40
        self.Tea_Price = self.Tea.get()*40
        
        self.Total_Grocery_Price.set(
                                (self.Rice_Price)+
                                (self.Food_Oil_Price)+
                                (self.Daal_Price)+
                                (self.Wheat_Price)+
                                (self.Sugar_Price)+
                                (self.Tea_Price)
        )
        self.Seven_Up_Price = self.Seven_Up.get()*40
        self.Pepsi_Price = self.Pepsi.get()*40
        self.Dew_Price = self.Dew.get()*40
        self.Fanta_Price = self.Fanta.get()*40
        self.Pakola_Price = self.Pakola.get()*40
        self.Diet_Juice_Price = self.Diet_Juice.get()*40
        
        self.Total_Cold_Drink_Price.set(
                                (self.Seven_Up_Price)+
                                (self.Pepsi_Price)+
                                (self.Dew_Price)+
                                (self.Fanta_Price)+
                                (self.Pakola_Price)+
                                (self.Diet_Juice_Price)
        )
        self.Cosmetic_Tax.set(
                                (self.Total_Cosmetic_Price.get()*0.05)
        )
        self.Grocery_Tax.set(
                                (self.Total_Grocery_Price.get()*0.05)
        )
        self.Cold_Drink_Tax.set(
                                (self.Total_Cold_Drink_Price.get()*0.05)
        )
        self.total = (
            (self.Total_Cosmetic_Price.get())+
            (self.Total_Grocery_Price.get())+
            (self.Total_Cold_Drink_Price.get())
        )
        
    def Welcome_Area(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t   Welcome To Shop")
        self.txtarea.insert(END,'\n')
        self.txtarea.insert(END,f"\nBill No: {self.C_Bill.get()}")
        self.txtarea.insert(END,f"\nCustomer Name: {self.C_Name.get()}")
        self.txtarea.insert(END,f"\nPhone Number: {self.C_Phn.get()}")
        self.txtarea.insert(END,"\n===================================")
        self.txtarea.insert(END,"\nProduct\t\tQTY\t     Price")
        self.txtarea.insert(END,"\n===================================")
    
    def Bill_Area(self):
        self.Welcome_Area()
        if self.Bath_Soap_Price != 0:
            self.txtarea.insert(END,f'\nBath Soap\t\t{self.Bath_Soap.get()}\t     {self.Bath_Soap_Price}')
        if self.Face_Cream_Price != 0:
            self.txtarea.insert(END,f'\nFace Cream\t\t{self.Face_Cream.get()}\t     {self.Face_Cream_Price}')
        if self.Face_Wash_Price != 0:
            self.txtarea.insert(END,f'\nFace Wash\t\t{self.Face_Wash.get()}\t     {self.Face_Wash_Price}')
        if self.Hair_Spray_Price != 0:
            self.txtarea.insert(END,f'\nHair Spray\t\t{self.Hair_Spray.get()}\t     {self.Hair_Spray_Price}')
        if self.Hair_Gel_Price != 0:
            self.txtarea.insert(END,f'\nHair Gel\t\t{self.Hair_Gel.get()}\t     {self.Hair_Gel_Price}')
        if self.Body_Loshan_Price != 0:
            self.txtarea.insert(END,f'\nBody Loshan\t\t{self.Body_Loshan.get()}\t     {self.Body_Loshan_Price}')

        if self.Rice_Price != 0:
            self.txtarea.insert(END,f'\nRice\t\t{self.Rice.get()}\t     {self.Rice_Price}')
        if self.Food_Oil_Price != 0:
            self.txtarea.insert(END,f'\nFood Oil\t\t{self.Food_Oil.get()}\t     {self.Food_Oil_Price}')
        if self.Daal_Price != 0:
            self.txtarea.insert(END,f'\nDaal\t\t{self.Daal.get()}\t     {self.Daal_Price}')
        if self.Wheat_Price != 0:
            self.txtarea.insert(END,f'\nWheat\t\t{self.Wheat.get()}\t     {self.Wheat_Price}')
        if self.Sugar_Price != 0:
            self.txtarea.insert(END,f'\nSugar\t\t{self.Sugar.get()}\t     {self.Sugar_Price}')
        if self.Tea_Price != 0:
            self.txtarea.insert(END,f'\nTea\t\t{self.Tea.get()}\t     {self.Tea_Price}')
        
        if self.Seven_Up_Price != 0:
            self.txtarea.insert(END,f'\nSeven Up\t\t{self.Seven_Up.get()}\t     {self.Seven_Up_Price}')
        if self.Pepsi_Price != 0:
            self.txtarea.insert(END,f'\nPepsi\t\t{self.Pepsi.get()}\t     {self.Pepsi_Price}')
        if self.Dew_Price != 0:
            self.txtarea.insert(END,f'\nDew\t\t{self.Dew.get()}\t     {self.Dew_Price}')
        if self.Fanta_Price != 0:
            self.txtarea.insert(END,f'\nFanta\t\t{self.Fanta.get()}\t     {self.Fanta_Price}')
        if self.Pakola_Price != 0:
            self.txtarea.insert(END,f'\nPakola\t\t{self.Pakola.get()}\t     {self.Pakola_Price}')
        if self.Diet_Juice_Price != 0:
            self.txtarea.insert(END,f'\nDiet Juice\t\t{self.Diet_Juice.get()}\t     {self.Diet_Juice_Price}')
        
        self.txtarea.insert(END,"\n===================================")
        self.txtarea.insert(END,f"\nTotal:                       {self.total}")
        self.txtarea.insert(END,"\n===================================")
        
root = Tk()
Obj = BillingApp(root)
root.mainloop()