import mariadb
import tkinter as tk
from tkinter import messagebox

conn = mariadb.connect(
    user="root",
    password="root",
    host="127.0.0.1",
    database="recordStore")

# made a cursor to navigate the database
currStock = conn.cursor()

def updateStockOperation():
    osuN = osuRecordName.get().strip()
    osuS = osuRecordStock.get()
    osuS = int(osuS)
    currStock.execute("UPDATE records SET recordStock = ? WHERE recordName = ?", (osuS, osuN))
    conn.commit()

    messagebox.showinfo("Stock Updated")


# function that opens add record screen

osuWindow = tk.Tk()
osuWindow.title("Add a Record!")
osuWindow.geometry('1024x768')
osuWindow.configure(bg='black')
osuLabel = tk.Label(osuWindow, text="Update Record Stock", bg="black", fg="red3", font=("times", 32, "bold"))
osuLabel.pack(pady=10)

##Setting up variables in entry boxes

osuRecordName = tk.StringVar()
osuRecordStock = tk.IntVar()

# Creating the entry boxes, label and placements
osuStockLabel = tk.Label(
    osuWindow, text="Record Name", bg="black", fg="red3", font=("times", 32, "bold")
)
osuStockLabel.place(x=100, y=200)

osuRecordNameEntry = tk.Entry(
    osuWindow, bg="black", fg="red3", font=("times", 20), width=25, textvariable=osuRecordName
)
osuRecordNameEntry.place(x=800, y=210)

osuNameLabel = tk.Label(
    osuWindow, text="New Record Stock", bg="black", fg="red3", font=("times", 32, "bold")
)
osuNameLabel.place(x=100, y=300)

osuRecordStockEntry = tk.Entry(
    osuWindow, bg="black", fg="red3", font=("times", 20), width=25, textvariable=osuRecordStock
)
osuRecordStockEntry.place(x=800, y=310)

recordAddButton = tk.Button(
    osuWindow, text="Update Album Stock", bg="black", fg="red3", font=("times", 25), command=updateStockOperation
)
recordAddButton.place(x=250, y=450)
osuWindow.mainloop()
