from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk, Image, ImageDraw
import os

#Tkinter frame
root= Tk()
#Frame geometry
root.state('zoomed')
root.resizable(width=True, height=True)
root.title("NEUROPIXEL GUI")

    
    
#Importing function for image file
def open_img():
    global image_list
    global folder_name
    folder_name=filedialog.askdirectory()
    image_list=os.listdir(folder_name)
    render_img()

    
#Image rendering function
def render_img():
    global img
    global photo_img
    global panel
    global str_id
    global num
    global filename
    num=0
    str_id=str(num).zfill(6)
    if len(image_list)==0:
        return 
    filename=image_list.pop(0)
    filename=folder_name+'/'+filename
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    photo_img_temp = ImageTk.getimage(img)
    photo_img=photo_img_temp
    
    img_sub = img._PhotoImage__photo.subsample(10)
    panel = Label(root, image=img_sub)
    panel.image = img_sub
    panel.place(relx=1.0, rely=0.0, anchor='ne')

    


#Exporting function for image file
def save_img():
    filename = filedialog.asksaveasfile(mode='wb', title='save', filetype=(('all files','*.*'),('image files','*.png')), defaultextension='.png', initialfile=str_id+'_'+str1+'_'+str2)
    if not filename:
        return
    photo_img.save(filename)
    panel.destroy()
    render_img()
    



#Dropdown menu item to id function
def select_option1(event):
    global str1
    if variable1.get()=='Model':
        olabel = Label(root)
        olabel.pack()
        str1='0'
    else:
        olabel = Label(root)
        olabel.pack()
        str1='1'
    
    
def select_option2(event):
    global str2
    if variable2.get()=='Front view':
        olabel = Label(root)
        olabel.pack()
        str2='0'
    elif variable2.get()=='Back view':
        olabel = Label(root)
        olabel.pack()
        str2='1'
    elif variable2.get()=='60 Left':
        olabel = Label(root)
        olabel.pack()
        str2='2'
    elif variable2.get()=='60 Right':
        olabel = Label(root)
        olabel.pack()
        str2='3'
    elif variable2.get()=='120 Left':
        olabel = Label(root)
        olabel.pack()
        str2='4'
    else:
        olabel = Label(root)
        olabel.pack()
        str2='5'


#Function for opening new file
def new_file():
    root.destroy()
    os.popen("neuropixel_gui.ipynb")

        
#Create a label and a Button to Open the dialog
Label(root, text="NEUROPIXEL GUI", font=('Caveat 15 bold')).pack(pady=20)
button_imp= ttk.Button(root, text="Select Folder", command= open_img)
button_imp.pack(side = TOP, pady = 20)


#Creating a main menu
main_menu=Menu(root)
root.config(menu=main_menu)

filemenu=Menu(main_menu)
main_menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New', command=new_file)
filemenu.add_command(label='Exit', command=root.destroy)

helpmenu=Menu(main_menu)
main_menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')



#Creating dropdown list
OPTIONS1=['Model','Mannequin']
variable1 = StringVar(root)
variable1.set(OPTIONS1[0])
o1 = OptionMenu(root, variable1, *OPTIONS1, command=select_option1)
o1.pack()

OPTIONS2=['Front view','Back view','60 Left','60 Right','120 Left','120 Right']
variable2 = StringVar(root)
variable2.set(OPTIONS2[0])
o2 = OptionMenu(root, variable2, *OPTIONS2, command=select_option2)
o2.pack()



#Exporting the image file
button_exp = ttk.Button(root, text = 'Save', command =save_img)
button_exp.pack(side = TOP, pady = 20)

root.mainloop()