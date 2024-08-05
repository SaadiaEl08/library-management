from tkinter import messagebox


def deleteSupplier(id):
    if(messagebox.askyesno("Confirmation",f"Are you sure you want to delete the supplier with the Number {id}")):
      from model.conn_creatTables.conn import conn
      req="""Delete from `db_library`.`supplier` where NUMSUP = %s """
      curs=conn.cursor()
      curs.execute(req,(id,))
      conn.commit()
      curs.close()
      conn.close
      messagebox.showinfo("info",f"the supplier with the Number {id} have been deleted successfully") 

      
   
    