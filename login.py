import mariadb
import tkinter as tk
import subprocess


def updateStock():
    subprocess.Popen(['python', 'updateStock.py'])
def runQueryKrish():
    subprocess.Popen(['python', 'queryKrish.py'])
def runAddKrish():
    subprocess.Popen(['python', 'addKrish.py'])
def runDeleteKrish():
    subprocess.Popen(['python', 'deleteKrish.py'])


# Once the username and password are correct and the "admin" button is clicked the admins panel pops up
def open_admin_window():
    admin_window = tk.Tk()
    admin_window.title("Admin Panel - Round-A-Bout-Records")
    admin_window.geometry('1024x768')
    admin_window.configure(bg='black')

    # Add your admin window widgets here
    label = tk.Label(admin_window, text="ADMIN PANEL", bg="black", fg="red3", font=("times", 32, "bold"))
    label.pack(pady=10)

    # Add Record button
    addRecordButton = tk.Button(admin_window, text="Add Record", bg="black", fg="red3", font=("times", 25),
                                command=runAddKrish)
    addRecordButton.pack(pady=30, padx=100)

    # Delete record button
    deleteRecordButton = tk.Button(admin_window, text="Delete Record", bg="black", fg="red3", font=("times", 25), command=runDeleteKrish)
    deleteRecordButton.pack(pady=50, padx=100)

    # Search or query
    queryButton = tk.Button(admin_window, text="Select in tables", bg="black", fg="red3", font=("times", 25), command=runQueryKrish)
    queryButton.pack(pady=70, padx=100)

    # Update record
    updateButton = tk.Button(admin_window, text="Update Record", bg="black", fg="red3", font=("times", 25), command=updateStock)
    updateButton.pack(pady=90, padx=100)

    admin_window.mainloop()


# once the username and password is right and the user button is clicked the user panel pops up
def open_user_window():
    user_window = tk.Tk()
    user_window.title("User Panel - Round-A-Bout-Records")
    user_window.geometry('1024x768')
    user_window.configure(bg='black')

    # Store checkbox variables in a dictionary
    checkbox_vars = {}

    # Create frame for the table
    table_frame = tk.Frame(user_window, bg='black')
    table_frame.pack(pady=20)

    # Create table headers
    headers = ['Select', 'Record Name', 'Artist', 'Price', 'Genre', 'Stock']
    for col, header in enumerate(headers):
        label = tk.Label(table_frame, text=header, bg='black', fg='red3', font=("times", 16, "bold"))
        label.grid(row=0, column=col, padx=10, pady=5)

    # Fetch data from database
    curr.execute("SELECT recordName, recordArtist, recordPrice, recordGenre, recordStock FROM records WHERE "
                 "recordStock > 0")
    records = curr.fetchall()

    # Create table rows with checkboxes
    for row, record in enumerate(records, start=1):
        # Checkbox
        checkbox_vars[row] = tk.BooleanVar()
        checkbox = tk.Checkbutton(table_frame, bg='black', variable=checkbox_vars[row])
        checkbox.grid(row=row, column=0, padx=10, pady=5)

        # Record data
        for col, value in enumerate(record, start=1):
            label = tk.Label(table_frame, text=str(value), bg='black', fg='red3', font=("times", 14))
            label.grid(row=row, column=col, padx=10, pady=5)

    # once order is finalized you get a reciept
    def finalize_order():
        total_price = 0
        order_items = []

        # Check which items were selected
        for row, var in checkbox_vars.items():
            if var.get():  # If checkbox is checked
                # Get the record data
                record = records[row - 1]
                order_items.append(record)
                total_price += record[2]  # Add price to total

                # Update stock in database
                curr.execute("""
                    UPDATE records 
                    SET recordStock = recordStock - 1 
                    WHERE recordName = ?""",
                             (record[0],))
                conn.commit()

        # Create order review window
        review_window = tk.Toplevel(user_window)
        review_window.title("Order Review")
        review_window.geometry('400x600')
        review_window.configure(bg='black')

        # Display order items
        tk.Label(review_window, text="Your Order:", bg='black', fg='red3',
                 font=("times", 20, "bold")).pack(pady=10)

        for item in order_items:
            tk.Label(review_window,
                     text=f"{item[0]} by {item[1]} - ${item[2]}",
                     bg='black', fg='red3',
                     font=("times", 14)).pack(pady=5)

        tk.Label(review_window,
                 text=f"\nTotal: ${total_price:.2f}",
                 bg='black', fg='red3',
                 font=("times", 16, "bold")).pack(pady=20)

    # Add Finalize Order button
    finalize_button = tk.Button(user_window,
                                text="Finalize Order",
                                bg="black", fg="red3",
                                font=("times", 20),
                                command=finalize_order)
    finalize_button.pack(pady=20)

    user_window.mainloop()


