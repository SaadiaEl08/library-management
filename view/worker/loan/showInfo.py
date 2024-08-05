from tkinter import ttk
from customtkinter import *
from model.loan.loan import Loan
from view.worker.loan import modifyLoan
from controler.worker.loan.deleteLoan import deleteLoan
from controler.worker.loan.searchLoan import *
from tkinter import messagebox

class ShowInfo:
    def __init__(self,win,numBook=None,numMember=None):
        self.numBook = numBook
        self.numMember = numMember
        self.i=0
        if self.numBook != None:
            self.rows=searchByBookNumber(self.numBook)
        elif self.numMember != None:
            self.rows=searchByMemberNumber(self.numMember)
        elif self.numBook == None and self.numMember == None:
            self.rows=All()
        if len(self.rows) == 0:
            messagebox.showwarning("Not found","No Loan Founded ")
            return 
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("700x500+400+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Show Loan(s) ")
        self.win.grab_set()
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=700,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkFrame(self.backFrame,width=600,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack_propagate(False)

        #show----------------------------------------
        self.showLb=CTkLabel(self.backFrame,text="Show Loan(s)",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.showLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=1.5)
        # Create a Treeview widget-----------------------------
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Baskerville",15))
        style.configure("Custom.Treeview.Heading",font= ("Baskerville",15,"bold"), foreground="black")
        
        
        self.tree = ttk.Treeview(self.frame,columns=("1", "2", "3"),show="headings",style="Custom.Treeview")

        # Format column headers
        self.tree.heading("1", text="N° member ")
        self.tree.heading("2", text="N° book")
        self.tree.heading("3", text="Date loan")

        # Insert data into the table
        for row in self.rows:
           self.tree.insert("", "end", values=(row[0], row[1], row[2]))
        self.tree.bind("<<TreeviewSelect>>",self.select)
        # Add the Treeview widget to the root window
        self.tree.pack()
        self.modifyBtn=CTkButton(self.frame,text="Modify",font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.deleteBtn=CTkButton(self.frame,text="Delete",font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
    def select(self,even):
           for x in self.tree.selection():
              numMember=self.tree.item(x)["values"][0]
              numBook=self.tree.item(x)["values"][1]
              loan=Loan(self.tree.item(x)["values"][0],self.tree.item(x)["values"][1])
           self.modifyBtn.configure(command=lambda:modifyLoan.Modify(self.win,numBook,loan))
           self.deleteBtn.configure(command=lambda:deleteLoan(numBook,numMember))
           
           self.modifyBtn.pack(pady=20)
           self.deleteBtn.pack()
    