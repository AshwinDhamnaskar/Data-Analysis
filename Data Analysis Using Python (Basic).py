#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


dict1 ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv',
                'Mittal','Archana'],
                'Marks':[98,np.nan,99,87,np.nan,83,99],
                'Gender':['Male','Female','Female','Male','Male',
                         'Female','Female'],
                'Email':['priyang@gmail.com','aadhya@gmail.com',
                        'krisha@gmail.com','vedant@yahoo.com','parshv@hotmail.com',
                         'mittal@yahoo.com','archana@yahoo.com']
               }


# In[3]:


dict1


# In[6]:


df1=pd.DataFrame(dict1)


# In[7]:


df1


# In[8]:


df1.head(3)


# In[9]:


df1.tail(3)


# In[11]:


df1.head(-3)


# In[12]:


df1.tail(-3)


# In[13]:


df1.shape


# In[14]:


print("NUmber of row",df1.shape[0])
print("NUmber of columns",df1.shape[1])


# In[15]:


df1


# In[16]:


df1['Marks'].shape


# In[17]:


df1.info()


# In[22]:


df1.isnull().sum()


# In[24]:


df1.describe(include='all')


# In[25]:


df1['Gender'].unique()


# In[26]:


df1['Marks'].unique()


# In[30]:


df1['Gender'].nunique()


# In[31]:


df1.nunique()


# In[33]:


df1['Gender'].value_counts()


# In[39]:


df1.dropna(how='any')


# In[40]:


df1.dropna(how='all')


# In[41]:


df1


# In[42]:


df1.fillna(0)


# In[45]:


df1['Marks']=df1['Marks'].fillna(df1['Marks'].mean())


# In[46]:


df1


# In[50]:


sum((df1['Marks']>=80) & (df1['Marks']<=90))


# In[52]:


df1['Marks'].between(80,90).sum()


# In[60]:


df1[df1['Marks'].min()==df1['Marks']]['Name']


# In[66]:


df1.nlargest(5,'Marks')[['Name','Marks']]


# In[70]:


df1.sort_values(by='Marks',ascending=False).head(5)[['Name','Marks']]


# In[75]:


df1['Marks'].mean()


# In[76]:


def marks(x):
    return(x/2)


# In[78]:


df1['Half_Marks']=df1['Marks'].apply(marks)


# In[79]:


df1


# In[80]:


df1


# In[82]:


df1['Male_Female']=df1['Gender'].map({"Male":1,"Female":0})


# In[87]:


df1.drop('Male_Female',axis=1,inplace=True)


# In[88]:


df1


# In[92]:


df1.sort_values(by='Marks',ascending=False)


# In[96]:


df1[df1['Gender']=='Female'][['Name','Marks']]


# In[101]:


df1[df1['Gender'].isin(['Female'])][['Name','Marks']]


# In[102]:


df1


# In[103]:


df1['Marks']


# In[105]:


df1.rename(columns={'Marks':'Final_marks'})


# In[106]:


df2=pd.DataFrame({'Name':'Anil','Marks':90,'Gender':'Male','Email':"anil@gmail.com"},index=[0])


# In[107]:


df3=pd.concat([df1,df2],ignore_index=True)


# In[108]:


df3


# In[109]:


df1.loc[:,'Marks':'Gender']


# In[113]:


df1.iloc[:,1:3]


# In[120]:


df1['Name_marks']=df1['Name']+' : '+df1['Marks'].apply(str)


# In[121]:


df1['Name_marks']


# In[122]:


df1


# In[130]:


type(df1.groupby('Gender')['Marks'].mean().sort_values(ascending=True).to_frame())


# In[146]:


df1['Email'][0].split('@')[1]


# In[147]:


list1=[]
for email in df1['Email']:
    list1.append(email.split('@')[1])


# In[151]:


df1['temp']=list1


# In[154]:


df1['temp'].value_counts()


# In[159]:


df1['Email'].apply(lambda x:x.split('@')[1]).value_counts().head()


# In[ ]:


.apply()

