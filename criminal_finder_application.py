from tkinter import *
import sqlite3
import tabulate
import random
from datetime import time
import time
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import filedialog

base = Tk()
base.geometry("1200x750")
#base.config(background="#ffa500")
base.config(background="#211916")
base.title("Hermes")
#=====database
con = sqlite3.connect("Hermes.db")

#------------------------------- Events Starts -------------------------------------------
def event1():
    temp = Frame(rightFrame, width=1250, height=850)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#211916")

    def event1_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)

    h1 = Label(temp, text="ADD NEW CRIMINAL", height="2", width="30", font=20)
    h1.place(x=330, y=10)

    criminal_id = Label(temp, text="ENTER CRIMINAL ID", fg="white", background="#283A90", font="20")
    criminal_id.place(x=100, y=65)
    txt1 = Entry(temp, width="57")
    txt1.place(x=330, y=65)

    criminal_name = Label(temp, text="ENTER CRIMINAL NAME", fg="white", background="#283A90", font="20")
    criminal_name.place(x=100, y=115)
    txt2 = Entry(temp, width="57")
    txt2.place(x=330, y=115)

    criminal_mob = Label(temp, text="ENTER CRIMINAL MOB NO", fg="white", background="#283A90", font="20")
    criminal_mob.place(x=100, y=165)
    txt3 = Entry(temp, width="57")
    txt3.place(x=330, y=165)

    criminal_dob = Label(temp, text="ENTER CRIMINAL D.O.B.", fg="white", background="#283A90", font="20")
    criminal_dob.place(x=100, y=215)
    txt4 = DateEntry(temp, font=('Times New Roman', 12, 'bold'), width=20)
    #txt4 = Entry(temp, width="40")
    txt4.place(x=330, y=215)

    criminal_gender = Label(temp, text="ENTER CRIMINAL GENDER.", fg="white", background="#283A90", font="20")
    criminal_gender.place(x=100, y=260)
    var = IntVar()
    Radiobutton(temp, text="Male", padx=5, variable=var, value=1).place(x=330, y=260)
    Radiobutton(temp, text="Female", padx=20, variable=var, value=2).place(x=400, y=260)
    Radiobutton(temp, text="Other", padx=20, variable=var, value=3).place(x=515, y=260)

    criminal_addr = Label(temp, text="ENTER CRIMINAL ADDRESS", fg="white", background="#283A90", font="20")
    criminal_addr.place(x=100, y=300)
    txt5 = Entry(temp, width="57")
    txt5.place(x=330, y=307)
    
    #criminal_image = Label(temp, text="UPLOAD CRIMINAL IMAGE", fg="white", background="#283A90", font="20")
    #criminal_image.place(x=100, y=340)
    #upload = Button(temp, width="25", height="1", bd="2", activebackground="green", text="UPLOAD AN IMAGE")
    #upload.place(x=330, y=344)

    crime_type = Label(temp, text="ENTER CRIME TYPE", fg="white", background="#283A90", font="20")
    crime_type.place(x=100, y=380)
    txt6 = Entry(temp, width="57")
    txt6.place(x=330, y=380)

    crime_city = Label(temp, text="ENTER CRIME CITY", fg="white", background="#283A90", font="20")
    crime_city.place(x=100, y=420)
    txt7 = Entry(temp, width="57")
    txt7.place(x=330, y=420)

    crime_date = Label(temp, text="ENTER CRIME DATE", fg="white", background="#283A90", font="20")
    crime_date.place(x=100, y=460)
    txt8 = DateEntry(temp, font=('Times New Roman', 12, 'bold'), width=20)
    txt8.place(x=330, y=460)

    crime_time = Label(temp, text="ENTER CRIME TIME", fg="white", background="#283A90", font="20")
    crime_time.place(x=100, y=500)
    txt9 = Entry(temp, width="57")
    txt9.place(x=330, y=500)

    jail_name = Label(temp, text="ENTER JAIL NAME", fg="white", background="#283A90", font="20")
    jail_name.place(x=100, y=540)
    txt10 = Entry(temp, width="57")
    txt10.place(x=330, y=540)

    jail_addr = Label(temp, text="ENTER JAIL ADDRESS", fg="white", background="#283A90", font="20")
    jail_addr.place(x=100, y=580)
    txt11 = Entry(temp, width="57")
    txt11.place(x=330, y=580)
    #def save():
     #   con = sqlite3.connect("Hermes.db")
      #  cursor=con.cursor()
       # query = '''insert into criminal_data(criminal_id,criminal_name,crime_type,crime_date,crime_time,crime_city,criminal_mobile_number,criminal_gender,criminal_dob,criminal_address,jail_name,jail_address)
         #           values(txt1.get(),str(text2.get()),str(text3.get()),str(text4.get()),str(text5.get()),str(text6.get()),text7.get()),str(text8.get()),str(text9.get()),str(text10.get()),str(text11.get()))'''
        #con.execute(query)
        #con.commit()
        #con.close()
        #messagebox.askokcancel("","criminal information saved!!")
    
    def save():
        con = sqlite3.connect("Hermes.db")
        query = "insert into criminal_data values criminal_name='"+str(txt2.get())+"', crime_type='"+str(txt6.get())+"', crime_date='"+str(txt8.get())+"', crime_time='"+str(txt9.get())+"', crime_city='"+str(txt7.get())+"', criminal_mobile_number="+txt3.get()+", criminal_gender='"+str(var.get())+"', criminal_dob='"+str(txt4.get())+"', criminal_address='"+str(txt5.get())+"', jail_name='"+str(txt10.get())+"',jail_address='"+str(txt11.get())+"' where criminal_id="+str(txt1.get())
        con.execute(query)
        con.commit()
        con.close()
        messagebox.askokcancel("","criminal information saved!!")
    btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="SAVE",command=save)
    btn1.place(x=250, y=605)

    # ---------------------
    def event1_reset():
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt5.delete(0, END)
        txt6.delete(0, END)
        txt7.delete(0, END)
        txt8.delete(0, END)
        txt9.delete(0, END)
        txt10.delete(0, END)
        txt11.delete(0, END)
        txt1.focus()
    # ----------------------

    btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset", command=event1_reset)
    btn2.place(x=450, y=605)

    btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event1_back)
    btn3.place(x=650, y=605)

