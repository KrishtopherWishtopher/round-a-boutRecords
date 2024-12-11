import mariadb
import tkinter as tk
from tkinter import messagebox

conn = mariadb.connect(
    user="root",
    password="root",
    host="127.0.0.1",
    database="recordStore")

# made a cursor to navigate the database
currAdd = conn.cursor()

def addRecordOperation():
    rid = newUserID.get()
    rn = newUserName.get()
    rp = newUserPassword.get()

    currAdd.execute("INSERT INTO records (recordID, recordName, recordArtist, recordYear, recordGenre, recordStock, recordPrice) VALUES (?,?,?,?,?,?,?)", (rid, rn, ra, ry, rg, rs, rp,))
    conn.commit()

    messagebox.showinfo("Record Added!")


# function that opens add record screen

oarWindow = tk.Tk()
oarWindow.title("Add a user!")
oarWindow.geometry('1024x768')
oarWindow.configure(bg='black')
oarLabel = tk.Label(oarWindow, text="Create new user", bg="black", fg="red3", font=("times", 32, "bold"))
oarLabel.pack(pady=10)

##Setting up variables in entry boxes
newUserID = tk.IntVar()
newUserName = tk.StringVar()
newUserPassword = tk.StringVar()


# Creating the entry boxes, label and placements
newUserIDLabel = tk.Label(oarWindow, text="Record ID", bg="black", fg="red3", font=("times", 20, "bold"))
newUserIDLabel.place(x=10, y=30)
newUserIDEntry = tk.Entry(oarWindow, bg="black", fg="red3", font=("times", 20), width=25, textvariable=newUserID)
newUserIDEntry.place(x=30, y=70)

newUserNameLabel = tk.Label(oarWindow, text="Record Name", bg="black", fg="red3", font=("times", 20, "bold"))
newUserNameLabel.place(x=10, y=130)
newUserNameEntry = tk.Entry(oarWindow, bg="black", fg="red3", font=("times", 20), width=25,
                            textvariable=newUserName)
newUserNameEntry.place(x=30, y=170)

newUserPasswordLabel = tk.Label(oarWindow, text="Record Name", bg="black", fg="red3", font=("times", 20, "bold"))
newUserPasswordLabel.place(x=10, y=130)
newUserPasswordEntry = tk.Entry(oarWindow, bg="black", fg="red3", font=("times", 20), width=25, textvariable=newUserPassword)
newUserPasswordEntry.place(x=30, y=170)


recordAddButton = tk.Button(oarWindow, text="add album", bg="black", fg="red3", font=("times", 25),
                            command=addRecordOperation)
recordAddButton.place(x=200, y=800)

oarWindow.mainloop()
