
from logging import root
from tkinter import*
import math,random,os
from tkinter import messagebox
class bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#33A1C9"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #===========Variables================
        
        #==============shirt variables==============
        self.cotton_shirt = IntVar()
        self.synthetic_shirt =IntVar()
        self.polyester_shirt = IntVar()
        self.denim_shirt = IntVar()
        self.jean_shirt = IntVar()
        self.mix_shirt =IntVar()
        
        #=============pant variables================
        self.cotton_pant = IntVar()
        self.lyagra_pant =IntVar()
        self.shoot_pant = IntVar()
        self.tear_pant = IntVar()
        self.jean_pant = IntVar()
        self.mix_pant = IntVar()
        
        #===============Tshirt variables=============
        self.cotton_tshirt = IntVar()
        self.lyagra_tshirt = IntVar()
        self.leecop_tshirt = IntVar()
        self.addidas_tshirt = IntVar()
        self.balman_tshirt = IntVar()
        self.local_tshirt = IntVar()
        #==============Total product prize & tax variables===========
        self.total_shirt_price =StringVar()
        self.total_pant_price = StringVar()
        self.total_tshirt_price = StringVar()
        
        self.total_shirt_tax =StringVar()
        self.total_pant_tax =StringVar()
        self.total_tshirt_tax =StringVar()
        
        #=====================customers=====================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no =StringVar()
        x=random.randint(100,9999)
        self.bill_no.set(str(x))
        self.search_bill =StringVar()
        
        
        #===========Customer Details frame==================
        
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        
        cname_lbl=Label(F1,text="Customer Name",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable = self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        
        cphn_lbl=Label(F1,text="Customer Ph No",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable = self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)
        
        cbill_lbl=Label(F1,text="Bill number",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable = self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)
        
        bill_btn=Button(F1,command=self.find_bill,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=5)
        
        #=====================Shirt Details frame==================
        
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Shirts",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)
        
        cot_lal=Label(F2,text="cotton shirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        cot_txt=Entry(F2,width=10,textvariable = self.cotton_shirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        syn_lal=Label(F2,text="synthetic shirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=1,column=0,padx=10,pady=10,sticky='w')
        syn_txt=Entry(F2,width=10,textvariable = self.synthetic_shirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        pol_lal=Label(F2,text="polyester shirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        pol_txt=Entry(F2,width=10,textvariable = self.polyester_shirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        den_lal=Label(F2,text="denim shirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        den_txt=Entry(F2,width=10,textvariable = self.denim_shirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        jen_lal=Label(F2,text="jean shirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        jen_txt=Entry(F2,width=10,textvariable = self.jean_shirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        mix_lal=Label(F2,text="mix shirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=5,column=0,padx=10,pady=10,sticky='w')
        mix_txt=Entry(F2,width=10,textvariable = self.mix_shirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #=====================Pant Details frame==================
        
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Pants",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)
        
        cotpt_lal=Label(F3,text="cotton pant",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        cotpt_txt=Entry(F3,width=10,textvariable = self.cotton_pant,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        synpt_lal=Label(F3,text="lyagra pant",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=1,column=0,padx=10,pady=10,sticky='w')
        synpt_txt=Entry(F3,width=10,textvariable = self.lyagra_pant,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        polpt_lal=Label(F3,text="shoot pant",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        polpt_txt=Entry(F3,width=10,textvariable = self.shoot_pant,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        denpt_lal=Label(F3,text="tear pant",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        denpt_txt=Entry(F3,width=10,textvariable = self.tear_pant,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        jenpt_lal=Label(F3,text="jean pant",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        jenpt_txt=Entry(F3,width=10,textvariable = self.jean_pant,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        mixpt_lal=Label(F3,text="mix pant",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=5,column=0,padx=10,pady=10,sticky='w')
        mixpt_txt=Entry(F3,width=10,textvariable = self.mix_pant,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
         #=====================Tshirts Details frame==================
        
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Tshirt",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)
        
        cotst_lal=Label(F4,text="cotton tshirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        cotst_txt=Entry(F4,width=10,textvariable = self.cotton_tshirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        synst_lal=Label(F4,text="lyagra tshirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=1,column=0,padx=10,pady=10,sticky='w')
        synst_txt=Entry(F4,width=10,textvariable = self.lyagra_tshirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        polst_lal=Label(F4,text="leecop tshirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        polst_txt=Entry(F4,width=10,textvariable = self.leecop_tshirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        denst_lal=Label(F4,text="adidas tshirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        denst_txt=Entry(F4,width=10,textvariable = self.addidas_tshirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        jenst_lal=Label(F4,text="balman tshirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        jenpt_txt=Entry(F4,width=10,textvariable = self.balman_tshirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        mixst_lal=Label(F4,text="local tshirt",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=5,column=0,padx=10,pady=10,sticky='w')
        mixst_txt=Entry(F4,width=10,textvariable = self.local_tshirt,bd=5,font=("times new roman",16,"bold"),relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
      
      #======================bill area Frame==================
      
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=355,height=380)
        bill_title=Label(F5,text="Bill area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
      #=====================Button Frame========================
      
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Billing Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)  
        
        m1_lbl=Label(F6,text="Total shirt Price",bg=bg_color,fg="darkblue",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky='w')
        m1_txt=Entry(F6,width=18,textvariable = self.total_shirt_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl=Label(F6,text="Total Pant Price",bg=bg_color,fg="darkblue",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky='w')
        m2_txt=Entry(F6,width=18,textvariable = self.total_pant_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
        m3_lbl=Label(F6,text="Total Tshirt Price",bg=bg_color,fg="darkblue",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky='w')
        m3_txt=Entry(F6,width=18,textvariable = self.total_tshirt_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        c1_lbl=Label(F6,text="shirt tax",bg=bg_color,fg="darkblue",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky='w')
        c1_txt=Entry(F6,width=18,textvariable = self.total_shirt_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl=Label(F6,text="Pant tax",bg=bg_color,fg="darkblue",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky='w')
        c2_txt=Entry(F6,width=18,textvariable = self.total_pant_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        
        c3_lbl=Label(F6,text="Tshirt tax",bg=bg_color,fg="darkblue",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky='w')
        c3_txt=Entry(F6,width=18,textvariable = self.total_tshirt_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)
        
        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=11,bd=5,font="arial 12 bold ").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,command=self.bill_area,text="Bill generate",bg="cadetblue",fg="white",pady=15,bd=5,width=11,font="arial 12 bold ").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,command=self.clear_data,text="Clear",bg="cadetblue",fg="white",pady=15,width=11,bd=5,font="arial 12 bold ").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,command=self.Exit_app,text="Exit",bg="cadetblue",fg="white",pady=15,width=11,bd=5,font="arial 12 bold ").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
        
    def total(self):
      self.s_cs_p=self.cotton_shirt.get()*470
      self.s_ss_p=self.synthetic_shirt.get()*240
      self.s_ps_p=self.polyester_shirt.get()*250
      self.s_ds_p=self.denim_shirt.get()*450
      self.s_js_p=self.jean_shirt.get()*500
      self.s_ms_p=self.mix_shirt.get()*350
      
      self.shirt_price=float(
                        (self.s_cs_p)+
                        (self.s_ss_p)+
                        (self.s_ps_p)+
                        (self.s_ds_p)+
                        (self.s_js_p)+
                        (self.s_ms_p)
      )
      self.total_shirt_price.set("Rs ."+str(self.shirt_price)) 
      self.s_tax= round((self.shirt_price*0.05),2)
      self.total_shirt_tax.set("Rs. "+str(self.s_tax)) 
      
      self.p_cp_p=self.cotton_pant.get()*400
      self.p_lyp_p=self.lyagra_pant.get()*370
      self.p_sp_p=self.shoot_pant.get()*750
      self.p_tp_p=self.tear_pant.get()*800
      self.p_jp_p=self.jean_pant.get()*570
      self.p_mp_p=self.mix_pant.get()*350
      
      self.pant_price=float(
                        (self.p_cp_p)+
                        (self.p_lyp_p)+
                        (self.p_sp_p)+
                        (self.p_tp_p)+
                        (self.p_jp_p)+
                        (self.p_mp_p)
      )
      self.total_pant_price.set("Rs ."+str(self.pant_price))   
      self.p_tax=round((self.pant_price*0.04),2)               
      self.total_pant_tax.set("Rs. "+str(self.p_tax))
      
      self.ts_ct_p=self.cotton_tshirt.get()*300
      self.ts_lyt_p=self.lyagra_tshirt.get()*200
      self.ts_lt_p=self.leecop_tshirt.get()*1250
      self.ts_adt_p=self.addidas_tshirt.get()*1500
      self.ts_bt_p=self.balman_tshirt.get()*1750
      self.ts_lct_p=self.local_tshirt.get()*200
      
      self.tshirt_price=float(
                        (self.ts_ct_p)+
                        (self.ts_lyt_p)+
                        (self.ts_lt_p)+
                        (self.ts_adt_p)+
                        (self.ts_bt_p)+
                        (self.ts_lct_p)
      )
      self.total_tshirt_price.set("Rs ."+str(self.tshirt_price)) 
      self.ts_tax= round((self.tshirt_price*0.03),2)                
      self.total_tshirt_tax.set("Rs. "+str(self.ts_tax))
      
      self.Total_bill=float(self.shirt_price+
                            self.pant_price+
                            self.tshirt_price+
                            self.s_tax+
                            self.p_tax+
                            self.ts_tax
      )
    
    def welcome_bill(self):
      self.txtarea.delete('1.0',END)
      self.txtarea.insert(END,"\t Welcome Renuga Menswear\n") 
      self.txtarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")  
      self.txtarea.insert(END,f"\n Customer Name:{self.c_name.get()}")  
      self.txtarea.insert(END,f"\n Customer Phone no:{self.c_phone.get()}")
      self.txtarea.insert(END,f"\n=======================================")
      self.txtarea.insert(END,f"\n Products\t\tQwt\t\tPrice")
      self.txtarea.insert(END,f"\n=======================================")
         
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone=="":
          messagebox.showerror("Error","Customer details are required")
        elif self.total_shirt_price.get()=="Rs. 0.0" and self.total_pant_price.get()=="Rs. 0.0" and self.total_tshirt_price.get()=="Rs. 0.0":
          messagebox.showerror("Error","No item purchased")
        else:
          self.welcome_bill()
            #==============shirt=============================
          if self.cotton_shirt.get()!=0:
              self.txtarea.insert(END,f"\n cotton shirt\t\t{self.cotton_shirt.get()}\t\t{self.s_cs_p}")
          if self.synthetic_shirt.get()!=0:
              self.txtarea.insert(END,f"\n Synthetic shirt\t\t{self.synthetic_shirt.get()}\t\t{self.s_ss_p}")
          if self.polyester_shirt.get()!=0:
              self.txtarea.insert(END,f"\n Polyester shirt\t\t{self.polyester_shirt.get()}\t\t{self.s_ps_p}")
          if self.denim_shirt.get()!=0:
              self.txtarea.insert(END,f"\n denim shirt\t\t{self.denim_shirt.get()}\t\t{self.s_ds_p}")
          if self.jean_shirt.get()!=0:
              self.txtarea.insert(END,f"\n jean shirt\t\t{self.jean_shirt.get()}\t\t{self.s_js_p}")
          if self.mix_shirt.get()!=0:
              self.txtarea.insert(END,f"\n mix shirt\t\t{self.mix_shirt.get()}\t\t{self.s_ms_p}")
            #======================pant=========================
          if self.cotton_pant.get()!=0:
              self.txtarea.insert(END,f"\n cotton pant\t\t{self.cotton_shirt.get()}\t\t{self.p_cp_p}")
          if self.lyagra_pant.get()!=0:
              self.txtarea.insert(END,f"\n lyagra pant\t\t{self.lyagra_pant.get()}\t\t{self.p_lyp_p}")
          if self.shoot_pant.get()!=0:
              self.txtarea.insert(END,f"\n shoot pant\t\t{self.shoot_pant.get()}\t\t{self.p_sp_p}")
          if self.tear_pant.get()!=0:
              self.txtarea.insert(END,f"\n tear pant\t\t{self.tear_pant.get()}\t\t{self.p_tp_p}")
          if self.jean_pant.get()!=0:
              self.txtarea.insert(END,f"\n jean pant\t\t{self.jean_pant.get()}\t\t{self.p_jp_p}")
          if self.mix_pant.get()!=0:
              self.txtarea.insert(END,f"\n mix pant\t\t{self.mix_pant.get()}\t\t{self.p_mp_p}")
            #=======================tshirt======================
          if self.cotton_tshirt.get()!=0:
              self.txtarea.insert(END,f"\n cotton tshirt\t\t{self.cotton_tshirt.get()}\t\t{self.ts_ct_p}")
          if self.lyagra_tshirt.get()!=0:
              self.txtarea.insert(END,f"\n lyagra tshirt\t\t{self.lyagra_pant.get()}\t\t{self.ts_lyt_p}")
          if self.leecop_tshirt.get()!=0:
              self.txtarea.insert(END,f"\n leecop tshirt\t\t{self.leecop_tshirt.get()}\t\t{self.ts_lt_p}")
          if self.addidas_tshirt.get()!=0:
              self.txtarea.insert(END,f"\n addidas tshirt\t\t{self.tear_pant.get()}\t\t{self.ts_adt_p}")
          if self.balman_tshirt.get()!=0:
              self.txtarea.insert(END,f"\n balman tshirt\t\t{self.balman_tshirt.get()}\t\t{self.ts_bt_p}")
          if self.local_tshirt.get()!=0:
              self.txtarea.insert(END,f"\n local tshirt\t\t{self.mix_pant.get()}\t\t{self.ts_lct_p}")
              
          self.txtarea.insert(END,f"\n***************************************")
          if self.total_shirt_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n shirt Tax\t\t\t{self.total_shirt_tax.get()}")
          if self.total_pant_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n pant Tax\t\t\t{self.total_pant_tax.get()}")
          if self.total_tshirt_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n Tshirt Tax\t\t\t{self.total_tshirt_tax.get()}")
          self.txtarea.insert(END,f"\n***************************************")
          self.txtarea.insert(END,f"\n Total amount:\t\t\tRs. {self.Total_bill}")
          self.txtarea.insert(END,f"\n***************************************")
          self.save_bill()
          
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You want to save the Bill?")
        if op>0:
          self.bill_data = self.txtarea.get('1.0',END)
          f1=open("bills/"+str(self.bill_no.get())+".txt","w")
          f1.write(self.bill_data)  
          f1.close() 
          messagebox.showinfo("Saved",f"Bill no.:{self.bill_no.get()} saved succesfully")
        else:
          return
    
    def  find_bill(self):
      present = "no"
      for i in os.listdir("bills/"):
        if i.split('.')[0]==self.search_bill.get():
            f1=open(f"bills/{i}","r")
            self.txtarea.delete('1.0',END)
            for d in f1:
             self.txtarea.insert(END,d)
            f1.close()
            present = "yes"
      if present == "no":
        messagebox.showerror("Error","Invalid Bill No.")
    
    def clear_data(self):
        op= messagebox.askyesno("Clear","Do you really want to clear the data?")
        if op>0:
           
          #==============shirt variables==============
          self.cotton_shirt.set(0)
          self.synthetic_shirt.set(0)
          self.polyester_shirt.set(0)
          self.denim_shirt.set(0)
          self.jean_shirt.set(0)
          self.mix_shirt.set(0)
          
          #=============pant variables================
          self.cotton_pant.set(0)
          self.lyagra_pant.set(0)
          self.shoot_pant.set(0)
          self.tear_pant.set(0)
          self.jean_pant.set(0)
          self.mix_pant.set(0)
          
          #===============Tshirt variables=============
          self.cotton_tshirt.set(0)
          self.lyagra_tshirt.set(0)
          self.leecop_tshirt.set(0)
          self.addidas_tshirt.set(0)
          self.balman_tshirt.set(0)
          self.local_tshirt.set(0)
          #==============Total product prize & tax variables===========
          self.total_shirt_price.set("")
          self.total_pant_price.set("")
          self.total_tshirt_price.set("")
          
          self.total_shirt_tax.set("")
          self.total_pant_tax.set("")
          self.total_tshirt_tax.set("")
          
          #=====================customers=====================
          self.c_name.set("")
          self.c_phone.set("")
          self.bill_no.set("")
          x=random.randint(100,9999)
          self.bill_no.set(str(x))
          self.search_bill.set("")
          self.welcome_bill()
          
    def Exit_app(self):
      op=messagebox.askyesno("Exit","Do you really want to exit?")
      if op>0:
        self.root.destroy()
                      
root=Tk()
obj= bill_app(root)
root.mainloop()       
