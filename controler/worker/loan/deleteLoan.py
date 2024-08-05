from tkinter import messagebox
from model.conn_creatTables.conn import conn

def deleteLoan(idBook,idMember):
    if(messagebox.askyesno("Confirmation",f"Are you sure you want to delete the Loan with the Member id = {idMember} , and Book id = {idBook}")):
      req1="""Delete from `db_library`.`loan` where NUMBOOK = %s and IDMEMBER = %s"""
      req2="""update `db_library`.`book` set STATUBOOK ="Available" where NUMBOOK = %s;"""
      curs=conn.cursor()
      curs.execute(req1,(idBook,idMember))
      conn.commit()
      curs.execute(req2,(idBook,))
      conn.commit()
      curs.close()
      conn.close
      messagebox.showinfo("info",f"the loan with the Member id {idMember} , and Book id = {idBook} have been deleted successfully") 