def event2():
    temp = Frame(rightFrame, width=1250, height=850)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#211916")

    def event2_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)

    h1 = Label(temp, text="UPDATE CRIMINAL INFO", height="2", width="30", font=20)
    h1.place(x=330, y=10)

    retrieve = Button(temp, width="13", height="1", bd="5", activebackground="green", text="Retrieve")
    retrieve.place(x=700, y=50)
   
    def upload():
        result = filedialog.askopenfilename(initialdir="/", title="select file", filetypes=(
        ("image files", ".jpg"), ("image files", "jpeg"), ("image files", ".png")))
        result = bytearray(result)

    criminal_id = Label(temp, text="ENTER CRIMINAL ID", fg="white", background="#283A90", font="20")
    criminal_id.place(x=100, y=100)
    txt1 = Entry(temp, width="57")
    txt1.place(x=330, y=100)

    criminal_name = Label(temp, text="ENTER CRIMINAL NAME", fg="white", background="#283A90", font="20")
    criminal_name.place(x=100, y=140)
    txt2 = Entry(temp, width="57")
    txt2.place(x=330, y=140)

    criminal_mob = Label(temp, text="ENTER CRIMINAL MOB NO.", fg="white", background="#283A90", font="20")
    criminal_mob.place(x=100, y=180)
    txt3 = Entry(temp, width="57")
    txt3.place(x=330, y=180)

    criminal_dob = Label(temp, text="ENTER CRIMINAL D.O.B.", fg="white", background="#283A90", font="20")
    criminal_dob.place(x=100, y=220)
    txt4 = DateEntry(temp, font=('Times New Roman', 12, 'bold'), width=20)
    # txt4 = Entry(temp, width="40")
    txt4.place(x=330, y=220)

    criminal_gender = Label(temp, text="ENTER CRIMINAL GENDER.", fg="white", background="#283A90", font="20")
    criminal_gender.place(x=100, y=260)
    var = IntVar()
    Radiobutton(temp, text="Male", padx=5, variable=var, value=1).place(x=330, y=260)
    Radiobutton(temp, text="Female", padx=20, variable=var, value=2).place(x=400, y=260)
    Radiobutton(temp, text="Other", padx=20, variable=var, value=3).place(x=515, y=260)


    criminal_addr = Label(temp, text="ENTER CRIMINAL ADDRESS", fg="white", background="#283A90", font="20")
    criminal_addr.place(x=100, y=300)
    txt5 = Entry(temp, width="57")
    txt5.place(x=330, y=307)

    criminal_image = Label(temp, text="UPLOAD CRIMINAL IMAGE", fg="white", background="#283A90", font="20")
    criminal_image.place(x=100, y=340)
    upload = Button(temp, width="25", height="1", bd="2", activebackground="green", text="UPLOAD AN IMAGE",command=upload)
    upload.place(x=330, y=344)

    crime_type = Label(temp, text="ENTER CRIME TYPE", fg="white", background="#283A90", font="20")
    crime_type.place(x=100, y=380)
    txt6 = Entry(temp, width="57")
    txt6.place(x=330, y=380)

    crime_city = Label(temp, text="ENTER CRIME CITY", fg="white", background="#283A90", font="20")
    crime_city.place(x=100, y=420)
    txt7 = Entry(temp, width="57")
    txt7.place(x=330, y=420)

    crime_date = Label(temp, text="ENTER CRIME DATE", fg="white", background="#283A90", font="20")
    crime_date.place(x=100, y=460)
    txt8 = DateEntry(temp, font=('Times New Roman', 12, 'bold'), width=20)
    txt8.place(x=330, y=460)

    crime_time = Label(temp, text="ENTER CRIME TIME", fg="white", background="#283A90", font="20")
    crime_time.place(x=100, y=500)
    txt9 = Entry(temp, width="57")
    txt9.place(x=330, y=500)

    jail_name = Label(temp, text="ENTER JAIL NAME", fg="white", background="#283A90", font="20")
    jail_name.place(x=100, y=540)
    txt10 = Entry(temp, width="57")
    txt10.place(x=330, y=540)

    jail_addr = Label(temp, text="ENTER JAIL ADDRESS", fg="white", background="#283A90", font="20")
    jail_addr.place(x=100, y=580)
    txt11 = Entry(temp, width="57")
    txt11.place(x=330, y=580)
    
    def event2_save():
        con = sqlite3.connect("Hermes.db")
        query = "update criminal_data set criminal_name='"+str(txt2.get())+"', crime_type='"+str(txt6.get())+"', crime_date='"+str(txt8.get())+"', crime_time='"+str(txt9.get())+"', crime_city='"+str(txt7.get())+"', criminal_mobile_number="+txt3.get()+", criminal_gender='"+str(var.get())+"', criminal_dob='"+str(txt4.get())+"', criminal_address='"+str(txt5.get())+"', jail_name='"+str(txt10.get())+"',jail_address='"+str(txt11.get())+"' where criminal_id="+str(txt1.get())
        con.execute(query)
        con.commit()
        con.close()
        messagebox.askokcancel("","Criminal information updated!!")
    btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="SAVE",command=event2_save)
    btn1.place(x=250, y=600)

    # ---------------------
    def event2_reset():
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt5.delete(0, END)
        txt6.delete(0, END)
        txt7.delete(0, END)
        txt8.delete(0, END)
        txt9.delete(0, END)
        txt10.delete(0, END)
        txt11.delete(0, END)
        txt1.focus()
    # ----------------------

    btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset", command=event2_reset)
    btn2.place(x=450, y=600)

    btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event2_back)
    btn3.place(x=650, y=600)

