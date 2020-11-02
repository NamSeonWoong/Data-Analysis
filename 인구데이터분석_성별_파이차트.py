import csv
f=open('gender.csv')
data= csv.reader(f)
size=[]

name=input('찾고싶은 지역을 입력하세요 :')

for row in data:
    if name in row[0]:
        m=0
        f=0
        for i in range(101):
            m+=int(row[i+3].replace(',',''))
            f+=int(row[i+106].replace(',',''))
       
        break
size.append(m)
size.append(f)


import matplotlib.pyplot as plt


plt.figure(figsize=(8,4),dpi=200)
plt.rc('font', family='Malgun Gothic')
color=['crimson','darkcyan']
plt.axis('equal')

plt.pie(size,labels=['남','여'], autopct='%.1f%%', colors=color, startangle=90)
plt.title(name+'지역의 남녀 성별 비율')
# plt.legend()
plt.show()
print(name+'의 남자 인구는',m,'명', '여자 인구는',f,'명 입니다.')

