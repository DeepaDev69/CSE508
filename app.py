from tkinter import *
import os

frame1=Tk()

def frame2():
	os.system('python frame2.py')
	
######################## Images
image1 = PhotoImage(file = 'bg1.gif')
background = Label(frame1, image=image1)
background.place(x=0, y=0)
#background.image = image1
########################

######################## Window
frame1.title('Four wheeler Recommendation System')
frame1.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(frame1.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(frame1.winfo_screenheight()/2 - windowHeight/2)
frame1.geometry("+{}+{}".format(position_x, position_y))
icon=Image('photo',file='icon1.png')
frame1.tk.call('wm', 'iconphoto', frame1._w, icon)
########################

######################## Text Box
text=Text(frame1, height=4, width=25, bg='#252525', fg='yellow', font=('',14), bd=-2)
text.insert(5.0, "Developers :\nAlfayeed, Deepa, Himanshi, Neha")
text.config(state='disabled')
text.place(x=750, y=450)
########################

######################## Buttons
exit_button = Button(frame1, text = 'EXIT', width = 6, command = frame1.destroy, fg='red', bg='#252525', font=('',30), bd=-2)
exit_button.place(x=50,y=445)

continue_button = Button(frame1, text = 'CONTINUE', width = 8, height = 1, bg='#7CFC00', fg='red', font=('',30), borderwidth=5, command=frame2)
continue_button.place(x=560,y=250)
########################

frame1.mainloop()
