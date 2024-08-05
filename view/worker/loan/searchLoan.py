from customtkinter import *
from view.worker.loan import modifyLoan,showInfo
class Parent:
    def __init__(self,win):
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Search Loan by Book Number")
        win.after(0, lambda: self.win.lift())
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack_propagate(False)

        
class ByBookNumber(Parent):
    def __init__(self,win):
        super().__init__(win)
        #search----------------------------------------
        self.searchLb=CTkLabel(self.backFrame,text="Search Supplier by number",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.searchLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=20)
        #widgets------------------------------
        label=CTkLabel(self.frame,text="Entre the Book Number",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.numBook=StringVar()
        entry=CTkEntry(self.frame,textvariable=self.numBook)
        btn=CTkButton(self.frame,text="Search",command=lambda:showInfo.ShowInfo(win,self.numBook.get(),None),font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        #place---------------------------------------------------
        label.pack()
        entry.pack()
        btn.pack(pady=20)
class ByMemberId(Parent):
    def __init__(self,win):
        super().__init__(win)
        #search----------------------------------------
        self.searchLb=CTkLabel(self.backFrame,text="Search Supplier by number",font=("Baskerville",30,"bold"),pady=40,text_color="#FFD700")
        
        self.searchLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=20)
        #widgets------------------------------
        label=CTkLabel(self.frame,text="Entre the Member number",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.numberMember=IntVar()
        entry=CTkEntry(self.frame,textvariable=self.numberMember)
        btn=CTkButton(self.frame,text="Search",command=lambda:showInfo.ShowInfo(win,None,self.numberMember.get()),font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        #place---------------------------------------------------
        label.pack()
        entry.pack()
        btn.pack(pady=20)
