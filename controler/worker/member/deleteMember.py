from tkinter import messagebox
from model.conn_creatTables.conn import conn


def deleteMember(id):
    if(messagebox.askyesno("Confirmation",f"Are you sure you want to delete the member with the id {id}")):
      req="""Delete from `db_library`.`Member` where IDMEMBER = %s """
      curs=conn.cursor()
      curs.execute(req,(id,))
      conn.commit()
      curs.close()
      conn.close
      messagebox.showinfo("info",f"the member with the id {id} have been deleted successfully") 

      
   
    