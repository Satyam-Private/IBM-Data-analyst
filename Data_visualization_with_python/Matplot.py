import matplotlib.pyplot as plt 
import pandas as pd 
x = [1, 2, 3, 4, 5]
y = [10 , 20 , 30 , 40 , 50]


dataframe = pd.DataFrame({'x':x, 'y':y})
print(dataframe)
# plt.plot(x,y)
# plt.show()

dataframe.plot(x='x', y='y', kind='line')