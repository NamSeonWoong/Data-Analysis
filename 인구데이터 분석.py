import csv
import matplotlib.pyplot as plt


f= open('age.csv')
data= csv.reader(f)
result=[]

for row in data:
    if '북구 우산동' in row[0]:
        for i in row[3:]:
            result.append(int(i))
print(result)

plt.style.use('ggplot')
plt.plot(result)
plt.show()