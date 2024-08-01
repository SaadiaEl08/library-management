from customtkinter import *
from tkinter import messagebox
from model.genre.genre import Genre
from controler.worker.genre.addGenre import addGenre

class Add:
      def __init__(self,win):
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")  
        self.win.title("Add Genre")
        self.win.wm_transient(win)
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack_propagate(False)
        #ADD----------------------------------------
        self.addLb=CTkLabel(self.backFrame,text="Add Genre",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.addLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=25)
        #NAMEGENRE---------------------------------------------------------------------------
        self.NAMEGENRELB=CTkLabel(self.frame,text="Genre Name:" ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.NAMEGENRE=StringVar()
        self.NAMEGENREEN=CTkEntry(self.frame,textvariable=self.NAMEGENRE,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.NAMEGENRELB.pack()
        self.NAMEGENREEN.pack()
        
        #Add btn-----------------------------------------------------------------------------
        self.ADDBTN=CTkButton(self.frame,text="Add genre",command=self.validateInfo ,font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.ADDBTN.pack(pady=20)
      def validateInfo(self):
          if(self.NAMEGENRE.get()!=""):
              newGenre=Genre(self.NAMEGENRE.get())
              result=addGenre(newGenre)
              if (result):
                  self.NAMEGENRE.set("")
                  messagebox.showinfo("info", "The Genre has been added successfully")
  
              else:
                  messagebox.showwarning("Warning", "The Genre has not been added,maybe it is existed")
  
                  
          else:
              messagebox.showwarning("Warning", "All information are required")
  