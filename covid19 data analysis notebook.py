#!/usr/bin/env python
# coding: utf-8

# # Welcome to Covid19 Data Analysis Notebook
# ------------------------------------------

# ### Let's Import the modules 

# In[1]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# ## Task 2 

# ### Task 2.1: importing covid19 dataset
# importing "Covid19_Confirmed_dataset.csv" from "./Dataset" folder. 
# 

# In[4]:


corona_dataset_csv= pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head(10)


# #### Let's check the shape of the dataframe

# In[6]:


corona_dataset_csv.shape


# ### Task 2.2: Delete the useless columns

# In[15]:


df= corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)


# In[16]:


corona_dataset_csv.head(10)


# ### Task 2.3: Aggregating the rows by the country

# In[17]:


corona_dataset_aggregated=corona_dataset_csv.groupby("Country/Region").sum( )


# In[18]:


corona_dataset_aggregated.head()


# In[19]:


corona_dataset_aggregated.shape


# ### Task 2.4: Visualizing data related to a country for example China
# visualization always helps for better understanding of our data.

# In[25]:


corona_dataset_aggregated.loc["China"].plot()
plt.legend()
corona_dataset_aggregated.loc["Spain"].plot()
corona_dataset_aggregated.loc["Italy"].plot()

plt.legend()
plt.legend()


# ### Task3: Calculating a good measure 
# we need to find a good measure reperestend as a number, describing the spread of the virus in a country. 

# In[27]:


corona_dataset_aggregated.loc['China'].plot()


# In[29]:


corona_dataset_aggregated.loc["China"][:3].plot()


# ### task 3.1: caculating the first derivative of the curve

# In[33]:


corona_dataset_aggregated.loc["China"].diff().plot()


# ### task 3.2: find maxmimum infection rate for China

# In[34]:


corona_dataset_aggregated.loc["China"].diff().max()


# In[41]:


corona_dataset_aggregated.loc["Italy"].diff().max()


# In[37]:


corona_dataset_aggregated.loc["Spain"].diff().max()


# ### Task 3.3: find maximum infection rate for all of the countries. 

# In[48]:


countries= list(corona_dataset_aggregated.index)
max_infection_rates= []
for c in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
max_infection_rates

corona_dataset_aggregated["max_infection_rate"] = max_infection_rates


# In[50]:


corona_dataset_aggregated.head()


# ### Task 3.4: create a new dataframe with only needed column 

# In[72]:


corona_data = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])


# In[73]:


corona_data.head()


# ### Task4: 
# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis

# ### Task 4.1 : importing the dataset

# In[74]:


happiness_report_csv = pd.read_csv("Datasets/worldwide_happiness_report.csv")


# In[75]:


happiness_report_csv.head()


# ### Task 4.2: let's drop the useless columns 

# In[76]:


useless_cols = ["Overall rank", "Score","Generosity","Perceptions of corruption"]


# In[77]:


happiness_report_csv.drop(useless_cols,axis=1,inplace=True)
happiness_report_csv.head()


# ### Task 4.3: changing the indices of the dataframe

# In[78]:


happiness_report_csv.set_index("Country or region",inplace=True)
happiness_report_csv.head()


# ### Task4.4: now let's join two dataset we have prepared  

# #### Corona Dataset :

# In[81]:


corona_data.head()
corona_data.shape


# #### wolrd happiness report Dataset :

# In[82]:


happiness_report_csv.shape


# In[83]:


data = corona_data.join(happiness_report_csv,how="inner")
data.head()


# ### Task 4.5: correlation matrix 

# In[84]:


data.corr()


# ### Task 5: Visualization of the results
# our Analysis is not finished unless we visualize the results in terms figures and graphs so that everyone can understand what you get out of our analysis

# In[85]:


data.head()


# ### Task 5.1: Plotting GDP vs maximum Infection rate

# In[88]:


x = data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))


# In[89]:


sns.regplot(x,np.log(y))


# ### Task 5.2: Plotting Social support vs maximum Infection rate

# In[90]:


x = data["Social support"]
y = data["max_infection_rate"]
sns.regplot(x,np.log(y))


# In[91]:


x = data["Social support"]
y = data["max_infection_rate"]
sns.regplot(x,np.log(y))


# ### Task 5.3: Plotting Healthy life expectancy vs maximum Infection rate

# In[92]:


x = data["Healthy life expectancy"]
y = data["max_infection_rate"]
sns.regplot(x,np.log(y))


# In[93]:


x = data["Healthy life expectancy"]
y = data["max_infection_rate"]
sns.regplot(x,np.log(y))


# ### Task 5.4: Plotting Freedom to make life choices vs maximum Infection rate

# In[94]:


x = data["Freedom to make life choices"]
y = data["max_infection_rate"]
sns.regplot(x,np.log(y))


# In[112]:


x = data["Freedom to make life choices"]
y = data["max_infection_rate"]
sns.regplot(x,np.log(y))

