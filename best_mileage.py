import matplotlib.pyplot as plt,csv
from textwrap import wrap

fo = open('data1_clean.csv')
data = csv.reader(fo,delimiter='|')
headers = next(data)

sort = sorted ( data,key=lambda t: float(t[7]), reverse=True )

names=[]
mileages=[]

for row in sort:
	names.append(row[1]+' '+row[2]+' '+row[3])
	mileages.append(float(row[7]))
	
if len(names)>8:
	names=names[:8]
	mileages=mileages[:8]

names = [ '\n'.join(wrap(l, 10)) for l in names ]
 
x = names
x_pos = [i for i, _ in enumerate(x)]

fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, mileages, color='g', label='Mileage')
plt.xlabel("Car Models")
plt.ylabel("Mileage [in KMPL]")
plt.title("Best Mileage Cars")
plt.xticks(x_pos, x)
# Turning on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customizing the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%0.2f' % float(height),ha='center', va='bottom')
autolabel(rects1)

plt.legend()	
plt.show()
