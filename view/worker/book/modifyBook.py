from customtkinter import *
from tkcalendar import *
from tkinter import messagebox
from datetime import datetime
from controler.worker.book import modifyBook
from model.book import book
from model.conn_creatTables.conn import conn as connector
class Modify:
    def __init__(self,win,id,book):
        self.id=id  
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.win.title("Modify Book")
        win.after(0, lambda: self.win.lift())
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkScrollableFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        #modify----------------------------------------
        self.modifyLb=CTkLabel(self.backFrame,text="Modify Book",font=("Baskerville",30,"bold"),pady=30,bg_color="#0B0B41",text_color="#FFD700")
        
        self.modifyLb.pack()
        #NAMEBOOK---------------------------------------------------------------------------
        self.NAMEBOOKLB=CTkLabel(self.frame,text="Book Name:",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.NAMEBOOK=StringVar()
        self.NAMEBOOKEN=CTkEntry(self.frame,textvariable=self.NAMEBOOK ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        self.NAMEBOOK.set(book.NAMEBOOK)
        
        self.NAMEBOOKLB.pack()
        self.NAMEBOOKEN.pack()
        #LOANDURATION-------------------------------------------------------------------
        self.LOANDURATIONLB=CTkLabel(self.frame,text="Loan duration: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.LOANDURATION=StringVar()
        self.LOANDURATIONEN=CTkEntry(self.frame,textvariable=self.LOANDURATION ,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))
        self.LOANDURATION.set(book.LOANDURATION)
        
        self.LOANDURATIONLB.pack()
        self.LOANDURATIONEN.pack()
        #STATUBOOK--------------------------------------------------------------------
        self.STATUBOOKLB=CTkLabel(self.frame,text="Book status: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.STATUBOOKCBX=CTkComboBox(self.frame,state="readonly",values=("Available","On Loan","Overdue"),width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",button_color="#FFD700",dropdown_fg_color="#0B0B41",dropdown_hover_color="#FFD700",font=("Baskerville",15))
        self.STATUBOOKCBX.set(book.STATUBOOK)
        
        
        self.STATUBOOKLB.pack()
        self.STATUBOOKCBX.pack()
        #NAMEGENRE---------------------------------------------------------------------
        self.NAMEGENRELB=CTkLabel(self.frame,text="Genre Name: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.NAMEGENRECBX=CTkComboBox(self.frame,state="readonly",width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",button_color="#FFD700",dropdown_fg_color="#0B0B41",dropdown_hover_color="#FFD700",font=("Baskerville",15))
        
        conn=connector
        req=("SELECT NAMEGENRE FROM namegenre;")
        curs=conn.cursor()
        curs.execute(req)
        rowNAMEGENRE=curs.fetchall()
        self.NAMEGENRECBX.configure(values=[f"{row[0]}" for row in rowNAMEGENRE])
        curs.close()
        conn.close
        
        self.NAMEGENRECBX.set(book.NAMEGENRE)
        
        self.NAMEGENRELB.pack()
        self.NAMEGENRECBX.pack()
        
        #NAMESUP--------------------------------------------------------------------------------------
        self.NUMSUPLB=CTkLabel(self.frame,text="Supplier : ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.NUMSUPCBX=CTkComboBox(self.frame,state="readonly",width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",button_color="#FFD700",dropdown_fg_color="#0B0B41",dropdown_hover_color="#FFD700",font=("Baskerville",15))
        
        conn=connector
        req=("select NUMSUP,LASTNAMESUP from SUPPLIER;")
        curs=conn.cursor()
        curs.execute(req)
        rowNUMSUP=curs.fetchall()  
        values=[f"{row[0]}-{row[1]}" for row in rowNUMSUP] 
        self.NUMSUPCBX.configure(values=values)
        curs.close()
        conn.close
        
        numSup = [element for element in values if element.split("-")[0] == str(book.NUMSUP)]
        self.NUMSUPCBX.set(numSup)
        
        
        self.NUMSUPLB.pack()
        self.NUMSUPCBX.pack()
        #NAMEAUT-----------------------------------------------------------------------------------------
        self.NUMAUTLB=CTkLabel(self.frame,text="Author : ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.NUMAUTCBX=CTkComboBox(self.frame,state="readonly",width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",button_color="#FFD700",dropdown_fg_color="#0B0B41",dropdown_hover_color="#FFD700",font=("Baskerville",15))
        
        conn=connector
        req=("select NUMAUT,LASTNAMEAUT,FIRSTNAMEAUT from AUTHOR;")
        curs=conn.cursor()
        curs.execute(req)
        rowNUMAUT=curs.fetchall()
        values=[f"{row[0]}-{row[1]}-{row[2]}" for row in rowNUMAUT]
        self.NUMAUTCBX.configure(values=values)
        curs.close()
        conn.close
        
        numAut =[element for element in values if element.split("-")[0] == str(book.NUMAUT)]
        self.NUMAUTCBX.set(numAut)
        
        self.NUMAUTLB.pack()
        self.NUMAUTCBX.pack()
        #BOOKWRITINGDATE-----------------------------------------------------------------------------------
        self.BOOKWRITINGDATELB=CTkLabel(self.frame,text="Book writing date: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.BOOKWRITINGDATEEN=DateEntry(self.frame,width=30, background='darkblue',foreground='white', borderwidth=2)
        self.BOOKWRITINGDATEEN.set_date(datetime.strptime(book.BOOKWRITINGDATE,"%Y-%m-%d"))
        
        self.BOOKWRITINGDATELB.pack()
        self.BOOKWRITINGDATEEN.pack()
        #description-------------------------------------------
        self.DESCRIPTIONLB=CTkLabel(self.frame,text="Description : ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.DESCRIPTIONTXT=CTkTextbox(self.frame,width=200,height=150,corner_radius=20,border_width=0.5,fg_color="black",border_color="#FFD700")
        self.DESCRIPTIONTXT.insert(0.1,f"{book.DESCRIPTION}")
        
        self.DESCRIPTIONLB.pack()
        self.DESCRIPTIONTXT.pack()
        #Add btn-----------------------------------------------------------------------------
        self.MODBTN=CTkButton(self.frame,text="Modify Book",command=self.validateInfo,font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.MODBTN.pack(pady=20)
    def validateInfo(self):
        if(self.LOANDURATION.get().isdigit() and self.NAMEBOOK.get()!="" and self.STATUBOOKCBX.get() !="" and self.NAMEGENRECBX.get() !="" and self.NUMSUPCBX.get() !="" and self.NUMAUTCBX.get()!="" and self.BOOKWRITINGDATEEN.get_date() !="" and self.DESCRIPTIONTXT.get("1.0", END)):
            numAut=int(self.NUMAUTCBX.get().split("-")[0])
            numSup=int(self.NUMSUPCBX.get().split("-")[0])
            newBook=book.Book(self.LOANDURATION.get(),self.STATUBOOKCBX.get(),self.NAMEGENRECBX.get(),self.NAMEBOOK.get(),numSup,numAut,self.BOOKWRITINGDATEEN.get_date(),self.DESCRIPTIONTXT.get("1.0", END))
            result=modifyBook.modify(self.id,newBook)
            if (result):
                messagebox.showinfo("info", "The book has been modified successfully")
                self.win.destroy()
            else:
                messagebox.showwarning("Warning", "The book has not been modified,maybe it is existed")

                
        else:
            messagebox.showwarning("Warning", "All information are required")
