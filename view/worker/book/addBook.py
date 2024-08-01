from customtkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from datetime import datetime
from model.book import book
from controler.worker.book.addBook import addBook
from model.conn_creatTables.conn import conn as connector
class Add:
    def __init__(self,win):
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Add Book")
        self.win.wm_transient(win)
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkScrollableFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        #ADD----------------------------------------
        self.addLb=CTkLabel(self.backFrame,text="Add Book",font=("Baskerville",30,"bold"),pady=30,bg_color="#0B0B41",text_color="#FFD700")
        
        self.addLb.pack()
        #NAMEBOOK---------------------------------------------------------------------------
        self.NAMEBOOKLB=CTkLabel(self.frame,text="Book Name:" ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.NAMEBOOK=StringVar()
        self.NAMEBOOKEN=CTkEntry(self.frame,textvariable=self.NAMEBOOK,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.NAMEBOOKLB.pack()
        self.NAMEBOOKEN.pack()
        #LOANDURATION-------------------------------------------------------------------
        self.LOANDURATIONLB=CTkLabel(self.frame,text="Loan duration: " ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.LOANDURATION=StringVar()
        self.LOANDURATIONEN=CTkEntry(self.frame,textvariable=self.LOANDURATION,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.LOANDURATIONLB.pack()
        self.LOANDURATIONEN.pack()
        #STATUBOOK--------------------------------------------------------------------
        self.STATUBOOKLB=CTkLabel(self.frame,text="Book status: " ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.STATUBOOKCBX=CTkComboBox(self.frame,state="readonly",values=("Available","On Loan","Overdue") ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",button_color="#FFD700",dropdown_fg_color="#0B0B41",dropdown_hover_color="#FFD700",font=("Baskerville",15))
        
        
        self.STATUBOOKLB.pack()
        self.STATUBOOKCBX.pack()
        #NAMEGENRE---------------------------------------------------------------------
        self.NAMEGENRELB=CTkLabel(self.frame,text="Genre Name: " ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.NAMEGENRECBX=CTkComboBox(self.frame,state="readonly" ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",button_color="#FFD700",dropdown_fg_color="#0B0B41",dropdown_hover_color="#FFD700",font=("Baskerville",15))
        conn=connector
        req=("SELECT NAMEGENRE FROM namegenre;")
        curs=conn.cursor()
        curs.execute(req)
        rowNAMEGENRE=curs.fetchall()
        self.NAMEGENRECBX.configure(values=[f"{row[0]}" for row in rowNAMEGENRE])
        curs.close()
        conn.close
        
        self.NAMEGENRELB.pack()
        self.NAMEGENRECBX.pack()
        
        #NAMESUP--------------------------------------------------------------------------------------
        self.NUMSUPLB=CTkLabel(self.frame,text="Supplier : " ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.NUMSUPCBX=CTkComboBox(self.frame,state="readonly" ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",button_color="#FFD700",dropdown_fg_color="#0B0B41",dropdown_hover_color="#FFD700",font=("Baskerville",15))
        
        conn=connector
        req=("select NUMSUP,LASTNAMESUP from SUPPLIER;")
        curs=conn.cursor()
        curs.execute(req)
        rowNUMSUP=curs.fetchall()        
        self.NUMSUPCBX.configure(values=[f"{row[0]}-{row[1]}" for row in rowNUMSUP])
        curs.close()
        conn.close
        
        
        self.NUMSUPLB.pack()
        self.NUMSUPCBX.pack()
        #NAMEAUT-----------------------------------------------------------------------------------------
        self.NUMAUTLB=CTkLabel(self.frame,text="Author : " ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.NUMAUTCBX=CTkComboBox(self.frame,state="readonly",width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",button_color="#FFD700",dropdown_fg_color="#0B0B41",dropdown_hover_color="#FFD700",font=("Baskerville",15))
        
        conn=connector
        req=("select NUMAUT,LASTNAMEAUT,FIRSTNAMEAUT from AUTHOR;")
        curs=conn.cursor()
        curs.execute(req)
        rowNUMAUT=curs.fetchall()
        self.NUMAUTCBX.configure(values=[f"{row[0]}-{row[1]}-{row[2]}" for row in rowNUMAUT])
        curs.close()
        conn.close
        
        self.NUMAUTLB.pack()
        self.NUMAUTCBX.pack()
        #BOOKWRITINGDATE-----------------------------------------------------------------------------------
        self.BOOKWRITINGDATELB=CTkLabel(self.frame,text="Book writing date: " ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.BOOKWRITINGDATEEN=DateEntry(self.frame ,background='darkblue',foreground='white', borderwidth=2,width=30,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        
        self.BOOKWRITINGDATELB.pack()
        self.BOOKWRITINGDATEEN.pack()
        #description-------------------------------------------
        self.DESCRIPTIONLB=CTkLabel(self.frame,text="Description : " ,font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.DESCRIPTIONTXT=CTkTextbox(self.frame,width=200,height=150,corner_radius=20,border_width=0.5,fg_color="black",border_color="#FFD700")
        
        self.DESCRIPTIONLB.pack()
        self.DESCRIPTIONTXT.pack()
        #Add btn-----------------------------------------------------------------------------
        self.ADDBTN=CTkButton(self.frame,text="Add Book",command=self.validateInfo,font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.ADDBTN.pack(pady=20)
    def validateInfo(self):
        if(self.LOANDURATION.get().isdigit() and self.NAMEBOOK.get()!="" and self.STATUBOOKCBX.get() !="" and self.NAMEGENRECBX.get() !="" and self.NUMSUPCBX.get() !="" and self.NUMAUTCBX.get()!="" and self.BOOKWRITINGDATEEN.get_date() !="" and self.DESCRIPTIONTXT.get("1.0", END)):
            numAut=int(self.NUMAUTCBX.get().split("-")[0])
            numSup=int(self.NUMSUPCBX.get().split("-")[0])
            newBook=book.Book(self.LOANDURATION.get(),self.STATUBOOKCBX.get(),self.NAMEGENRECBX.get(),self.NAMEBOOK.get(),numSup,numAut,self.BOOKWRITINGDATEEN.get_date(),self.DESCRIPTIONTXT.get("1.0", END))
            result=addBook(newBook)
            if (result):
                self.NAMEBOOK.set("")
                self.LOANDURATION.set("")
                self.NUMSUPCBX.set("")
                self.NUMAUTCBX.set("")
                self.BOOKWRITINGDATEEN.set_date(datetime.now())
                self.DESCRIPTIONTXT.delete(1.0, 'end')
                messagebox.showinfo("info", "The book has been added successfully")

            else:
                messagebox.showwarning("Warning", "The book has not been added,maybe it is existed")

                
        else:
            messagebox.showwarning("Warning", "All information are required ")
