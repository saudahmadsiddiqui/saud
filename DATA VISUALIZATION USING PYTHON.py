#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('dark_background')


# In[10]:


df = pd.read_csv('E:\\saud\\zomato.csv')
df.head()


# In[11]:


df.shape


# In[13]:


df.columns


# In[14]:


df = df.drop(['url', 'address', 'phone', 'menu_item', 'dish_liked', 'reviews_list'], axis = 1)
df.head()


# In[15]:


df.info()


# In[16]:


df.drop_duplicates(inplace = True)
df.shape


# In[17]:


df['rate'].unique()


# In[18]:


def handlerate(value):
    if(value=='NEW' or value=='-'):
        return np.nan
    else:
        value = str(value).split('/')
        value = value[0]
        return float(value)
    
df['rate'] = df['rate'].apply(handlerate)
df['rate'].head()


# In[19]:


df['rate'].fillna(df['rate'].mean(), inplace = True)
df['rate'].isnull().sum()


# In[20]:


df.info()


# In[21]:


df.dropna(inplace = True)
df.head()


# In[22]:


df.rename(columns = {'approx_cost(for two people)':'Cost2plates', 'listed_in(type)':'Type'}, inplace = True)
df.head()


# In[23]:


df['location'].unique()


# In[24]:


df['listed_in(city)'].unique()


# In[25]:


df = df.drop(['listed_in(city)'], axis = 1)


# In[26]:


df['Cost2plates'].unique()


# In[27]:


def handlecomma(value):
    value = str(value)
    if ',' in value:
        value = value.replace(',', '')
        return float(value)
    else:
        return float(value)
    
df['Cost2plates'] = df['Cost2plates'].apply(handlecomma)
df['Cost2plates'].unique()


# In[28]:


df.head()


# In[29]:


rest_types = df['rest_type'].value_counts(ascending  = False)
rest_types


# In[30]:


rest_types_lessthan1000 = rest_types[rest_types<1000]
rest_types_lessthan1000


# In[32]:


def handle_rest_type(value):
    if(value in rest_types_lessthan1000):
        return 'others'
    else:
        return value
        
df['rest_type'] = df['rest_type'].apply(handle_rest_type)
df['rest_type'].value_counts()


# In[34]:


location = df['location'].value_counts(ascending  = False)

location_lessthan300 = location[location<300]



def handle_location(value):
    if(value in location_lessthan300):
        return 'others'
    else:
        return value
        
df['location'] = df['location'].apply(handle_location)
df['location'].value_counts()


# In[35]:


cuisines = df['cuisines'].value_counts(ascending  = False)


cuisines_lessthan100 = cuisines[cuisines<100]



def handle_cuisines(value):
    if(value in cuisines_lessthan100):
        return 'others'
    else:
        return value
        
df['cuisines'] = df['cuisines'].apply(handle_cuisines)
df['cuisines'].value_counts()


# In[36]:


df.head()


# In[37]:


plt.figure(figsize = (16,10))
ax = sns.countplot(df['location'])
plt.xticks(rotation=90)


# In[38]:


#visualisation of online order
plt.figure(figsize = (6,6))
sns.countplot(df['online_order'], palette = 'inferno')


# In[39]:


#visualisation Book Table
plt.figure(figsize = (6,6))
sns.countplot(df['book_table'], palette = 'rainbow')


# In[40]:


#visualisation online order vs rate
plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = df)


# In[41]:


#visualisation Book table vs rate
plt.figure(figsize = (6,6))
sns.boxplot(x = 'book_table', y = 'rate', data = df)


# In[42]:


#visualizing  online order facility location wise
df1 = df.groupby(['location','online_order'])['name'].count()
df1.to_csv('location_online.csv')
df1 = pd.read_csv('location_online.csv')
df1 = pd.pivot_table(df1, values=None, index=['location'], columns=['online_order'], fill_value=0, aggfunc=np.sum)
df1


# In[43]:


df1.plot(kind = 'bar', figsize = (15,8))


# In[44]:


#Visualizing book table facility location wise
df2 = df.groupby(['location','book_table'])['name'].count()
df2.to_csv('location_booktable.csv')
df2 = pd.read_csv('location_booktable.csv')
df2 = pd.pivot_table(df2, values=None, index=['location'], columns=['book_table'], fill_value=0, aggfunc=np.sum)
df2


# In[45]:


df2.plot(kind = 'bar', figsize = (15,8))


# In[46]:


# visualizing types of restaurant vs rate 
plt.figure(figsize = (14, 8))
sns.boxplot(x = 'Type', y = 'rate', data = df, palette = 'inferno')


# In[47]:


#Grouping types of restaurant location wise
df3 = df.groupby(['location','Type'])['name'].count()
df3.to_csv('location_Type.csv')
df3 = pd.read_csv('location_Type.csv')
df3 = pd.pivot_table(df3, values=None, index=['location'], columns=['Type'], fill_value=0, aggfunc=np.sum)
df3


# In[48]:


df3.plot(kind = 'bar', figsize = (36,8))


# In[49]:


#No. of votes location wise
df4 = df[['location', 'votes']]
df4.drop_duplicates()
df5 = df4.groupby(['location'])['votes'].sum()
df5 = df5.to_frame()
df5 = df5.sort_values('votes', ascending=False)
df5.head()


# In[51]:


plt.figure(figsize = (15,8))
sns.barplot(df5.index , df5['votes'])
plt.xticks(rotation = 90)


# In[52]:


df.head()


# In[53]:


#visualizing top cuisines
df6 = df[['cuisines', 'votes']]
df6.drop_duplicates()
df7 = df6.groupby(['cuisines'])['votes'].sum()
df7 = df7.to_frame()
df7 = df7.sort_values('votes', ascending=False)
df7.head()


# In[54]:


df7 = df7.iloc[1:, :]
df7.head()


# In[55]:


plt.figure(figsize = (15,8))
sns.barplot(df7.index , df7['votes'])
plt.xticks(rotation = 90)


# In[ ]:




