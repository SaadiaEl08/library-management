from tkinter import messagebox
def Verify(win,user,password):
    if(user != "worker" or password != "work1234"):
      messagebox.showerror("Error", "the user or password are wrong")
    else:
      from model.conn_creatTables import createTables
      from view.worker import home
      home.Home(win)
