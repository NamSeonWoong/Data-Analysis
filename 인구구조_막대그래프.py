import csv
f = open('gender.csv')
data = csv.reader(f)
result=[]

name=input('궁금한 동네가 어디인가요?: ')
for row in data :
    if name in row[0]:
        for i in range(3,104):
          result.append(int(row[i])- int(row[i+103]))
        break

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False
plt.rc('font', family='Malgun Gothic')
plt.title(name+ '지역의 연령대별 남여 인구 구조')
plt.bar(range(101), result)
plt.show()