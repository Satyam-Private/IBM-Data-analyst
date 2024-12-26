import matplotlib.pyplot as plt 
import pandas as pd 

#sample random data
x = [1, 2, 3, 4, 5]
y = [10 , 20 , 30 , 40 , 50]

#convert to dataframe
dataframe = pd.DataFrame({'x':x, 'y':y})
print(dataframe)

#plotting with matplotlib
# plt.plot(x,y)
# plt.show()

#plotting with pandas
dataframe.plot(x='x', y='y', kind='line')