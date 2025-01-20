#!/usr/bin/env python
# coding: utf-8

# # Day 1 (20-1-25)

# ## Importing the data 
# 
# Link to data - https://www.kaggle.com/datasets/alfathterry/bbc-full-text-document-classification?resource=download

# In[4]:


import pandas as pd 
import numpy as np 


# In[5]:


df = pd.read_csv('bbc_data.csv')


# In[6]:


df


# In[7]:


df['labels'].value_counts()


# In[8]:


df['labels'].unique()


# In[9]:


df['labels'].nunique()


# In[10]:


df['data'].nunique()


# In[11]:


df[['data','labels',]].drop_duplicates()


# In[14]:


df.isna().sum()


# In[15]:


df['labels'].value_counts()


# In[17]:


dir(l)


# In[30]:


l1=[1,2,3,4]
l2=[5,6,7,8]
l1.remove(3)
l1.append(l2)
l1.extend(l2)
print(l1)
print(l2)


# In[ ]:




