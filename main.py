##################### Imports ################ 
import os
import re
import sys
import tkinter.font as tkfont
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import showerror, showinfo, showwarning

import idlelib.colorizer as ic
import idlelib.percolator as ip
import yaml
from suggestion import Suggestion

from src.Minimap import TextPeer
################# App init ###################
app = Tk()
app.title("StormCode")
app.geometry("1100x650")
app.iconbitmap("img\icon.ico")

style=ttk.Style()
style.theme_use("alt")
style.configure("Vertical.TScrollbar", background="#3e3e3e", bordercolor="grey", arrowcolor="white")

scrollbar = ttk.Scrollbar(app, orient='vertical')
scrollbar.pack(side=RIGHT, fill=BOTH)

################## Splash Screen ##############
splash_label = Label(app,text="StormCode V0.1.0",font=16,foreground="black")
splash_label.pack()
def main(): 
    # destroy splash window
    splash_label.destroy()
app.after(2200,main)

################# Settings #####################
with open("data\settings.yml") as config:
    settings = yaml.safe_load(config)
    
Minimap = settings["settings"]["Minimap"]

Themefg = settings["settings"]["Theme"]["Foreground"]
Themebg = settings["settings"]["Theme"]["Background"]

Comment = settings["settings"]["Syntax"]["Comment"]
Keyword = settings["settings"]["Syntax"]["Keyword"]
Builtin = settings["settings"]["Syntax"]["Builtin"]
String = settings["settings"]["Syntax"]["String"]
Definition = settings["settings"]["Syntax"]["Definition"]

Font = settings["settings"]["Font_size"]["Font"]
Minifont = settings["settings"]["Font_size"]["Minimapfont"]

if Minimap == True:
    editor = Text(app,wrap=None,yscrollcommand=scrollbar.set)
    editor.pack(fill=BOTH,expand=1)
    editor.focus()
    
    editor.config(fg=Themefg,bg=Themebg,insertbackground='grey')
    editor.config(font=(f"Tahoma {Font}"))
    
    font = tkfont.Font(font=editor['font'])  # get font associated with Text widget
    tab_width = font.measure(' ' * 4)  # compute desired width of tabs
    editor.config(tabs=(tab_width,))
    
    minimap = TextPeer(editor, font=f"Tahoma {Minifont}", state="disabled",
                   background=Themebg, foreground="white")
    minimap.pack(side="right", fill="y")
    editor.pack(side="left", fill="both", expand=True)
elif Minimap == False:

############ Text Editor Code ################

    editor = Text(app,wrap=None,yscrollcommand=scrollbar.set)
    editor.pack(fill=BOTH,expand=1)
    editor.focus()
    editor.config(fg=Themefg,bg=Themebg,insertbackground='grey')
    editor.config(font=(f"Tahoma {Font}"))

    font = tkfont.Font(font=editor['font'])  # get font associated with Text widget
    tab_width = font.measure(' ' * 4)  # compute desired width of tabs
    editor.config(tabs=(tab_width,))

else:
    print("Minimap setting is wrong only inputs allowed are True / False\n")
    print(f"You said {Minimap} make sure its True or False(go to data\settings.yml to fix)")
    exit()

############ Menus ########################
menu = Menu(app,background="red", fg="white")
app.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
theme_menu = Menu(menu, tearoff=0)
other_menu = Menu(menu, tearoff=0)

############## Add cascades to Menu ############
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label ="Theme", menu=theme_menu)
menu.add_cascade(label="Other",menu=other_menu)


################ File options ############
# Open file func

def open_file(event=None):
    global code, file_path,open_path
    #code = editor.get(1.0, END)
    open_path = askopenfilename(filetypes=[(".*", "*")])
    file_path = open_path
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
        app.title("Editing " + open_path)
app.bind("<Control-o>", open_file)

# Save file func

def save_file(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        file_path =save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = editor.get(2.0, END)
        file.write(code) 
app.bind("<Control-s>", save_file)

# Save as file func

def save_as(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    save_path = asksaveasfilename(defaultextension = ".", filetypes=[("", "*")])
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
app.bind("<Control-S>", save_as)

def edit_config():
    open_path = "data\settings.yml"
    file_path = open_path
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
        app.title("Editing " + open_path)
        sys.stdout.flush() 
        os.execv()

def PPI():
    import src.PPI

############### Status bar ###################
"""
show_status_bar = BooleanVar()
show_status_bar.set(True)

def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False 
    else :
        status_bars.pack(side=BOTTOM)
        show_status_bar = True
        
view_menu.add_checkbutton(label = "Status Bar" , onvalue = True, offvalue = 0,variable = show_status_bar , command = hide_statusbar)
# create a label for status bar
status_bars = ttk.Label(app,text = f"https://github.com/Lunar-Code/Lunar-Code \tV1.1.0\t characters: 0 words: 0")
status_bars.pack(side = BOTTOM)

# function to display count and word characters
text_change = False
def change_word(event = None):
    global text_change
    if editor.edit_modified():
        text_change = True
        word = len(editor.get(1.0, "end-1c").split())
        chararcter = len(editor.get(1.0, "end-1c").replace(" ",""))
        status_bars.config(text = f"https://github.com/Lunar-Code/Lunar-Code \tV1.1.0\t characters: {chararcter} words: {word}")
    editor.edit_modified(False)
"""
##################### Run code , Close app and erase text(start new file) ###########################
def close(event=None):
    showwarning("Exit","Make sure you saved your work!")
    app.destroy()
app.bind("<Control-q>", close)

def running(event=None):
    global code    
    code = editor.get(1.0, END)
    showinfo("check terminal","Python file Ran in the terminal")
    exec(code)
app.bind("<Control-r>", running)
menu.add_command(label="Run",command=running)


def erase_text():
    editor.delete("1.0",END)
app.bind("<Control-N>",erase_text)

################ Auto completion #############
DATASET = "data\\autocomp.txt"
suggestion = Suggestion(editor, dataset=DATASET)

############### Auto indent #################
def autoindent(event):
    # the text widget that received the event
    widget = event.widget

    # get current line
    line = widget.get("insert linestart", "insert lineend")

    # compute the indentation of the current line
    match = re.match(r'^(\s+)', line)
    current_indent = len(match.group(0)) if match else 0

    # compute the new indentation
    new_indent = current_indent + 4

    # insert the character that triggered the event,
    # a newline, and then new indentation
    widget.insert("insert", event.char + "\n" + " "*new_indent)

    # return 'break' to prevent the default behavior
    return "break"

editor.bind(":", autoindent)

############### Help command ################
#TODO: Create help command 

################ syntax highlighting #########
cdg = ic.ColorDelegator()
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat().pattern, re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.tagdefs['MYGROUP'] = {'foreground': 'blue', 'background': 'transparent'}

cdg.tagdefs['COMMENT'] = {'foreground': Comment, 'background': 'transparent'}
cdg.tagdefs['KEYWORD'] = {'foreground': Keyword, 'background': 'transparent'}
cdg.tagdefs['BUILTIN'] = {'foreground': Builtin, 'background': 'transparent'}
cdg.tagdefs['STRING'] = {'foreground': String, 'background': 'transparent'}
cdg.tagdefs['DEFINITION'] = {'foreground': Definition, 'background': 'transparent'}
ip.Percolator(editor).insertfilter(cdg)

################ Themes :) ###################
def monokai():
    editor.config(fg="#F8F8F2",bg="#272822")
    minimap.config(fg="#F8F8F2",bg="#272822")
    
def light():
    editor.config(fg="black",bg="white")
    minimap.config(fg="black",bg="white")
    
def dark():
    editor.config(fg="white",bg="black")
    minimap.config(fg="white",bg="black")
    
def light_blue():
    editor.config(fg="white",bg="#3F425D")
    minimap.config(fg="white",bg="#3F425D")
    
def off_white():
    editor.config(fg="black",bg="#D6E5E4")
    minimap.config(fg="black",bg="#D6E5E4")

################ Functions to menus #####################

theme_menu.add_command(label="Monkai(default)",command=monokai)
theme_menu.add_command(label="Light",command=light)
theme_menu.add_command(label="Dark",command=dark)
theme_menu.add_command(label="Light Blue",command=light_blue)
theme_menu.add_command(label="Off white",command=off_white)

file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save as",command=save_as)
file_menu.add_command(label="New",command=erase_text)
file_menu.add_command(label="Quit",command=close)

other_menu.add_command(label="Edit config file",command=edit_config)
other_menu.add_command(label="Open PPI",command=PPI) 

############# Start App ########################

if __name__ == "__main__":
    scrollbar.config(command=editor.yview)
    config.close()
    app.mainloop()