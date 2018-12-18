import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


data = pd.read_csv('PAD.csv')
print(data.head())
#g = sn.jointplot('20% Strain', '50% Strain', data, kind='kde')
# 分组的小提琴图
#sn.violinplot('Thickness','30% Strain',hue='Speed',data=data,inner='quartile',palette=['lightblue','lightpink'])

sn.pairplot(data, vars=['30% Strain','Size', 'Speed', 'Thickness'], kind='reg')
#sn.pairplot(data, vars=['Peak Stress', 'Size', 'Thickness'], kind='reg', hue='Speed')

#sn.pairplot(data, vars=['10% Strain','20% Strain', '30% Strain', '40% Strain', '50% Strain', 'Peak Stress'], kind='reg')
#sn.lmplot(y='20% Strain', x='10% Strain', data=data)
#sn.lmplot(y='10% Strain', x='Peak Stress', data=data)
#sn.lmplot(y='20% Strain', x='Size', data=data)
#sn.lmplot(y='20% Strain', x='Thickness', data=data)

#热力图
#sn.heatmap(data[['Size','Speed','Thickness','20% Strain','30% Strain','40% Strain']].corr())

plt.show()
