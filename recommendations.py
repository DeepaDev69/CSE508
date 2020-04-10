import csv, os
from tkinter import *

fo_temp = open('temp.csv')
data_temp = csv.reader(fo_temp,delimiter='|')
headers = next(data_temp)


sort = sorted ( data_temp,key=lambda t: float(t[8]) )

str_models=''
str_prices=''
str_mileages=''
for row in sort:
	str_models=str_models+'['+row[0]+']'+' '+row[1]+' '+row[2]+' '+row[3]+'\n'
	str_prices=str_prices+row[8]+' L'+'\n'
	str_mileages=str_mileages+row[7]+'\n'
		

root=Tk()
root.title('Recommendations')
root.geometry('800x400')
windowWidth = 800
windowHeight = 400
position_x = int(root.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(position_x, position_y))
root.config(bg='#DCDCDC')

def more_info():
	os.system('python more_info.py')
	
def graphical_visualization():
	os.system('python recommendation_graph.py')


text=Text(root, height=1, width=25, bg='#DCDCDC', fg='red', font=('',14), bd=-2)
text.insert(5.0, "Our Recommendations")
text.config(state='disabled')
text.place(x=300, y=10)


text=Text(root, height=8, width=100, bg='#DCDCDC', fg='black', font=('',14), bd=-2)
text.insert(5.0, str_models)
text.config(state='disabled')
text.place(x=20, y=70)

text=Text(root, height=8, width=50, bg='#DCDCDC', fg='black', font=('',14), bd=-2)
text.insert(5.0, str_prices)
text.config(state='disabled')
text.place(x=550, y=70)

text=Text(root, height=8, width=50, bg='#DCDCDC', fg='black', font=('',14), bd=-2)
text.insert(5.0, str_mileages)
text.config(state='disabled')
text.place(x=700, y=70)

text=Text(root, height=1, width=25, bg='#DCDCDC', fg='green', font=('',14), bd=-2)
text.insert(5.0, "Price")
text.config(state='disabled')
text.place(x=550, y=45)

text=Text(root, height=1, width=25, bg='#DCDCDC', fg='green', font=('',14), bd=-2)
text.insert(5.0, "Mileage [in KMPL]")
text.config(state='disabled')
text.place(x=635, y=45)

back_button = Button(root, text = 'BACK', command = root.destroy, font=('',12), bd=-2, bg='white')
back_button.place(x=30,y=365)

graph_button = Button(root, text = 'GRAPHICAL VISUALIZATION', command = graphical_visualization, font=('',12), bd=-2, bg='grey',fg='white')
graph_button.place(x=500,y=300)
	
root.mainloop()
