import tkinter as tk
from tkinter import filedialog as tkf
from tkinter import messagebox as tkmb

import os

def open_file():
    global filename
    if text.edit_modified():
        save = tkmb.askyesnocancel("notepad", "新しくファイルを開く前に, 今の内容を保存しますか?")
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
        root.title("{} - Notepad".format(os.path.basename(filename)))  # Display only the filename in the title.

def save_file():
    global filename
    if not filename:
        filename = tkf.asksaveasfilename(
            title="Save the txt file.",
            filetypes=[('txt files', '.txt')],
            initialdir="./",  # Your directory.
            defaultextension="txt",
        )
    if filename:
        with open(filename, 'w') as f:
            f.write(text.get("1.0", tk.END))  # Writes input to a text file.
        root.title("{} - Notepad".format(os.path.basename(filename)))  # Display only the filename in the title.
        print(filename)

def new_file():
    global filename
    if text.edit_modified():
        save = tkmb.askyesnocancel("notepad", "新しいファイルを作成する前に, 今の内容を保存しますか?")
        if save:
            save_file()
        elif save is None:
            return
    filename = None
    text.delete('1.0', tk.END)
    root.title("Untitled - Notepad")  # Update the title of the window
    print("New file created.")

def on_closing():
    if text.edit_modified():  # Check if text has been modified.
        save = tk.messagebox.askyesnocancel("notepad", "このメモ帳を閉じる前に, 内容を保存しますか?")
        if save:
            save_file()
        elif save is None:
            return
    root.destroy()

def resize_text(event):
    # 常時eventを取得しているから重い模様. -> ウィンドウのサイズを可変にしたときに現象が見られた.
    # text.place(x=0, y=0, width=event.width, height=event.height)  
    
    # ウィンドウのリサイズ時にも呼び出しを行わないように, 処理を変更
    if event.widget is text:
        if text.edit_modified():
            text.edit_modified(False)
        text.pack(fill="both", expand=True)

root = tk.Tk()
root.title("Untitled - Notepad")
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
root.bind("<Control-n>", lambda event: new_file())  # lambdaで関数を直接渡して, 別の関数を定義して渡す必要をなくしている.
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-q>", lambda event: on_closing())

'''
# Text edit.
text = tk.Text(root)
# Add a binding to resize the text box when the window is resized.
text.bind("<Configure>", resize_text)
text.place(x=0, y=0, relwidth=1, relheight=1)
'''

# テキストウィジェットを中央に配置するフレームを作成する
text_frame = tk.Frame(root)
text_frame.pack(fill="both", expand=True)

# Textウィジェットをフレームに配置する
text = tk.Text(text_frame)
text.pack(fill="both", expand=True)

# テキストウィジェットのサイズを変更するためのバインディングを追加する
text.bind("<Configure>", resize_text)
root.mainloop()
