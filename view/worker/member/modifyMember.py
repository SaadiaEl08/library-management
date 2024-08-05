from customtkinter import *
from tkinter import messagebox
from model.member import member
from controler.worker.member import modifyMember
class Modify:
    def __init__(self,win,id,member):
        self.member = member
        self.id=id
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Modify member")
        self.win.wm_transient(win)
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkScrollableFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        #modify----------------------------------------
        self.modifyLb=CTkLabel(self.backFrame,text="Modify Member",font=("Baskerville",30,"bold"),pady=30,bg_color="#0B0B41",text_color="#FFD700")
        
        self.modifyLb.pack()
        #FIRSTNAMEMEMBER---------------------------------------------------------------------------
        self.FIRSTNAMEMEMBERLB=CTkLabel(self.frame,text="Member first Name:",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.FIRSTNAMEMEMBER=StringVar()
        self.FIRSTNAMEMEMBEREN=CTkEntry(self.frame,textvariable=self.FIRSTNAMEMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.FIRSTNAMEMEMBER.set(f"{self.member.FIRSTNAMEMEMBER}")
        
        self.FIRSTNAMEMEMBERLB.pack()
        self.FIRSTNAMEMEMBEREN.pack()
        #LASTNAMEMEMBER---------------------------------------------------------------------------
        self.LASTNAMEMEMBERLB=CTkLabel(self.frame,text="Member Last Name:",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.LASTNAMEMEMBER=StringVar()
        self.LASTNAMEMEMBEREN=CTkEntry(self.frame,textvariable=self.LASTNAMEMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.LASTNAMEMEMBER.set(f"{self.member.LASTNAMEMEMBER}")
        
        self.LASTNAMEMEMBERLB.pack()
        self.LASTNAMEMEMBEREN.pack()
        #LOGINMEMBER-------------------------------------------------------------------
        self.LOGINMEMBERLB=CTkLabel(self.frame,text="Login Member: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.LOGINMEMBER=StringVar()
        self.LOGINMEMBEREN=CTkEntry(self.frame,textvariable=self.LOGINMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.LOGINMEMBER.set(self.member.LOGINMEMBER)
        
        self.LOGINMEMBERLB.pack()
        self.LOGINMEMBEREN.pack()
        #PASSWORDMEMBER-------------------------------------------------------------------
        self.PASSWORDMEMBERLB=CTkLabel(self.frame,text="Password Member: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.PASSWORDMEMBER=StringVar()
        self.PASSWORDMEMBEREN=CTkEntry(self.frame,textvariable=self.PASSWORDMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.PASSWORDMEMBER.set(self.member.PASSWORDMEMBER)
        
        self.PASSWORDMEMBERLB.pack()
        self.PASSWORDMEMBEREN.pack()
        #CITYMEMBER-------------------------------------------------------------------
        self.CITYMEMBERLB=CTkLabel(self.frame,text="City Member: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.CITYMEMBER=StringVar()
        self.CITYMEMBEREN=CTkEntry(self.frame,textvariable=self.CITYMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.CITYMEMBER.set(self.member.CITYMEMBER)
        
        self.CITYMEMBERLB.pack()
        self.CITYMEMBEREN.pack()
        #TELMEMBER-------------------------------------------------------------------
        self.TELMEMBERLB=CTkLabel(self.frame,text="Member tel: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.TELMEMBER=StringVar()
        self.TELMEMBEREN=CTkEntry(self.frame,textvariable=self.TELMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.TELMEMBER.set(self.member.TELMEMBER)
        
        self.TELMEMBERLB.pack()
        self.TELMEMBEREN.pack()
        
        
        #Add btn-----------------------------------------------------------------------------
        self.MODIFYBTN=CTkButton(self.frame,text="Modify Member",command=self.validateInfo,font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.MODIFYBTN.pack(pady=20)
    def validateInfo(self):
          if(self.TELMEMBER.get().isdigit() and self.FIRSTNAMEMEMBER.get()!=""and self.LASTNAMEMEMBER.get()!="" and self.CITYMEMBER.get() !="" and self.LOGINMEMBER.get() !=""and self.PASSWORDMEMBER.get() !="" ):
              newMEMBER=member.Member(self.LASTNAMEMEMBER.get(),self.FIRSTNAMEMEMBER.get(),self.LOGINMEMBER.get(),self.PASSWORDMEMBER.get(),self.CITYMEMBER.get(),self.TELMEMBER.get())
              result=modifyMember.modifyMember(self.id,newMEMBER)
              if (result):
                  self.FIRSTNAMEMEMBER.set("")
                  self.LASTNAMEMEMBER.set("")
                  self.TELMEMBER.set(0)
                  self.LOGINMEMBER.set("")
                  self.PASSWORDMEMBER.set("")
                  self.CITYMEMBER.set("")
                  messagebox.showinfo("info", "The Member has been modified successfully")
  
              else:
                  messagebox.showwarning("Warning", "The Member has not been modified,maybe it is existed")
  
                  
          else:
              messagebox.showwarning("Warning", "All information are required")
  