def event3():
    temp = Frame(rightFrame, width=1250, height=850)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#211916")

    def event3_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)

    h1 = Label(temp, text="REMOVE CRIMINAL", height="2", width="30", font=20)
    h1.place(x=360, y=30)

    r_criminal_id = Label(temp, text="ENTER CRIMINAL ID", fg="white", background="#283A90", font="20")
    r_criminal_id.place(x=200, y=150)
    txt1 = Entry(temp, width="57")
    txt1.place(x=500, y=150)

    def remove_data():
        if txt1.get()!="":
            con = sqlite3.connect("Hermes.db")
            query = "delete from criminal_data where criminal_id="+txt1.get()
            con.execute(query)
            con.commit()
            con.close()
            messagebox.askokcancel("","Data deleted!!")
        else:
            messagebox.showerror("","Insert criminal id")
    btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="Remove",command=remove_data)
    btn1.place(x=300, y=250)

    #---------------------
    def event3_reset():
        txt1.delete(0, END)
        txt1.focus()
    #----------------------

    btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset",command=event3_reset)
    btn2.place(x=500, y=250)

    btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event3_back)
    btn3.place(x=700, y=250)

def event4():
    temp = Frame(rightFrame, width=1250, height=850)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#211916")

    def event4_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)

    def s1():
        temp = Frame(rightFrame, width=1250, height=850)
        temp.grid(row=0, column=1, padx=0, pady=0)
        temp.config(background="#211916")

        h1 = Label(temp, text="SEARCH BY CRIMINAL ID", height="2", width="30", font=20)
        h1.place(x=360, y=30)

        def event41_back():
            temp.destroy()
            rightFrame = Frame(base, width=0, height=0)
            rightFrame.grid(row=0, column=1, padx=0, pady=90)

        s_criminal_id = Label(temp, text="ENTER CRIMINAL ID", fg="white", background="#283A90", font="20")
        s_criminal_id.place(x=200, y=150)
        txt1 = Entry(temp, width="57")
        txt1.place(x=500, y=150)

        def search_by_id():
            a = int(txt1.get())
            con = sqlite3.connect("Hermes.db")
            cur = con.cursor()
            query = "select * from criminal_data where criminal_id=" + str(a)
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            con.close()
            base = Tk()
            base.geometry("600x600")
            base.configure(bg="Blue")
            name = Label(base, text="Name:", bg="Light blue", font=12)
            name.place(x=10, y=100)
            name1 = Entry(base, font=12)
            name1.place(x=150, y=100)
            ctype = Label(base, text="Crime type:", bg="Light blue", font=12)
            ctype.place(x=10, y=130)
            ctype1 = Entry(base, font=12)
            ctype1.place(x=150, y=130)
            cdate = Label(base, text="crime date:", bg="Light blue", font=12)
            cdate.place(x=10, y=160)
            cdate1 = Entry(base, font=12)
            cdate1.place(x=150, y=160)
            ctime = Label(base, text="crime time:", bg="Light blue", font=12)
            ctime.place(x=10, y=190)
            ctime1 = Entry(base, font=12)
            ctime1.place(x=150, y=190)
            city = Label(base, text="crime city:", bg="Light blue", font=12)
            city.place(x=10, y=220)
            city1 = Entry(base, font=12)
            city1.place(x=150, y=220)
            mno = Label(base, text="Mobile no:", bg="Light blue", font=12)
            mno.place(x=10, y=250)
            mno1 = Entry(base, font=12)
            mno1.place(x=150, y=250)
            gender = Label(base, text="Gender:", bg="Light blue", font=12)
            gender.place(x=10, y=280)
            gender1 = Entry(base, font=12)
            gender1.place(x=150, y=280)
            dob = Label(base, text="DOB:", bg="Light blue", font=12)
            dob.place(x=10, y=310)
            dob1 = Entry(base, font=12)
            dob1.place(x=150, y=310)
            addr = Label(base, text="Address:", bg="Light blue", font=12)
            addr.place(x=10, y=340)
            addr1 = Entry(base, font=12)
            addr1.place(x=150, y=340)
            jname = Label(base, text="Jail Name:", bg="Light blue", font=12)
            jname.place(x=10, y=370)
            jname1 = Entry(base, font=12)
            jname1.place(x=150, y=370)
            jaddr = Label(base, text="Jail addr:", bg="Light blue", font=12)
            jaddr.place(x=10, y=400)
            jaddr1 = Entry(base, font=12)
            jaddr1.place(x=150, y=400)
            name1.insert(0, data[0][1])
            ctype1.insert(0, data[0][2])
            cdate1.insert(0, data[0][3])
            ctime1.insert(0, data[0][4])
            city1.insert(0, data[0][5])
            mno1.insert(0, data[0][6])
            gender1.insert(0, data[0][7])
            dob1.insert(0, data[0][8])
            addr1.insert(0, data[0][9])
            jname1.insert(0, data[0][10])
            jaddr1.insert(0, data[0][11])
            #with open("image.png",'wb') as f:
            #    f.write(bytes(str(data[0][6])))
            #img = PhotoImage(file='image.png')
            #l1 = Label(base,image=img)
            #l1.place(x=100,y=10)
            base.mainloop()
        btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="Search",command=search_by_id)
        btn1.place(x=300, y=250)

        # ---------------------
        def event41_reset():
            txt1.delete(0, END)
            txt1.focus()
        # ----------------------

        btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset",command=event41_reset)
        btn2.place(x=500, y=250)

        btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event41_back)
        btn3.place(x=700, y=250)

    def s2():
        temp = Frame(rightFrame, width=1250, height=850)
        temp.grid(row=0, column=1, padx=0, pady=0)
        temp.config(background="#211916")

        h1 = Label(temp, text="SEARCH BY CRIMINAL NAME", height="2", width="30", font=20)
        h1.place(x=360, y=30)

        def event42_back():
            temp.destroy()
            rightFrame = Frame(base, width=0, height=0)
            rightFrame.grid(row=0, column=1, padx=0, pady=90)

        s_criminal_name = Label(temp, text="ENTER CRIMINAL NAME", fg="white", background="#283A90", font="20")
        s_criminal_name.place(x=200, y=150)
        txt2 = Entry(temp, width="57")
        txt2.place(x=500, y=150)
        
        def search_by_name():
            a = str(txt2.get())
            con = sqlite3.connect("Hermes.db")
            cur = con.cursor()
            query = "select * from criminal_data where criminal_name='" + str(a)+"'"
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            con.close()
            base = Tk()
            base.geometry("600x600")
            base.configure(bg="Blue")
            name = Label(base, text="Name:", bg="Light blue", font=12)
            name.place(x=10, y=100)
            name1 = Entry(base, font=12)
            name1.place(x=150, y=100)
            ctype = Label(base, text="Crime type:", bg="Light blue", font=12)
            ctype.place(x=10, y=130)
            ctype1 = Entry(base, font=12)
            ctype1.place(x=150, y=130)
            cdate = Label(base, text="crime date:", bg="Light blue", font=12)
            cdate.place(x=10, y=160)
            cdate1 = Entry(base, font=12)
            cdate1.place(x=150, y=160)
            ctime = Label(base, text="crime time:", bg="Light blue", font=12)
            ctime.place(x=10, y=190)
            ctime1 = Entry(base, font=12)
            ctime1.place(x=150, y=190)
            city = Label(base, text="crime city:", bg="Light blue", font=12)
            city.place(x=10, y=220)
            city1 = Entry(base, font=12)
            city1.place(x=150, y=220)
            mno = Label(base, text="Mobile no:", bg="Light blue", font=12)
            mno.place(x=10, y=250)
            mno1 = Entry(base, font=12)
            mno1.place(x=150, y=250)
            gender = Label(base, text="Gender:", bg="Light blue", font=12)
            gender.place(x=10, y=280)
            gender1 = Entry(base, font=12)
            gender1.place(x=150, y=280)
            dob = Label(base, text="DOB:", bg="Light blue", font=12)
            dob.place(x=10, y=310)
            dob1 = Entry(base, font=12)
            dob1.place(x=150, y=310)
            addr = Label(base, text="Address:", bg="Light blue", font=12)
            addr.place(x=10, y=340)
            addr1 = Entry(base, font=12)
            addr1.place(x=150, y=340)
            jname = Label(base, text="Jail Name:", bg="Light blue", font=12)
            jname.place(x=10, y=370)
            jname1 = Entry(base, font=12)
            jname1.place(x=150, y=370)
            jaddr = Label(base, text="Jail addr:", bg="Light blue", font=12)
            jaddr.place(x=10, y=400)
            jaddr1 = Entry(base, font=12)
            jaddr1.place(x=150, y=400)
            name1.insert(0, data[0][1])
            ctype1.insert(0, data[0][2])
            cdate1.insert(0, data[0][3])
            ctime1.insert(0, data[0][4])
            city1.insert(0, data[0][5])
            mno1.insert(0, data[0][6])
            gender1.insert(0, data[0][7])
            dob1.insert(0, data[0][8])
            addr1.insert(0, data[0][9])
            jname1.insert(0, data[0][10])
            jaddr1.insert(0, data[0][11])
            base.mainloop()
        btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="Search",command=search_by_name)
        btn1.place(x=300, y=250)

        # ---------------------
        def event42_reset():
            txt2.delete(0, END)
            txt2.focus()
        # ----------------------

        btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset",command=event42_reset)
        btn2.place(x=500, y=250)

        btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event42_back)
        btn3.place(x=700, y=250)

    def s3():
        temp = Frame(rightFrame, width=1250, height=850)
        temp.grid(row=0, column=1, padx=0, pady=0)
        temp.config(background="#211916")

        h1 = Label(temp, text="SEARCH BY CRIMINAL MOBILE NUMBER", height="2", width="40", font=20)
        h1.place(x=330, y=30)

        def event43_back():
            temp.destroy()
            rightFrame = Frame(base, width=0, height=0)
            rightFrame.grid(row=0, column=1, padx=0, pady=90)

        s_criminal_mob = Label(temp, text="ENTER CRIMINAL MOBILE NUMBER", fg="white", background="#283A90", font="20")
        s_criminal_mob.place(x=200, y=150)
        txt3 = Entry(temp, width="57")
        txt3.place(x=500, y=150)
        
        def search_by_mo():
            a = int(txt3.get())
            con = sqlite3.connect("Hermes.db")
            cur = con.cursor()
            query = "select * from criminal_data where criminal_mobile_number=" + str(a)
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            con.close()
            base = Tk()
            base.geometry("600x600")
            base.configure(bg="Blue")
            name = Label(base, text="Name:", bg="Light blue", font=12)
            name.place(x=10, y=100)
            name1 = Entry(base, font=12)
            name1.place(x=150, y=100)
            ctype = Label(base, text="Crime type:", bg="Light blue", font=12)
            ctype.place(x=10, y=130)
            ctype1 = Entry(base, font=12)
            ctype1.place(x=150, y=130)
            cdate = Label(base, text="crime date:", bg="Light blue", font=12)
            cdate.place(x=10, y=160)
            cdate1 = Entry(base, font=12)
            cdate1.place(x=150, y=160)
            ctime = Label(base, text="crime time:", bg="Light blue", font=12)
            ctime.place(x=10, y=190)
            ctime1 = Entry(base, font=12)
            ctime1.place(x=150, y=190)
            city = Label(base, text="crime city:", bg="Light blue", font=12)
            city.place(x=10, y=220)
            city1 = Entry(base, font=12)
            city1.place(x=150, y=220)
            mno = Label(base, text="Mobile no:", bg="Light blue", font=12)
            mno.place(x=10, y=250)
            mno1 = Entry(base, font=12)
            mno1.place(x=150, y=250)
            gender = Label(base, text="Gender:", bg="Light blue", font=12)
            gender.place(x=10, y=280)
            gender1 = Entry(base, font=12)
            gender1.place(x=150, y=280)
            dob = Label(base, text="DOB:", bg="Light blue", font=12)
            dob.place(x=10, y=310)
            dob1 = Entry(base, font=12)
            dob1.place(x=150, y=310)
            addr = Label(base, text="Address:", bg="Light blue", font=12)
            addr.place(x=10, y=340)
            addr1 = Entry(base, font=12)
            addr1.place(x=150, y=340)
            jname = Label(base, text="Jail Name:", bg="Light blue", font=12)
            jname.place(x=10, y=370)
            jname1 = Entry(base, font=12)
            jname1.place(x=150, y=370)
            jaddr = Label(base, text="Jail addr:", bg="Light blue", font=12)
            jaddr.place(x=10, y=400)
            jaddr1 = Entry(base, font=12)
            jaddr1.place(x=150, y=400)
            name1.insert(0, data[0][1])
            ctype1.insert(0, data[0][2])
            cdate1.insert(0, data[0][3])
            ctime1.insert(0, data[0][4])
            city1.insert(0, data[0][5])
            mno1.insert(0, data[0][6])
            gender1.insert(0, data[0][7])
            dob1.insert(0, data[0][8])
            addr1.insert(0, data[0][9])
            jname1.insert(0, data[0][10])
            jaddr1.insert(0, data[0][11])

        btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="Search",command=search_by_mo)
        btn1.place(x=300, y=250)
        # ---------------------
        def event43_reset():
            txt3.delete(0, END)
            txt3.focus()
        # ----------------------

        btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset",command=event43_reset)
        btn2.place(x=500, y=250)

        btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event43_back)
        btn3.place(x=700, y=250)

    h1 = Label(temp, text="SEARCH CRIMINAL", height="2", width="30", font=20)
    h1.place(x=360, y=30)

    btn1 = Button(temp, width="35", height="2", bd="5", activebackground="green", text="SEARCH BY CRIMINAL ID", command=s1)
    btn1.place(x=400, y=150)

    btn2 = Button(temp, width="35", height="2", bd="5", activebackground="red", text="SEARCH BY CRIMINAL NAME", command=s2)
    btn2.place(x=400, y=300)

    btn3 = Button(temp, width="35", height="2", bd="5", activebackground="red", text="SEARCH BY CRIMINAL MOBILE NUMBER", command=s3)
    btn3.place(x=400, y=450)

    btn4 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event4_back)
    btn4.place(x=480, y=600)

