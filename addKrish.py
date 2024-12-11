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
    rid = eRecordID.get()
    rn = eRecordName.get()
    ra = eRecordArtist.get()
    ry = eRecordYear.get()
    rg = eRecordGenre.get()
    rs = eRecordStock.get()
    rp = eRecordPrice.get()

    currAdd.execute("INSERT INTO records (recordID, recordName, recordArtist, recordYear, recordGenre, recordStock, recordPrice) VALUES (?,?,?,?,?,?,?)", (rid, rn, ra, ry, rg, rs, rp,))
    conn.commit()

    messagebox.showinfo("Record Added!")


# function that opens add record screen

oarWindow = tk.Tk()
oarWindow.title("Add a Record!")
oarWindow.geometry('1024x768')
oarWindow.configure(bg='black')
oarLabel = tk.Label(oarWindow, text="Add Records", bg="black", fg="red3", font=("times", 32, "bold"))
oarLabel.pack(pady=10)

##Setting up variables in entry boxes
eRecordID = tk.IntVar()
eRecordName = tk.StringVar()
eRecordArtist = tk.StringVar()
eRecordYear = tk.IntVar()
eRecordGenre = tk.StringVar()
eRecordStock = tk.IntVar()
eRecordPrice = tk.DoubleVar()

# Creating the entry boxes, label and placements
eRecordIDLabel = tk.Label(oarWindow, text="Record ID", bg="black", fg="red3", font=("times", 20, "bold"))
eRecordIDLabel.place(x=10, y=30)
eRecordIDEntry = tk.Entry(oarWindow, bg="black", fg="red3", font=("times", 20), width=25, textvariable=eRecordID)
eRecordIDEntry.place(x=30, y=70)

eRecordNameLabel = tk.Label(oarWindow, text="Record Name", bg="black", fg="red3", font=("times", 20, "bold"))
eRecordNameLabel.place(x=10, y=130)
eRecordNameEntry = tk.Entry(oarWindow, bg="black", fg="red3", font=("times", 20), width=25,
                            textvariable=eRecordName)
eRecordNameEntry.place(x=30, y=170)

eRecordArtistLabel = tk.Label(oarWindow, text="Record Artist", bg="black", fg="red3", font=("times", 20, "bold"))
eRecordArtistLabel.place(x=10, y=230)
eRecordArtistEntry = tk.Entry(oarWindow, bg="black", fg="red3", font=("times", 20), width=25,
                              textvariable=eRecordArtist)
eRecordArtistEntry.place(x=30, y=270)

eRecordYearLabel = tk.Label(oarWindow, text="Record Year", bg="black", fg="red3", font=("times", 20, "bold"))
eRecordYearLabel.place(x=10, y=330)
eRecordYearEntry = tk.Entry(oarWindow, bg="black", fg="red3", font=("times", 20), width=25,
                            textvariable=eRecordYear)
eRecordYearEntry.place(x=30, y=370)

eRecordGenreLabel = tk.Label(oarWindow, text="Record Genre", bg="black", fg="red3", font=("times", 20, "bold"))
eRecordGenreLabel.place(x=10, y=430)
eRecordGenreEntry = tk.Entry(oarWindow, bg="black", fg="red3", font=("times", 20), width=25,
                             textvariable=eRecordGenre)
eRecordGenreEntry.place(x=30, y=470)

eRecordStockLabel = tk.Label(oarWindow, text="Record Stock", bg="black", fg="red3", font=("times", 20, "bold"))
eRecordStockLabel.place(x=10, y=530)
eRecordStockEntry = tk.Entry(oarWindow, bg="black", fg="red3", font=("times", 20), width=25,
                             textvariable=eRecordStock)
eRecordStockEntry.place(x=30, y=570)

eRecordPriceLabel = tk.Label(oarWindow, text="Record Price", bg="black", fg="red3", font=("times", 20, "bold"))
eRecordPriceLabel.place(x=10, y=630)
eRecordPriceEntry = tk.Entry(oarWindow, bg="black", fg="red3", font=("times", 20), width=25,
                             textvariable=eRecordPrice)
eRecordPriceEntry.place(x=30, y=670)

recordAddButton = tk.Button(oarWindow, text="add album", bg="black", fg="red3", font=("times", 25),
                            command=addRecordOperation)
recordAddButton.place(x=200, y=800)

oarWindow.mainloop()
