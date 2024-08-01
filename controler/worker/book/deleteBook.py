from tkinter import messagebox
from model.conn_creatTables.conn import conn
def deleteBook(id):
    if(messagebox.askyesno("Confirmation",f"Are you sure you want to delete the Book with the Number {id}")):
      req="""Delete from `db_library`.`Book` where NUMBOOK = %s """
      curs=conn.cursor()
      curs.execute(req,(id,))
      conn.commit()
      curs.close()
      conn.close
      messagebox.showinfo("info",f"the Book.py with the Number {id} have been deleted successfully") 

      
   
    