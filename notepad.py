import tkinter as tk
from tkinter import filedialog as tkf
from tkinter import messagebox as tkmb

def open_file():
    global filename
    if text.edit_modified():
        save = tkmb.askyesnocancel("Save Changes", "Do you want to save changes before opening a new file?")
        if save:
            save_file()
        elif save is None:
            return
    filename = tkf.askopenfilename(
        title="Open the txt file.",
        filetypes=[('txt files', '.txt')],
        # initialdir="./",  # Your directory.
    )
    if filename:
        with open(filename, 'r', encoding='utf-8') as f:
            text.delete('1.0', tk.END)  # Clear current text.
            text.insert('1.0', f.read())
        print(filename)

def save_file():
    global filename
    if not filename:
        filename = tkf.asksaveasfilename(
            title="Save the txt file.",
            filetypes=[('txt files', '.txt')],
            initialdir="./",  # Your directory.
            defaultextension="txt",
        )
        if not filename:
            return
    with open(filename, 'w') as f:
        f.write(text.get("1.0", tk.END))  # Writes input to a text file.
    print(filename)
    text.edit_modified(False)

def new_file():
    global filename
    if text.edit_modified():
        save = tkmb.askyesnocancel("Save Changes", "Do you want to save changes before creating a new file?")
        if save:
            save_file()
        elif save is None:
            return
    filename = None
    text.delete('1.0', tk.END)
    print("New file created.")

def on_closing():
    if text.edit_modified():  # Check if text has been modified.
        save = tkmb.askyesnocancel("Save Changes", "Do you want to save changes before quitting?")
        if save:
            save_file()
        elif save is None:
            return
    root.destroy()

root = tk.Tk()
root.title("Notepad")
root.protocol("WM_DELETE_WINDOW", on_closing)  # Add event handler for window close button.

# Create a menubar.
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a filebar.
file_menu = tk.Menu(menu_bar, tearoff=0)  # tearoff(メニューの切り取り可否) -> filebarを別枠に表示させない.
menu_bar.add_cascade(label="File", menu=file_menu)

# Crate commands in the file bar.
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()  # Separator Line.
file_menu.add_command(label="Exit", command=root.quit, accelerator="Ctrl+Q")

# Add keybindings to commands in the file bar.
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-q>", lambda event: on_closing())

# Text edit.
filename = None     # ファイルの読み込みと保存両方の機能をつけるのに必要.
text = tk.Text(root)
text.pack()
root.mainloop()
