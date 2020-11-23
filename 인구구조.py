import numpy as np
import csv

f=open('age.csv')
data= csv.reader(f)
next(data)
data=list(data)

name = input('인구 구조가 알고싶은곳은 어디인가요? : ')
mn=1
result_name=''
result=0

for row in data:
    if name in row[0]:
        home = np.array(row[3:], dtype=int)/int(row[2])

for row in data:
    away = np.array(row[3:], dtype=int)/int(row[2])
    s = np.sum((home-away)**2)
    if s < mn and name not in row[0]:
        mn=s
        result_name=row[0]
        result=away

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.figure(figsize=(6,3), dpi=300)
plt.rc('font', family="Malgun Gothic")
plt.title(name+' 지역과 가장 비슷한 지역')
plt.plot(home, label=name)
plt.plot (result, label=result_name)
plt.legend()
plt.show()