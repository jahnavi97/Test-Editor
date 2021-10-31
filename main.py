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

#######################status bar###############################

########################shortcut keys###########################

main_application.mainloop()
