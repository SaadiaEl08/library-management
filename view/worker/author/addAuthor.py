from customtkinter import *
from tkinter import messagebox
from model.author import author
from controler.worker.author.addAuthor import addAuthor
class Add:
      def __init__(self,win):
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Add Author")
        self.win.wm_transient(win)
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkScrollableFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        #ADD----------------------------------------
        self.addLb=CTkLabel(self.backFrame,text="Add Author",font=("Baskerville",30,"bold"),pady=35,text_color="#FFD700")
        
        self.addLb.pack()

        #FIRSTNAMEAUTHOR---------------------------------------------------------------------------
        self.FIRSTNAMEAUTLB=CTkLabel(self.frame,text="Author first name:" ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.FIRSTNAMEAUT=StringVar()
        self.FIRSTNAMEAUTEN=CTkEntry(self.frame,textvariable=self.FIRSTNAMEAUT ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.FIRSTNAMEAUTLB.pack()
        self.FIRSTNAMEAUTEN.pack()
        #LASTNAMEAUT---------------------------------------------------------------------------
        self.LASTNAMEAUTLB=CTkLabel(self.frame,text="Author Last name:" ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.LASTNAMEAUT=StringVar()
        self.LASTNAMEAUTEN=CTkEntry(self.frame,textvariable=self.LASTNAMEAUT ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.LASTNAMEAUTLB.pack()
        self.LASTNAMEAUTEN.pack()
        #TELAUT-------------------------------------------------------------------
        self.TELAUTLB=CTkLabel(self.frame,text="Author tel: " ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.TELAUT=StringVar()
        self.TELAUTEN=CTkEntry(self.frame,textvariable=self.TELAUT ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.TELAUTLB.pack()
        self.TELAUTEN.pack()
        #EMAILAUT-------------------------------------------------------------------
        self.EMAILAUTLB=CTkLabel(self.frame,text="Author Email: " ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.EMAILAUT=StringVar()
        self.EMAILAUTEN=CTkEntry(self.frame,textvariable=self.EMAILAUT ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.EMAILAUTLB.pack()
        self.EMAILAUTEN.pack()
        
        #Add btn-----------------------------------------------------------------------------
        self.ADDBTN=CTkButton(self.frame,text="Add Author",command=self.validateInfo,font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.ADDBTN.pack(pady=20)
      def validateInfo(self):
          if(self.TELAUT.get().isdigit() and self.FIRSTNAMEAUT.get()!="" and self.LASTNAMEAUT.get()!="" and self.EMAILAUT.get() !="" ):
              newAut=author.Author(self.LASTNAMEAUT.get(),self.FIRSTNAMEAUT.get(),self.TELAUT.get(),self.EMAILAUT.get())
              result=addAuthor(newAut)
              if (result):
                  self.FIRSTNAMEAUT.set("")
                  self.LASTNAMEAUT.set("")
                  self.TELAUT.set("")
                  self.EMAILAUT.set("")
                  messagebox.showinfo("info", "The Author has been added successfully")
  
              else:
                  messagebox.showwarning("Warning", "The Author has not been added,maybe it is existed")
  
                  
          else:
              messagebox.showwarning("Warning", "All information are required")
  