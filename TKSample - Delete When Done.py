# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 07:45:07 2022

@author: hitejad
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 07:55:43 2018

@author: hitej
Notes and Changelog:
    User Interface for Teradata login and query. Currently returns name from MRN. Handles login, opening and closing database,
    and returning the result.
    6/28/2017 - Called DB_Open Commands directly from Tera_OO and removed the go-between functions. 
    6/27/2018 - Labelled Password Box
    6/27/2018 - Removed Less Secure Password Input Box and Replaced with pyautogui popup. 
    6/22/2018 - Added Open Database and Close Database Buttons
    6/21/2018 - Session initilization was throwing an error under the main function. Moved it into the IF/Main statement.
    6/14/2018 - Changed Terra_OO to object oriented format for cleaner look. 

To Do:
    Create a log of past searches and errors
    Create more user feedback options (Show if database is connected, option to connect as a different user)
    Error Message Popups?
    Query Writer? 

"""

from tkinter import *
from tkinter import ttk
import Tera_OO
import pyautogui


class configure:
    
    #Login GUI
    def __init__(self, master):
        #Master Frame
        self.frame = ttk.Frame(master)
        self.frame.pack()
        
        #UID Input
        self.UID_Box = ttk.Entry(self.frame)
        self.UID_Box.insert(0, "User ID")
        self.UID_Box.grid(row = 0, column = 0)
        #PWD Input
        #self.PWD_Box = ttk.Entry(self.frame)
        #self.PWD_Box.insert(0, "Password")
        #self.PWD_Box.grid(row = 1, column = 0)
        #Database Input
        self.DB_Box = ttk.Entry(self.frame)
        self.DB_Box.insert(0, "Database")
        self.DB_Box.grid(row = 2, column = 0)
        #Submit Button
        self.Button = ttk.Button(self.frame, text = "Submit", command = self.login_submit)
        self.Button.grid(row = 3, column = 0)
    
    #Query Box GUI            
    def query_screen(self):
        #Master Frame
        self.q_screen = ttk.Frame()
        self.q_screen.pack()
        #Query Box
        self.q_box = ttk.Entry(self.q_screen)
        self.q_box.insert(0, "MRN")
        self.q_box.grid(row = 1, column = 0, columnspan = 3)
        #Response Space
        self.response_box = ttk.Entry(self.q_screen)
        self.response_box.insert(0, "Result")
        self.response_box.grid(row = 2, column = 0, columnspan = 3)
        #Submit Button
        self.q_submit = ttk.Button(self.q_screen, text = "Submit Query", command = self.query_submit)
        self.q_submit.grid(row = 1, column = 4)
        #Open DB Button
        self.open_db = ttk.Button(self.q_screen, text = "Open Database", command = session.open_db)
        self.open_db.grid(row = 0, column = 0)
        #Close DB Button
        self.open_db = ttk.Button(self.q_screen, text = "Close Database", command = session.close_db)
        self.open_db.grid(row = 0, column = 2)

        
        
    #Handler Functions
    #Collects the Username, and Database name, creates password box and collects password, initializes the query screen. 
    def login_submit(self):
        global session
        session.User = str(self.UID_Box.get())
        session.DB = str(self.DB_Box.get())
        self.frame.destroy()
        session.Pass = pyautogui.password(text = "Password", title = "Password")
        self.query_screen()
        
    def query_submit(self):
        global session
        self.response_box.delete(0, END)
        MRN = str(self.q_box.get())
        Name = session.cursor.execute(f"SELECT Patient_First_Name, Patient_Last_Name FROM REVENUECYCLE_V.CUBE_Account_ZERO WHERE Medical_Record_Number = '{MRN}'").fetchone()
        out = (Name[0].strip() + " " + Name[1].strip())
        self.response_box.insert(0, out)
        
        
def main():
    global session 
    session = Tera_OO.session("User", "Password", "DB")
    config = Tk()
    setup = configure(config)
    config.mainloop()

    
if __name__ == "__main__":
    session = ()
    main()