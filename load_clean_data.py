import csv, os
from tkinter import *

######################## Loading Dataset into Memory
file_object = open('data1.csv')
dataset = csv.reader(file_object, delimiter='|')
headers = next(dataset)
######################## Dataset Loaded


######################## Opening new file for Data Cleaning
fo=open('data1_clean.csv','w')
######################## Writing Header
fo.write('ID|BRAND|MODEL|VARIANT|ENGINE|TRANSMISSION|FUEL|MILEAGE|PRICE|SEATS|URL')

######################## Cleaning Data
for row in dataset:
	
	row[4]=row[4].replace(' cc','')
	row[4]=row[4].replace('cc','')
	row[4]=row[4].replace('cc ','')
	row[4]=row[4].replace(' cc ','')
	
	row[7]=row[7].replace(' kmpl','')
	row[7]=row[7].replace('kmpl','')
	row[7]=row[7].replace('kmpl ','')
	row[7]=row[7].replace(' kmpl ','')
	
	row[8]=row[8].replace(' Rs.','')
	row[8]=row[8].replace('Rs.','')
	row[8]=row[8].replace('Rs. ','')
	row[8]=row[8].replace(' Rs. ','')
	
	str1='|'.join(row)
	fo.write('\n')
	fo.write(str1)
	
fo.close()
######################## Data Cleaned

######################## Show cleaned data
def show_data():
	os.system("python3 show_data.py")

######################## Acknowledgement
ack=Tk()
ack.title('Acknowledgement')
ack.geometry('450x150')
windowWidth = 450
windowHeight = 150
position_x = int(ack.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(ack.winfo_screenheight()/2 - windowHeight/2)
ack.geometry("+{}+{}".format(position_x, position_y))
########################
text=Text(ack, bg='#DCDCDC', bd=-2, font=('',14))
text.insert(5.0,'\n       Data Loaded and Cleaned Successfully!')
text.config(state='disabled')
text.pack()
ok_button = Button(ack, text = 'OK', command = ack.destroy, width = 4, font=('',16), bd=-2, fg='yellow', bg='#252525')
ok_button.place(x=85,y=100)
show_data = Button(ack, text = 'Show Data', command = show_data, width = 9, font=('',16), bd=-2, fg='yellow', bg='#252525')
show_data.place(x=205,y=100)
ack.mainloop()
######################## Data Loaded, Cleaned, Acknowledged to User
