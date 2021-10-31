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
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

file = tk.Menu(main_menu, tearoff=False)




##--------------edit------------------##  
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_menu, tearoff=False)


##-------------view---------------------## 
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)


##-------------color theme--------------## 
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

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

tool_bar = ttk.Label(main_application) # label will display the box where you can place text or images. The text displayed by this widget can be updated at any time you want.
tool_bar.pack(side=tk.TOP , fill=tk.X) #pack() method declares the position of widgets in relation to each other.

#font box
font_tuple = tk.font.families() #It will give all the font families present in the tk.
font_family = tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly') #Combobox is the drop-down list.
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5) #grid widget is split into a number of rows and columns

#size box
size_var = tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly') #Combobox is for drop-down list.
font_size['values']=tuple(range(8,80,2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5) #grid widget is used to  split into a number of rows and columns

## bold button 
bold_icon = tk.PhotoImage(file='icons2/bold.png') # photoimage is Used to add the images
bold_btn = ttk.Button(tool_bar, image=bold_icon) #button is used to add buttons
bold_btn.grid(row=0, column=2, padx=5) #grid widget is split into a number of rows and columns

## italic button 
italic_icon = tk.PhotoImage(file='icons2/italic.png') # photoimage is Used to add the images
italic_btn = ttk.Button(tool_bar, image=italic_icon)#button is used to add buttons
italic_btn.grid(row=0, column=3, padx=5) #grid widget is split into a number of rows and columns

## underline button 
underline_icon = tk.PhotoImage(file='icons2/underline.png') # photoimage is Used to add the images
underline_btn = ttk.Button(tool_bar, image = underline_icon) #button is used to add buttons
underline_btn.grid(row = 0, column=4, padx=5) #grid widget is split into a number of rows and columns

## font color button 
font_color_icon = tk.PhotoImage(file='icons2/font_color.png') # photoimage is Used to add the images
font_color_btn = ttk.Button(tool_bar, image=font_color_icon) #button is used to add buttons
font_color_btn.grid(row=0, column=5,padx=5) #grid widget is split into a number of rows and columns

## align left 
align_left_icon = tk.PhotoImage(file='icons2/align_left.png') # photoimage is Used to add the images
align_left_btn = ttk.Button(tool_bar, image=align_left_icon) #button is used to add buttons
align_left_btn.grid(row=0, column=6, padx=5)#grid widget is split into a number of rows and columns

## align center 
align_center_icon = tk.PhotoImage(file='icons2/align_center.png') # photoimage is Used to add the images
align_center_btn = ttk.Button(tool_bar, image=align_center_icon) #button is used to add buttons
align_center_btn.grid(row=0, column=7, padx=5) #grid widget is split into a number of rows and columns

## align right 
align_right_icon = tk.PhotoImage(file='icons2/align_right.png') # photoimage is Used to add the images
align_right_btn = ttk.Button(tool_bar, image=align_right_icon) #button is used to add buttons
align_right_btn.grid(row=0, column=8, padx=5) #grid widget is split into a number of rows and columns

######################End Tool Bar##############################

######################text editor###############################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and font size functionality
current_font_family = 'Arial'
current_font_size = 12

def change_font(main_application):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(main_application):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

########### button functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)


# italic functionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))

italic_btn.configure(command=change_italic)

# underline functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['slant'] == '1':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)


## font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)

## align functionality
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

# center
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

# right
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)






text_editor.configure(font=('Arial', 12))   
######################## end text editor ####################

#######################status bar###############################

########################shortcut keys###########################

main_application.config(menu=main_menu)
main_application.mainloop()
