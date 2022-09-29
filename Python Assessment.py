#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #Pandas is usually imported under the pd alias
import numpy as np #To perform a number of mathematical operations on arrays such as trigonometric, statistical, and algebraic routines.


# In[2]:


df=pd.read_csv('transaction.csv',sep=';') #Used to load a CSV file as a pandas dataframe


# In[3]:


##This function returns the first and rows for the object based on position
df.head()


# In[4]:


##The info() method prints information about the DataFrame
df.info()


# In[5]:


##The describe() method is used for calculating some statistical data like percentile, mean and std of the numerical values of the Series or DataFrame
df.describe()


# In[6]:


##Pandas value_counts() function returns a Series containing counts of unique values
df.value_counts()


# In[7]:


##The nunique() method searches column-wise and returns the number of unique values for each row.
df.nunique()


# In[8]:


##We use the df.count() function to calculate the number of values that are present in the rows and ignore all the null or NaN ...
df.count(axis='columns')


# In[10]:


##We can use a Python dictionary to add a new column in pandas DataFrame. Use an existing column as the key values and their respective values
df['CostPerTransaction']=df['NumberOfItemsPurchased']*df['CostPerItem']
df


# In[11]:


df['SalesPerTransaction']=df['NumberOfItemsPurchased']*df['CostPerItem']
df


# In[12]:


df['ProfitPerTransaction']=df['NumberOfItemsPurchased']*df['CostPerItem']
df


# In[13]:


##The round() method rounds the values in the DataFrame into numbers with the specified number of decimals, default 0 decimals.
df['ProfitPerTransaction'] = df['ProfitPerTransaction'].apply(lambda x: round(x, 0) if x > 1 else round(x, 4))
df


# In[14]:


df['Date'] = df['Day'].map(str) + '-' + df['Month'].map(str) + '-' + df['Year'].map(str)
df


# In[15]:


##we convert any string with uppercase to lowercase using a Python built-in function or method is known as lower(). This method or function lower() returns the string in lowercase if it is in uppercase; else, it will return the same original string itself.
df["ItemDescription"] = df["ItemDescription"].str.lower()
df


# In[16]:


##split()function is used to split strings around given separator/delimiter. The function splits the string in the Series/Index from the beginning, at the specified delimiter string
df[['Senior','Middle Age','Young Adult']]=df['ClientKeywords'].str.split(',',expand=True)
df


# In[17]:


##The drop() function is used to remove a set of labels from a row or column. We may exclude rows or columns by defining label names and matching axes or directly defining index or column names
df.drop("ClientKeywords", axis=1, inplace=True)
df


# In[ ]:


df.to_csv(r'export_transaction.csv',index=False)

