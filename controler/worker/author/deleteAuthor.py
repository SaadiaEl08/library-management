from tkinter import messagebox
from model.conn_creatTables.conn import conn


def deleteAuthor(id):
    if(messagebox.askyesno("Confirmation",f"Are you sure you want to delete the author with the Number {id}")):
      req="""Delete from `db_library`.`author` where NUMAUT = %s """
      curs=conn.cursor()
      curs.execute(req,(id,))
      conn.commit()
      curs.close()
      conn.close
      messagebox.showinfo("info",f"the Author with the Number {id} have been deleted successfully") 

      
   
    