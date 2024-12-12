# pandas 사용하기
import numpy as np # numpy 도 함께 import
import pandas as pd
\

#Series
obj = pd.Series([4, 7, -5, 3])
print(obj)

data = {'name': ['Beomwoo', 'Beomwoo', 'Beomwoo', 'Kim', 'Park'],
        'year': [2013, 2014, 2015, 2016, 2015],
        'points': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)
print(df)

#DataFrame을 생성하면서 index를 같이 생성하기
df2 = pd.DataFrame(data, columns=['year', 'name', 'points', 'penalty'],
                  index=['one', 'two', 'three', 'four', 'five'])
print(df2)
print("describe : \n", df2.describe())
