from tkinter import *
import os

######################## Window
frame3=Tk()
frame3.title('Car Recommendation Window')
frame3.config(background='#DCDCDC')
frame3.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(frame3.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(frame3.winfo_screenheight()/2 - windowHeight/2)
frame3.geometry("+{}+{}".format(position_x, position_y))
########################
######################## Function Definitions
def reset_frame():
	frame3.destroy()
	os.system('python frame3.py')
	
def more_info():
	os.system('python more_info.py')

def car_loans():
	os.system('python car_loans.py')
	
def recommendations():
	os.system('python recommendations.py')
	
def suggest():
	if entry1.get() == '':
		family_members = 1
	else:
		family_members = int(entry1.get())
	if entry2.get() == '':
		budget = 8000
	else:
		budget = float(entry2.get())
	fuel = fuel_type.get()

	import csv
	fo = open('data1_clean.csv')
	data = csv.reader(fo, delimiter = '|')
	
	fo1 = open('temp.csv','w')
	fo1.write('ID|BRAND|MODEL|VARIANT|ENGINE|TRANSMISSION|FUEL|MILEAGE|PRICE|SEATS|URL')

	######################## Minimum Price of Car
	fo.seek(0)
	headers = next(data)
	min_price = 8000
	for row in data:
		if min_price >= float(row[8]):
			min_price = float(row[8])
	######################## Maximum Number of Seats		
	fo.seek(0)
	headers = next(data)
	max_seats = 0
	for row in data:
		if max_seats <= int(row[9]):
			max_seats = int(row[9])
	########################				
			
	if family_members<=0 or budget<=0:
		err_text=Text(frame3, height=5, width=27, bg='#DCDCDC', font=('',20), bd=-2)
		err_text.insert(5.0, "Please enter a value greater than ZERO...\n\nClick RESET button to retry.")
		err_text.config(state='disabled')
		err_text.place(x=500, y=250)
	else:
		if family_members>max_seats:
			err_text=Text(frame3, height=8, width=32, bg='#DCDCDC', font=('',20), bd=-2)
			err_text.insert(5.0, "Dear User, a car has got limited number of seats.\n\nPlease consider buying some other \nmotor vehicle.\n\nClick RESET button to retry.")
			err_text.config(state='disabled')
			err_text.place(x=500, y=200)
			
		else:
			if budget<min_price:
				err_text=Text(frame3, height=8, width=30, bg='#DCDCDC', font=('',20), bd=-2)
				err_text.insert(5.0, "Sorry, we don't have any CAR MODEL in this price segment.\nPlease try to increase your budget.\n\nGOOD NEWS :\nGood schemes are available on \nCAR LOANS.\nCheck them out! See you soon :-)")
				err_text.config(state='disabled')
				err_text.place(x=500, y=150)
				
				loan_button = Button(frame3, text = 'CHECK CAR LOANS', width = 15, fg='yellow', bg='#252525', font=('',14), bd=-2, command=car_loans)
				loan_button.place(x=630,y=450)
				
			else:
				count=0
				if fuel=='Anything' :
					fo.seek(0)
					headers = next(data)
					for row in data:
						if float(row[8])<=budget and int(row[9])>=family_members:
							count=count+1
					if count>0:
						fo.seek(0)
						headers = next(data)
						str_result=''
						for row in data:
							if float(row[8])<=budget and int(row[9])>=family_members:
								str_result = str_result+'[ '+row[0]+' ] '+row[1]+' '+row[2]+' '+row[3]+'\n'
								
								str_temp='|'.join(row)
								fo1.write('\n')
								fo1.write(str_temp)
						fo1.close()

				else:
					fo.seek(0)
					headers = next(data)
					for row in data:
						if row[6]==fuel and float(row[8])<=budget and int(row[9])>=family_members:
							count=count+1
					if count>0:
						fo.seek(0)
						headers = next(data)
						str_result=''
						for row in data:
							if row[6]==fuel and float(row[8])<=budget and int(row[9])>=family_members:
								str_result = str_result+'[ '+row[0]+' ] '+row[1]+' '+row[2]+' '+row[3]+'\n'
								
								str_temp='|'.join(row)
								fo1.write('\n')
								fo1.write(str_temp)
						fo1.close()
						
				if count>0:
					text3=Text(frame3, height=1, width=30, bg='#DCDCDC',fg='purple', font=('',20), bd=-2)
					text3.insert(5.0, ">>> We have something for you!")
					text3.config(state='disabled')
					text3.place(x=500, y=100)
					
					text_result = Text(frame3, height=10, width=38, bg='cyan', font=('',16), bd=-2)
					text_result.insert(5.0, str_result)
					text_result.config(state='disabled')
					text_result.place(x=500, y=150)
					recommendations_button = Button(frame3, text = 'OUR RECOMMENDATIONS', width = 25, fg='yellow', bg='#252525', font=('',12), bd=-2, command=recommendations)
					recommendations_button.place(x=580,y=450)
					
				else:
					err_text=Text(frame3, height=8, width=27, bg='#DCDCDC', font=('',20), bd=-2)
					err_text.insert(5.0, "There are currently NO CARS \nmeeting your requirements...\nWe hope to see you back soon.\n\nClick RESET button to modify your requirements.")
					err_text.config(state='disabled')
					err_text.place(x=500, y=200)
				
				if count>10:
					text3=Text(frame3, height=1, width=18, bg='#DCDCDC',fg='purple', font=('',12), bd=-2)
					text3.insert(5.0, "<Please Scroll Down>")
					text3.config(state='disabled')
					text3.place(x=870, y=420)
	
######################## Text Box
text1=Text(frame3, height=1, width=18, bg='#DCDCDC',fg='red', font=('',26), bd=-2)
text1.insert(5.0, "Car Recommendation")
text1.config(state='disabled')
text1.place(x=350, y=10)

text1=Text(frame3, height=1, width=25, bg='#DCDCDC',fg='green', font=('',14), bd=-2)
text1.insert(5.0, "(Please fill the following fields)")
text1.config(state='disabled')
text1.place(x=390, y=50)

text2=Text(frame3, height=1, width=25, bg='#DCDCDC', font=('',20), bd=-2)
text2.insert(5.0, "Click RESET to reset fields.")
text2.config(state='disabled')
text2.place(x=30, y=480)
########################
######################## Fields
label1 = Label(frame3, text='Family Members :\n( Including Driver )', font=('',15), bg='#DCDCDC')
label1.place(x=30,y=100)
entry1=Entry(frame3)
entry1.place(x=270,y=100,height=30)
temp1=Label(frame3, text='[Leave blank to skip field]', font=('',12), bg='#DCDCDC')
temp1.place(x=270,y=130)
  	
label2 = Label(frame3, text='Budget :\n(in Lacs)', font=('',15), bg='#DCDCDC')
label2.place(x=30,y=200)
entry2=Entry(frame3)
entry2.place(x=270,y=200,height=30,width=70)
lacs=Label(frame3, text='Lacs', font=('',15), bg='#DCDCDC')
lacs.place(x=350,y=200)
temp2=Label(frame3, text='[Leave blank to skip field]', font=('',12), bg='#DCDCDC')
temp2.place(x=270,y=230)

fuel_type=StringVar()
fuel_type.set('Petrol')
label3 = Label(frame3, text='Fuel Type :', font=('',15), bg='#DCDCDC')
label3.place(x=30,y=300)
entry3=OptionMenu(frame3,fuel_type,'Petrol','Diesel','CNG','Anything')
entry3.place(x=270,y=300,height=30,width=100)
########################
submit_button=Button(frame3, text = 'SUBMIT', font=('',18), fg='red', bg='white', borderwidth=5, command=suggest)
submit_button.place(x=80,y=400)
reset_button=Button(frame3, text = 'RESET', font=('',18), bg='white', borderwidth=5, command=reset_frame)
reset_button.place(x=250,y=400)
back_button = Button(frame3, text = 'BACK', command = frame3.destroy, font=('',12), bd=-2, bg='white')
back_button.place(x=30,y=540)
########################
frame3.mainloop()
