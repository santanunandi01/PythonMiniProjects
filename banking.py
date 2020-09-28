#importing module
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from sqlite3 import IntegrityError



#creating database
conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS administation(
            username TEXT PRIMARY KEY NOT NULL,
            password TEXT NOT NULL,
            security_pin INTEGER NOT NULL)""")

c.execute("""CREATE TABLE IF NOT EXISTS users(
            name TEXT NOT NULL,
            accountno INTEGER PRIMARY KEY NOT NULL,
            contactno INTEGER NOT NULL,
            city TEXT NOT NULL,
            pincode INTEGER NOT NULL,
            balance INTEGER NOT NULL)""")

conn.commit()
conn.close()


#creating functions
def print_st():
    pt_scr = Toplevel(int_scr)
    pt_scr.title("statement")
    
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""SELECT name, accountno, balance FROM users WHERE accountno=?""", (acc,))
    st = c.fetchall()

    
    Label(pt_scr, text="Bank account information", font=("calibri", 13)).grid(row=0, sticky=None, pady=10, padx=10)
    Label(pt_scr, text="Name: ", font=("calibri", 12)).grid(row=1, sticky=W, padx=10)
    Label(pt_scr, text="Account no: ", font=("calibri", 12)).grid(row=2, sticky=W, padx=10)
    Label(pt_scr, text="Balance: ", font=("calibri", 12)).grid(row=3, sticky=W, padx=10)
    
    Label(pt_scr, text=str(st[0][0]), font=("calibri", 12)).grid(row=1, sticky=E, padx=25)
    Label(pt_scr, text=str(st[0][1]), font=("calibri", 12)).grid(row=2, sticky=E, padx=25)
    Label(pt_scr, text="Rs. "+str(st[0][2]), font=("calibri", 12)).grid(row=3, sticky=E, padx=25)
    Label(pt_scr, text="Thank You", font=("calibri", 12), fg="green").grid(row=4, pady=10, sticky=None)



def finish_del():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    try:
        c.execute("DELETE FROM users WHERE accountno=?", (acc,))
        conn.commit()
        notif_del.config(fg="green", text="Account deleted, please exit")
        return
    except:
        notif_del.config(fg="red", text="can't delete account")


def delete_acc():
    global del_scr
    global notif_del
    del_scr = Toplevel(int_scr)
    del_scr.title("Delete Account")

    Label(del_scr, text="Do you want delete the account", font=("calibri", 13), fg="red").grid(row=0, sticky=None, padx=10, pady=10)
    notif_del = Label(del_scr, font=("calibri", 13))
    notif_del.grid(row=2, sticky=None, pady=10, padx=10)
    
    Button(del_scr, text="Sure", font=("calibri", 12), width=20, command=finish_del).grid(row=1, sticky=None, padx=10, pady=10)

def finish_with():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    try:
        c.execute("SELECT balance FROM users WHERE accountno = ?", (acc,))
        amt = c.fetchall()
        new_amt = amt[0][0]
        if with_amt.get()=="" or int(with_amt.get())<=0 or int(with_amt.get())>=20000:
            notif_with.config(fg="red", text="enter a valid ammount")
            return
        
        elif int(new_amt) < int(with_amt.get()):
            notif_with.config(fg="red", text="Not enough balance")
            return
            
        else:
            new_amt = int(amt[0][0]) - int(with_amt.get())
            c.execute("""UPDATE users SET balance= ? WHERE accountno= ? """, (new_amt, acc,))
            conn.commit()
            conn.close()
            notif_with.config(fg="green", text="Withdrawl successfully")
    except:
        notif_with.config(fg="red", text="enter a valid ammount")



def withdrawl():
    global with_scr
    global with_amt
    global notif_with
    
    with_amt = StringVar()
    
    with_scr = Toplevel(int_scr)
    with_scr.title("Withdrawl") 

    #creating labels
    Label(with_scr, text="Enter the ammount to withdrawl", font=("calibri", 13)).grid(row=0, sticky=None, pady=10, padx=10)
    notif_with = Label(with_scr, font=("calibri", 13))
    notif_with.grid(row=3, sticky=None, pady=10, padx=5)

    #CREATING ENTRIES
    Entry(with_scr, textvariable=with_amt, width=20).grid(row=1, sticky=None, padx=10)

    #creating button
    Button(with_scr, text="submit", font=("calibri", 12), width=20, command=finish_with).grid(row=2, sticky=None, pady=10)
    

