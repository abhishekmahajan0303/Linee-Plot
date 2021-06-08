#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


from matplotlib import pyplot as plt


# In[3]:


x = np.arange(1,11)


# In[4]:


x


# In[5]:


y=2*x
y


# In[6]:


plt.plot(x,y)
plt.show()


# In[7]:


# Labelling x and y axis


# In[10]:


plt.plot(x,y)
plt.title('Graph between X  and Y')
plt.xlabel('This is x axis')
plt.ylabel('This is y axis')
plt.show()


# In[11]:


# Showing grid


# In[12]:


plt.plot(x,y)
plt.title('Graph between X  and Y')
plt.xlabel('This is x axis')
plt.ylabel('This is y axis')
plt.grid(True)
plt.show()


# In[13]:


# To change line color and line style and line width


# In[14]:


plt.plot(x,y,color='g',linestyle=':',linewidth=4)
plt.show()


# In[15]:


# Adding two lines in the same plot


# In[16]:


x


# In[19]:


y1=4*x


# In[20]:


y1


# In[21]:


y2=8*x
y2


# In[22]:


plt.plot(x,y1)
plt.plot(x,y2)
plt.show()


# In[23]:


# Now making different graphs for representing these two lines so that 
# these different lines graphs can be understood easily 


# In[24]:


# Making sub plot i.e. Two column and one row graph


# In[31]:


plt.subplot(1,2,1)
plt.plot(x,y1,color='r')
plt.title("Graph between x and y1")
plt.xlabel('This is x axis')
plt.ylabel('This is y1 axis')


plt.subplot(1,2,2)
plt.plot(x,y2,color='g',linestyle=":")
plt.title("Graph between x and y2 axis")
plt.xlabel('This is x axis')
plt.ylabel('This is y2 axis')
plt.grid(True)
plt.show()


# In[ ]:




