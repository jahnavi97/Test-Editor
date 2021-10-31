import tkinter as tk #tk is a class in tkinter
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_application=tk.Tk() 
#tk is alias of tkinter 
# main_application is object
#  Tk is class in tkinter
main_application.geometry('1200x800')
main_application.title('Text Editor')

####################### main menu ###############################

main_menu = tk.Menu()


##---------------file------------------##
new_icon = tk.PhotoImage(file='icons/new.png')
open_icon = tk.PhotoImage(file='icons/open.png')
save_icon = tk.PhotoImage(file='icons/save.png')
save_as_icon = tk.PhotoImage(file='icons/save_as.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')

file = tk.Menu(main_menu, tearoff=False)




##--------------edit------------------##  
copy_icon = tk.PhotoImage(file='icons/copy.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
find_icon = tk.PhotoImage(file='icons/find.png')

edit = tk.Menu(main_menu, tearoff=False)


##-------------view---------------------## 
tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)


##-------------color theme--------------## 
light_default_icon = tk.PhotoImage(file='icons/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
dark_icon = tk.PhotoImage(file='icons/dark.png')
red_icon = tk.PhotoImage(file='icons/red.png')
monokai_icon = tk.PhotoImage(file='icons/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')

color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {  
    'Light Default ' : ('#000000', '#ffffff'),  
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
             }


#-----Adding file/edit/view/colortheme  to menu-----------------#
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

#----filedropdown-----#
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label='Save As', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q')

#----editdropdown-----# 
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C')
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V')
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X')
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X')
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F')

#----viewdropdown-----#
view.add_checkbutton(label='Tool Bar', image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label='Status Bar', image=status_bar_icon, compound=tk.LEFT)

count = 0 
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT)
    count += 1 




######################tool bar ##################################

######################text editor###############################

#######################status bar###############################

########################shortcut keys###########################
main_application.config(menu=main_menu)
main_application.mainloop()
