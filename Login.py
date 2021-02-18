from tkinter import *
import os
from PIL import ImageTk,Image
from tkinter import messagebox
def mandatory():
    if os.path.isfile('databases/userdetail.dat'):
        return
    else:
        os.system("mkdir databases")
        file=open('userdetail.dat' , "w")
        user_set=input("Set UserName:")
        pass_set=input("Set PassWord:")
        cnfrm_pass=input("Confirm PassWord:")
        if pass_set==cnfrm_pass:
            data=user_set+"/"+pass_set
            file.write(data)
        file.close()
mandatory()
class login:
    def __init__(self,root):
            self.root=root
            self.root.title("Hermes_Login")
            #====BG Image====
            image2=Image.open("F:\project_Hermes\project_3\Online_crime\crime.png")
            self.bg=ImageTk.PhotoImage(image2)
            self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
            w = self.bg.width()
            h = self.bg.height()
            root.geometry('{}x{}'.format(w,h))
        
            #====Login frame=====
            Frame_login=Frame(self.root)
            Frame_login.place(x=h//2-200,y=w//2-200,height=400,width=400)


            title=Label(Frame_login,text="Login To Hermes",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=40,y=30)
            desc=Label(Frame_login,text="Crime Investigators Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white")
            desc.place(relx=30,rely=100)


            lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=140)
            self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
            self.txt_user.place(x=30,y=170,width=350,height=35)

            lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=210)
            self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
            self.txt_pass.place(x=30,y=240,width=350,height=35)

            forget_btn=Button(Frame_login,text="Forget Password?",command=mandatory,cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=30,y=280)
            Login_btn=Button(self.root,command=self.Login_function, cursor="hand2",text="Login",bg="black",fg="#d77337",font=("times new roman",20)).place(x=w//2-90,y=420,width=180,height=40)

    def Login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
                       messagebox.showerror("Error","All fields are required",parent=self.root)
                       
        file=open('userdetail.dat',"r")
        data=file.read()
        file.close()
        data=list(data.split("/"))
        if self.txt_user.get()==data[0] and self.txt_pass.get()==data[1]:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}",parent=self.root)
            self.root.destroy()
            os.system("F:\project_Hermes\project_1\Crime_Database\criminal_finder_application.py")
            return
        else:
            print("UnAuthorized!! Try Again.")
            return
        

      
                   
                   
root=Tk()  
obj=login(root)
mainloop()
