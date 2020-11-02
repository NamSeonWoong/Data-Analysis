import csv
f=open('gender.csv')
data= csv.reader(f)
m=[]
f=[]

name=input('알고싶은 지역을 입력하세요 :')

for row in data:
    if name in row[0]:
        for i in row[3:104]:
            m.append(int(i))
        for i in row[106:]:
            f.append(-int(i))


import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.figure(figsize=(8,4),dpi=200)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False
plt.barh(range(101),m,label='남성')
plt.barh(range(101),f,label='여성')
plt.title(name+'지역의 남녀 성별 인구 분포')
plt.legend()
plt.show()


