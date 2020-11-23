import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table',header=0,index_col=0)
summer=df[1].iloc[:,:5]
summer.columns=['경기수','금','은','동','계']
print(summer.sort_values('금',ascending=True))
summer.to_excel('하계올림픽메달.xlsx')
