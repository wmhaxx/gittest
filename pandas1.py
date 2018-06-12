import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range("20180612", periods = 6)
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns =list("ABCD"))

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

s1 = pd.Series([1,2,3,4,5,6], index = dates)
print (s1)

df["F"] = s1
df1 = df.reindex(index = dates[0:4], columns = list(df.columns) + ['E'])
df1.loc[dates[0:1], 'E'] = 1
print(df1)
piece1 = df1.iloc[:,:2]
piece2 = df1.iloc[:,2:4]
piece = [piece1,piece2]
print(piece1)
print(piece2)
print(pd.concat(piece))
print(pd.concat(piece, axis = 1))