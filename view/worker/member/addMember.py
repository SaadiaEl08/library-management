from customtkinter import *
from tkinter import messagebox
from model.member import member
from controler.worker.member.addMember import addMember
class Add:
      def __init__(self,win):
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")        
        self.win.title("Add Member")
        self.win.wm_transient(win)
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkScrollableFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        #ADD----------------------------------------
        self.addLb=CTkLabel(self.backFrame,text="Add Member",font=("Baskerville",30,"bold"),pady=30,bg_color="#0B0B41",text_color="#FFD700")
        
        self.addLb.pack()
        #LASTNAMEMEMBER---------------------------------------------------------------------------
        self.LASTNAMEMEMBERLB=CTkLabel(self.frame,text="Member Last Name:",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.LASTNAMEMEMBER=StringVar()
        self.LASTNAMEMEMBEREN=CTkEntry(self.frame,textvariable=self.LASTNAMEMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.LASTNAMEMEMBERLB.pack()
        self.LASTNAMEMEMBEREN.pack()
        #FIRSTNAMEMEMBER---------------------------------------------------------------------------
        self.FIRSTNAMEMEMBERLB=CTkLabel(self.frame,text="Member First Name:",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.FIRSTNAMEMEMBER=StringVar()
        self.FIRSTNAMEMEMBEREN=CTkEntry(self.frame,textvariable=self.FIRSTNAMEMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.FIRSTNAMEMEMBERLB.pack()
        self.FIRSTNAMEMEMBEREN.pack()
        #TELMEMBER-------------------------------------------------------------------
        self.TELMEMBERLB=CTkLabel(self.frame,text="Member tel: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.TELMEMBER=StringVar()
        self.TELMEMBEREN=CTkEntry(self.frame,textvariable=self.TELMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.TELMEMBERLB.pack()
        self.TELMEMBEREN.pack()
        #LOGINMEMBER-------------------------------------------------------------------
        self.LOGINMEMBERLB=CTkLabel(self.frame,text="Member Login: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.LOGINMEMBER=StringVar()
        self.LOGINMEMBEREN=CTkEntry(self.frame,textvariable=self.LOGINMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.LOGINMEMBERLB.pack()
        self.LOGINMEMBEREN.pack()
        #PASSWORDMEMBER-------------------------------------------------------------------
        self.PASSWORDMEMBERLB=CTkLabel(self.frame,text="Member Password: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.PASSWORDMEMBER=StringVar()
        self.PASSWORDMEMBEREN=CTkEntry(self.frame,textvariable=self.PASSWORDMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.PASSWORDMEMBERLB.pack()
        self.PASSWORDMEMBEREN.pack()
        #CITYMEMBER-------------------------------------------------------------------
        self.CITYMEMBERLB=CTkLabel(self.frame,text="Member City: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.CITYMEMBER=StringVar()
        self.CITYMEMBEREN=CTkEntry(self.frame,textvariable=self.CITYMEMBER,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.CITYMEMBERLB.pack()
        self.CITYMEMBEREN.pack()
        
        #Add btn-----------------------------------------------------------------------------
        self.ADDBTN=CTkButton(self.frame,text="Add Member",command=self.validateInfo,font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.ADDBTN.pack(pady=20)
      def validateInfo(self):
          if(self.TELMEMBER.get().isdigit() and self.LASTNAMEMEMBER.get()!="" and self.FIRSTNAMEMEMBER.get()!="" and self.LOGINMEMBER.get()!="" and self.PASSWORDMEMBER.get()!="" and self.CITYMEMBER.get() !="" ):
              newMember=member.Member(self.LASTNAMEMEMBER.get(),self.FIRSTNAMEMEMBER.get(),self.LOGINMEMBER.get(),self.PASSWORDMEMBER.get(),self.CITYMEMBER.get(),self.TELMEMBER.get())
              result=addMember(newMember)
              if (result):
                  self.LASTNAMEMEMBER.set("")
                  self.TELMEMBER.set("")
                  self.LOGINMEMBER.set("")
                  self.PASSWORDMEMBER.set("")
                  self.FIRSTNAMEMEMBER.set("")
                  self.CITYMEMBER.set("")
                  messagebox.showinfo("info", "The Member has been added successfully")
  
              else:
                  messagebox.showwarning("Warning", "The Member has not been added,maybe it is existed")
  
                  
          else:
              messagebox.showwarning("Warning", "All information are required")
  