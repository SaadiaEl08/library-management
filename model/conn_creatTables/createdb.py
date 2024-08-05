from tkinter import messagebox
import mysql.connector
class CreateDatabase:
   def __init__(self):
      self.conn=mysql.connector.connect(user="root", password="",host="localhost")
      self.req="create database IF NOT EXISTS db_LIBRARY;"
      try:
         self.curs=self.conn.cursor()
         self.curs.execute(self.req)
         self.conn.commit()
         self.curs.close()
         self.conn.close
      except :
         messagebox.showerror("Error connecting","Error connecting to data base")
CreateDatabase()