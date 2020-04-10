from tkinter import *
import csv, os, webbrowser
fo = open('data1_clean.csv')
data = csv.reader(fo, delimiter = '|')

######################## Basic Structure
root=Tk()
root.title('More Information')
root.geometry('794x446')
windowWidth = 794
windowHeight = 446
position_x = int(root.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(position_x, position_y))
root.config(background='#DCDCDC')

######################## Maximum Car ID
fo.seek(0)
headers = next(data)
max_id = 0
for row in data:
	if max_id <= int(row[0]):
		max_id = int(row[0])
########################

######################## Function Definition
def buy_now(url):
    webbrowser.open(url)

def reset_frame():
	root.destroy()
	os.system('python3 more_info.py')
	
def show_info():
	identifier = int(entry1.get())
	if identifier<=0 or identifier>max_id:
		err_text=Text(root, height=5, width=27, bg='#DCDCDC', font=('',20), bd=-2)
		err_text.insert(5.0, "Please enter a valid CAR ID...\n\nClick RESET button to retry.")
		err_text.config(state='disabled')
		err_text.place(x=350, y=150)
		
	else:
		fo.seek(0)
		headers = next(data)
		for row in data:
			if identifier==int(row[0]):
				str1='BRAND                  :   '+row[1]+'\nMODEL                  :   '+row[2]+'\nVARIANT               :   '+row[3]+'\nENGINE                 :   '+row[4]+' CC'+'\nTRANSMISSION     :   '+row[5]+'\nFUEL                     :   '+row[6]+'\nMILEAGE               :   '+row[7]+' KMPL'+'\nPRICE                    :   '+row[8]+' Lacs'+'\nSEATS                   :   '+row[9]
				url = row[10]
				text1 = Text(root, height=10, width=35, bg='#DCDCDC',fg='purple', font=('',16), bd=-2)
				text1.insert(5.0, str1)
				text1.config(state='disabled')
				text1.place(x=300, y=100)
				
				link1 = Label(root, text='CHECK ONLINE',fg='red',bg='cyan',width=12,cursor='hand2',font=('',20))
				link1.place(x=390,y=370)
				link1.bind('<Button-1>',lambda e:buy_now(url))
				    

######################## Text Box
text1=Text(root, height=1, width=16, bg='#DCDCDC',fg='red', font=('',27), bd=-2)
text1.insert(5.0, "Car Specifications")
text1.config(state='disabled')
text1.place(x=230, y=15)

label1 = Label(root, text='Enter CAR ID :', font=('',18), bg='#DCDCDC')
label1.place(x=50,y=100)
entry1=Entry(root)
entry1.place(x=50,y=150,height=30)

######################## Button
go_button=Button(root, text = 'GO',width=4, font=('',14), fg='red', bg='white', command=show_info)
go_button.place(x=90,y=225)
reset_button=Button(root, text = 'RESET',width=7, font=('',14), bg='white', command=reset_frame)
reset_button.place(x=70,y=340)
back_button = Button(root, text = 'BACK',width=7, command = root.destroy, font=('',14), bg='white')
back_button.place(x=70,y=390)

root.mainloop()
