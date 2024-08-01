from customtkinter import *
from tkinter import *
from controler.worker.verifyLogin import Verify
    
#win----------------------------------------------------------------
win=CTk()
win.geometry("500x500+500+100")
win.resizable(width=False, height=False)
set_appearance_mode("dark")
win.title("Log in page ")
#backFrame-----------------------------------------------------
backFrame = CTkFrame(win,width=500,height=500,fg_color="#0B0B41",bg_color="#0B0B41",border_width=0)
backFrame.place(relx=0.5, rely=0.5, anchor="center")
backFrame.pack_propagate(False)
#frame-----------------------------------------------------
frame = CTkFrame(backFrame,width=300,height=300,fg_color="#04042E",border_width=0,corner_radius=20)
frame.place(relx=0.5, rely=0.5, anchor="center")
frame.pack_propagate(False)

#Welcome back message----------------------------------------
welcomeBackLb=CTkLabel(win,text="Welcome Back Our Worker",font=("Georgia",25),pady=10,bg_color="#0B0B41",text_color="#FFD700")

welcomeBackLb.place(x=100,y=20)
#Login----------------------------------------
loginLb=CTkLabel(frame,text="Login",font=("Baskerville",30,"bold"),pady=30,text_color="#FFD700")

loginLb.pack()
#User------------------------------------------------------
userLb=CTkLabel(frame,text="User: ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
user=StringVar()
userEn=CTkEntry(frame,textvariable=user,width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))

userLb.pack()
userEn.pack()
#Password ----------------------------------------------------
passwordLb=CTkLabel(frame,text="Password : ",font=("Baskerville",18),pady=10 ,text_color="#FFD700")
password=StringVar()
passwordEn=CTkEntry(frame,textvariable=password,show="*",width=150,height=30,corner_radius=10,border_width=0.5,border_color="#FFD700",fg_color="#0B0B41",font=("Baskerville",15))

passwordLb.pack()
passwordEn.pack()
#Button login--------------------------------------------------
sloginBtn=CTkButton(frame,text="Login",command=lambda:Verify(win,user.get(),password.get()),font=("Baskerville",18),corner_radius=20,border_width=0,hover_color="white",fg_color="#FFD700",text_color="#04042E")
sloginBtn.pack(pady=20)


win.mainloop()