def finish_deposite():
    amount = dep_ammount.get()

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    
    try:
        if int(amount) <= 0 or int(amount)>=50001 or dep_ammount.get()=="":
            notif_dep.config(fg="red", text="Not a valid amount\nenter ammount from 1 to 50000")
            return
        else:
            c.execute("SELECT balance FROM users WHERE accountno = ?", (acc,))
            amt = c.fetchall()
            new_amt = int(amt[0][0]) + int(amount)
            c.execute("""UPDATE users SET balance= ? WHERE accountno= ? """, (new_amt, acc,))
            conn.commit()
            conn.close()
            notif_dep.config(fg="green", text="Deposited successfully")
    except:
        notif_dep.config(fg="red", text="Not a valid amount\nenter ammount from 1 to 50000")



def deposite():
    global dep_ammount
    global notif_dep
    dep_ammount = StringVar()
    dep_scr = Toplevel(int_scr)
    dep_scr.title("Deposite")

    #creating labels
    Label(dep_scr, text="Enter the ammount to deposite", font=("calibri", 13)).grid(row=0, sticky=None, pady=10, padx=10)
    notif_dep = Label(dep_scr, font=("calibri", 13))
    notif_dep.grid(row=3, sticky=None, pady=10, padx=5)

    #CREATING ENTRIES
    Entry(dep_scr, textvariable=dep_ammount, width=20).grid(row=1, sticky=None, padx=10)

    #creating button
    Button(dep_scr, text="submit", font=("calibri", 12), width=20, command=finish_deposite).grid(row=2, sticky=None, pady=10)
    


def user_interface():
    global notif_user
    global int_scr
    int_scr = Toplevel(main_scr)
    int_scr.title("User Interface")

    #labels
    Label(int_scr, text="Do the operations you want", font=("calibri", 13)).grid(row=0, sticky=None, pady=10, padx=10)
    notif_user = Label(int_scr, font=("calibri", 13))
    notif_user.grid(row=5, sticky=None, pady=10, padx=10)
    

    #Buttons
    Button(int_scr, text="Deposite",font=("calibri", 12), width=20, command=deposite).grid(row=1, sticky=None, pady=5)
    Button(int_scr, text="Withdrawl",font=("calibri", 12), width=20, command=withdrawl).grid(row=2, sticky=None, pady=5)
    Button(int_scr, text="Print Statement",font=("calibri", 12), width=20, command=print_st).grid(row=3, sticky=None, pady=5)
    Button(int_scr, text="Delete Account",font=("calibri", 12), width=20, command=delete_acc).grid(row=4, sticky=None, pady=5)



def entry_account():
    global acc
    acc = entry_acc.get()
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    if acc=="":
       notif_procced.config(fg="red", text="This field can't be empty *")
       return
    else:
        c.execute("""SELECT EXISTS(SELECT 1 FROM users WHERE accountno=?)""",(acc,))
        ex = c.fetchall()
        if(ex[0][0]==1):
            notif_procced.config(fg="green", text="Successfully entered into the account")
            user_interface()
        else:
            notif_procced.config(fg="red", text="* User not found *\n* try to create a new account *")
            return
        


def finish_create_acc():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    if new_name.get()=="" or new_acc_no.get()=="" or new_contact_no.get()=="" or new_city.get()=="" or new_pincode.get()=="" or new_fund.get()=="":
        notif_acc_create.config(fg="red", text="All fields are required *")
        return
    else:
        try:
            c.execute("""INSERT INTO users(name, accountno, contactno, city, pincode, balance)
            VALUES(?, ?, ?, ?, ?, ?)""",(new_name.get(), new_acc_no.get(), new_contact_no.get(), new_city.get(),new_pincode.get(), new_fund.get()))
            conn.commit()
            
            notif_acc_create.config(fg="green", text="Account has been created succesfully")
            
        except IntegrityError as E:
            notif_acc_create.config(fg="red", text="Account already registered *")
            
conn.close()



def create_account():
    global notif_acc_create
    global new_name
    global new_acc_no
    global new_contact_no
    global new_city
    global new_pincode
    global new_fund
    new_name = StringVar()
    new_acc_no = StringVar()
    new_contact_no = StringVar()
    new_city = StringVar()
    new_pincode = StringVar()
    new_fund = StringVar()
    
    acc_scr = Toplevel(main_scr)
    acc_scr.title("Create New Account")

    #creatin labels
    Label(acc_scr, text="Enter all the details below to create a new account", font=("calibri", 13)).grid(row=0, sticky=None, pady=15, padx=10)
    Label(acc_scr, text="Name: ", font=("calibri", 12)).grid(row=1, sticky=W, padx=10)
    Label(acc_scr, text="Account No: ", font=("calibri", 12)).grid(row=2, sticky=W, padx=10)
    Label(acc_scr, text="Contact No: ", font=("calibri", 12)).grid(row=3, sticky=W, padx=10)
    Label(acc_scr, text="City: ", font=("calibri", 12)).grid(row=4, sticky=W, padx=10)
    Label(acc_scr, text="Pincode: ", font=("calibri", 12)).grid(row=5, sticky=W, padx=10)
    Label(acc_scr, text="Opening fund: ", font=("calibri", 12)).grid(row=6, sticky=W, padx=10)
    notif_acc_create = Label(acc_scr, font=("calibri", 12))
    notif_acc_create.grid(row=8, sticky=None, pady=10)

    #creating entries
    Entry(acc_scr, textvariable=new_name, width=25).grid(row=1, sticky=None)
    Entry(acc_scr, textvariable=new_acc_no, width=25).grid(row=2, sticky=None)
    Entry(acc_scr, textvariable=new_contact_no, width=25).grid(row=3, sticky=None)
    Entry(acc_scr, textvariable=new_city, width=25).grid(row=4, sticky=None)
    Entry(acc_scr, textvariable=new_pincode, width=25).grid(row=5, sticky=None)
    Entry(acc_scr, textvariable=new_fund, width=25).grid(row=6, sticky=None)


    #creating buttons
    Button(acc_scr, text="Create Account", font=("calibri", 12), width=20, command=finish_create_acc).grid(row=7, sticky=None, pady=10)


def main_operations():
    global main_scr
    global entry_acc
    global notif_procced
    entry_acc = StringVar()
    main_scr = Toplevel(log_scr)
    main_scr.title("Account management page")

    #creating lables
    Label(main_scr, text="Enter a registered account no.", font=("calibri", 13)).grid(row=0, sticky=None, pady=10, padx=20)
    Label(main_scr, text="Or\nCreate a new account", font=("calibri", 13)).grid(row=4, sticky=None)
    Label(main_scr).grid(row=6, sticky=None, pady=10)
    notif_procced = Label(main_scr, font=("calibri", 12))
    notif_procced.grid(row=6, sticky=None, pady=15)


    #creating entries
    Entry(main_scr, textvariable=entry_acc, width=30).grid(row=1, sticky=None, padx=10, pady=3)



    #creating buttons
    Button(main_scr, text="Procced", width=20, font=("calibri", 12), command=entry_account).grid(row=2, sticky=None, pady=7)
    Button(main_scr, text="Create Account", width=20, font=("calibri", 12), command=create_account).grid(row=5, sticky=None, pady=7)



def finish_registration():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    if temp_username.get()=="" or temp_pass.get()=="" or temp_pin.get()=="":
        notif_reg.config(fg="red", text="All fields are required * ")


    elif temp_pin.get()=="53539":
        try:
            c.execute("""INSERT INTO administation(username, password, security_pin)
            VALUES(?, ?, ?)""",(temp_username.get(), temp_pass.get(), temp_pin.get()))
            conn.commit()
            
            notif_reg.config(fg="green", text="Registration has done succesfully")
            
        except IntegrityError as E:
            print("accoutn already exists")
            notif_reg.config(fg="red", text="Account already registered *")

    else:
        notif_reg.config(fg="red", text="Check the security pin *")
            

