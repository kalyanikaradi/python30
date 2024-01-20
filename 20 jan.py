#!/usr/bin/env python
# coding: utf-8

# In[4]:


#data manipulation
import pandas as pd
import numpy as np


# In[5]:


data=pd.read_csv("train.csv")


# In[6]:


data


# In[7]:


pd.reset_option('display.max_rows',None)


# In[8]:


data


# In[9]:


data[['Survived','Age','Sex']]


# In[15]:


dff=data.loc[data['Sex']=='female']


# In[16]:


dff


# In[18]:


dff.Survived.value_counts()


# In[19]:


dff.Age.mean()


# In[20]:


df1=data.loc[(data['Age']>65)]


# In[21]:


df1


# In[22]:


df1.shape


# In[23]:


data.loc[(data['Sex']=='female')&(data['Age']<38)]


# In[24]:


data.loc[data['Survived']==1]


# In[25]:


data.loc[(data['Sex']=='female')|(data['Age']<38)]


# In[26]:


data.loc[(data['Sex']=='female')&(data['Age']<38)|(data['Fare']<2000)]


# In[27]:


data['DS']='Data Science'


# In[28]:


data


# In[29]:


data.drop(1,axis=0,inplace=True)


# In[30]:


data.head()


# In[31]:


data.drop([2,3],axis=0)


# In[33]:


data.isnull().sum()


# In[34]:


data.Age.isnull().sum()


# In[ ]:




