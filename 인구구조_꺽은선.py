import csv
f = open('gender.csv')
data = csv.reader(f)
m=[]
f=[]

name=input('궁금한 동네가 어디인가요?: ')
for row in data :
    if name in row[0]:
        for i in range(3,104):
            m.append(int(row[i]))
            f.append(int(row[i+103]))
        break

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.title(name+ '지역의 인구 구조')
plt.plot(m, label="남자")
plt.plot(f, label="여자")
plt.legend()
plt.show()