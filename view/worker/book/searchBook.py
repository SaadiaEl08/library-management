from customtkinter import *
from view.worker.book import showInfo
class Parent:
    def __init__(self,win):
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Search Book by name")
        win.after(0, lambda: self.win.lift())
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack_propagate(False)

        
class ByName(Parent):
    def __init__(self,win):
        super().__init__(win)
        #search----------------------------------------
        self.searchLb=CTkLabel(self.backFrame,text="Search Book by name",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.searchLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=20)
        #widgets------------------------------
        label=CTkLabel(self.win,text="Entre the Book name",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.name=StringVar()
        entry=CTkEntry(self.win,textvariable=self.name,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        btn=CTkButton(self.win,text="Search",command=lambda:showInfo.ShowInfo(win,self.name.get(),None,None,None),font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        #place---------------------------------------------------
        label.pack()
        entry.pack()
        btn.pack(pady=20)
class ByNumber(Parent):
    def __init__(self,win):
        super().__init__(win)
        #search----------------------------------------
        self.searchLb=CTkLabel(self.backFrame,text="Search book by number",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.searchLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=20)
        #widgets------------------------------
        label=CTkLabel(self.win,text="Entre the book name",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.number=IntVar()
        entry=CTkEntry(self.win,textvariable=self.number,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        btn=CTkButton(self.win,text="Search",command=lambda:showInfo.ShowInfo(win,None,self.number.get(),None,None),font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        #place---------------------------------------------------
        label.pack()
        entry.pack()
        btn.pack(pady=20)
class ByAuthor(Parent):
    def __init__(self,win):
        super().__init__(win)
        #search----------------------------------------
        self.searchLb=CTkLabel(self.backFrame,text="Search book by Author",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.searchLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=20)
        #widgets------------------------------
        label=CTkLabel(self.win,text="Entre the book Author last name",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.author=StringVar()
        entry=CTkEntry(self.win,textvariable=self.author,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        btn=CTkButton(self.win,text="Search",command=lambda:showInfo.ShowInfo(win,None,None,self.author.get(),None),font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        #place---------------------------------------------------
        label.pack()
        entry.pack()
        btn.pack(pady=20)
class ByGenre(Parent):
    def __init__(self,win):
        super().__init__(win)
        
        #search----------------------------------------
        self.searchLb=CTkLabel(self.backFrame,text="Search Book by genre",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.searchLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=20)
        #widgets------------------------------
        label=CTkLabel(self.win,text="Entre the book genre",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.genre=StringVar()
        entry=CTkEntry(self.win,textvariable=self.genre,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        btn=CTkButton(self.win,text="Search",command=lambda:showInfo.ShowInfo(win,None,None,None,self.genre.get()),font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        #place---------------------------------------------------
        label.pack()
        entry.pack()
        btn.pack(pady=20)
        
        
        
    