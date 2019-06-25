#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

dataframe = pd.read_csv("./train.csv")


# In[5]:


dataframe.columns


# In[20]:


dataframe.describe()
dataframe['age'].describe()
# dataframe['age'].plot()
dataframe['age'].hist(bins=16)


# In[22]:


dataframe.plot.scatter('age', 'fare')


# In[26]:


df = dataframe.sort_values('age')
df.plot('age', 'fare')


# In[34]:


survecu = dataframe[dataframe['survived'] == 1]
femmes = dataframe[(dataframe['sex'] == 'female') & (dataframe['survived'] == 0)]
femmes


# In[ ]:


# Moyenne et std des ages des survivants
# Moyenne et std des ages des morts

# Moyenne et std des ages des survivants hommes
# Moyenne et std des ages des morts femmes

# Afficher un nuage de points (scatter) fare/age pour hommes qui ont survécu
# Afficher un nuage de points (scatter) fare/age pour hommes qui sont morts
# Afficher un nuage de points (scatter) fare/age pour femmes qui ont survécu
# Afficher un nuage de points (scatter) fare/age pour femmes qui sont morts

