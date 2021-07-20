from tkinter import *
from tkinter import filedialog

def browseFile():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a file",
                                          filetypes=(("Text files", "*.txt*"),
                                                    ("all files", "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

window = Tk()

window.title('File Explorer')
window.geometry("700x500")
window.config(background="white")

label_file_explorer = Label(window,
                            text="File Explorer using Tkinter",
                            width=100, height=4, fg="blue")

button_explore = Button(window,
                        text="Browse Files",
                        command=browseFile)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing the widgets at respective positions
# in a table like structure by specifying rows and columns
label_file_explorer.grid(column=1, row=1)
button_explore.grid(column=1, row=2)
button_exit.grid(column=1, row=3)

window.mainloop()