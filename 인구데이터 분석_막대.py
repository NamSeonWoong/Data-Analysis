import csv
import matplotlib.pyplot as plt


f= open('age.csv')
data= csv.reader(f)
name=input('알고싶은 지역을 입력하세요 :')
result=[]

for row in data:
    if name in row[0]:
        for i in row[3:]:
            result.append(int(i.replace(',','')))
print(result)

plt.rc('font', family='Malgun Gothic')
plt.bar(range(101),result)
plt.title(name+'지역의 인구 구조')
plt.plot(result)
plt.show()