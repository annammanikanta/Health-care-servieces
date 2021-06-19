import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

from functools import partial
#c=conn.cursor()

class Application:


    def __init__(self, master):

        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=1200, height=720, bg='lightblue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        # labels for the window
        self.heading = Label(self.left, text="Helath Care Services", font=('arial 40 bold'), fg='black',
                             bg='lightblue')
        self.heading.place(x=0, y=0)
        # patients name
        self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.name.place(x=0, y=100)

        # age
        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.age.place(x=0, y=140)

        # gender
        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.gender.place(x=0, y=180)

        # location
        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.location.place(x=0, y=220)

        # appointment time
        self.time = Label(self.left, text="Appointment Date", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.time.place(x=0, y=260)

        #time
        self.time1 = Label(self.left, text="Time", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.time1.place(x=0, y=300)


        # phone
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.phone.place(x=0, y=340)

        # Entries for all labels============================================================
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=105)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=145)

        # Radiobutton variables:
        gender_ent = tk.StringVar()

        #self.gender_ent = Entry(self.left, width=30)

        # Radiobutton set1:
        r1=tk.Radiobutton(master, text="Male",value="male", font="BahnschriftLight 14", bg=["white"],
                           selectcolor=["white"], activebackground=["lightblue"],
                           variable=gender_ent).place(x=250, y=185)


        # Radiobutton set2:
        r2=tk.Radiobutton(master, text="Female ",value="female", font="BahnschriftLight 14", bg=["white"],
                           selectcolor=["white"], activebackground=["lightblue"],
                           variable=gender_ent).place(x=350, y=185)
        self.gender_ent=gender_ent






        #lbl_gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",10,"bold"))
        #lbl_gender.grid(row=4,column=0,pady=4,padx=20,sticky="w")

        #self.gender_ent(combo_gender=tk.Combobox(Manage_Frame,textvariable=self.gender_ent,font=("times new roman",10,"bold"),state='readonly'))
        #combo_gender["values"]=("Male", "Female", "Other")
        #self.gender_ent.place(combo_gender.grid(row=4,column=1,pady=4,padx=20))

        #self.button=Radiobutton(master,text="male",variable="m",value="Male",option=values)
        #option = StringVar()
        #self.gender_ent(R1=Radiobutton(root,text="MALE",value="male",var=option))
        #self.gender_ent(R2=Radiobutton(root,text="FEMALE",value="female",var=option))


        #self.gender_ent = Entry(self.left, width=30)
        #self.gender_ent.place(x=250, y=185)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=225)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=265)

        self.time1_ent = Entry(self.left, width=30)
        self.time1_ent.place(x=250, y=305)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=345)

        # button to perform a command
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue',
                             command=self.add_appointment)
        self.submit.place(x=280, y=400)

        #abt
        self.submit = Button(self.left, text="DISPLAY", width=20, height=2, bg='steelblue',
                             command=self.display)
        self.submit.place(x=900, y=90)

        #update
        self.submit = Button(self.left, text="UPDATE", width=20, height=2, bg='steelblue',
                             command=self.update)
        self.submit.place(x=900, y=200)

        #doc
        self.submit = Button(self.left, text="ADMIN", width=20, height=2, bg='steelblue',
                             command=self.admin)
        self.submit.place(x=900, y=310)

        #del
        self.submit = Button(self.left, text="DELETE", width=20, height=2, bg='steelblue',
                             command=self.delete)
        self.submit.place(x=900, y=420)



    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()
        self.val7 = self.time1_ent.get()


        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            mydb=mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="manikanta",
                                         database= 'appointment'
            )
            mycursor=mydb.cursor()
            mycursor1 = mydb.cursor()
            mycursor.execute("insert into book values(%s,%s,%s,%s,%s,%s)",(self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            mycursor1.execute("insert into appoint values(%s,%s)", (self.val5, self.val7))
                                                                           #mycursor.execute("INSERT INTO 'details' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)")
            #a=(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            #mydb.commit()

            #db="CREATE TABLE 'details'(name varchar(10), age int PRIMARY KEY, gender varchar(10), location varchar (10), scheduled_time date, phone int"

            #mycursor.execute(db,val)

            mydb.commit()

            messagebox.showinfo("Success", "Appointment for " + str(self.val1) + " has been created")

            #self.box.insert(END, 'Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val5))




    def display(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()


        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="manikanta",
                                       database='appointment'
                                       )

        mycursor = mydb.cursor()
        mycursor.execute("select * from book")
        master=Tk()
        master.geometry('500x500')
        master.title('DETAILS')

        
        Label1 = Label(master, text="NAME", width=10,font='green')
        Label1.grid(row=0, column=0)
        Label2 = Label(master, text="AGE", width=10,font='green')
        Label2.grid(row=0, column=1)
        Label3 = Label(master, text="GENDER", width=10,font='green')
        Label3.grid(row=0, column=2)
        Label1 = Label(master, text="LOCATION", width=10,font='green')
        Label1.grid(row=0, column=3)
        Label1 = Label(master, text="SCH DATE", width=10,font='green')
        Label1.grid(row=0, column=4)
        Label1 = Label(master, text="PHONE", width=15,font='green')
        Label1.grid(row=0, column=5)

        for index, dat in enumerate(mycursor):
            Label(master, text=dat[0]).grid(row=index + 1, column=0)
            Label(master, text=dat[1]).grid(row=index + 1, column=1)
            Label(master, text=dat[2]).grid(row=index + 1, column=2)
            Label(master, text=dat[3]).grid(row=index + 1, column=3)
            Label(master, text=dat[4]).grid(row=index + 1, column=4)
            Label(master, text=dat[5]).grid(row=index + 1, column=5)


    def delete(self):
        master = Tk()
        master.geometry('1200x720+0+0')
        master.title('Del..')
        self.left = Frame(master, width=1200, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)
        self.heading = Label(self.left, text=".......Deleting.....", font=('arial 40 bold'), fg='black',
                             bg='lightgreen')
        self.heading.place(x=400, y=100)

        self.s2 = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.s2.place(x=50, y=300)
        self.s2_ent = Entry(self.left, width=30)
        self.s2_ent.place(x=300, y=305)

        self.submit = Button(self.left, text="Submit", width=20, height=2, bg='steelblue',
                             command=self.submit3)
        self.submit.place(x=450, y=350)

    def submit3(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()
        self.val7 = self.s2_ent.get()
        print(self.val7)

        if self.val7 != '':
            mydb = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="manikanta",
                                           database='appointment'
                                           )

            mycursor = mydb.cursor()
            mycursor.execute("DELETE FROM book WHERE name= '%s'" %(self.val7))
            mydb.commit()
            messagebox.showinfo("Success", "Appointment for " + str(self.val7) + " has been deleted")
            #messagebox.showinfo("success", "(self.val7) deleted succefully")
        else:
            messagebox.showinfo("error","no data found")

        print("del")

    def update(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        master = Tk()
        master.geometry('1200x720+0+0')
        master.title('UPDATE')
        self.left = Frame(master, width=1200, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)
        self.heading = Label(self.left, text=".......Updating.....", font=('arial 40 bold'), fg='black',
                             bg='lightgreen')
        self.heading.place(x=400, y=100)

        self.s1 = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.s1.place(x=50, y=300)
        self.s1_ent = Entry(self.left, width=30)
        self.s1_ent.place(x=300, y=305)

        self.submit = Button(self.left, text="Submit", width=20, height=2, bg='steelblue',
                             command=self.submit4)
        self.submit.place(x=450, y=350)
    def submit4(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()
        self.val7 = self.s1_ent.get()
        print(self.val7)
        if self.val7 != '':
            mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="manikanta",
                                       database='appointment'
                                       )

            mycursor = mydb.cursor()
            mycursor.execute("UPDATE book SET age= 22 WHERE name= '%s'" %(self.val7))
            mydb.commit()
            messagebox.showinfo("Success", "Updated age for " + str(self.val7) + "")
        else:
            messagebox.showinfo("wrong""No Details Found")





    def admin(self):
        master = Tk()
        master.geometry('500x500')
        master.title('log')
        self.master = master
        self.master.title("Login System")
        self.master.geometry('900x500')
        self.master.config(bg='crimson')
        self.frame = Frame(self.master, bg='crimson')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text="ADMIN LOGIN PAGE", font=("arial", 50, 'bold'),
                              bg='crimson', fg='cornsilk')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=20)

        # =================================================================================================================

        self.LoginFrame1 = LabelFrame(self.frame, width=1250, height=300, fg='cornsilk', text="Login",
                                      font=('arial', 20, 'bold'), relief='ridge', bg='crimson', bd=15)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=900, height=130, fg='cornsilk', text="Log",
                                      font=('arial', 20, 'bold'), relief='ridge', bg='crimson', bd=15)
        self.LoginFrame2.grid(row=2, column=0)

        # =================================================================================================================

        self.lblUsername = Label(self.LoginFrame1, text="Username", font=("arial", 15, 'bold'), bd=10, bg='crimson',
                                 fg='cornsilk')
        self.lblUsername.grid(row=0, column=0)

        self.txtUsername = Entry(self.LoginFrame1, font=("arial", 15, 'bold'), bd=7, textvariable=self.Username,
                                 width=23)
        self.txtUsername.grid(row=0, column=1, padx=120)

        self.lblPassword = Label(self.LoginFrame1, text="Password", font=("arial", 15, 'bold'), bd=10, bg='crimson',
                                 fg='cornsilk')
        self.lblPassword.grid(row=1, column=0)

        self.txtPassword = Entry(self.LoginFrame1, font=("arial", 15, 'bold'), show='*', bd=7,
                                 textvariable=self.Password, width=23)
        self.txtPassword.grid(row=1, column=1, columnspan=2, pady=30)

        # =================================================================================================================

        self.btnLogin = Button(self.LoginFrame2, text='Login', width=15, font=('arial', 20, 'bold'), bg='crimson',
                               fg='cornsilk', command=self.Login_System)
        self.btnLogin.grid(row=3, column=0, pady=10, padx=8)

        #self.btnReset = Button(self.LoginFrame2, text='Reset', width=15, font=('arial', 20, 'bold'), bg='crimson',
