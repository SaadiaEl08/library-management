from tkinter import ttk
from customtkinter import *
from model.member.member import Member
from view.worker.member import modifyMember
from controler.worker.member.deleteMember import deleteMember
from controler.worker.member.searchMember import *
from tkinter import messagebox

class ShowInfo:
    def __init__(self,win,id=None,name=None,login=None):
        self.id = id
        self.name = name
        self.login = login
        if self.id != None:
            self.rows=searchByNumber(self.id)
        elif self.name != None:
            self.rows=searchByName(self.name)
        elif self.login != None:
            self.rows=searchByLogin(self.login)
        elif self.id == None and self.name == None and self.login == None:
            self.rows=All()
        if len(self.rows) == 0:
            messagebox.showwarning("Not found","No Member Founded ")
            return 
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("950x500+300+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Show Member(s) ")
        self.win.grab_set()
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=950,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkFrame(self.backFrame,width=900,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack_propagate(False)

        #show----------------------------------------
        self.showLb=CTkLabel(self.backFrame,text="Show Member(s)",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.showLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=1.5)
        # Create a Treeview widget-----------------------------
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Baskerville",15))
        style.configure("Custom.Treeview.Heading",font= ("Baskerville",15,"bold"), foreground="black")
       
        self.tree = ttk.Treeview(self.frame,columns=("1", "2", "3","4","5","6","7"),show="headings",style="Custom.Treeview")

        # Format column headers
        self.tree.heading("1", text="ID")
        self.tree.heading("2", text="Last Name")
        self.tree.heading("3", text="First Name")
        self.tree.heading("5", text="Login")
        self.tree.heading("6", text="Password")
        self.tree.heading("7", text="city")
        self.tree.heading("4", text="Tel")

        # Insert data into the table
        for row in self.rows:
           self.tree.insert("", "end", values=(row[0],row[1], row[2],row[3],row[4],row[5],row[6]))
        self.tree.bind("<<TreeviewSelect>>",self.select)
        # Add the Treeview widget to the root window
        self.tree.pack()
        self.modifyBtn=CTkButton(self.frame,text="Modify",font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.deleteBtn=CTkButton(self.frame,text="Delete",font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
    def select(self,even):
        for x in self.tree.selection():
           numMember=self.tree.item(x)["values"][0]
           member=Member(self.tree.item(x)["values"][1],self.tree.item(x)["values"][2],self.tree.item(x)["values"][3],self.tree.item(x)["values"][4],self.tree.item(x)["values"][5],self.tree.item(x)["values"][6])
        self.modifyBtn.configure(command=lambda:modifyMember.Modify(self.win,numMember,member))
        self.deleteBtn.configure(command=lambda:deleteMember(numMember))
        
        self.modifyBtn.pack(pady=20)
        self.deleteBtn.pack()
    