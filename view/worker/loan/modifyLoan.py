from customtkinter import *
from tkcalendar import *
from tkinter import messagebox
from datetime import datetime
from controler.worker.loan import modifyLoan
from model.loan import loan
from model.conn_creatTables.conn import conn as connector
class Modify:
    def __init__(self,win,id,loan):
        self.id=id  
        #win---------------------------------------------------------------------------------
        self.win=CTkToplevel(win)
        self.win.geometry("500x500+500+100")
        self.win.resizable(width=False, height=False)
        set_appearance_mode("dark")  
        self.win.title("Modify loan")
        win.after(0, lambda: self.win.lift())
        #backFrame-----------------------------------------------------
        self.backFrame = CTkFrame(self.win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
        self.backFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.backFrame.pack_propagate(False)
        #frame-----------------------------------------------------
        self.frame = CTkFrame(self.backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack_propagate(False)
        #modify----------------------------------------
        self.modifyLb=CTkLabel(self.backFrame,text="Modify Loan",font=("Baskerville",30,"bold"),pady=40,bg_color="#0B0B41",text_color="#FFD700")
        
        self.modifyLb.pack()
        #space---------------------------------------------------------------------------
        self.space=CTkLabel(self.frame,text="")
                
        self.space.pack(pady=15)
        #NUMBOOK---------------------------------------------------------------------
        self.NUMBOOKLB=CTkLabel(self.frame,text="Book number: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.NUMBOOKCBX=CTkComboBox(self.frame,state="readonly",width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",button_color="#FFD700",dropdown_fg_color="#0B0B41",dropdown_hover_color="#FFD700",font=("Baskerville",15))
        
        conn=connector
        req=("SELECT NUMBOOK FROM Book;")
        curs=conn.cursor()
        curs.execute(req)
        rowNUMBOOK=curs.fetchall()
        self.NUMBOOKCBX.configure(values=[f"{row[0]}" for row in rowNUMBOOK])
        curs.close()
        conn.close
        self.NUMBOOKCBX.set(loan.NUMBOOK)

        
        self.NUMBOOKLB.pack()
        self.NUMBOOKCBX.pack()
        #IDMEMBER--------------------------------------------------------------------------------------
        self.IDMEMBERLB=CTkLabel(self.frame,text="ID member : ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
        self.IDMEMBERCBX=CTkComboBox(self.frame,state="readonly",width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",button_color="#FFD700",dropdown_fg_color="#0B0B41",dropdown_hover_color="#FFD700",font=("Baskerville",15))
        
        conn=connector
        req=("select IDMEMBER from MEMBER;")
        curs=conn.cursor()
        curs.execute(req)
        rowIDMEMBER=curs.fetchall()        
        self.IDMEMBERCBX.configure(values=[f"{row[0]}" for row in rowIDMEMBER])
        curs.close()
        conn.close
        self.IDMEMBERCBX.set(loan.IDMEMBER)

        
        self.IDMEMBERLB.pack()
        self.IDMEMBERCBX.pack()
       
        #Add btn-----------------------------------------------------------------------------
        self.MODBTN=CTkButton(self.frame,text="Modify Loan",command=self.validateInfo,corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
        self.MODBTN.pack(pady=20)
    def validateInfo(self):
        if(self.IDMEMBERCBX.get() !="" and self.NUMBOOKCBX.get() !="" ):
            newLoan=loan.Loan(self.IDMEMBERCBX.get(),self.NUMBOOKCBX.get())
            result=modifyLoan.modifyLoan(self.id,newLoan)
            if (result):
                self.IDMEMBERCBX.set("")
                self.NUMBOOKCBX.set("")
                messagebox.showinfo("info", "The Loan has been added successfully")

            else:
                messagebox.showwarning("Warning", "The Loan has not been added,maybe it is existed")

                
        else:
            messagebox.showwarning("Warning", "All information are required")
