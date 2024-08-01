from tkinter import ttk
from customtkinter import *
from model.book.book import Book
from view.worker.book import modifyBook
from controler.worker.book.deleteBook import deleteBook
from controler.worker.book.searchBook import *
from tkinter import messagebox

class ShowInfo:
    def __init__(self,win,name=None,number=None,author=None,genre=None):
        self.name = name
        self.number = number
        self.author = author
        self.genre = genre
        if self.name != None:
            self.rows=searchByName(self.name)
        elif self.number != None:
            self.rows=searchByNumber(self.number)
        elif self.author != None:
            self.rows=searchByAuthor(self.author)
        elif self.genre != None:
            self.rows=searchByGenre(self.genre)
        elif self.number == None and self.name == None and self.genre == None and self.author == None:
            self.rows=All()
        if len(self.rows) == 0:
            messagebox.showwarning("Not found","No Book Founded ")
            return 
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("950x500+300+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Show Book(s) ")
        self.win.after(0,self.win.focus)
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
        self.showLb=CTkLabel(self.backFrame,text="Show Book(s)",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.showLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=1.5)
        # Create a Treeview widget-----------------------------
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Baskerville",15))
        style.configure("Custom.Treeview.Heading",font= ("Baskerville",15,"bold"), foreground="black")
        
        self.tree = ttk.Treeview(self.frame,columns=("1", "2", "3","4","5","6","7","8","9","10"),show="headings",style="Custom.Treeview")

        # Format column headers
        self.tree.heading("1", text="N°")
        self.tree.heading("2", text="Name")
        self.tree.heading("3", text="Genre")
        self.tree.heading("4", text="Loan duration")
        self.tree.heading("5", text="Author")
        self.tree.heading("6", text="Writing date")
        self.tree.heading("7", text="Supplier")
        self.tree.heading("8", text="Status")
        self.tree.heading("9", text="Description")
        self.tree.heading("10", text="Loan by")
        # Format column width
        self.tree.column("1", width=50)
        self.tree.column("2", width=150)
        self.tree.column("3", width=150)
        self.tree.column("4", width=150)
        self.tree.column("5", width=150)
        self.tree.column("6", width=150)
        self.tree.column("7", width=150)
        self.tree.column("8", width=150)
        self.tree.column("9", width=150)
        self.tree.column("10",width=150)
        

        # Insert data into the table
        for row in self.rows:
           row9="no one" if row[9] == "null" else row[9]
           self.tree.insert("", "end", values=(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row9))
        self.tree.bind("<<TreeviewSelect>>",self.select)
        # Add the Treeview widget to the root window
        self.tree.pack()
        self.modifyBtn=CTkButton(self.frame,text="Modify",font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.deleteBtn=CTkButton(self.frame,text="Delete",font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
    def select(self,even):
        for x in self.tree.selection():
            numBook=self.tree.item(x)["values"][0]
            numSup=self.tree.item(x)["values"][6].split(" ")[1]
            numAut=self.tree.item(x)["values"][4].split(" ")[1]
            book=Book(self.tree.item(x)["values"][3],self.tree.item(x)["values"][7],self.tree.item(x)["values"][2],self.tree.item(x)["values"][1],numSup,numAut,self.tree.item(x)["values"][5],self.tree.item(x)["values"][8])
        self.modifyBtn.configure(command=lambda:modifyBook.Modify(self.win,numBook,book))
        self.deleteBtn.configure(command=lambda:deleteBook(numBook))
         
        self.modifyBtn.pack(pady=20)
        self.deleteBtn.pack()
    