def event5():
    temp = Frame(rightFrame, width=1250, height=850)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#211916")

    h1 = Label(temp, text="CRIME STATISTICS", height="2", width="30", font=20)
    h1.place(x=360, y=30)

    def event5_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)

    btn1 = Button(temp, width="35", height="2", bd="5", activebackground="green", text="STATEWISE STATISTICS")
    btn1.place(x=400, y=200)

    btn2 = Button(temp, width="35", height="2", bd="5", activebackground="blue",text="DISTRICTWISE STATISTICS")
    btn2.place(x=400, y=350)

    btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event5_back)
    btn3.place(x=480, y=500)

def event6():
    temp = Frame(rightFrame, width=1250, height=850)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#211916")

    h1 = Label(temp, text="DOWNLOAD RECORD PDF", height="2", width="30", font=20)
    h1.place(x=360, y=30)

    def event6_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)
    def districtwise_pdf():
        con = sqlite3.connect("Hermes.db")
        cur = con.cursor()
        query = "select * from criminal_data group by crime_city"
        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        con.close()
        fp = open("tempFile.txt", "w")
        fp.write("")
        fp.close()
        fp = open("tempFile.txt", "a")
        for i in data:
            str1 =  str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + " \t" + str(i[
                3]) + " \t" + str(i[4]) + "\t" + str(i[5]) + "\t" + "\t" + str(i[
                       7]) + "\t" + str(i[8]) + "\t" + str(i[9]) + "\t" + str(i[10]) + "\t" + str(
                i[11]) + "\t"  + "\n\n"
            fp.write(str1)
        import os
        os.startfile("tempFile.txt", "print")
        fp.close()

    #btn1 = Button(temp, width="35", height="2", bd="5", activebackground="green", text="STATEWISE PDF",command=statewise_pdf)
    #btn1.place(x=400, y=200)

    btn2 = Button(temp, width="35", height="2", bd="5", activebackground="blue",text="DISTRICTWISE PDF",command=districtwise_pdf)
    btn2.place(x=400, y=350)

    btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event6_back)
    btn3.place(x=480, y=500)

