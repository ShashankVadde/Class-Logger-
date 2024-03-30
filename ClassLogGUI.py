import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import os

# main window
root = tk.Tk()
root.title("Event Logger") 
root.geometry("400x200")
logFile = "classLogs.txt"

# Create tabs
tabControl = ttk.Notebook(root)
tabLog = ttk.Frame(tabControl)
tabView = ttk.Frame(tabControl)
tabDelete = ttk.Frame(tabControl)
tabControl.add(tabLog, text = 'Log Event')
tabControl.add(tabView, text = 'View Event')
tabControl.add(tabDelete, text = 'Delete Event')
tabControl.pack(expand = 1, fill = 'both')

viewText = tk.Text(tabView, wrap="word", state=tk.DISABLED)
viewText.pack(padx = 10, pady = 5)

def logClass():
    className = classNameEntry.get()
    startTime = startTimeEntry.get()
    endTime = endTimeEntry.get()
    date = dateEntry.get_date()

    if not className or not startTime or not endTime or not date:
        messagebox.showerror("Error", "Please fill in all the fields.")
        return
    # elif not startTime:
    #     messagebox.showerror("Error", "Please fill in all the fields.")
    #     return
    # elif not endTime:
    #     messagebox.showerror("Error", "Please fill in all the fields.")
    #     return
    # elif not date:
    #     messagebox.showerror("Error", "Please fill in all the fields.")
    #     return
    
    formattedDate = date.strftime("%Y-%m-%d")
    
    with open(logFile, 'a') as file:
        file.write(f"{className}, {date}, {startTime}, {endTime}\n")
        
    print(f"Class logged: {className}, Date: {date}, Start Time: {startTime}, End Time: {endTime}")
    
    viewClasses()
    
def viewClasses():
    viewText.config(state=tk.NORMAL)
    viewText.delete('1.0', tk.END) 
    
    with open(logFile, 'r') as file:
        for line in file:
            viewText.insert(tk.END, line)
        viewText.config(state=tk.DISABLED) 
        
viewClasses()

def deleteAll():
    warning = messagebox.askyesno("Delete All Data", "Are you sure you want to delete all data? \n Deleted data cannot be retrieved.")
    if warning:
        if os.path.exists(logFile):
            with open(logFile, 'w') as file:
                file.truncate(0)
            viewText.delete('1.0', tk.END)
    if os.path.exists(logFile):
        with open(logFile, 'w') as file:
            file.truncate(0)
        viewText.delete('1.0', tk.END)
    


# Log Class
logLabel = tk.Label(tabLog, text="Log a Class:")
logLabel.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "w")

classNameEntry = tk.Entry(tabLog)
classNameEntry.grid(row = 0, column = 1, padx = 10, pady = 5)

dateLabel = tk.Label(tabLog, text="Date:")
dateLabel.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = "w")
dateEntry = DateEntry(tabLog)
dateEntry.grid(row = 1, column = 1, padx = 10, pady = 5)

startTimeLabel = tk.Label(tabLog, text="Start Time:")
startTimeLabel.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = "w")
startTimeEntry = tk.Entry(tabLog)
startTimeEntry.grid(row = 2, column = 1, padx = 10, pady = 5)

endTimeLabel = tk.Label(tabLog, text="End Time:")
endTimeLabel.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = "w")
endTimeEntry = tk.Entry(tabLog)
endTimeEntry.grid(row = 3, column = 1, padx = 10, pady = 5) 

logButton = tk.Button(tabLog, text="Log Class", command = logClass)
logButton.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 5)

deleteAllButton = tk.Button(tabDelete, text = "Delete All", command = deleteAll)
deleteAllButton.pack(padx = 10, pady = 5)

root.mainloop()
