import matplotlib.pyplot as plt,csv,numpy as np
from textwrap import wrap

fo = open('data1_clean.csv')
data = csv.reader(fo,delimiter='|')
headers = next(data)

sort = sorted ( data,key=lambda t: float(t[8]) )

names=[]
prices=[]
mileages=[]

for row in sort:
	names.append(row[1]+' '+row[2]+' '+row[3])
	prices.append(float(row[8]))
	mileages.append(float(row[7]))
	
if len(names)>8:
	names=names[:8]
	prices=prices[:8]
	mileages=mileages[:8]

names = [ '\n'.join(wrap(l, 10)) for l in names ]

barWidth = 0.25

fig, ax = plt.subplots()
# Set position of bar on X axis
r1 = np.arange(len(names))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Make the plot
rects1 = ax.bar(r1, prices, color='b', width=barWidth, edgecolor='white', label='Price')
rects2 = ax.bar(r2, mileages, color='g', width=barWidth, edgecolor='white', label='Mileage')
 
# Add xticks on the middle of the group bars
plt.xlabel('Car Models', fontweight='bold')
plt.ylabel('Price [in Lacs] | Mileage [in KMPL]', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(names))], names)
plt.title('Best Priced Cars with Mileages')

def autolabel1(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%0.2f L' % float(height),ha='center', va='bottom')
autolabel1(rects1)
def autolabel2(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%0.2f KMPL' % float(height),ha='center', va='bottom')
autolabel2(rects2)
 
# Create legend & Show graphic
plt.legend()
plt.show()