# this checks to see if the username and password are right
def userloginisclicked():
    global dataFromDB1
    global dataFromDB2
    global dataFromDB3

    username = stringOne.get()
    password = stringTwo.get()

    curr.execute("SELECT userName, userPassword FROM users WHERE userName = ?", (username,))
    dataFromDB1 = curr.fetchone()

    curr.execute("SELECT userPassword FROM users WHERE userName = ?", (username,))
    dataFromDB2 = curr.fetchone()

    if dataFromDB1[0] == username and dataFromDB2[0] == password:
        window.destroy()
        open_user_window()
    else:
        print(f"Error")


# this checks and sees if the admins name and password are correct
def adminloginisclicked():
    global dataFromDB11
    global dataFromDB22
    global dataFromDB33

    adname = stringOne.get()
    adpass = stringTwo.get()

    curr.execute("SELECT adminName FROM admins WHERE adminName = ?", (adname,))
    dataFromDB11 = curr.fetchone()

    curr.execute("SELECT adminPassword FROM admins WHERE adminName = ?", (adname,))
    dataFromDB22 = curr.fetchone()

    if dataFromDB11[0] == adname and dataFromDB22[0] == adpass:
        window.destroy()
        open_admin_window()
    else:
        print(f"Error")


# the window
window = tk.Tk()
window.title("Round-A-Bout-Records!")
window.geometry('1024x768')
window.configure(bg='black')

# Variables that get text from textbox
stringOne = tk.StringVar()
stringTwo = tk.StringVar()

global eRecordID
global eRecordName
global eRecordArtist
global eRecordYear
global eRecordGenre
global eRecordStock
global eRecordPrice

# Connection to my Mariadb
conn = mariadb.connect(
    user="root",
    password="root",
    host="127.0.0.1",
    database="recordStore")

# made a cursor to navigate the database
curr = conn.cursor()

# Global variables
whereAreWe = 0
dataFromDB1 = None
dataFromDB2 = None
dataFromDB3 = None
dataFromDB11 = None
dataFromDB22 = None
dataFromDB33 = None



# the giant label at the top
label = tk.Label(window, text="WElCOME TO ROUND-A-BOUT-RECORDS", bg="black", fg="red3", font=("times", 32, "bold"))
label.pack(pady=10)

# usernameField
userNameLabel = tk.Label(window, text="U", bg="black", fg="red3", font=("times", 28))
userNameLabel.place(x=50, y=200)
userNameEntry = tk.Entry(window, bg="black", fg="red3", font=("times", 20), width=25, textvariable=stringOne)
userNameEntry.place(x=150, y=200)

# password Field
passwordLabel = tk.Label(window, text="P", bg="black", fg="red3", font=("times", 28))
passwordLabel.place(x=50, y=400)
passwordEntry = tk.Entry(window, show="*", bg="black", fg="red3", font=("times", 20), width=25, textvariable=stringTwo)
passwordEntry.place(x=150, y=400)

# users login button
userLoginButton = tk.Button(window, text="user", bg="black", fg="red3", font=("times", 25), command=userloginisclicked)
userLoginButton.place(x=500, y=600)

# admins login button
adminLoginButton = tk.Button(window, text="admin", bg="black", fg="red3", font=("times", 25),
                             command=adminloginisclicked)
adminLoginButton.place(x=500, y=800)

# picture
mayhemImage = tk.PhotoImage(file="proj/mayhem.jpeg")
image_label = tk.Label(window, image=mayhemImage)
image_label.place(x=1000, y=150)

window.mainloop()