def event7():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit from Hermes?')
    if (res == True):
        base.destroy()
#------------------------------- Events Ends -------------------------------------------

#---------------------------- Clock Starts ----------------------------------
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(1000,tick)

clock = Label(base,font=('Times new roman',14,'bold'),relief=RIDGE,borderwidth=4,bg='linen')
clock.place(x=0,y=0)
tick()
#---------------------------- Clock Ends ----------------------------------

#-------------------------------------- Slidebar Starts -----------------------------------------------------

ss = 'Hermes'
count = 0
text = ''

SliderLabel = Label(base,text=ss,font=('Times new roman',30,'bold'),relief=RIDGE,borderwidth=4,width=35,bg='white')
SliderLabel.place(x=350,y=0)

#-------------------------------------- Slidebar Ends -----------------------------------------------------

#--------------------------- leftFrame Starts -------------------------------
leftFrame = Frame(base, width=500, height = 710)
leftFrame.grid(row=0, column=0, padx=2, pady=90)
#leftFrame.config(background = "#FF6E33")
leftFrame.config(background = "#211916")
#---------------------------------- leftFrame Ends -----------------------------------------

#------------------------------- RighttFrame Starts ----------------------------------------
rightFrame = Frame(base, width=500, height = 650)
rightFrame.grid(row=0, column=1, padx=0, pady=90)
#rightFrame.config(background = "#FFE633")
#------------------------------- RighttFrame Ends ----------------------------------------