#                               fg='cornsilk', command=self.iReset)
        #self.btnReset.grid(row=3, column=1, pady=10, padx=8)

        self.btnExit = Button(self.LoginFrame2, text='Exit', width=15, font=('arial', 20, 'bold'), bg='crimson',
                              fg='cornsilk', command=self.iExit)
        self.btnExit.grid(row=3, column=2, pady=10, padx=8)

        # =================================================================================================================

    def Login_System(self):
        self.user = self.txtUsername.get()
        self.pas = self.txtPassword.get()
        if (self.user == str('mani') and self.pas == str(1234)):
            messagebox.showinfo("yaaa","entered")

            mydb = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="manikanta",
                                           database='appointment'
                                           )
            mycursor = mydb.cursor()
            mycursor.execute("insert into login values(%s,%s)", (self.user, self.pas))
            mydb.commit()
            b.abt()


        elif (self.user == str(12345678) and self.pas == str(123456)):
            tkinter.messagebox.askyesno("Admin", "login")
            #self.Login_details()
            print("yes yaaa")
        else:
            import tkinter
            tkinter.messagebox.askyesno("Admin", "Invalid Login details")
            self.Username.set("")
            self.Password.set("")

    def iReset(self):
        self.Username.set("")
        self.Password.set("")

    def iExit(self):
        import tkinter
        self.iExit = tkinter.messagebox.askyesno("Community Management System", "Confirm if you want to Exit")
        if self.iExit > 0:
            self.master.destroy()
            return


    def abt(self):

        master = Tk()
        master.geometry('1200x720+0+0')
        master.title('welcome')
        self.left = Frame(master, width=1200, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)
        self.heading = Label(self.left, text="WELCOME", font=('arial 40 bold'), fg='black',
                             bg='lightgreen')
        self.heading.place(x=400, y=100)
        self.submit = Button(self.left, text="DISPLAY", width=20, height=2, bg='steelblue',
                             command=self.display)
        self.submit.place(x=50, y=200)
        self.submit = Button(self.left, text="MEDICINES", width=20, height=2, bg='steelblue',
                             command=self.medicine)
        self.submit.place(x=400, y=200)
        self.submit = Button(self.left, text="DELETE", width=20, height=2, bg='steelblue',
                             command=self.delete)
        self.submit.place(x=750, y=200)



    def display(self):
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="manikanta",
                                       database='appointment'
                                       )
        mycursor = mydb.cursor()
        mycursor.execute("select * from book")

        master = Tk()
        master.geometry('500x500')
        master.title('DETAILS')

        Label1 = Label(master, text="NAME", width=10, font='green')
        Label1.grid(row=0, column=0)
        Label2 = Label(master, text="AGE", width=10, font='green')
        Label2.grid(row=0, column=1)
        Label3 = Label(master, text="GENDER", width=10, font='green')
        Label3.grid(row=0, column=2)
        Label1 = Label(master, text="LOCATION", width=10, font='green')
        Label1.grid(row=0, column=3)
        Label1 = Label(master, text="SCH DATE", width=10, font='green')
        Label1.grid(row=0, column=4)
        Label1 = Label(master, text="PHONE", width=15, font='green')
        Label1.grid(row=0, column=5)

        for index, dat in enumerate(mycursor):
            Label(master, text=dat[0]).grid(row=index + 1, column=0)
            Label(master, text=dat[1]).grid(row=index + 1, column=1)
            Label(master, text=dat[2]).grid(row=index + 1, column=2)
            Label(master, text=dat[3]).grid(row=index + 1, column=3)
            Label(master, text=dat[4]).grid(row=index + 1, column=4)
            Label(master, text=dat[5]).grid(row=index + 1, column=5)

    def medicine(self):
        master = Tk()
        master.geometry('1200x720+0+0')
        master.title('MEDICINE DETAILS')
        self.left = Frame(master, width=1200, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)
        self.heading = Label(self.left, text="MEDICINE DETAILS", font=('arial 40 bold'), fg='black',
                             bg='lightgreen')
        self.heading.place(x=400, y=100)

        self.m_id = Label(self.left, text="MEDICINE ID", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.m_id.place(x=350, y=250)

        self.m_name = Label(self.left, text="MEDICINE NAME", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.m_name.place(x=350, y=300)

        self.m_manf = Label(self.left, text="MEDICINE MANF DATE", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.m_manf.place(x=350, y=350)

        self.m_exp = Label(self.left, text="MEDICINE EXPIRY", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.m_exp.place(x=350, y=400)

        self.p_name = Label(self.left, text="PATIENT NAME", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.p_name.place(x=350, y=450)



        self.mid_ent = Entry(self.left, width=30)
        self.mid_ent.place(x=560, y=255)

        self.m_name_ent = Entry(self.left, width=30)
        self.m_name_ent.place(x=560, y=305)

        self.m_manf_ent = Entry(self.left, width=30)
        self.m_manf_ent.place(x=560, y=355)

        self.m_exp_ent = Entry(self.left, width=30)
        self.m_exp_ent.place(x=560, y=405)

        self.p_name_ent = Entry(self.left, width=30)
        self.p_name_ent.place(x=560, y=455)

        self.submit = Button(self.left, text="SUBMIT", width=20, height=2, bg='steelblue',
                             command=self.submit2)
        self.submit.place(x=560, y=550)


    def submit2(self):
        self.m1 = self.mid_ent.get()
        self.m2 = self.m_name_ent.get()
        self.m3 = self.m_manf_ent.get()
        self.m4 = self.m_exp_ent.get()
        self.m5 = self.p_name_ent.get()

        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="manikanta",
                                       database='appointment'
                                       )
        mycursor = mydb.cursor()
        mycursor.execute("insert into medicine values(%s,%s,%s,%s,%s)",(self.m1, self.m2, self.m3, self.m4,self.m5))
        mydb.commit()
        messagebox.showinfo("Success", "medicine for " + str(self.m5) + " has been booked")



    print("haii")



root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()


