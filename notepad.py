import tkinter as tk
from tkinter import filedialog as tkf

def open_file():
    # to do
    filename = tkf.askopenfilename(
        title = "open the txt file.",
        filetypes = [('txt files', '.txt')],
        initialdir = "./", # Your directory.
    )
    # with open(filename, 'r') as f:
    #     f.readline()
    # print(filename)
    

def save_file():
    # to do
    filename = tkf.asksaveasfilename(
        title = "save the txt file.",
        filetypes = [('txt files', '.txt')],
        initialdir = "./", # Your directory.
        defaultextension = "txt",
    )
    with open(filename, 'w') as f:
        f.write(text.get("1.0", tk.END)) # Writes input to a text file.
    print(filename)

root = tk.Tk()
root.title("Notepad")

# Create a menubar.
menu_bar = tk.Menu(root)
root.config(menu = menu_bar)

# Create a filebar.
file_menu = tk.Menu(menu_bar, tearoff = 0) # tearoff(メニューの切り取り可否) -> filebarを別枠に表示させない.
menu_bar.add_cascade(label = "File", menu = file_menu)

# Crate commands in the file bar.
file_menu.add_command(label = "open", command = open_file, accelerator = "Ctrl+O")
file_menu.add_command(label = "save", command = save_file, accelerator = "Ctrl+s")
file_menu.add_separator() # Separator Line.
file_menu.add_command(label = "exit", command = root.quit, accelerator = "Ctrl+q")

# file_menu.bind_all("<Control-o>", open_file)
# file_menu.bind_all("<Control-s>", save_file)

# Text edit.
text = tk.Text(root)
text.pack()
root.mainloop()