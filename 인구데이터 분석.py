import csv
import matplotlib.pyplot as plt


f= open('age.csv')
data= csv.reader(f)
name=input('알고싶은 지역을 입력하세요 :')
result=[]

for row in data:
    if '북구 우산동' in row[0]:
        for i in row[3:]:
            result.append(int(i.replace(',','')))
print(result)

plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title(name+'지역의 인구 구조')
plt.plot(result)
plt.show()