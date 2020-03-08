import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import urllib.request

baseFolder = "."

def selectFolder():
    global baseFolder
    baseFolder = filedialog.askdirectory(parent=root,initialdir=baseFolder,title='Please select a directory')
    print(baseFolder)

def downloadChar():
    global baseFolder
    try:
        urllib.request.urlretrieve("http://s3.wasabisys.com/webao/base/characters/" + char_name.get().lower() + "/char.ini", baseFolder + "/characters/" + char_name.get().lower() + "/char.ini")
    except ValueError:
        pass

root = tk.Tk()
root.title("Character downloader")

main = tk.Frame(root)
main.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

char_name = tk.StringVar()

tk.Label(main, text="Character name:").grid(column=1, row=1, sticky=tk.W)
tk.Checkbutton(main, text="Overwrite files").grid(column=1, row=2, sticky=tk.W)
ttk.Progressbar(main).grid(column=1, row=3, sticky=tk.S)

name_entry = tk.Entry(main, width=15, textvariable=char_name)
name_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
tk.Button(main, text="Download", command=downloadChar).grid(column=2, row=2, sticky=tk.E)
tk.Button(main, text="Base Folder...", command=selectFolder).grid(column=2, row=3, sticky=tk.E)

for child in main.winfo_children(): child.grid_configure(padx=5, pady=5)

name_entry.focus()
root.bind('<Return>', downloadChar)

root.mainloop()