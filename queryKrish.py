import mariadb
import tkinter as tk
from tkinter import messagebox

# Connect to the database
conn = mariadb.connect(
    user="root",
    password="root",
    host="127.0.0.1",
    database="recordStore"
)
currSelect = conn.cursor()


def selectOperation():
    # Retrieve user inputs
    selectOP = condition1.get().strip()
    fromOP = condition2.get().strip()
    whereOP = condition3.get().strip()

    if not selectOP or not fromOP:
        messagebox.showerror("Input Error", "SELECT and FROM fields cannot be empty.")
        return

    # Build query string dynamically
    query = f"SELECT {selectOP} FROM {fromOP}"
    if whereOP:
        query += f" WHERE {whereOP}"

    try:
        # Execute query
        currSelect.execute(query)
        results = currSelect.fetchall()

        # Display results
        output_text.delete("1.0", tk.END)  # Clear previous output
        if results:
            for row in results:
                output_text.insert(tk.END, f"{row}\n")
        else:
            output_text.insert(tk.END, "No results found.")
    except mariadb.Error as e:
        messagebox.showerror("Database Error", f"Error executing query: {e}")


# GUI setup
osrWindow = tk.Tk()
osrWindow.title("Search for Records")
osrWindow.geometry('1024x768')
osrWindow.configure(bg='black')

# Labels and input fields
osrLabel = tk.Label(
    osrWindow,
    text="Enter SELECT columns, FROM table, and optional WHERE condition:",
    bg="black",
    fg="red3",
    font=("times", 20, "bold")
)
osrLabel.pack(pady=10)

condition1 = tk.StringVar()
condition2 = tk.StringVar()
condition3 = tk.StringVar()

osrEntry1 = tk.Entry(osrWindow, bg="black", fg="red3", font=("times", 20), width=50, textvariable=condition1)
osrEntry1.pack(pady=10)

osrEntry2 = tk.Entry(osrWindow, bg="black", fg="red3", font=("times", 20), width=50, textvariable=condition2)
osrEntry2.pack(pady=20, padx=20)

osrEntry3 = tk.Entry(osrWindow, bg="black", fg="red3", font=("times", 20), width=50, textvariable=condition3)
osrEntry3.pack(pady=20, padx=30)

# Execute query button
osrButton = tk.Button(
    osrWindow,
    text="Execute Query",
    bg="black",
    fg="red3",
    font=("times", 25),
    command=selectOperation
)
osrButton.pack(pady=30)

# Output area
output_text = tk.Text(osrWindow, height=15, width=80, bg="black", fg="red3", font=("times", 14))
output_text.pack(pady=20)

# Run the GUI loop
osrWindow.mainloop()

# Close the connection when the GUI is closed
currSelect.close()
conn.close()
