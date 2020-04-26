import tkinter.ttk as tkr
from tkinter import *
import ambsql.ambsql as amb
import tkinter as tk
import tkinter.messagebox as tm

#DocsPage contains text about command Documentation
class DocsPage():
    def __init__(self):
        #Open new window
        root = Tk()
        root.title(" Docs ")
        #object for Scrollbar
        Scrl = tk.Scrollbar(root)
        Txt = tk.Text(root, height=200, width=500)
        Scrl.pack(side=tk.RIGHT, fill=tk.Y)
        Txt.pack(side=tk.LEFT, fill=tk.Y)
        Scrl.config(command=Txt.yview)
        Txt.config(yscrollcommand=Scrl.set)
        quote = """
        connect                                                                 - To login to Database
        Note: Username: 'system', password: '123'
        logout()                                                                - To Logout
        clear()                                                                 - To clear the Screen
        deleteuser(<user_name>)                                                 - To delete a User
        createuser(<user_name> , <password>)                                    - To create new User
        createtable(<table-name>, <column1-name> , <column2-name>, ....)        - To create new Table
        insertvalues(<table_name>, <column1-value> , <column2-value>, ...)      - To enter the values in Table
        showtable(<table_name>)                                                 - To show the Table schema
        showvalues(<table_name>)                                                - To show the Table values
        updatevalue(<table_name> , <assignment>)                                - To Update all values of column
        updatevalue(<table_name> , <assignment> , <condition>)                  - To Update the values of column
        deletetable(<table_name>)                                               - To truncate the Table
        deletetable(<table_name> , <condition>)(e.g- deletetable(ab,name==jack))- To delete row(s) from Table
        counttable(<table_name>)                                                - To count the rows/records of Table
        sumvalue(<table_name>, <attribute>)                                     - To sum of records of particular attribute of Table
        maxvalue(<table_name>, <attribute>)                                     - To find the max value of particular attribute of Table
        minvalue(<table_name>, <attribute>)                                     - To find the min value of particular attribute of Table
        avgvalue(<table_name>, <attribute>)                                     - To find the average value of particular attribute of Table
        droptable(<table_name>)                                                 - To drop the Table
        counttable(<table_name>)                                                - To count the rows/records of Table
        altertable(<old-table_name> , <new-table_name>)                         - To rename Table Name
        Copyright (c) 2018, Ambuj. All rights reserved.
        """
        Txt.insert(END, quote)
        root.mainloop()
##
class AmbSQLPage():
    def docs():
        DocsPage()
    def __init__(self):
        window=Tk()
        window.title(" AmbSQL ")
        #Define window size according to screen size
        width  = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.geometry('%sx%s' % (int(width/2), int(height/2)))
        # creating a menu instance
        menu = Menu(window)
        window.config(menu=menu)
        #Create menu object: Table_DDL, Table_DML others
        Table_DDL = Menu(menu)
        Table_DDL.add_command(label="Create Table",)
        Table_DDL.add_command(label="Drop Table",)
        Table_DDL.add_command(label="ALTER Table",)
        menu.add_cascade(label="DDL query", menu=Table_DDL)


        Table_DML = Menu(menu)
        Table_DML.add_command(label="Insert table")
        Table_DML.add_command(label="update table")
        Table_DML.add_command(label="Show table", command =self.show_values)
        Table_DML.add_command(label="Sum value ")
        Table_DML.add_command(label="Max value")
        Table_DML.add_command(label="Average value")
        Table_DML.add_command(label="count table")
        menu.add_cascade(label="DML query", menu=Table_DML)

        others = Menu(menu)
        others.add_command(label="Documentation", command=DocsPage)
        others.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="others ", menu=others)
        window.mainloop()
    def client_exit(self):
        exit()
    def show_values(self):
        #name_label = Label(self, text="Table name")
        # self.label_username.grid(row=0, sticky=E)
        # self.table_name = Entry(self)
        # self.table_name.grid(row=0, column=1)
        #amb.showvalues("studenttable")
        print( "hello!")
class LoginPage(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.Title = Label(self, text="AmbSQL")
        self.Title.config(font=("Arial", 25))
        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.Title.grid(row=0,column=1, sticky="")
        self.label_username.grid(row=1, sticky=E)
        self.label_password.grid(row=2, sticky=E)
        self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=2, column=1)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(row=3,column=0, sticky=E)
        self.helpbtn = Button(self, text="Help", command=self.docs_btn_clicked)
        self.helpbtn.grid(row=3,column=1, sticky=W)
        self.pack()

    def _login_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "system" and password == "123":
            self.master.withdraw()
            bb = AmbSQLPage()
        else:
            tm.showerror("Login error", "Incorrect username")

    def docs_btn_clicked(self):
        DocsPage()

root = Tk()
root.geometry("500x200+400+400")
root.title("LoginPage")
lf = LoginPage(root)
root.mainloop()
