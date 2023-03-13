#!/usr/bin/env python
# coding: utf-8
Question 1 : Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a scatter plot for age and fare columns in the titanic dataset.
# In[1]:


import seaborn as sns
import plotly.express as px

# Load the titanic dataset using seaborn
titanic_df = sns.load_dataset("titanic")

# Plot a scatter plot for age and fare columns using Plotly express
fig = px.scatter(titanic_df, x="age", y="fare")

# Show the plot
fig.show()

Question 2 : Using the tips dataset in the Plotly library, plot a box plot using Plotly express.
# In[2]:


import plotly.express as px

# Load the tips dataset from Plotly
tips_df = px.data.tips()

# Create a box plot using Plotly express
fig = px.box(tips_df, x="day", y="total_bill", color="sex")

# Show the plot
fig.show()

Question 3 : Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day" column with the color parameter.
# In[3]:


import plotly.express as px

# Load the tips dataset from Plotly
tips_df = px.data.tips()

# Create a box plot using Plotly express
fig = px.histogram(tips_df, x="sex", y="total_bill", color="day", pattern_shape='smoker')

# Show the plot
fig.show()

Question 4 : Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for the color parameter. Note: Use "sepal_length", "sepal_width", "petal_length", "petal_width" columns only with the dimensions parameter.
# In[4]:


import seaborn as sns
import plotly.express as px

iris=px.data.iris()
fig=px.scatter_matrix(iris,dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],color="species")
fig.show()
     

Question 5 : What is Distplot? Using Plotly express, plot a distplot.

Answer : Distplot is a function in the Plotly library that creates a histogram and a kernel density estimation (KDE) plot of a single variable in a dataset. The histogram shows the distribution of values in the variable, while the KDE plot shows the estimated probability density function of the variable.
# In[5]:


import plotly.express as px

# Load the tips dataset from Plotly
tips_df = px.data.tips()

# Create a box plot using Plotly express
fig = px.box(tips_df, x="day", y="total_bill", color="sex")

# Show the plot
fig.show()


# In[ ]:




