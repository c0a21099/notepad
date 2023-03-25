import tkinter as tk
from tkinter import filedialog as tkf

def open_file():
    # to do
    filename = tkf.askopenfilename(
        title = "open the txt file.",
        filetypes = [('txt files', '*.txt')],
        initialdir = "./", # Your directory.
    )
    print(filename)
    

def save_file():
    pass
    # to do

root = tk.Tk()
root.title("Notepad")

# Create a menubar.
menu_bar = tk.Menu(root)
root.config(menu = menu_bar)

# Create a filebar.
file_menu = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file_menu)

# Crate commands in the file bar.
file_menu.add_command(label = "open", command = open_file)
file_menu.add_command(label = "save", command = save_file)
file_menu.add_command(label = "exit", command = root.quit)

# Text edit.
text = tk.Text(root)
text.pack()
root.mainloop()