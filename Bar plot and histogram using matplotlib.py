#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


from matplotlib import pyplot as plt


# In[3]:


student = {'Bob':87,'Arian':45,'Anie':98,'Ralph':35}
student


# In[4]:


# Now extract keys from dict


# In[5]:


names=list(student.keys())
names


# In[6]:


# No extract value from dict


# In[7]:


marks=list(student.values())
marks


# In[8]:


#Vertical bar graph plot


# In[9]:


plt.bar(names,marks)
plt.show()


# In[10]:


# Now naming graph using commands


# In[11]:


plt.title("This is vertical bar graph")
plt.xlabel("This is x axis represnting names")
plt.ylabel('This is y axis represnting marks')
plt.bar(names,marks)
plt.show()


# In[12]:


# Horizontal bar plot


# In[13]:


plt.barh(names,marks)
plt.show()


# In[14]:


# Now naming graph using commands


# In[15]:


plt.title("This is horizontal bar graph")
plt.xlabel("This is x axis represnting names")
plt.ylabel('This is y axis represnting marks')
plt.barh(names,marks)
plt.show()


# In[16]:


# Scatter plot


# In[17]:


x=[1,2,3,4,5,6,7,8,9,7,8,9,5,7,6,4,5,6,4,1,2,2]
y=[5,2,6,7,7,8,6,9,8,4,5,6,1,2,3,5,4,5,7,5,6,7]
print(x,y)


# In[18]:


plt.scatter(x,y)
plt.show()


# In[19]:


# Now naming graph using commands


# In[20]:


plt.title("This is Scatter bar plot")
plt.xlabel("This is x axis")
plt.ylabel('This is y axis')
plt.scatter(x,y)
plt.show()


# In[21]:


# Changing mark asthetics


# In[22]:


plt.scatter(x,y,marker='*',c='r',s=50)


# In[23]:


# Adding two marker in the same plot


# In[24]:


z=[7,6,5,4,6,1,2,3,4,6,4,5,6,6,7,8,9,7,5,6,4,6]
z


# In[25]:


plt.scatter(x,z,c='b',s=30)
plt.show()


# In[26]:


# Adding subplot in which two rows and one column are there


# In[28]:


plt.subplot(2,1,1)
plt.scatter(x,y,marker='*',c='r',s=25)
plt.title("This is Scatter bar plot between x and y axis")
plt.xlabel("This is x axis")
plt.ylabel('This is y axis')


plt.subplot(2,1,2)
plt.scatter(x,z,c='b',s=30)
plt.title("This is Scatter bar plot between x and z axis")
plt.xlabel("This is x axis")
plt.ylabel('This is z axis')
plt.show()


# In[29]:


# Making histogram


# In[36]:


a=[2,1,2,3,4,5,4,5,6,0,8,9,7,8,9,4,5,6,7,8,9,1,2,3,4]
a


# In[37]:


plt.hist(a)
plt.show()


# In[38]:


# giving colors and bins to histogram


# In[42]:


plt.hist(a,color='r',bins=4)
plt.show()


# In[46]:


# Box plot


# In[47]:


a=[1,2,3,4,5,5,6,7,8,4,5]
b=[5,6,7,8,9,4,5,6,1,2,3]
c=[4,6,7,8,9,4,5,6,4,2,3]
a,b,c


# In[51]:


box=list([a,b,c])
box


# In[52]:


plt.title("This is box plot")
plt.xlabel("This is x axis")
plt.ylabel('This is y axis')
plt.boxplot(box)
plt.show()


# In[53]:


# Violin plot


# In[54]:


a=[1,2,3,4,5,5,6,7,8,4,5]
b=[5,6,7,8,9,4,5,6,1,2,3]
c=[4,6,7,8,9,4,5,6,4,2,3]
a,b,c


# In[55]:


violin=list([a,b,c])
violin


# In[58]:


plt.title("This is Violin plot")
plt.xlabel("This is x axis")
plt.ylabel('This is y axis')
plt.violinplot(violin,showmedians=True)
plt.show()


# In[59]:


# Pie chart


# In[62]:


fruit = ['Apple','Mango','Orange','Grapes']
quantity=[20,40,15,60]
fruit,quantity


# In[67]:


plt.pie(quantity,labels=fruit)
plt.show()


# In[69]:


plt.pie(quantity,labels=fruit,autopct='%0.1f%%',colors=['yellow','pink','red','blue'])
plt.show()


# In[70]:


# Doughnut Chart


# In[83]:


plt.pie(quantity,labels=fruit,radius=3)
plt.pie([1],colors=['w'],radius=2)
plt.show()


# In[ ]:




