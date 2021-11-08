import sqlite3
import tkinter as tk
from tkinter import messagebox
def Check_Validity(value):
    phoneCount = 0
    phoneCount1 = 0
    validation = 0
    for x in value:
        if (x.isdigit()):
            phoneCount += 1
            if phoneCount == 1:
                if x == "0":
                    validation = 1
            if phoneCount == 2:
                if x == "3":
                    validation = 2

        phoneCount1 += 1
    result = phoneCount1 - phoneCount
    return result,validation,phoneCount
def Get_Employees():

    conn = sqlite3.connect("LoginDetails.db")
    cursor = conn.cursor()
    pos = "EMPLOYEE"
    cursor.execute("SELECT Username FROM LoginTable WHERE Position = ?", (pos,))
    count = 0
    for x in cursor.fetchall():
        count += 1

    pos = "OWNER"
    cursor.execute("SELECT Username FROM LoginTable WHERE Position = ?", (pos,))
    count1 = 0
    for x in cursor.fetchall():
        count1 += 1
    data = [str(count),str(count1)]
    return data
def Get_Profile_Details(name):
    # DataBase Opening
    conn = sqlite3.connect("LoginDetails.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Gender FROM LoginTable WHERE Full_Name =?", (name,))
    gender = cursor.fetchall()
    gender = str(gender[0][0])
    cursor.execute("SELECT Username FROM LoginTable WHERE Full_Name =?", (name,))
    UserName = cursor.fetchall()
    UserName = str(UserName[0][0])
    cursor.execute("SELECT Password FROM LoginTable WHERE Full_Name =?", (name,))
    Pass = cursor.fetchall()
    Pass = str(Pass[0][0])
    data = [UserName,Pass,gender]
    return data
def update(Status,emailEnt,phoneEnt,PassEnt,position,Email,Contact_Number, Pass, name, EmailVarify):

    change = 0
    error = 0
    email = 0

    if emailEnt.get() == "" or phoneEnt.get() == "" or PassEnt == "":
        tk.messagebox.showerror("Fields Empty","Fill The Fields Properly. Fields Should Not be Empty")
        error = 1
    passCount = 0
    passCount1 = 0
    Password = PassEnt.get()
    for i in Password:
        if (i.isdigit()):
            passCount += 1
        passCount1 += 1
    phoneCount = 0
    phoneCount1 = 0
    Phone = phoneEnt.get()
    validation = 0
    for x in Phone:
        if (x.isdigit()):
            phoneCount += 1
            if phoneCount == 1:
                if x == "0":
                    validation = 1
            if phoneCount == 2:
                if x == "3":
                    validation = 2

        phoneCount1 += 1



    if Status.get() != position:
        change = 1
    if Email != emailEnt.get():
        change = 2
        email = 1
    else:
        if EmailVarify != 1 and email == 1:
            error = 1
            tk.messagebox.showerror("Email Varification Failed","Please Enter a valid Email Address")
    if phoneEnt.get() != Contact_Number:
        change = 3
    else:
        if phoneCount1 != 11 or phoneCount1 - phoneCount != 0:
            tk.messagebox.showerror("Phone Number Failed", "Invalid Mobile Number. NOTE: It should contain 11 numeric digits")
            error = 1
        if validation != 2:
            tk.messagebox.showerror("Phone Validation Failed","Phone Number should start with 03. Format [03123456789]")
            error = 1
    if PassEnt.get() != Pass:
        change = 4
    else:
        if passCount1 <6:
            tk.messagebox.showerror("Password Failed","Password Should contain 6 Charachters minimum")
            error = 1
    if error == 0 and change >0:
        conn = sqlite3.connect("LoginDetails.db")
        cursor = conn.cursor()
        query = "UPDATE LoginTable SET Password=?,Contact=?,Email=?,Position=? WHERE Full_Name=?"
        cursor.execute(query,(PassEnt.get(),phoneEnt.get(),emailEnt.get(),Status.get(),name))
        conn.commit()
        cursor.close()
        conn.close()
        tk.messagebox.showinfo("Profile Updated", "Profile Updated Successfully")
    elif change == 0:
        tk.messagebox.showerror("NO CHANGES", "You made no changes, Record Remained Same")
    else:
        tk.messagebox.showerror("Data Entry Error", "Unable to save record becaue of your mistakes")
