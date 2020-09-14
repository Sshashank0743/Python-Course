#!/usr/bin/env python
# coding: utf-8

# ### 1. Find all the indices of peaks in a 1D numpy array n. Peaks are points surrounded by smaller values on both sides.

# In[1]:


import numpy as np
def generate():
    n = np.array([2, 7, 1, 3, 7, 1, 2, 6, 0, 1, 3, 7, 6])
    doublediff = np.diff(np.sign(np.diff(n)))
    peak_locations = np.where(doublediff == -2)[0] + 1
    print(peak_locations)
    return None
generate()


# ### 2. Create a 8x8 matrix and fill it with a chessboard pattern as shown in the below figure.
# ![image.png](attachment:image.png)

# In[2]:


import numpy as np
def generate():
    Z = np.zeros((8,8),dtype=int)
    Z[1::2,::2] = 1
    Z[::2,1::2] = 1
    print(Z)
generate()


# ### 3. Generate one hot encodings ( for each unique value in the array create dummy binary variables ) for a given array. (To know more about one hot encoding, here is a link: [One hot encoding](https://www.pittfagan.com/blog/2016/05/29/one-hot-encoding-visual-example/))

# In[3]:


np.random.seed(101) 
arr = np.random.randint(1,4, size=6)
arr
def generate(arr):
    uniqs = np.unique(arr)
    out = np.zeros((arr.shape[0], uniqs.shape[0]))
    for i, k in enumerate(arr):
        out[i, k-1] = 1
    print(out)
    return None
generate(arr)


# ### 4.  Write a Python program to display all the dates for the month of April, 1994. Also print number of weekdays in April 1994. Also check if 7th April was a weekday or not. Return True if it was a weekday.

# In[11]:


import numpy as np
def generate():
    print("April, 1994")
    print(np.arange('1994-04', '1994-05', dtype='datetime64[D]'))
    print(np.busday_count('1994-04', '1994-05'))
    return np.is_busday(np.datetime64('1994-04-07'))
generate()


# ### 5. Create a 5*5  array with 1 on the border and 2 inside. Now pad this array with a two layer border (filled with 7's) to get an array named "nyp". Return the inner product of "nyp" with itself.

# In[12]:


import numpy as np
def generate():
    x = np.ones((5,5))
    print("Original array:")
    print(x)
    print("1 on the border and 0 inside in the array")
    x[1:-1,1:-1] = 2
    print(x)
    print("7 on the border")
    nyp = np.pad(x, pad_width=2, mode='constant', constant_values=7)
    print(nyp)
    return np.inner(nyp, nyp)
generate()


# ### 6. Given a dataframe df with an integer column 'int', for each value, count the difference back to the previous 7 (or the start of the Series, whichever is closer).  Make this a new column 'Y'. For example if the sequence is [2,3,7,1,2,7,3] then the output should be :[0,1,0,1,2,0,1]. 

# In[20]:


import pandas as pd
import numpy as np
df = pd.DataFrame({'int': [2, 2, 0, 7, 4, 2, 5, 7, 3, 5]})
def generate():
    print(df)
    izero = np.r_[-1, (df['int'] == 7).nonzero()[0]]            # indices of zeros
    print(izero)
    idx = np.arange(len(df))
    print(idx)
    df['Y'] = idx - izero[np.searchsorted(izero - 1, idx) - 1]
    print(df['Y'])
    return None
generate()


# ### 7. Create three DataFrames (data 1,data 2 and data3) based on the given raw data. Join data1 and data2 along rows to form data_all_row. Merge data_all_row and data3 along the subject_id value to form merge1. Merge all values in data1 and data2, with matching records from both sides where available to form merge2. Print out merge1, merge2.

# In[15]:


import pandas as pd
raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
def generate():
    data1 = pd.DataFrame(raw_data_1, columns = ['subject_id', 'first_name', 'last_name'])
    data2 = pd.DataFrame(raw_data_2, columns = ['subject_id', 'first_name', 'last_name'])
    data3 = pd.DataFrame(raw_data_3, columns = ['subject_id','test_id'])
    data_all_row =  pd.concat([data1, data2])
    merge1 = pd.merge(data_all_row, data3, on='subject_id')
    merge2 = pd.merge(data1, data2, on='subject_id', how='outer')
    print(merge1)
    print(merge2)
generate()


# ### 8. Create a dataframe named army from the given data. Set the 'origin' colum as the index of the dataframe. Find how many total veterans are there. Select rows where 'deaths' is greater than 450 or less than 45. Select all the regiments not named "Dragoons". Select the rows called Texas and Arizona. What's in the fifth cell in the row named Texas. 

# In[17]:


import pandas as pd
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}
def generate():
    army= pd.DataFrame(raw_data, columns= ['regiment', 'company', 'deaths', 'battles', 'size', 'veterans', 'readiness', 
                                      'armored', 'deserters', 'origin']) 
    army = army.set_index('origin')
    print(army.veterans.sum())
    print(army[(army['deaths'] > 450) | (army['deaths'] < 45)])
    army[(army['regiment'] != 'Dragoons')]
    army.ix[['Arizona', 'Texas']]
    return army.ix['Texas', 4]
generate()


# ### 9. Filter out and capitalise all letters of  words that contain atleast 2 vowels from a series? 

# In[18]:


import pandas as pd
series = pd.Series(['Insaid', 'strives', 'for', 'bringing','out','the', 'best','in','you' ])
def generate():
    from collections import Counter
    mask = series.map(lambda x: sum([Counter(x.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
    s = series[mask].str.upper()
    print(s)
    return None
generate()


# ### 10. Create a dataframe from a 4*4 array containing elements from 0 to15 in a squential order. Swap rows third and fourth by creating a generic function to swap two rows. Now print the dataframe obtained after reversing the elements of each column.

# In[54]:


import pandas as pd
import numpy as np
def generate():
    df = pd.DataFrame(np.arange(16).reshape(4,4))
    print(df)
    # Solution
    def swap_rows(df, i1, i2):
        a, b = df.iloc[i1, :].copy(), df.iloc[i2, :].copy()
        df.iloc[i1, :], df.iloc[i2, :] = b, a
        return df

    print(swap_rows(df, 2, 3))
    print(df.iloc[::-1, :])
    return None
generate()