#creating finish login method
def finish_login():
    username=login_username.get()
    password=login_password.get()
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    try:
        if username=="" or password=="":
            notif_log.config(fg="red", text="All fields are required *")
            return
        else:
            c.execute("SELECT password FROM administation WHERE username = ?", (username,))
            passs = c.fetchall()
            if passs[0][0] != password:
                notif_log.config(fg="red", text="Check your username and password *")
                return
            else:
                notif_log.config(fg="green", text="Succesfully logged in")
                main_operations()
    except:
        notif_log.config(fg="red", text="Invalid username *")

conn.close()


#creating register function
def register():
    global temp_username
    global temp_pass
    global temp_pin
    global notif_reg
    global reg_scr
    temp_username = StringVar()
    temp_pass = StringVar()
    temp_pin = StringVar()

    #creating a new window
    reg_scr = Toplevel(root)
    reg_scr.title("Registration Page")

    #creating labels
    Label(reg_scr, text="Please Enter All The Details Below To Register", font=("calibri", 13)).grid(row=0, sticky=None, pady=10, padx=20)
    Label(reg_scr, text="Username: ", font=("calibri", 12)).grid(row=1, sticky=W, padx=10)
    Label(reg_scr, text="Password: ", font=("calibri", 12)).grid(row=2, sticky=W, padx=10)
    Label(reg_scr, text="Security Pin: ", font=("calibri", 12)).grid(row=3, sticky=W, padx=10)
    notif_reg = Label(reg_scr, font=("calibri", 12))
    notif_reg.grid(row=5, sticky=None, pady=10)
    
    #creating entries
    Entry(reg_scr, textvariable=temp_username, width=25).grid(row=1, sticky=None)
    Entry(reg_scr, textvariable=temp_pass, width=25).grid(row=2, sticky=None)
    Entry(reg_scr, textvariable=temp_pin, width=25).grid(row=3, sticky=None)

    #creating buttons
    Button(reg_scr, text="Register", command=finish_registration, width=18, font=("calibri", 12)).grid(row=4, sticky=None, pady=10)



#creating login method
def login():
    global login_username
    global login_password
    global notif_log
    global log_scr
    login_username = StringVar()
    login_password = StringVar()
    log_scr = Toplevel(root)
    log_scr.title("Loging Page")

    
    #creating labels
    Label(log_scr, text="Please enter your login credintails", font=("calibri", 13)).grid(row=0, sticky=None, pady=10, padx=50)
    Label(log_scr, text="Username: ", font=("calibri", 12)).grid(row=1, sticky=W, padx=10)
    Label(log_scr, text="Password: ", font=("calibri", 12)).grid(row=2, sticky=W, padx=10)
    notif_log=Label(log_scr, font=("calibri", 12))
    notif_log.grid(row=4, sticky=None, pady=10)


    #creating entries
    Entry(log_scr, textvariable=login_username, width =25).grid(row=1, sticky=None)
    Entry(log_scr, textvariable=login_password, width =25).grid(row=2, sticky=None)


    #creating buttons
    Button(log_scr, text="Login", width=20, font=("calibri", 12), command=finish_login).grid(row=3, sticky=None, pady=10)


#creating the main window
root = Tk()
root.title("Administration login")


#importing images
img = Image.open('bankimg.png')
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)


#creating labels
Label(root, text="Login With Your Credintials or Register", font=("calibri", 13)).grid(row=0, sticky=None, pady=10, padx=10)
Label(root, image=img).grid(row=1, sticky=None, pady=10)
Label(root).grid(row=5, pady=5)


#creating buttons
Button(root, text="Register", width=20, font=("calibri", 12), command=register).grid(row=4, sticky=None)
Button(root, text="Login", width=20, font=("calibri", 12), command=login).grid(row=3, sticky=None, pady=10)


root.mainloop()
