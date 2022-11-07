#!/usr/bin/env python
# coding: utf-8

# #                                      THE COVID-19 PROJECT                                             #

# In[1]:


import pandas as pd
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


#To read csv file
pro=pd.read_csv("4. covid_19_data.csv")


# In[3]:


pro


# In[4]:


#To show how many rows and columns
pro.shape


# In[5]:


#count
pro.count()


# In[6]:


pro.isnull().sum()


# In[7]:


#Showing Boolean values by Heat Map
sns.heatmap(pro.isnull())
plt.show()


# In[8]:


#First 5 records
pro.head()


# In[9]:


#Last 5 records
pro.tail()


# In[10]:


#Total records groupby Region
pro.groupby("Region").sum()


# In[11]:


#Top 20 records
pro.groupby("Region").sum().head(20)


# In[12]:


#Total Confirmed cases by Region
pro.groupby("Region")["Confirmed"].sum()


# In[13]:


#Total Confirmed cases by Decending order
pro.groupby("Region")["Confirmed"].sum().sort_values(ascending=False).head(10)


# In[14]:


#Total Confirmed cases,Recovered by region
pro.groupby("Region")["Confirmed","Recovered"].sum()


# In[15]:


#Total Deaths by Regions
pro.groupby("Region")["Deaths"].sum()


# In[16]:


#Total top Deaths cases by Region by ascending order
pro.groupby("Region")["Deaths"].sum().sort_values(ascending=True).head(60)


# In[17]:


# pro[(pro.Confirmed < 10)]


# In[18]:


pro[(~pro.Confirmed < 10)]


# In[19]:


#Top 10 records
pro.head(10)


# In[20]:


#Top 10 States Recovered by ascending order 
pro.sort_values(by = ["Recovered"],ascending=True).head(10)


# # Showing the Records by Visualization 

# In[21]:


#Confirmed cases vs Recovered cases
a=pro["Confirmed"]
b=pro["Recovered"]
sns.scatterplot(a,b,color="orange",s=500)
plt.show()


# In[22]:


pro.sort_values(by = ["Confirmed"],ascending=True).head(10)


# In[23]:


recovered=pro[1:10]
recovered


# In[24]:


#Recovered cases vs Region
sns.set(rc={"figure.figsize":(10,8)})
sns.barplot(x="Region",y="Recovered",data=recovered)
plt.show()


# In[25]:


deaths=pro[1:12]
deaths


# In[26]:


b=pro["Deaths"]
b


# In[27]:


#Deaths cases vs Region
sns.set(rc={"figure.figsize":(10,8)})
sns.barplot(x="Region",y="Deaths",data=deaths)
plt.show()


# In[28]:


a=pro["Confirmed"]
a


# In[29]:


confirmed=pro[1:10]
confirmed


# In[30]:


#Confirmed cases vs Region
sns.set(rc={"figure.figsize":(10,8)})
sns.lineplot(x="Region",y="Confirmed",data=confirmed)
plt.show()


# In[31]:


top_states_death=pro[0:10]
top_states_death


# In[33]:


#Deaths vs Confirmed 
a=pro["Confirmed"]
b=pro["Deaths"]
sns.scatterplot(a,b,color="red",s=1080)
plt.show()


# In[34]:


#Region vs Recovered
sns.set(rc={"figure.figsize":(10,10)})
sns.lineplot(x="Region",y="Recovered",data=top_states_death)
plt.show()


# In[35]:


top_states_deaths=pro[1:15]
top_states_deaths


# In[36]:


#Deaths vs Recovered
sns.set(rc={"figure.figsize":(10,10)})
sns.barplot(x="Deaths",y="Recovered",data=top_states_deaths)
plt.show()


# #                                               #  THE END                                          #
