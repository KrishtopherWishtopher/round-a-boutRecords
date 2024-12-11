import mariadb
import tkinter as tk
from tkinter import messagebox

conn = mariadb.connect(
    user="root",
    password="root",
    host="127.0.0.1",
    database="recordStore")

# made a cursor to navigate the database
currDelete = conn.cursor()


def deleteRecordOperation():
    dName = dRecordName.get()
    currDelete.execute("DELETE FROM records WHERE recordName = ?", (dName,))
    conn.commit()
    messagebox.showinfo("Record Deleted!")


odrWindow = tk.Tk()
odrWindow.title("Delete a Record!")
odrWindow.geometry('1024x768')
odrWindow.configure(bg='black')
odrLabel = tk.Label(odrWindow, text="Enter a records name and we will delete it!!", bg="black", fg="red3", font=("times", 32, "bold"))
odrLabel.pack(pady=10)
dRecordName = tk.StringVar()
odrEntry = tk.Entry(odrWindow, bg="black", fg="red3", font=("times", 20), width=25, textvariable=dRecordName)
odrEntry.pack(pady=50)



recordDeleteButton = tk.Button(odrWindow, text="Delete album", bg="black", fg="red3", font=("times", 25), command=deleteRecordOperation)
recordDeleteButton.place(x=200, y=800)

odrWindow.mainloop()
