from tkinter import messagebox
from model.conn_creatTables.conn import conn
def deleteGenre(name):
    if(messagebox.askyesno("Confirmation",f"Are you sure you want to delete the Genre with the Name {name}")):
      req="""Delete from `db_library`.`namegenre` where NAMEGENRE = %s """
      curs=conn.cursor()
      curs.execute(req,(name,))
      conn.commit()
      curs.close()
      conn.close
      messagebox.showinfo("info",f"the genre with the name {name} have been deleted successfully") 

      
   
    