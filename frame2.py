from tkinter import *
import os

######################## Basic Structure
frame2=Tk()
frame2.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(frame2.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(frame2.winfo_screenheight()/2 - windowHeight/2)
frame2.geometry("+{}+{}".format(position_x, position_y))
frame2.title('MENU')
########################

######################## Functions
def f1():
	os.system('python load_clean_data.py')
def f2():
	os.system('python frame3.py')

########################

######################## Images
image1 = PhotoImage(file = 'bg2.gif')
background = Label(frame2, image=image1)
background.place(x=0, y=0)
#background.image = image1
########################

######################## Text Box
text=Text(frame2, height=1, width=16, bg='#252525', fg='red', font=('',34), bd=-2)
text.insert(5.0, "Available Functions")
text.config(state='disabled')
text.place(x=310, y=70)
########################

######################## Buttons
back_button = Button(frame2, text = 'BACK', command = frame2.destroy, font=('',36), bd=-2, fg='red', bg='#252525')
back_button.place(x=450,y=450)
########################
b1=Button(frame2, text='Load and\nClean Data', font=('',27),width=10, fg='red', bg='#252525', borderwidth=5, command=f1)
b1.place(x=250,y=240)
b2=Button(frame2, text='Suggest me\na Car', font=('',27), fg='red', bg='#252525', borderwidth=5, command=f2)
b2.place(x=650,y=240)

frame2.mainloop()
