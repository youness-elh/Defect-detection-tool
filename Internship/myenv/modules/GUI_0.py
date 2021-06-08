# -*- coding: utf-8 -*-
"""
Created on Wed Jun 05 10:00:27 2019

@author: elh
"""

import tkinter as tk
from PIL import ImageTk,Image   

root = tk.Tk() 
root.title('DDT') 

'''menu'''
#create a frame widget for placing menu 
my_menu_bar = tk.Frame(root, relief='raised', bd=2) 
my_menu_bar.pack(fill=tk.X) 

# Create  Menu Widget 1 and Sub Menu 1 
my_menu_button = tk.Menubutton( 
        my_menu_bar, 
        text='Set threshold', 
        ) 
my_menu_button.pack(side=tk.LEFT) #text on the left

#menu widget 
my_menu = tk.Menu(my_menu_button, tearoff=0) 
my_menu_button['menu'] = my_menu 
my_menu.add('command', label='Recognition')  #Add Sub Menu 1 
my_menu.add('command', label='Labeling')  #Add Sub Menu 1 

'''inputs'''
my_frame1 = tk.Frame(root, relief='raised', bd=2)
my_frame1.pack(side=tk.LEFT) 
'''scale'''
#scale widget 
tk.Scale(my_frame1, from_=0.0, to=255.0, label='Reognition', 
         orient=tk.HORIZONTAL).pack() 
'''listbox'''

#add my_listbox widget to my_frame_2 
tk.Label(my_frame1, text='Labeling').pack() 
my_listbox = tk.Listbox(my_frame1, height=4) 
for line in ['Big defects', 'Medium defects', 'Small defects']: 
    my_listbox.insert(tk.END, line) 
    my_listbox.pack()

'''Image input''' 
tk.Label(my_frame1, text='UT Image').pack() 
img = Image.open('C:/Users/elh/Desktop/image.png')
dance_photo = ImageTk.PhotoImage(img) 
dance_photo_label = tk.Label(my_frame1, image=dance_photo) 
dance_photo_label.image = dance_photo 
dance_photo_label.pack(padx=10, pady=10) 

'''outputs'''
my_frame2 = tk.Frame(root).pack(side=tk.RIGHT)
'''ouput options'''
label_option = tk.Label(my_frame2, text="Output choice:") 
label_option.pack()
tk.Radiobutton(my_frame2, text='The scatter plots', value=1).pack() 
tk.Radiobutton(my_frame2, text='Extract oordinates', value=1).pack() 
tk.Radiobutton(my_frame2, text='Extraction of areas', value=1).pack() 
 

'''ouput button'''

my_label = tk.Label(my_frame2, text="Tresholding") 
my_button = tk.Button(my_frame2, text="OK") 
my_button.pack(side=tk.BOTTOM)
my_label.pack(side=tk.BOTTOM)  
  

root.mainloop() 