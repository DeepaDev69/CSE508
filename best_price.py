import matplotlib.pyplot as plt,csv
from textwrap import wrap

fo = open('data1_clean.csv')
data = csv.reader(fo,delimiter='|')
headers = next(data)

sort = sorted ( data,key=lambda t: float(t[8]) )

names=[]
prices=[]
for row in sort:
	names.append(row[1]+' '+row[2]+' '+row[3])
	prices.append(float(row[8]))
	
if len(names)>8:
	names=names[:8]
	prices=prices[:8]

names = [ '\n'.join(wrap(l, 10)) for l in names ]

x = names
x_pos = [i for i, _ in enumerate(x)]

fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, prices, color='cyan', label='Price')
plt.xlabel("Car Models")
plt.ylabel("Prices [in Lacs]")
plt.title("Best Priced Cars")
plt.xticks(x_pos, x)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%0.2f L' % float(height),ha='center', va='bottom')
autolabel(rects1)

plt.legend()	
plt.show()
