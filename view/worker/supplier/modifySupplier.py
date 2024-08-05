from customtkinter import *
from tkinter import messagebox
from model.supplier import supplier
from controler.worker.supplier import modifySupplier
class Modify:
    def __init__(self,win,id,supplier):
        self.supplier = supplier
        self.id=id
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Modify Supplier")
        self.win.wm_transient(win)
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack_propagate(False)

        #modify----------------------------------------
        self.modifyLb=CTkLabel(self.backFrame,text="Modify Supplier",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.modifyLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=1.5)
        #LASTNAMESUP---------------------------------------------------------------------------
        self.LASTNAMESUPLB=CTkLabel(self.frame,text="Supplier Last Name:",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.LASTNAMESUP=StringVar()
        self.LASTNAMESUPEN=CTkEntry(self.frame,textvariable=self.LASTNAMESUP,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.LASTNAMESUP.set(f"{self.supplier.LASTNAMESUP}")
        
        self.LASTNAMESUPLB.pack()
        self.LASTNAMESUPEN.pack()
        #TELSUP-------------------------------------------------------------------
        self.TELSUPLB=CTkLabel(self.frame,text="Supplier tel: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.TELSUP=StringVar()
        self.TELSUPEN=CTkEntry(self.frame,textvariable=self.TELSUP,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.TELSUP.set(self.supplier.TELSUP)
        
        self.TELSUPLB.pack()
        self.TELSUPEN.pack()
        #EMAILSUP-------------------------------------------------------------------
        self.EMAILSUPLB=CTkLabel(self.frame,text="Supplier Email: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.EMAILSUP=StringVar()
        self.EMAILSUPEN=CTkEntry(self.frame,textvariable=self.EMAILSUP,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.EMAILSUP.set(f"{self.supplier.EMAILSUP}")
        
        self.EMAILSUPLB.pack()
        self.EMAILSUPEN.pack()
        
        #Add btn-----------------------------------------------------------------------------
        self.MODIFYBTN=CTkButton(self.frame,text="Modify Supplier",command=self.validateInfo,font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.MODIFYBTN.pack(pady=20)
    def validateInfo(self):
          if(self.TELSUP.get().isdigit()  and self.LASTNAMESUP.get()!="" and self.EMAILSUP.get() !="" ):
              newSup=supplier.Supplier(self.LASTNAMESUP.get(),self.TELSUP.get(),self.EMAILSUP.get())
              result=modifySupplier.modifySupplier(self.id,newSup)
              if (result):
                  self.LASTNAMESUP.set("")
                  self.TELSUP.set("")
                  self.EMAILSUP.set("")
                  messagebox.showinfo("info", "The Supplier has been modified successfully")
  
              else:
                  messagebox.showwarning("Warning", "The Supplier has not been modified,maybe it is existed")
  
                  
          else:
              messagebox.showwarning("Warning", "All information are required")
  