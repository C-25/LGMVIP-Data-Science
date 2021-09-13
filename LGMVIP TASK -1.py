#!/usr/bin/env python
# coding: utf-8

# # LGMVIP TASK-1
# # LEVEL-INTERMEDIATE
# # EXPLORATORY DATA ANALYSIS ON DATASET TERRORISM
# # OBJECTIVE - AS A SECURITY/DEFENCE ANALYST TRY TO FIND OUT THE HOT ZONE OF TERRORISM
# # AUTHOR - CHIRAG GHOSH

# In[51]:


##IMPORTING NECESSARY LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[5]:


##READING AND UNDERSTANDING THE DATASET
data = pd.read_csv("C:\\Users\\CHIRAG\\Desktop\global terrorism.csv",dtype = 'unicode',encoding ='latin1')
data.head()


# In[12]:


data.tail()


# In[6]:


data.columns.values


# In[15]:


data.shape


# In[16]:


data.info()


# In[17]:


data.describe()


# In[13]:


##FINDING NULL VALUES
data.isnull().sum()


# In[18]:


##TOP 5 COUNTRIES WITH MOST TERRORIST ATTACKS
print(data['country_txt'].value_counts().head(5))


# In[19]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['country_txt'].value_counts()[:5].index,data['country_txt'].value_counts()[:5].values)
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


## IRAQ IS THE MOST AFFECTED COUNTRY WITH TERRORIST ATTACKS


# In[20]:


##TOP 5 REGIONS WITH MOST TERRORIST ATTACKS
print(data['region_txt'].value_counts().head(5))


# In[21]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['region_txt'].value_counts()[:5].index,data['region_txt'].value_counts()[:5].values)
plt.xlabel('Region')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


## MIDDLE EAST AND NORTH AFRICA IS THE REGION WITH MOST TERRORIST ATTACKS FOLLOWED BY SOUTH ASIA


# In[22]:


##TOP 5 CITIES WITH MOST TERRORIST ATTACKS
print(data['city'].value_counts().head(5))


# In[23]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['city'].value_counts()[:5].index,data['city'].value_counts()[:5].values)
plt.xlabel('city')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


## BAGHDAD IS THE CITY WITH MOST TERRORIST ATTACKS SINCE FIRST ONE IS UNKNOWN


# In[24]:


##TOP 5 STATES WITH MOST TERRORIST ATTACKS
print(data['provstate'].value_counts().head(5))


# In[25]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['provstate'].value_counts()[:5].index,data['provstate'].value_counts()[:5].values)
plt.xlabel('state')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


## BAGHDAD IS THE STATE WITH MOST TERRORIST ATTACKS


# In[38]:


## YEARS WITH MOST AND LEAST TERRORIST ATTACKS
print(data['iyear'].value_counts())


# In[40]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['iyear'].value_counts().index,data['iyear'].value_counts().values)
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


## 2014 IS THE YEAR WITH THE MOST AND 1971 IS THE YEAR WITH LEAST TERRORIST ACTIVITIES 


# In[28]:


##TOP 5 MOST ACTIVE TERRORIST GROUPS
print(data['gname'].value_counts().head(5))


# In[29]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['gname'].value_counts()[:5].index,data['gname'].value_counts()[:5].values)
plt.xlabel('Terrorist Group')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


## TALIBAN IS THE MOST ACTIVE TERRORIST GROUP SINCE FIRST ONE IS UNKNOWN


# In[30]:


##TOP 5 MONTHS WITH MOST TERRORIST ATTACKS
print(data['imonth'].value_counts().head(5))


# In[31]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['imonth'].value_counts()[:5].index,data['imonth'].value_counts()[:5].values)
plt.xlabel('Month')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


## MOST TERRORIST ATTACKS TOOK PLACE IN THE MONTH OF MAY


# In[48]:


##TOP 5 METHOD OF TERRORIST ATTACKS
print(data['attacktype1_txt'].value_counts().head(5))


# In[49]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['attacktype1_txt'].value_counts()[:5].index,data['attacktype1_txt'].value_counts()[:5].values)
plt.xlabel('Attack Type')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


## BOMBING/EXPLOSION IS THE MOST COMMON METHOD USED IN TERRORIST ATTACKS


# In[42]:


##TOP 5 TARGETS OF TERRORIST ATTACKS
print(data['targtype1_txt'].value_counts().head(5))


# In[43]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['targtype1_txt'].value_counts()[:5].index,data['targtype1_txt'].value_counts()[:5].values)
plt.xlabel('Affected Targets')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


## PRIVATE CITIZENS AND PROPERTY ARE MOST AFFECTED BY TERRORIST ATTACKS FOLLOWED BY MILITARY,POLICE,GENERAL GOVERNMENT AND BUSINESS 


# In[44]:


##TOP 5 WEAPONS USED FOR TERRORIST ATTACKS
print(data['weaptype1_txt'].value_counts().head(5))


# In[45]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['weaptype1_txt'].value_counts()[:5].index,data['weaptype1_txt'].value_counts()[:5].values)
plt.xlabel('Weapons Used')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


## EXPLOSIVES ARE MOSTLY USED AS WEAPONS FOR TERRORIST ATTACKS


# In[46]:


data['success'].value_counts()


# In[ ]:


## TERRORISTS ARE SUCCESSFUL 161632 TIMES AND FAILED 20059 IN CONDUCTING TERRORIST ATTACKS


# In[47]:


data['suicide'].value_counts()


# In[ ]:


## 6633 PEOPLE COMMITTED SUICIDE DURING THE ATTACKS


# # CONCLUSIONS
# 
# 1. MOST AFFECTED COUNTRY- IRAQ
# 2. MOST AFFECTED STATE- BAGHDAD
# 3. MOST AFFECTED CITY- BAGHDAD
# 4. MOST AFFECTED REGION- MIDDLE EAST AND NORTH AFRICA
# 5. MOST TERRIFIC YEAR- 2014
# 6. YEAR WITH LEAST TERRORIST ACTIVITIES- 1971
# 7. MOST COMMONLY USED ATTACK TYPE- BOMBING/EXPLOSION
# 8. WEAPON USED MOST NUMBER OF TIMES- EXPLOSIVES
# 9. MOST ACTIVE TERRORIST GROUP WITH MAXIMUM NUMBER OF ATTACKS- TALIBAN
# 10. AFFECTED TARGETS OF TERRORIST ATTACKS - PRIVATE CITIZENS AND PROPERTY ARE MOST AFFECTED BY TERRORIST ATTACKS FOLLOWED BY MILITARY,POLICE,GENERAL GOVERNMENT AND BUSINESS 
# 11. MONTH WITH MOST ATTACKS- MAY
# ## THEY WERE SUCCESS MOST NUMBER OF TIMES IN THEIR ATTACKS
# 
# 
# # HOTZONE OF TERRORISM: IRAQ
# 
# # THANK YOU
# 
# 

# In[ ]:




