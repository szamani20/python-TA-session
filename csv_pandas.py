import pandas as pd
import matplotlib.pyplot as plt

# Read from file
df = pd.read_csv('sample.csv',
                 header=0,  # specify header row(s)
                 names=['customerId', 'accountId', 'transactionDate', 'transactionTime'],
                 # specify the header row (if not specified in file)
                 index_col=2,  # specify the index column
                 usecols=[3],  # specify which columns to include in dataframe
                 converters={'customerId': str,
                             'accountId': str,
                             'transactionDate': str,
                             'transactionTime': int},  # specify the data type of each column
                 skiprows=lambda x: x % 2 == 0,  # rows to skip
                 skipfooter=5,  # ignore last 5 lines
                 nrows=10,  # number of rows to read
                 )
print(df)

# print first or last n rows
print(df.head(5))
print(df.tail(5))

# print max value of a column
print(df['transactionTime'].max())

# Visualization using matplotlib
df['transactionTime'].plot()
plt.show()

# Sort based on one or multiple columns
df.sort_values(by=['transactionTime', 'accountId'],
               ascending=False,
               inplace=True)
print(df)

#################################################################
#################################################################
#################################################################
#################################################################
#################################################################

# Data
names = ['jaime', 'daenerys', 'ramsay', 'john', 'samwell', 'theon', 'arya']
houses = ['lannister', 'targaryen', 'bolton', 'snow', 'tarly', 'greyjoy', 'stark']

# zip data
got = list(zip(names, houses))

# convert to DataFrame
df = pd.DataFrame(got, columns=['First_Name', 'House'])
print(df)
'''
  First_Name      House
0      jaime  lannister
1   daenerys  targaryen
2     ramsay     bolton
3       john       snow
4    samwell      tarly
5      theon    greyjoy
6       arya      stark
'''

# Save to csv file
df.to_csv('got.csv', index=True, header=True)
