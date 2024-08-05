from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
from view.worker.book import addBook,searchBook,showInfo as showInfoBook
from view.worker.supplier import addSupplier,searchSupplier,showInfo as showInfoSupplier
from view.worker.member import addMember,searchMember,showInfo as showInfoMember
from view.worker.loan import addLoan,searchLoan,showInfo as showInfoLoan
from view.worker.author import addAuthor,searchAuthor,showInfo as showInfoAuthor
from view.worker.genre import addGenre,searchGenre,showInfo as showInfoGenre
class Home:
    def __init__(self,win):
        #win-----------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Home")
        self.win.wm_transient(win)
        self.win.configure(fg_color="#0B0B41")

        #Menu bar-----------------------------------------
        self.menuBar=Menu(self.win,tearoff=0)
        self.win.config(menu=self.menuBar)
        #supplier menu--------------------------------
        self.supMenu=Menu(self.menuBar,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.menuBar.add_cascade(label="Supplier",menu=self.supMenu)
        self.supMenu.add_command(label="Add",command=lambda:addSupplier.Add(self.win))
        self.searchSupMenu=Menu(self.supMenu,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.supMenu.add_cascade(label="Search",menu=self.searchSupMenu)
        self.searchSupMenu.add_command(label="All",command=lambda:showInfoSupplier.ShowInfo(self.win))
        self.searchSupMenu.add_command(label="By Number",command=lambda:searchSupplier.ByNumber(self.win))
        self.searchSupMenu.add_command(label="By Name",command=lambda:searchSupplier.ByName(self.win))
        #book genre menu--------------------------------
        self.genreMenu=Menu(self.menuBar,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.menuBar.add_cascade(label="Book genre",menu=self.genreMenu)
        self.genreMenu.add_command(label="Add",command=lambda:addGenre.Add(self.win))
        self.searchGenreMenu=Menu(self.genreMenu,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.genreMenu.add_cascade(label="Search",menu=self.searchGenreMenu)
        self.searchGenreMenu.add_command(label="All",command=lambda:showInfoGenre.ShowInfo(self.win))
        self.searchGenreMenu.add_command(label="Search By Name",command=lambda:searchGenre.ByName(self.win))
        #Author menu--------------------------------
        self.authMenu=Menu(self.menuBar,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.menuBar.add_cascade(label="Author",menu=self.authMenu)
        self.authMenu.add_command(label="Add",command=lambda:addAuthor.Add(self.win))
        self.searchAutMenu=Menu(self.authMenu,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.authMenu.add_cascade(label="Search",menu=self.searchAutMenu)
        self.searchAutMenu.add_command(label="All",command=lambda:showInfoAuthor.ShowInfo(self.win))
        self.searchAutMenu.add_command(label="By Number",command=lambda:searchAuthor.ByNumber(self.win))
        self.searchAutMenu.add_command(label="By Name",command=lambda:searchAuthor.ByName(self.win))
        self.searchAutMenu.add_command(label="By Book Number",command=lambda:searchAuthor.ByBookNumber(self.win))
        #book menu---------------------------------------------
        self.bookMenu=Menu(self.menuBar,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.menuBar.add_cascade(label="Book",menu=self.bookMenu)
        self.bookMenu.add_command(label="Add",command=lambda:addBook.Add(self.win))
        self.searchBookMenu=Menu(self.bookMenu,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.bookMenu.add_cascade(label="Search",menu=self.searchBookMenu)
        self.searchBookMenu.add_command(label="All",command=lambda:showInfoBook.ShowInfo(win))
        self.searchBookMenu.add_command(label="By Number",command=lambda:searchBook.ByNumber(win))
        self.searchBookMenu.add_command(label="By Name",command=lambda:searchBook.ByName(win))
        self.searchBookMenu.add_command(label="By Author",command=lambda:searchBook.ByAuthor(win))
        self.searchBookMenu.add_command(label="By Genre",command=lambda:searchBook.ByGenre(win))
        #Member menu----------------------------------------
        self.memberMenu=Menu(self.menuBar,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.menuBar.add_cascade(label="Member",menu=self.memberMenu)
        self.memberMenu.add_command(label="Add",command=lambda:addMember.Add(self.win))
        self.searchMemberMenu=Menu(self.memberMenu,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.memberMenu.add_cascade(label="Search",menu=self.searchMemberMenu)
        self.searchMemberMenu.add_command(label="All",command=lambda:showInfoMember.ShowInfo(self.win))
        self.searchMemberMenu.add_command(label="By ID",command=lambda:searchMember.ByNumber(self.win))
        self.searchMemberMenu.add_command(label="By Name",command=lambda:searchMember.ByName(self.win))
        self.searchMemberMenu.add_command(label="By Login",command=lambda:searchMember.ByLogin(self.win))
        #loan menu--------------------------------
        self.loanMenu=Menu(self.menuBar,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.menuBar.add_cascade(label="Loan a book",menu=self.loanMenu)
        self.loanMenu.add_command(label="Add",command=lambda:addLoan.Add(self.win))
        self.searchLoanMenu=Menu(self.loanMenu,tearoff=False,fg="white",bg="#04042E",font=("Baskerville",15),activebackground="#FFD700",activeforeground="black")
        self.loanMenu.add_cascade(label="Search",menu=self.searchLoanMenu)
        self.searchLoanMenu.add_command(label="All",command=lambda:showInfoLoan.ShowInfo(self.win))
        self.searchLoanMenu.add_command(label="By Book number",command=lambda:searchLoan.ByBookNumber(self.win))
        self.searchLoanMenu.add_command(label="By Member number",command=lambda:searchLoan.ByMemberId(self.win))
        #backgroundImage----------------------------------------
        self.backgroundImage = Image.open(r"C:\desctoop\OFPPTNew\Prof Sair\PROJECT FIN D ANNE\code\view\images\library.jpg")
        self.photo = ImageTk.PhotoImage(self.backgroundImage)
               
        self.backgroundImageLB=CTkLabel(self.win,text="",image=self.photo)
        
        self.backgroundImageLB.pack(pady=140)
       