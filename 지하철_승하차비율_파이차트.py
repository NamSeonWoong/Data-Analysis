import csv
import matplotlib.pyplot as plt

f=open('subwayfee.csv')
data = csv.reader(f)

next(data)

label=['유임승차','유임하차','무임승차','무임하차']
c=['red','blue','green','yellow']
plt.rc('font',family="Malgun Gothic")

for row in data:
    for i in range(4,8):
        row[i]=int(row[i])
        
    plt.figure(dpi=300)
    plt.title(row[3]+' '+row[1])
    plt.pie(row[4:8],labels=label, colors=c,autopct='%1.f%%')
    plt.axis('equal')
    plt.savefig(row[3]+' '+row[1]+'.png')