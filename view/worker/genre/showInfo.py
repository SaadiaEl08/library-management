from tkinter import ttk
from customtkinter import *
from model.genre.genre import Genre
from view.worker.genre import modifyGenre
from controler.worker.genre.deleteGenre import deleteGenre
from controler.worker.genre.searchGenre import *
from tkinter import messagebox

class ShowInfo:
    def __init__(self,win,name=None):
        self.name = name
        if self.name  != None:
          self.rows=searchByName(self.name)
        elif self.name == None :
            self.rows=All()
        if len(self.rows) == 0:
            messagebox.showwarning("Not found","No Genre Founded ")
            return 
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Show Genre ")
        self.win.grab_set()
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack_propagate(False)

        #show----------------------------------------
        self.showLb=CTkLabel(self.backFrame,text="Show Genre(s)",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.showLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=1.5)
        #------------------------------------------------------------------
        self.modifyBtn=CTkButton(self.frame,text="Modify",command=lambda:modifyGenre.Modify(self.win,self.name),font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.deleteBtn=CTkButton(self.frame,text="Delete",command=lambda:deleteGenre(self.name),font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        if len(self.rows)==1:
            label=CTkLabel(self.frame,text=self.rows[0][0],font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
            label.pack()
            self.modifyBtn.pack(pady=20)
            self.deleteBtn.pack()
        else:
            # Create a Treeview widget-----------------------------
            style = ttk.Style()
            style.configure("Custom.Treeview", font=("Baskerville",15))
            style.configure("Custom.Treeview.Heading",font= ("Baskerville",15,"bold"), foreground="black")
            self.tree = ttk.Treeview(self.frame,columns=("1"),show="headings",style="Custom.Treeview")
            # Format column headers
            self.tree.heading("1", text="Genre Name")
                 # Insert data into the table
            for row in self.rows:
               self.tree.insert("", "end", values=(row[0]))
            self.tree.bind("<<TreeviewSelect>>",self.select)
            # Add the Treeview widget to the root window
            self.tree.pack()
    def select(self,even):
       for x in self.tree.selection():
          genre=(self.tree.item(x)["values"][0])
       self.modifyBtn.configure(command=lambda:modifyGenre.Modify(self.win,genre))
       self.deleteBtn.configure(command=lambda:deleteGenre(genre))
  
       self.modifyBtn.pack(pady=20)
       self.deleteBtn.pack()
           