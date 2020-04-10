import csv, os
from tkinter import *

######################## Loading Dataset into Memory
file_object = open('data1_clean.csv')
dataset = csv.reader(file_object, delimiter='|')
headers = next(dataset)
str1 = "ID\tBRAND\tMODEL\t\tVARIANT\t\tENGINE\tTRANSMISSION\tFUEL\tMILEAGE\tPRICE\tSEATS"
str1 += "\n----------------------------------------------------------------------------------------------------------------------------------------------------------"

for row in dataset:
	str1 += "\n"+row[0]+"\t"+row[1]+"\t"+row[2]+"\t\t"+row[3]+"\t\t"+row[4]+"\t"+row[5]+"\t"+row[6]+"\t"+row[7]+"\t"+row[8]+"\t"+row[9]

######################## GUI
data = Tk()
data.title("Cleaned Data")
data.geometry("1058x595")
windowWidth = 1058
windowHeight = 595
position_x = int(data.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(data.winfo_screenheight()/2 - windowHeight/2)
data.geometry("+{}+{}".format(position_x, position_y))
data.config(bg='#DCDCDC')

text=Text(data, width=100, bg='#DCDCDC', fg='black', font=('',12), bd=-2)
text.insert(5.0, str1)
text.config(state='disabled')
text.place(x=60, y=10)

back_button = Button(data, text = 'BACK', command = data.destroy, width = 6, font=('',16), bd=-2, fg='yellow', bg='#252525')
back_button.place(x=480,y=500)

data.mainloop()