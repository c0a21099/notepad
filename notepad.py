import tkinter as tk
from tkinter import filedialog as tkf

filename = None
root = tk.Tk()
root.title("Untitled - Notepad")

def open_file():
    global filename
    filename = tkf.askopenfilename(
        title="Open the txt file.",
        filetypes=[('txt files', '.txt')],
        # initialdir="./",  # Your directory.
    )
    if filename:
        with open(filename, 'r', encoding='utf-8') as f:
            text.delete('1.0', tk.END)  # Clear current text.
            text.insert('1.0', f.read())
        root.title(f"{filename} - Notepad")

def save_file():
    global filename
    if filename is None:
        filename = tkf.asksaveasfilename(
            title="Save the txt file.",
            filetypes=[('txt files', '.txt')],
            initialdir="./",  # Your directory.
            defaultextension="txt",
        )
        if filename:
            with open(filename, 'w') as f:
                f.write(text.get("1.0", tk.END))  # Writes input to a text file.
            root.title(f"{filename} - Notepad")
    else:
        with open(filename, 'w') as f:
            f.write(text.get("1.0", tk.END))  # Writes input to a text file.
        root.title(f"{filename} - Notepad")

def on_closing():
    global filename
    if text.edit_modified():  # Check if text has been modified.
        save = tk.messagebox.askyesnocancel("Save Changes", "Do you want to save changes before quitting?")
        if save:
            save_file()
        elif save is None:
            return
    filename = None
    root.title("Untitled - Notepad")
    root.destroy()

# Create a menubar.
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a filebar.
file_menu = tk.Menu(menu_bar, tearoff=0)  # tearoff(メニューの切り取り可否) -> filebarを別枠に表示させない.
menu_bar.add_cascade(label="File", menu=file_menu)

# Crate commands in the file bar.
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()  # Separator Line.
file_menu.add_command(label="Exit", command=root.quit, accelerator="Ctrl+Q")

# Add keybindings to commands in the file bar.
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-q>", lambda event: on_closing())

# Text edit.
text = tk.Text(root)
text.pack()

root.mainloop()