#----------------------- Leftframe Menus Starts --------------------------------------
b1 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="ADD NEW CRIMINAL", command=event1)
b1.place(x=100, y=10)

b2 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="UPDATE CRIMINAL INFO", command=event2)
b2.place(x=100, y=85)

b3 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="REMOVE CRIMINAL", command=event3)
b3.place(x=100, y=150)

b4 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="SEARCH CRIMINAL", command=event4)
b4.place(x=100, y=225)

b5 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="CRIME STATISTICS", command=event5)
b5.place(x=100, y=300)

b6 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="DOWNLOAD RECORD PDF", command=event6)
b6.place(x=100, y=375)

b7 = Button(leftFrame, width="40", height="2", bd="5", activebackground="red", text="EXIT", command=event7)
b7.place(x=100, y=500)
#----------------------- Leftframe Menus Ends --------------------------------------

#----------------------------- Add Image To RightFrame Starts -----------------------------------
image = Image.open("F:\project_Hermes\project_1\Crime_Database\logo.jpeg")
photo = ImageTk.PhotoImage(image)
label = Label(rightFrame,image=photo, width=1050, height=700 ,bg="white")
label.grid(row=0, column=1, padx=0, pady=0)
#----------------------------- Add Image To RightFrame Ends -------------------------------------

base.mainloop()