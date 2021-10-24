import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import time
import datetime
global Varify
import Backend
import socket
import tkentrycomplete
from Requirments import *
os_name = str(socket.gethostname())
os_name = os_name.split("-")

# if os_name[1] == "MacBook" or os_name[1] == "MBP":
#     from tkmacosx import Button
Varify = 0
def ExitButton():
    exit()

def LogOut():
    global OwnerFrame
    global LoginWin

    result = tk.messagebox.askquestion("Log Out Alert!","Do you really Want to Log Out?")
    if result == "yes":
        try:
            user = Username
            pc = pc_name
            Backend.Remember_me(user, "0", pc)
            print("Account Status: 0")
        except:
            pass
        OwnerFrame.destroy()
        LoginWin()


#++++++++++++++++++++++++++++++++++++++++++Owner Dashboard Code++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#8#########################################SETTINGS############################################

def Generate_Table(myFrame,width,title):
    tableFrame = Frame(myFrame, width=770, height=300)
    tableFrame.pack()
    tableFrame.place(x=10, y=60)
    mylist = []
    for i in range(1,len(title)+1):
        mylist.append(i)
    scrollbar = ttk.Scrollbar(tableFrame, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    treeStyle = ttk.Style()
    treeStyle.theme_use("default")
    treeStyle.configure("Treeview", background="silver", foreground="blue", fieldbackground="silver", rowheight=35,
                        relief="flat", font=("Times 16 bold"))

    # TreeStyle.map("Treeview", background=[('selected', 'red')])
    Salerydata = ttk.Treeview(tableFrame, columns=(mylist), show="headings", style="Treeview",
                              yscrollcommand=scrollbar)
    index = 1
    for i in range(len(title)):
        Salerydata.heading(index, text=title[i])
        Salerydata.column(index, width=width[i])
        index += 1
    # tags
    Salerydata.tag_configure("Treeview", background="black", foreground="white", font=("Times 12"))

    Salerydata.pack()
    # Salerydata.bind("<ButtonRelease-1>", PaySalery)
    # Salerydata.bind("<Up>", PaySalery)
    # Salerydata.bind("<Down>", PaySalery)
    scrollbar.config(command=Salerydata.yview)
class Add_Agent(Button):
        def myAgent(self):
            agentFrame = Tk()
            agentFrame.title("Add New Agent")
            agentFrame.geometry("400x400")
            agFrame = Frame(agentFrame, bg="white")
            agFrame.pack(fill=BOTH, expand=1)
            titles = ["Agent Name", "Contact Number", "Email Address", "Department", "Address"]
            y = 50
            entries = []
            add = Button(agFrame)
            add.pack()
            add.place(x=145, y=270)
            for i in range(len(titles)):
                entries.append("")
                label = Label(agFrame, text=titles[i], bg="white", fg="black", font=("Times 14"))
                label.pack()
                label.place(x=10, y=y)
                entries[i] = Entry(agFrame, width=25, font=("Times 14"))
                entries[i].pack()
                entries[i].place(x=130, y=y)
                y += 50
            agentFrame.mainloop()

def Agents(agentFrame):
    menu = StringVar()
    combo = tkentrycomplete.AutocompleteCombobox(agentFrame, textvariable=menu, width=40, font=("Times 20 bold"))
    # List = Edit_Waiter_Combo()
    # combo.set_completion_list(List)

    combo.place(x=10, y=10)
    combo.focus()
    buttons = ["Add/Remove Agent","View Details"]
    button_command = [Add_Agent.myAgent,""]
    x = 460
    for i in range(len(buttons)):
        btn = Button(agentFrame,text=buttons[i],bg="#3D0D3E",fg="white",font=("Times 16"),activebackground="#C11AC4", command= lambda x = i:button_command[x])
        btn.pack()
        btn.place(x=x,y=20)
        btn.bind("<Enter>", lambda event, color=hover_color, btn=btn: change_color(event, btn, color))
        btn.bind("<Leave>", lambda event, color="#3D0D3E", btn=btn: change_color(event, btn, color))
        x += 170
    title = ["Date","Agent Name","Payment"]
    width = [90,520,90]
    Generate_Table(agentFrame,width,title)

def EditProfile(ProfileFrame):
    global ProfileBtn
    global Profile
    global EmployAcc
    global DelAcc
    global name,Email,position,Contact_Number,EmailValid
    if Profile == 1:
        tk.messagebox.showinfo("ALready Open", "Edit Profile is already opened")
    else:
        Profile = 1
        EmployAcc = 0
        DelAcc = 0

        profile_data = Backend.Get_Profile_Details(name)
        titles = ["Full Name:","Gender:","Your Position:","Your Email:","Contact Number:"]
        y = 20
        for i in range(len(titles)):
            nameLabel = Label(
                ProfileFrame,
                text=titles[i],
                font=("Times 12"),
                fg="white",
                bg=fg_color,
            )
            nameLabel.pack()
            nameLabel.place(x=10, y=y)
            y += 40
        NameEntry = Label(
            ProfileFrame,
            text = name,
            fg = light_fg,
            bg = fg_color,
            font = "Times 12 bold",
            #state = DISABLED
        )
        NameEntry.pack()

        NameEntry.place(x=200, y=20)

        genderEntry = Label(
            ProfileFrame,
            text=profile_data[2],
            font=("Times 12"),
            bg=fg_color,
            fg=light_fg,

        )
        genderEntry.pack()
        genderEntry.place(x=200,y=60)


        global Status
        Status = StringVar()
        Status.set(position)
        TypeMenu = OptionMenu(
            ProfileFrame,
            Status,
            "OWNER", "EMPLOYEE",
        )
        TypeMenu.pack()
        TypeMenu.place(x=200,y=100)



        global emailEnt
        emailEnt = tk.Entry(
            ProfileFrame,
            width=50,
            borderwidth=4,
            #state = DISABLED,
        )
        emailEnt.bind("@gmail.com", lambda event,frame=ProfileFrame,x=200,y=155: EmailValidation(event,frame,x,y))
        emailEnt.bind("@azeementerprises.com", lambda event,frame=ProfileFrame,x=200,y=155: EmailValidation(event,frame,x,y))
        emailEnt.bind("@yahoo.com", lambda event,frame=ProfileFrame,x=200,y=155: EmailValidation(event,frame,x,y))
        emailEnt.pack()
        emailEnt.insert(0, Email)
        emailEnt.place(x=200, y=140)

        global phoneEnt
        phoneEnt = tk.Entry(
            ProfileFrame,
            width=50,
            borderwidth=4,
            #state = DISABLED,
        )
        phoneEnt.pack()
        phoneEnt.insert(0, Contact_Number)
        phoneEnt.place(x=200, y=180)

        # UserFrame

        LoginFrame = LabelFrame(
            ProfileFrame,
            width=770,
            height=150,
            borderwidth=10,
            background=fg_color,
            text="Login Details",
            font="Times 14 bold",
            foreground=light_fg,
        )
        LoginFrame.pack()
        LoginFrame.place(x=10, y=230)

        User = Label(
            LoginFrame,
            text="Your Username: ",
            bg=fg_color,
            fg=light_fg,
            font=("Times 12"),
        )
        User.pack()
        User.place(x=10, y=10)
        UserEnt = Label(
            LoginFrame,
            text=profile_data[0],
            font=("Times 12 bold"),
            bg=fg_color,
            fg=light_fg,
            # state = DISABLED,
        )
        UserEnt.pack()

        UserEnt.place(x=150, y=10)

        # PASSOWORD
        password = Label(
            LoginFrame,
            text="Your Password: ",
            bg = fg_color,
            fg=light_fg,
            font=("Times 12"),
        )
        password.pack()
        password.place(x=10, y=60)
        global PassEnt
        PassEnt = tk.Entry(
            LoginFrame,
            width=45,
            borderwidth=4,
            # state = DISABLED,
        )
        PassEnt.pack()
        PassEnt.insert(0, profile_data[1])
        PassEnt.place(x=150, y=60)
        updateBtn = Button(
            LoginFrame,
            text =" Update ",
            activebackground="#C11AC4",
            bg="#3D0D3E",
            activeforeground="white",
            fg="white",
            relief = RAISED,
            font = ("Times 11"),
            command = lambda status = Status,email = emailEnt,phone = phoneEnt,pas=PassEnt,position = position,em = Email,contact = Contact_Number,Pass = profile_data[1],Name=name,valid = EmailValid: Backend.update(status,email,phone,pas,position,em,contact,Pass,Name,valid),
        )
        updateBtn.pack()
        updateBtn.place(x=650,y=60)
        updateBtn.bind("<Enter>", lambda event, color=hover_color, btn=updateBtn: change_color(event, btn, color))
        updateBtn.bind("<Leave>", lambda event, color="#3D0D3E", btn=updateBtn: change_color(event, btn, color))

def combobox():
    global tab
    if tab == "EMPLOYEE":
        pos = "EMPLOYEE"
    if tab == "OWNER":
        pos = "OWNER"
    conn = sqlite3.connect("LoginDetails.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Username FROM LoginTable WHERE Position =?", (pos,))
    Usernames = []
    for x in cursor.fetchall():
        Usernames.append(x[0])
    return Usernames
    conn.close()
def delete():
    global TypeMenu
    error = 0
    if TypeMenu.get() == "Choose Username":
        tk.messagebox.showerror("Error","Please select a Username first")
        error = 1
    conn = sqlite3.connect("LoginDetails.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM LoginTable WHERE Username =?", (TypeMenu.get(),))
    if cursor.fetchall():
        if error == 0:

            ask = tk.messagebox.askquestion("Delete Account", "Are you sure? you want to delete this account.")
            if ask == "yes":
                cursor.execute("DELETE FROM LoginTable WHERE Username =?", (TypeMenu.get(),))
                messagebox.showinfo("Account deleted", "Username "+TypeMenu.get()+" has been deleted")
    else:
        if error == 0:
            tk.messagebox.showerror("Username Error", "Please select a valid Username")
    conn.commit()
    cursor.close()
    conn.close()
def promote():
    global PromoMenu
    error = 0
    promote = "OWNER"
    if PromoMenu.get() == "Choose Username":
        tk.messagebox.showerror("Error", "Please select a Username first")
        error = 1
    conn = sqlite3.connect("LoginDetails.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM LoginTable WHERE Username =?", (PromoMenu.get(),))
    if cursor.fetchall():
        if error == 0:

            ask = tk.messagebox.askquestion("Promote Account", "Are you sure? you want to PROMOTE this account.")
            if ask == "yes":
                cursor.execute("UPDATE LoginTable SET Position=? WHERE Username =?", (promote,PromoMenu.get()))
                messagebox.showinfo("Account Updated", "Username " + PromoMenu.get() + " has been PROMOTED to OWNER Account")
    else:
        if error == 0:
            tk.messagebox.showerror("Username Error", "Please select a valid Username")
    conn.commit()
    cursor.close()
    conn.close()
def EmployeeAccounts(SettingFrame):
    global ProfileBtn
    global DetailBtn
    global delBtn
    global Profile
    global EmployAcc
    global DelAcc
    global tab
    tab = "EMPLOYEE"
    if EmployAcc == 1:
        tk.messagebox.showinfo("ALready Open", "Edit Profile is already opened")
    else:
        Profile = 0
        DelAcc = 0
        EmployAcc = 1
        EmployFrame = LabelFrame(
            SettingFrame,
            text="Employee Accounts",
            bg=fg_color,
            fg=light_fg,
            borderwidth=2,
            relief=GROOVE,
            height=410,
            width=790,
        )
        EmployFrame.pack()
        EmployFrame.place(x=0, y=0)
        title = ["Delete Account","Promote Account"]
        y = 10
        delframe = []
        for i in range(len(title)):
            delframe.append("")
            delframe[i] = LabelFrame(
                EmployFrame,
                text=title[i],
                bg=fg_color,
                fg=light_fg,
                width=770,
                height=70,
                borderwidth=5,
                relief=GROOVE,
            )
            delframe[i].pack()
            delframe[i].place(x=5, y=y)
            y += 80
        global TypeMenu
        TypeMenu = ttk.Combobox(delframe[0],)
        TypeMenu.pack()
        TypeMenu.place(x=20, y=10)
        TypeMenu.set("Choose Username")
        TypeMenu['value']=combobox()
        delbtn = Button(
            delframe[0],
            text = "Delete",
            bg = "#3D0D3E",
            fg = "white",
            relief = GROOVE,
            command = delete
        )
        delbtn.pack()
        delbtn.place(x=240,y=10)

        global PromoMenu
        PromoMenu = ttk.Combobox(delframe[1], )
        PromoMenu.pack()
        PromoMenu.place(x=20, y=10)
        PromoMenu.set("Choose Username")
        PromoMenu['value'] = combobox()
        promobtn = Button(
            delframe[1],
            text="Promote",
            bg="#3D0D3E",
            fg="white",
            relief=GROOVE,
            command=promote
        )
        promobtn.pack()
        promobtn.place(x=240, y=10)

        conn = sqlite3.connect("LoginDetails.db")
        cursor = conn.cursor()
        pos = "EMPLOYEE"
        row = 180
        cursor.execute("SELECT Username FROM LoginTable WHERE Position = ?",(pos,))
        for x in cursor.fetchall():
            x = str(x[0])
            if row == 100:
                UserLabel = Label(EmployFrame, text="Username", fg="white", bg="#E37E13", font=("Times 14"), width=10, )
                UserLabel.pack()
                UserLabel.place(x=30, y=row)
            row = row + 30
            UserLabel = Label(EmployFrame,text = x, fg = "white", bg ="#3D0D3E",font = ("Times 14"),width = 10, )
            UserLabel.pack()
            UserLabel.place(x=30,y=row)

        row = 180
        cursor.execute("SELECT Full_Name FROM LoginTable WHERE Position = ?", (pos,))
        for x in cursor.fetchall():
            x = str(x[0])
            if row == 100:
                UserLabel = Label(EmployFrame, text="Name", fg="white", bg="#E37E13", font=("Times 14"),
                                  width=15, )
                UserLabel.pack()
                UserLabel.place(x=140, y=row)
            row = row + 30
            UserLabel = Label(EmployFrame, text=x, fg="white", bg="#3D0D3E", font=("Times 14"), width=15, )
            UserLabel.pack()
            UserLabel.place(x=140, y=row)

        row = 180
        cursor.execute("SELECT Contact FROM LoginTable WHERE Position = ?", (pos,))
        for x in cursor.fetchall():
            x = str(x[0])
            if row == 100:
                UserLabel = Label(EmployFrame, text="Phone Number", fg="white", bg="#E37E13", font=("Times 14"),
                                  width=12, )
                UserLabel.pack()
                UserLabel.place(x=300, y=row)
            row = row + 30
            UserLabel = Label(EmployFrame, text=x, fg="white", bg="#3D0D3E", font=("Times 14"), width=12, )
            UserLabel.pack()
            UserLabel.place(x=300, y=row)

        row = 180
        cursor.execute("SELECT Email FROM LoginTable WHERE Position = ?", (pos,))
        for x in cursor.fetchall():
            x = str(x[0])
            if row == 100:
                UserLabel = Label(EmployFrame, text="Email", fg="white", bg="#E37E13", font=("Times 14"),
                                  width=20, )
                UserLabel.pack()
                UserLabel.place(x=430, y=row)
            row = row + 30
            UserLabel = Label(EmployFrame, text=x, fg="white", bg="#3D0D3E", font=("Times 14"), width=20, )
            UserLabel.pack()
            UserLabel.place(x=430, y=row)

def Add_Bill():
    bill_root = Tk()
    bill_root.title("Add New Bill")
    bill_root.geometry("1200x700")
    bill_frame= Frame(bill_root,bg=bg_color)
    bill_frame.pack(fill=BOTH,expand=1)
    fields = ["Department","Tax (%)","Firm Name","Subject"]
    depart,Firms,Subject,item_names,specs = Backend.Set_Billing_List()
    item_complition = 
    complition_list = [depart,Firms,Subject]
    item = ["Item Name","Quantity","Specifications","Amount"]
    prints = ["Tax Applicable","Quotation","Bill","Comparator","Estimate","Invoice"]
    height = [200,420]
    y = 30
    frames = []
    for i in range(2):
        labelframe = LabelFrame(bill_frame,bg=fg_color,borderwidth=4,width=1150,height=height[i])
        labelframe.pack()
        labelframe.place(x=25,y=y)
        y += 220
        frames.append(labelframe)
    y = 20
    comppletion_list_count = 0
    for i in range(len(fields)):
        if i == 1:
            x = 670
            y -= 40
            entry = Entry(frames[0], width=10, font=big_font)
            entry.pack()
            entry.place(x=x + 70, y=y-5)
            entry.insert(0, "17")
            entry['state'] = DISABLED
        else:
            x = 20
            value = StringVar()
            labelentry = tkentrycomplete.AutocompleteCombobox(frames[0], width=40, font=big_font,
                                                              textvariable=value)
            labelentry.set_completion_list(complition_list[comppletion_list_count])
            labelentry.place(x=x+90,y=y)
            comppletion_list_count += 1
        label = Label(frames[0],text=fields[i],bg=fg_color,fg=light_fg,font=font)
        label.pack()
        label.place(x=x,y=y)

        y += 45
    y = 20
    for i in range(len(prints)):
        if i == 0:
            x = 870
        elif i > 0 and i < 4:
            x = 700
        else:
            if i == 4:
                y = 60
            x = 840
        applicable = IntVar()
        paylabel = Checkbutton(frames[0], text=prints[i], bg=fg_color, fg=light_fg, variable=applicable,font=big_font)
        paylabel.pack()
        paylabel.place(x=x, y=y)
        y += 40
    x = 20
    width = [60,10,40,10]
    for i in range(len(item)):
        label = Label(frames[1],text=item[i],bg=fg_color,fg=light_fg,font=font)
        label.pack()
        label.place(x=x,y=15)
        if i == 0 or i == 2:
           value = StringVar()
           labelentry = tkentrycomplete.AutocompleteCombobox(frames[1], width=40, font=big_font,
                                                          textvariable=value)
           labelentry.set_completion_list(complition_list[comppletion_list_count])
           labelentry.place(x=x, y=30)


def Billing(Bill_Frame):
    x = 20
    text = ["Search","Filter by"]
    width = [80,10]
    Filter_List = ["All Bills","Firm Name","Department","Bill Title"]
    Search_List = [""]
    list_data = [Search_List,Filter_List]
    for i in range(2):
        label = Label(Bill_Frame,text=text[i],font=font,bg=fg_color,fg=light_fg)
        label.pack()
        label.place(x=x,y=20)
        value = StringVar()
        search = tkentrycomplete.AutocompleteCombobox(Bill_Frame, width=width[i], font=font,textvariable=value)
        search.set_completion_list(list_data[i])
        search.set(list_data[i][0])
        search.place(x=x, y=50)
        x += 680
    add_btn = Button(Bill_Frame,text="+",fg="black",bg=light_fg,font=big_font,width=10,command=Add_Bill)
    add_btn.pack()
    add_btn.place(x=830,y=50)


def Settings(SubFrame):
    global OwnerFrame
    global settingBtn
    global Profile
    Profile = 0
    global EmployAcc
    EmployAcc = 0
    global DelAcc
    DelAcc = 0
    global EmailVarify
    EmailVarify = 0
    title = ["Owners","Employees"]
    data = Backend.Get_Employees()
    x = 150
    for i in range(len(data)):
        Employeframe = LabelFrame(
            SubFrame,
            text=title[i],
            borderwidth=10,
            height=170,
            width=200,
            relief=GROOVE,
            bg=fg_color,
            fg=light_fg,
            font=("Times 12 bold")
        )
        Employeframe.pack()
        Employeframe.place(x=x, y=90)

        count1Label = Label(
            Employeframe,
            text=data[i],
            font=("Times 85 bold"),
            bg=fg_color,
            fg=light_fg,
        )
        count1Label.pack()
        count1Label.place(x=50, y=0)
        x += 200

def Create_Tabs(tab_names,Tab_Frame,tab_commands):
    x = 0
    ProfileBtn = []
    for i in range(len(tab_names)):
        ProfileBtn.append("")
        ProfileBtn[i] = Button(
            Tab_Frame,
            text=tab_names[i],
            font=("Times 13 bold"),
            bg="#FF14F8",
            fg=light_fg,
            activebackground="#3D0D3E",
            activeforeground=light_fg,
            relief=GROOVE,
            bd=4,
            width=200,
            command=lambda frame=Tab_Frame, func=tab_commands[i], tab="Half": Change_Tab(func, tab, frame, i)
        )
        ProfileBtn[i].pack()
        ProfileBtn[i].place(x=x, y=0)
        ProfileBtn[i].bind("<Enter>",
                           lambda event, color=hover_color, btn=ProfileBtn[i]: change_color(event, btn, color))
        ProfileBtn[i].bind("<Leave>",
                           lambda event, color="#FF14F8", btn=ProfileBtn[i]: change_color(event, btn, color))
        x += 200

def Change_Tab(open,tab,frame,tab_no):

    if tab ==  "Full":
        width = 1110
        height = 520
        x = 80
        y = 130
    else:
        width = 790
        height = 410
        x = 10
        y = 40
    if tab_no < 5:
        SettingFrame = LabelFrame(
            frame,
            height=height,
            width=width,
            bg=fg_color,
            fg=light_fg,
        )
        SettingFrame.pack()
        SettingFrame.place(x=x, y=y)

        if tab_no == 4:
            tab_names = [" EDIT PROFILE ", " EMPLOYEE ACCOUNTS ","Add/Remove Departments"]
            tab_commands = [EditProfile, EmployeeAccounts,EmployeeAccounts]
            # Buttons
        elif tab_no == 3:
            tab_names = ["Agents","Employees"]
            tab_commands = [Agents, EmployeeAccounts]
        elif tab_no == 2:
            tab_names = ["Daily Expense","Misc Expense"]
            tab_commands = [EditProfile, EmployeeAccounts]
        elif tab_no == 1:
            tab_names = ""
            tab_commands = ""
        else:
            tab_names = ["Stock Entry", "Petty Purchase","Tenders"]
            tab_commands = [EditProfile, EmployeeAccounts,EmployeeAccounts]
        if (tab_no != 0 and tab == "Full") or tab_no != 1:
           Create_Tabs(tab_names,SettingFrame,tab_commands)
        open(SettingFrame)
    else:
        open()
def LoggedInTime():
    global UserInfoFrame
    global entryData
    global years
    global months
    global days
    global hours
    global minutes
    TimeFrame = time.time()
    year = int(datetime.datetime.fromtimestamp(TimeFrame).strftime('%Y'))
    month = int(datetime.datetime.fromtimestamp(TimeFrame).strftime('%m'))
    day = int(datetime.datetime.fromtimestamp(TimeFrame).strftime('%d'))
    hour = int(datetime.datetime.fromtimestamp(TimeFrame).strftime('%H'))
    minute = int(datetime.datetime.fromtimestamp(TimeFrame).strftime('%M'))
    count = 0
    y = year - int(years)
    if y == 0:
        txt0 = " "
        count = 1
    else:
        if y<0:
            y = y*(-1)
        y = str(y)
        txt0 = y+" Year(s), "

    m = month - int(months)
    txt1 = " "
    if m == 0:
        txt1 = " "
        count = 2
    else:
        if m < 0:
            m = m * (-1)
        m = str(m)
        txt0 = m + " Months(s), "

    d = day - int(days)
    if d == 0:
        txt2 = " "
        count = 3
    else:
        if d < 0:
            d = d * (-1)
        d = str(d)
        txt2 = d + " Day(s), "

    h = hour - int(hours)
    if h == 0:
        txt3 = " "
        count = 4
    else:
        if h < 0:
            h = h * (-1)
        h = str(h)
        txt3 = h + " Hour(s), "

    min = minute - int(minutes)
    if min == 0:
        txt4 = " "
        count = 5
    else:
        if min < 0:
            min = min * (-1)
        min = str(min)
        txt4 = min + " Minute(s), "
    if count == 5:
        txt0 = "An Instant"



    txt = txt0
    txt_2 = txt1+txt2+txt3+txt4
    ContactText = Label(
        UserInfoFrame,
        text="Logged In After: ",
        font=("Times 14"),
        bg="#808080",
        fg="blue",
    )
    ContactText.pack()
    ContactText.place(x=500, y=0)

    LoginedLabel = Label(
        UserInfoFrame,
        text =txt+txt_2,
        font = ("Times 14"),
        bg = "#808080",
        fg = "white",
    )
    LoginedLabel.pack()
    LoginedLabel.place(x=630,y=0)

def change_color(event,btn,color):
    btn["bg"]=color

def OwnerDashboard(Username,name,Email,position,Contact_Number):
    global LoginPanel
    root.geometry("1200x700")
    if LoginStatus == False:
        LoginPanel.destroy()
    else:
        frame.destroy()
    global UserDate
    global OwnerFrame
    OwnerFrame = Frame(
        root,
        relief = RIDGE,
        bg = bg_color,
    )
    OwnerFrame.pack(fill=BOTH,expand=1)

    global UserInfoFrame
    UserInfoFrame = LabelFrame(
        OwnerFrame,
        relief = RIDGE,
        bg = fg_color,
        fg = light_fg,
        width = 1110,
        height = 100,
        borderwidth = 2,
    )
    UserInfoFrame.pack()
    UserInfoFrame.place(x=80,y=10)
    NameLabel = Label(
        UserInfoFrame,
        text=name,
        font=("Times 16 bold"),
        bg=fg_color,
        fg=light_fg,
    )
    NameLabel.pack()
    NameLabel.place(x=5, y=5)

    ContactLabel = Label(
        UserInfoFrame,
        text=Email+"\n"+Contact_Number,
        font=("Times 12 bold"),
        bg=fg_color,
        fg=light_fg,
    )
    ContactLabel.pack()
    ContactLabel.place(x=40, y=30)

    BtnFrame = LabelFrame(
        OwnerFrame,
        #relief = RIDGE,
        bg = fg_color,
        width = 70,
        height = 650,
    )
    BtnFrame.pack()
    BtnFrame.place(x=0,y=0)
    btn_imgs = [home,bill_img,cost_img,agents_img,setting_img,logout_img]
    btn_commands = [Settings,Billing,Settings,Settings,Settings,LogOut]
    y = 130
    DashBtn = []
    for i in range(len(btn_imgs)):
        DashBtn.append("")
        DashBtn[i] = Button(
            BtnFrame,
            image=btn_imgs[i],
            bg=fg_color,
            relief=FLAT,
            border=0,
            width=70,
            activebackground=bg_color,
            command = lambda openframe=OwnerFrame,open=btn_commands[i],tab_no=i:Change_Tab(open=open,tab="Full",frame=openframe,tab_no=tab_no)
        )
        DashBtn[i].pack()
        DashBtn[i].place(x=0, y=y)
        DashBtn[i].bind("<Enter>",lambda event, color=hover_color ,btn = DashBtn[i]: change_color(event,btn,color))
        DashBtn[i].bind("<Leave>", lambda event, color=fg_color, btn=DashBtn[i]: change_color(event, btn, color))
        y += 50




# =========================================================================================================================================================
# ============================================================Registration and Login Section=============================================================
def Notify(event):
    global passEntry
    passEntry.delete(0,"end")
    global LoginLabelFrame
    global Msg
    Msg = Label(
        LoginLabelFrame,
        text = "Password Should Contain 6-8 Characters minimum",
        font = ("TImes 10"),
        background = "white",
        foreground = "red",
    )
    Msg.pack()
    Msg.place(x=150, y=90)
def RePassClear(event):
    global RePassEntry
    RePassEntry.delete(0,"end")

def EmailClear(event):
    global emailEntry

    emailEntry.delete(0,"end")
def NameClear(event):
    global NameEntry
    NameEntry.delete(0, "end")
def NameNotify(event):
    global UserLabelFrame
    Notice = Label(
        UserLabelFrame,
        text="Special Characters are not allowed",
        font=("TImes 8"),
        background="white",
        foreground="red",
    )
    Notice.pack()
    Notice.place(x=100, y=44)
def phoneClear(event):
    global phoneEntry
    phoneEntry.delete(0, "end")
    global UserLabelFrame
    Notice = Label(
        UserLabelFrame,
        text="Note: Only Enter 11 Digit Phone Number [Format: 03123456789]",
        font=("TImes 10"),
        background="white",
        foreground="red",
    )
    Notice.pack()
    Notice.place(x=130, y=180)
def UserClear(event):
    global UserEntry
    UserEntry.delete(0,"end")
    global LoginLabelFrame
    MsgBox = Label(
        LoginLabelFrame,
        text="Note: Spaces are not allowed in Username",
        font=("TImes 10"),
        background="white",
        foreground="red",
    )
    MsgBox.pack()
    MsgBox.place(x=150, y=40)
def DataEntry():
    global NameEntry
    global phoneEntry
    global UserEntry
    global emailEntry
    global passEntry
    global clicked
    global clicks
    TimeFrame = time.time()
    date = str(datetime.datetime.fromtimestamp(TimeFrame).strftime('%Y-%m-%d %H:%M:%S'))
    conn = sqlite3.connect("LoginDetails.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO LoginTable (Datestemp, Username, Password, Full_Name, Email, Contact, Gender, Position) VALUES (?,?,?,?,?,?,?,?)",
        (date, UserEntry.get(), passEntry.get(), NameEntry.get(), emailEntry.get(), phoneEntry.get(), clicked.get(),
         clicks.get()))
    conn.commit()
    cursor.close()
    conn.close()
def SubmitFun():
    global MemberFrame
    global LoginLabelFrame
    global NameEntry
    global phoneEntry
    global UserEntry
    global emailEntry
    global RePassEntry
    global passEntry
    global clicked
    global clicks
    global EmailValid
    passCount = 0
    passCount1 = 0
    Password = passEntry.get()
    for i in Password:
        if (i.isdigit()):
            passCount += 1
        passCount1 += 1
    phoneCount = 0
    phoneCount1 = 0
    Phone = phoneEntry.get()
    validation = 0
    for x in Phone:
        if (x.isdigit()):
            phoneCount += 1
            if phoneCount==1:
                if x == "0":
                    validation = 1
            if phoneCount == 2:
                if x == "3":
                    validation = 2

        phoneCount1 +=1
    result = phoneCount1 - phoneCount
    digits = 11
    nameCount = 0
    nameCount1 = 0
    name = NameEntry.get()
    for y in name:
        if (y.isdigit()):
            nameCount += 1
        nameCount1 += 1
    userCount = 0
    userCount1 = 0
    user = UserEntry.get()
    space = 0
    for z in user:
        if (z.isdigit()):
            userCount +=1
        if z == " ":
            space = 1
        userCount1 += 1
    userResult = userCount1 - userCount
    error = 0
    if phoneEntry.get() =="" or passEntry.get() == "" or UserEntry.get() =="" or emailEntry.get() =="" or NameEntry.get() == "":
        tk.messagebox.showwarning("Form Entry Error", "Fields are empty, Fill the fields correctly then submit again")
        error = 1
    elif phoneEntry.get() =="Number" or passEntry.get() == "Password" or UserEntry.get() =="Username" or emailEntry.get() =="Email" or NameEntry.get() == "Name":
        tk.messagebox.showwarning("Form Entry Error", "Fill the form correctly and submit again")
        error = 1
    elif clicked.get() == "CHOOSE GENDER":
        tk.messagebox.showwarning("Choose an Option", "Let me know your Gender First")
        error = 1
    elif passEntry.get() != RePassEntry.get():
        tk.messagebox.showwarning("Password Miss-Matched", "Repeat Password is incorrect, Please Enter Correctly")
        RePassEntry.delete(0,"end")
        error = 1
    elif clicks.get() == "CHOOSE ONE OPTION":
        tk.messagebox.showwarning("Choose an Option", "Tell Me Your Designation/Position")
        error = 1
    elif EmailValid == 0:
        tk.messagebox.showwarning("Email Validation Failed", "Please Enter a valid Email [Allowed Formats are: Gmail/Yahoo/AzeemEnterprises]")
        error = 1
    elif passCount1 < 6:
        tk.messagebox.showwarning("Password Validation Failed", "Password is less Than 6 Characters, Make it Stronger")
        passEntry.delete(0, "end")
        RePassEntry.delete(0, "end")
        error = 1
    elif result != 0:
        tk.messagebox.showwarning("Contact Number Invalid", "Contact Number Invalid, Contact Number Should be Numeric")
        digits = 0
        error = 1
    elif digits == 11:
        if phoneCount1 != 11:
            num = str(phoneCount1)
            tk.messagebox.showwarning("Contact Number Invalid", "Contact Number Should contain 11 Characters,But You Entered: "+ num)
            error = 1
    if validation < 2:
        tk.messagebox.showwarning("Contact Number Invalid", "Contact Number is incorrect, It should start with 03 and Format: 03123456789")
        phoneEntry.delete(0,"end")
        error = 1
    elif nameCount != 0:
        tk.messagebox.showwarning("Name Invalid",
                               "Name should not contain digits")
        error = 1
    elif nameCount1 < 4:
        tk.messagebox.showinfo("Name Invalid",
                               "Name Should Contain minimum of 4 Characters")
        error = 1
    elif space == 1:
        tk.messagebox.showinfo("Username Invalid",
                               "Spaces are not allowed in Username")
        error = 1
    elif userCount1<4:
        tk.messagebox.showinfo("Username Invalid",
                               "Username Should Contain minimum of 4 Characters")
        error = 1
    elif userResult == 0:
        tk.messagebox.showinfo("Username Invalid",
                               "Username cannot be whole Numeric")
        error = 1
    if error == 0:
        EmailValid = 0
        conn= sqlite3.connect("LoginDetails.db")
        cursor = conn.cursor()
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS LoginTable (Datestemp TEXT, Username TEXT, Password TEXT, Full_Name TEXT, Email TEXT, Contact TEXT, Gender TEXT, Position TEXT)
                        """)
        cursor.execute("SELECT Full_Name FROM LoginTable WHERE Full_Name = ?", (NameEntry.get(),))
        seeResult1 = cursor.fetchall()
        if seeResult1:
            cursor.execute("SELECT Username FROM LoginTable WHERE Full_Name = ?", (NameEntry.get(),))
            thisUser = cursor.fetchall()
            see = tk.messagebox.askquestion("Credential Matched",
                                   "You Seem to be already registered a member. Do you want to see your registered Username?")
            if see == 'yes':
                myUser = str(thisUser[0])
                tk.messagebox.showinfo("Username Details",
                                       NameEntry.get()+" your registered Username is: "+myUser+". Use this to Login into your account")
            else:
                tk.messagebox.showinfo ("Name Error",
                                       "Change Your Name Please")
                NameEntry.delete(0,"end")
        else:
            cursor.execute("SELECT Username FROM LoginTable WHERE Username = ?", (UserEntry.get(),))
            seeResult = cursor.fetchall()
            if seeResult:
                tk.messagebox.showinfo("Username Error",
                                       "This Username already exists, Try another Username")
                UserEntry.delete(0, "end")
            else:
                DataEntry()
                tk.messagebox.showinfo("Registeration Successful",
                                       "You have been Registered Successfully " + NameEntry.get() + ". Use Username: " + UserEntry.get() + " Password: " + passEntry.get() + " to login into your account")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++Login and Recovery Window Code+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def LoginUserClear(event, entry,msg):
    entry.delete(0,"end")
    global LoginFrame
    if msg == "pass":
        label = Label(
            LoginFrame,
            text="Hint: Password Contains minimum 6 characters",
            background="#1c211e",
            fg="blue",
            font="Times 12",
        )
        label.pack()
        label.place(x=140, y=150)



def Login(Username,password,value):

    global Retry
    global years
    global months
    global days
    global hours
    global minutes
    global name,Email,position,Contact_Number

    error = 0
    if Username == "" or password.get() =="":
        tk.messagebox.showwarning("Login Error", "Fields are empty, Fill the fields correctly")
        error = 1
    if error == 0:
        try:
           conn = sqlite3.connect("LoginDetails.db")
           cursor = conn.cursor()
           cursor.execute("SELECT Username FROM LoginTable WHERE Username = ?", (Username,))
           userResult = cursor.fetchall()
        except:
            userResult = False
            tk.messagebox.showerror("No Account","Please get Registered First")
        if userResult:
            cursor.execute("SELECT Password FROM LoginTable WHERE Username = ?", (Username,))
            passResult = cursor.fetchone()
            if passResult[0] == passwordEntry.get():
                cursor.execute("SELECT Full_Name FROM LoginTable WHERE Username =?", (Username,))
                name = cursor.fetchall()
                name = name[0][0]
                name = str(name)
                cursor.execute("SELECT Datestemp FROM LoginTable WHERE Username =?", (Username,))
                global UserDate
                UserDate = cursor.fetchall()
                UserDate = UserDate[0][0]
                UserDate = str(UserDate)


                tk.messagebox.showinfo("Login Successful","Login Successful")
                cursor.execute("SELECT Position FROM LoginTable WHERE Username =?",(Username,))
                position = cursor.fetchall()
                position=str(position[0][0])

                cursor.execute("SELECT Email, Contact FROM LoginTable WHERE Username = ?", (Username,))
                data = cursor.fetchall()
                Contact_Number = str(data[0][1])
                Email = str(data[0][0])
                conn.commit()
                cursor.close()
                conn.close()
                Backend.Remember_me(Username,value.get(),pc_name)
                Retry = 0
                if position == "OWNER" or position=="EMPLOYEE":
                    OwnerDashboard(Username,name,Email,position,Contact_Number)
                #if position == "EMPLOYEE":
                    #EmployeeDashboard()

            else:
                cursor.execute("SELECT Full_Name FROM LoginTable WHERE Username = ?", (Username,))
                seeUsername = cursor.fetchone()
                seeUsername=str(seeUsername[0])
                tk.messagebox.showerror("Password Failed", seeUsername+" Your Password is incorrect. Forgot? then go to recover password section")
                password.delete(0,"end")
                Retry += 1
                if Retry == 3:
                    tk.messagebox.showerror("Harm ALert!","Three attempts Failed, You are disturbing me. I am going to terminate the window")
                    root.quit()
        else:
            tk.messagebox.showerror("Login Failed","Username is Incorrect, Please get registered first")
            LoginUserEntry.delete(0, "end")
            password.delete(0, "end")
def CheckUser():
    global DataPass
    TimeFrame = time.time()
    year = int(datetime.datetime.fromtimestamp(TimeFrame).strftime('%Y'))
    month = int(datetime.datetime.fromtimestamp(TimeFrame).strftime('%m'))
    day = int(datetime.datetime.fromtimestamp(TimeFrame).strftime('%d'))
    hour = int(datetime.datetime.fromtimestamp(TimeFrame).strftime('%H'))
    minute = int(datetime.datetime.fromtimestamp(TimeFrame).strftime('%M'))
    conn = sqlite3.connect("LoginDetails.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Year FROM LoginTime")
    for x in cursor.fetchall():
        save = int(x[0])
        y = year - save
        if y == 0:
            cursor.execute("SELECT Month FROM LoginTime WHERE Year = ?",(x[0],))
            for y in cursor.fetchall():
                save1 = int(y[0])
                m = month - save1
                if m == 0:
                    cursor.execute("SELECT Day FROM LoginTime WHERE Month = ?", (y[0],))
                    for z in cursor.fetchall():
                        save2 = int(z[0])

                        d = day - save2
                        if d == 0:
                            cursor.execute("SELECT Hour FROM LoginTime WHERE Day = ?", (z[0],))
                            for a in cursor.fetchall():
                                cursor.execute("SELECT Minute FROM LoginTime WHERE Day = ?", (a[0],))
                                for b in cursor.fetchall():
                                    cursor.execute("SELECT Username FROM LoginTime WHERE Day = ?", (b[0],))
                                    result = cursor.fetchall()

                                    DataPass = result[0][0]
                                cursor.execute("SELECT Username FROM LoginTime WHERE Hour = ?", (a[0],))
                                result = cursor.fetchall()

                                DataPass = result[0][0]
                        else:
                            cursor.execute("SELECT Username FROM LoginTime WHERE Month = ?", (y[0],))
                            result = cursor.fetchall()
                            DataPass = result[0]


global RetryRecovery
RetryRecovery = 0
def CheckRecovery(entry,choice):
    global EmailValid
    global EntryLabel
    global RecoverButton
    global RetryRecovery
    global attempts
    error = 0
    if choice.get() != "CHOOSE OPTION":

        if entry.get() == "":
            error = 1
            EmailValid = 0
            tk.messagebox.showerror("Field Empty", "Please Enter "+choice.get())
        elif choice.get() == "Contact Number":
            result,validation,phoneCount1 = Backend.Check_Validity(entry.get())
            if validation != 2 or phoneCount1 != 11 or result != 0:
                error = 1
                tk.messagebox.showerror("Invalid Number","Please write the number correctly. NOTE: 11 Numeric digits starting from city code")
        elif choice.get() == "Email":
            if EmailValid != 1:
                error = 1
                tk.messagebox.showerror("Email Validation Failed","Please enter a valid email address")

    else:
        error = 1
        tk.messagebox.showerror("Invalid Choice", "Please choose an option to start your recovery")

    if error == 0:
        conn = sqlite3.connect("LoginDetails.db")
        cursor = conn.cursor()
        if choice.get() == "Contact Number":
            query = "SELECT Password and Username FROM LoginTable WHERE Contact =?"

        elif choice.get() == "Email":
            query = "SELECT Password and Username FROM LoginTable WHERE Email =?"

        elif choice.get() == "Username":
            query = "SELECT Password FROM LoginTable WHERE Username =?"

        else:
            query = "SELECT Password FROM LoginTable WHERE Username =?"

        cursor.execute(query, (entry.get(),))
        password = cursor.fetchall()
        if password:
            tk.messagebox.showinfo("Password Recovered", "Password is: " + str(password[0][0]))
        else:
            tk.messagebox.showerror("NO RECORD FOUND","Sorry! This "+choice.get()+" is not registered in my database.")
        RetryRecovery = 3
        # retry = str(RetryRecovery)
        # attempts['text'] = retry
        # if RetryRecovery == 3:
        #
        #                 attempts['text'] = "0"
        #                 tk.messagebox.showerror("No more attempts", "Sorry! I can not offer more attempts")
        #                 RecoverButton['state'] = DISABLED
        #
        #             else:
        #                 attempts['text'] = retry
        #                 tk.messagebox.showwarning("Contact Not Found Error",
        #                                           "Contact Number Incorrect for the username " + LoginUserEntry.get())
        #     else:
        #         tk.messagebox.showerror("Username Error",
        #                                 "This username is not registered, click on Create account to get registered")
        #





def RecoverEntryClear(event,entry):
    global EntryLabel
    if entry=="Contact Number":
        EntryLabel['text'] = "Enter Contact Number"
    elif entry == "Username":
        EntryLabel['text'] = "Enter Username"
    if entry=="Email":
        EntryLabel['text']="Enter Email Address"
def EmailValidation(event,RecoveryFrame,x,y):
    global EmailValid
    EmailValid = 1
    label = Label(
        RecoveryFrame,
        text = "Email Validation Successful",
        font = ("Times 12"),
        bg = "white",
        fg = "blue",
    )
    label.pack()
    label.place(x=x,y=y)

def ForgotFun(user):
    RecoveryFrame = Tk()
    RecoveryFrame.geometry("500x200")
    RecoveryFrame.wm_resizable(0, 0)
    RecoveryFrame.title("Reset Password")
    Text = Label(
        RecoveryFrame,
        text = "Choose Recovery Option:",
        font = ("Times 14 bold"),
        bg = "white",
    )
    Text.pack()
    Text.place(x=30,y=20)
    RecoverOption = StringVar()
    RecoverOption.set("Username")
    RecoveryMenu = OptionMenu(
        RecoveryFrame,
        RecoverOption,
        "Email", "Contact Number","Username"
    )
    RecoveryMenu.pack()
    RecoveryMenu.place(x=290, y=20)
    global RecoverEntry
    RecoverEntry = tk.Entry(
        RecoveryFrame,
        width=15,
        font="Times 14",
        borderwidth=2,
        bg="white",
    )
    RecoverEntry.pack()
    RecoverEntry.place(x=200, y=60)
    # RecoverEntry.bind("<Button-1>", lambda event,e=RecoverOption.get():RecoverEntryClear(event,e))
    RecoverEntry.bind("@gmail.com", lambda event, frame=RecoveryFrame: EmailValidation(event,frame,310,100))
    RecoverEntry.bind("@yahoo.com",lambda event, frame=RecoveryFrame: EmailValidation(event,frame,310,100))
    RecoverEntry.bind("@azeementerprises.com",lambda event, frame=RecoveryFrame: EmailValidation(event,frame,310,100))
    RecoverEntry.insert(0,user)
    RecoverEntry.focus_force()
    global EntryLabel
    EntryLabel = Label(
        RecoveryFrame,
        font = "Times 14 bold",
        bg = "white",
    )
    EntryLabel.pack()
    EntryLabel.place(x=30,y=60)
    global RecoverButton
    RecoverButton = Button(
        RecoveryFrame,
        text = "RECOVER",
        bg = "blue",
        fg = "black",
        relief = RAISED,
        font = ("Times 11 bold"),
        border = 10,
        command = lambda entry = RecoverEntry,choice=RecoverOption: CheckRecovery(entry,choice),
    )
    RecoverButton.pack()
    RecoverButton.place(x=180,y=100)
    global attempts
    attemptFrame = LabelFrame(
        RecoveryFrame,
        font=("Times 11"),
        text = "Attempts",
        bg = "white",
        borderwidth = 2,
        width = 80,
        height = 80,
    )
    attemptFrame.pack()
    attemptFrame.place(x=380,y=20)
    attempts = Label(
        attemptFrame,
        font = "Time 20 bold",
        bg = "white",
        fg = "blue",
        text = "3",
    )
    attempts.pack()
    attempts.place(x=30,y=0)
global EmailValid
EmailValid = 0
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Login_Event(event,user,pas,v):
    Login(user,pas,v)
def LoginWin():
    global MemberFrame
    global Open
    global Open1
    global DataPass

    Open1 = 1
    if Open == 1:
        MemberFrame.destroy()
    if Open == 0:
        frame.destroy()
    global LoginPanel
    LoginPanel = Frame(
        root,
        relief = RIDGE,
        bg = bg_color
    )
    LoginPanel.pack(fill = BOTH, expand = 1)
    # logo = Label(LoginPanel,image=Logo,relief=FLAT,border=0)
    # logo.pack()
    # logo.place(x=30,y=5)

    global LoginFrame
    LoginFrame = LabelFrame(
        LoginPanel,
        relief = RIDGE,
        width = 400,
        height = 300,
        bg = fg_color,
        borderwidth = 2,
    )
    LoginFrame.pack()
    LoginFrame.place(x=250,y=150)
    Title = Label(
        LoginPanel,
        text = "LOGIN",
        bg = bg_color,
        fg = light_fg,
        font = ("Algerian 40 bold"),
    )
    Title.pack()
    Title.place(x=380,y=90)

    # USERNAME
    labels = ["Username","Password"]
    y = 70
    for i in labels:
        username = Label(
            LoginFrame,
            text=i,
            background=fg_color,
            font=("Times 14 bold"),
            fg = light_fg
        )
        username.pack()
        username.place(x=30, y=y)
        y += 50
    global LoginUserEntry, passwordEntry
    LoginUserEntry = tk.Entry(
        LoginFrame,
        width=20,
        borderwidth=2,
        font = "Times 14",
    )
    LoginUserEntry.pack()
    LoginUserEntry.bind("<Button-1>", lambda event, x=LoginUserEntry,msg="user": LoginUserClear(event,x,msg))
    #CheckUser()
    LoginUserEntry.insert(0, "Admin")
    LoginUserEntry.place(x=120, y=70)

    passwordEntry = tk.Entry(
        LoginFrame,
        width=20,
        borderwidth=2,
        font="Times 14",
        show = "*",
    )
    passwordEntry.pack()
    passwordEntry.insert(0, "")
    passwordEntry.place(x=120, y=120)
    passwordEntry.bind("<Button-1>", lambda event, x=passwordEntry,msg="pass": LoginUserClear(event, x,msg))
    passwordEntry.focus_force()
    value = IntVar()
    passCheck = Checkbutton(LoginFrame,bg=fg_color,text="Remember me",variable=value,fg=light_fg)
    passCheck.pack()
    passCheck.place(x=120,y=150)
    passwordEntry.bind("<Return>",
                       lambda event, user=LoginUserEntry.get(), pas=passwordEntry, v=value: Login_Event(event,user, pas,v))

    # LoginBut

    global LoginBut
    LoginBut = Button(
        LoginFrame,
        text = "LOGIN",
        bg = "sky blue",
        fg = "black",
        relief = FLAT,
        font = ("Times 14 bold"),
        borderwidth = 2,

        command = lambda user=LoginUserEntry.get(),password=passwordEntry,check = value:Login(user,password,check)
    )
    LoginBut.pack(side=TOP)
    LoginBut.place(x=170, y=180)

    CreateBut = Button(
        LoginFrame,
        text = "Create Account",
        bg = "sky blue",
        fg = "black",
        relief = RAISED,
        font = ("Times 14 bold"),
        borderwidth = 2,
        command = RegisterMember,
    )
    CreateBut.pack()
    CreateBut.place(x=140,y=220)

    #Password Recovery
    global Forgotbtn
    Forgotbtn = Button(
        LoginFrame,
        text = "FORGOT?",
        font = ("Times 11"),
        fg = "blue",
        bg = fg_color,
        relief = FLAT,
        command = lambda user=LoginUserEntry.get():ForgotFun(user),
    )
    Forgotbtn.pack()
    Forgotbtn.place(x=250,y=270)

# +++++++++++++++++++++++++++++++++++++++++++Registration Form Window Code+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def RegisterMember():
    global Open1
    global LoginPanel
    if Open1 == 0:
        frame.destroy()
    if Open1 == 1:
        LoginPanel.destroy()
    global Open
    Open = 1
    global MemberFrame
    MemberFrame = Frame (
        root,
        bg = 'white',
        relief = RIDGE,
    )
    MemberFrame.pack(fill= BOTH, expand = 1)
    RegLabel = Label(
        MemberFrame,
        text = "REGISTRATION FORM",
        font = ("Times 25 bold"),
        foreground = "red",
        background = "white",
    )
    RegLabel.pack()
    RegLabel.place(x=260,y=50)
    global UserLabelFrame
    UserLabelFrame = LabelFrame(
        MemberFrame,
        width = 700,
        height = 250,
        borderwidth = 10,
        background = "white",
        text="Personal Details",
        font="Times 14 bold",
        foreground="red",
    )
    UserLabelFrame.pack()
    UserLabelFrame.place(x=80, y=120)
    labels = ["Full Name:","Your Position","Your Email","Contact Number"]
    y = 20
    for i in labels:
        name = Label(
            UserLabelFrame,
            text=i,
            font=("Times 12"),
            background="white"
        )
        name.pack()
        name.place(x=10, y=y)
        y += 40
    global NameEntry
    NameEntry = tk.Entry(
        UserLabelFrame,
        width = 50,
        borderwidth = 4,
    )
    NameEntry.bind("<Button-1>", NameClear)
    NameEntry.bind("/", NameNotify)
    NameEntry.pack()
    NameEntry.insert(0, "Name")
    NameEntry.place(x=100, y=20)
    gender = Label(
        UserLabelFrame,
        text="Gender:",
        font=("Times 12"),
        background="white",
    )
    gender.pack()
    gender.place(x=400, y=60)
    global clicked
    clicked = StringVar()
    clicked.set("CHOOSE GENDER")
    GenderMenu= OptionMenu(
        UserLabelFrame,
        clicked,
        "Male", "Female",
    )
    GenderMenu.pack()
    GenderMenu.place(x=460, y=60)

    global clicks
    clicks = StringVar()
    clicks.set("CHOOSE ONE OPTION")
    TypeMenu = OptionMenu(
        UserLabelFrame,
        clicks,
        "OWNER", "EMPLOYEE",
    )
    TypeMenu.pack()
    TypeMenu.place(x=100, y=60)
    global emailEntry
    emailEntry = tk.Entry(
        UserLabelFrame,
        width=50,
        borderwidth=4,
    )
    emailEntry.bind("<Button-1>", EmailClear)
    emailEntry.bind("@gmail.com", lambda event,frame=UserLabelFrame,x=100,y=130: EmailValidation(event,frame,x,y))
    emailEntry.bind("@azeementerprises.com", lambda event,frame=UserLabelFrame,x=100,y=130: EmailValidation(event,frame,x,y))
    emailEntry.bind("@yahoo.com", lambda event,frame=UserLabelFrame,x=100,y=130: EmailValidation(event,frame,x,y))
    emailEntry.pack()
    emailEntry.insert(0, "Email")
    emailEntry.place(x=100, y=100)

    global phoneEntry
    phoneEntry = tk.Entry(
        UserLabelFrame,
        width=45,
        borderwidth=4,
    )
    phoneEntry.bind("<Button-1>", phoneClear)
    phoneEntry.pack()
    phoneEntry.insert(0, "Number")
    phoneEntry.place(x=130, y=150)

    #UserFrame

    global LoginLabelFrame
    LoginLabelFrame = LabelFrame(
        MemberFrame,
        width=700,
        height=200,
        borderwidth=10,
        background="white",
        text = "Login Details",
        font = "Times 14 bold",
        foreground = "red",
    )
    LoginLabelFrame.pack()
    LoginLabelFrame.place(x=80, y=380)

    #PASSOWORD
    password = Label(
        LoginLabelFrame,
        text="Create Password: ",
        background="white",
        font=("Times 12"),
    )
    password.pack()
    password.place(x=10, y=60)
    global passEntry
    passEntry = tk.Entry(
        LoginLabelFrame,
        width=50,
        borderwidth=4,
    )
    passEntry.bind("<Button-1>", Notify)
    passEntry.pack()
    passEntry.insert(0, "Password")
    passEntry.place(x=150, y=60)
    #RE-ENTER PASSWORD

    re_pass = Label(
        LoginLabelFrame,
        text="Repeat Password: ",
        background="white",
        font=("Times 12"),
    )
    re_pass.pack()
    re_pass.place(x=10, y=120)
    global RePassEntry
    RePassEntry = tk.Entry(
        LoginLabelFrame,
        width=50,
        borderwidth=4,
    )
    RePassEntry.bind("<Button-1>",RePassClear)
    RePassEntry.pack()
    RePassEntry.insert(0, "Repeat Password")
    RePassEntry.place(x=150, y=120)
    #USER NAME

    username = Label(
        LoginLabelFrame,
        text="Username: ",
        background="white",
        font=("Times 12"),
    )
    username.pack()
    username.place(x=10, y=10)
    global UserEntry
    UserEntry = tk.Entry(
        LoginLabelFrame,
        width=50,
        borderwidth=4,
    )
    UserEntry.bind("<Button-1>", UserClear)
    UserEntry.pack()
    UserEntry.insert(0, "Username")
    UserEntry.place(x=150, y=10)
    Submit = Button(
        MemberFrame,
        text = "SUBMIT",
        relief = FLAT,
        border = 0,
        font = ("Times 16 bold"),
        background = "red",
        foreground = "white",
        command = SubmitFun,
    )
    Submit.pack()
    Submit.place(x=400, y=600)

    #LOGIN BUTTON
    SignInBut = Button(
        MemberFrame,
        text="Sign In",
        font=("Times", 15, "bold"),
        background="gray",
        foreground = "white",
        relief=FLAT,
        border=0,
        command = LoginWin,
    )
    SignInBut.pack()
    SignInBut.place(x=800, y=570)
    MemberLabel = Label(
        MemberFrame,
        text = "Already Member?",
        font = ("Times 12"),
        bg = "white",
        fg = "sky blue",
    )
    MemberLabel.pack()
    MemberLabel.place(x=780, y=600)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Root Window and Program Starting Code++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root = Tk()
root.title("AZEEM OFFICE APPLICATION")
root.geometry(f'{root_width}x{root_height}')

root.wm_resizable(0,0)
global Retry
Retry = 0
frame=Frame(root,relief = RIDGE,bg= "white",)
frame.pack(fill=BOTH, expand = 1)

Logo = PhotoImage(file = Images[0])
RegImage = PhotoImage(file= Images[1])
home = PhotoImage(file=Images[2])
setting_img = PhotoImage(file=Images[3])
bill_img = PhotoImage(file=Images[4])
cost_img = PhotoImage(file=Images[5])
agents_img = PhotoImage(file=Images[6])
logout_img = PhotoImage(file=Images[7])
LogoImage = Label(frame,image = Logo,relief = FLAT,border = 0,)
LogoImage.pack(side=TOP)
Register = Button(frame,image = RegImage,relief = FLAT,border = 0,command = RegisterMember,)
Register.pack()
SignIn = Label(frame,text="Already a member?",font=("Times", 11),foreground="#00CCFF",background="#ffffff",)
SignIn.pack()
global Open
Open = 0
global Open1
Open1 = 0
#------------------------------------------------------------------------------------------------------

SignInLabel = Button(
    frame,
    text="Sign In",
    font=("Times", 11, "underline"),
    background="#FFFFFF",
    relief=FLAT,
    border=0,
    cursor ="plus",
    command = LoginWin,
)
SignInLabel.pack()
ExitImage = PhotoImage(file="exit.png")
ExitLabel = Button (
    frame,
    image = ExitImage,
    relief = FLAT,
    border = 0,
    width = 70,
    height = 70,
    command = ExitButton,
)
ExitLabel.pack()
ExitLabel.place(x=70, y=560)

LoginStatus,data = Backend.Login_Status(pc_name)
if LoginStatus:
    Username = data[0]
    name = data[1]
    Email = data[2]
    position = data[3]
    Contact_Number = data[4]
    OwnerDashboard(Username,name,Email,position,Contact_Number)


mainloop()