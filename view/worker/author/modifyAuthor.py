from customtkinter import *
from tkinter import messagebox
from model.author import author
from controler.worker.author import modifyAuthor
class Modify:
    def __init__(self,win,id,author):
        self.author = author
        self.id=id
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Modify author")
        self.win.wm_transient(win)
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkScrollableFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        #modify----------------------------------------
        self.modifyLb=CTkLabel(self.backFrame,text="Modify Author",font=("Baskerville",30,"bold"),pady=35,text_color="#FFD700")
        
        self.modifyLb.pack()

        #FIRSTNAMEAUT---------------------------------------------------------------------------
        self.FIRSTNAMEAUTLB=CTkLabel(self.frame,text="author first Name:",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.FIRSTNAMEAUT=StringVar()
        self.FIRSTNAMEAUTEN=CTkEntry(self.frame,textvariable=self.FIRSTNAMEAUT ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.FIRSTNAMEAUT.set(f"{self.author.FIRSTNAMEAUT}")
        
        self.FIRSTNAMEAUTLB.pack()
        self.FIRSTNAMEAUTEN.pack()
        #LASTNAMEAUT---------------------------------------------------------------------------
        self.LASTNAMEAUTLB=CTkLabel(self.frame,text="author Last Name:",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.LASTNAMEAUT=StringVar()
        self.LASTNAMEAUTEN=CTkEntry(self.frame,textvariable=self.LASTNAMEAUT ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.LASTNAMEAUT.set(f"{self.author.LASTNAMEAUT}")
        
        self.LASTNAMEAUTLB.pack()
        self.LASTNAMEAUTEN.pack()
        #TELAUT-------------------------------------------------------------------
        self.TELAUTLB=CTkLabel(self.frame,text="Author tel: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.TELAUT=StringVar()
        self.TELAUTEN=CTkEntry(self.frame,textvariable=self.TELAUT ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.TELAUT.set(self.author.TELAUT)
        
        self.TELAUTLB.pack()
        self.TELAUTEN.pack()
        #EMAILAUT-------------------------------------------------------------------
        self.EMAILAUTLB=CTkLabel(self.frame,text="Author Email: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.EMAILAUT=StringVar()
        self.EMAILAUTEN=CTkEntry(self.frame,textvariable=self.EMAILAUT ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.EMAILAUT.set(f"{self.author.EMAILAUT}")
        
        self.EMAILAUTLB.pack()
        self.EMAILAUTEN.pack()
        
        #Add btn-----------------------------------------------------------------------------
        self.MODIFYBTN=CTkButton(self.frame,text="Modify Author",command=self.validateInfo,font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.MODIFYBTN.pack(pady=20)
    def validateInfo(self):
          if(self.TELAUT.get().isdigit() and self.FIRSTNAMEAUT.get()!=""and self.LASTNAMEAUT.get()!="" and self.EMAILAUT.get() !="" ):
              newAut=author.Author(self.LASTNAMEAUT.get(),self.FIRSTNAMEAUT.get(),self.TELAUT.get(),self.EMAILAUT.get())
              result=modifyAuthor.modifyAuthor(self.id,newAut)
              if (result):
                  self.FIRSTNAMEAUT.set("")
                  self.LASTNAMEAUT.set("")
                  self.TELAUT.set("")
                  self.EMAILAUT.set("")
                  messagebox.showinfo("info", "The Author has been modified successfully")
  
              else:
                  messagebox.showwarning("Warning", "The Author has not been modified,maybe it is existed")
  
                  
          else:
              messagebox.showwarning("Warning", "All information are required")
  