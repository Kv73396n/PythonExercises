
# coding: utf-8

# In[1]:


float(123)


# In[2]:


float('123')


# In[3]:


float('123.23')


# In[4]:


int(123.23)


# In[5]:


int('123.23')


# In[6]:


int(float('123.23'))


# In[7]:


str(12)


# In[8]:


str(12.2)


# In[9]:


bool('a')


# In[10]:


bool(0)


# In[11]:


bool(0.1)


# In[ ]:


#Ashley Vargas, Karina Vargas CS361
#A. 123.0 - float values have a decimal point so it adds the decimal to change the int value into a float value.
#B. 123.0 - cast number as a float. It works as a float.
#C. 123.23 - cast number as float, works as a float.
#D. 123 - int values don't have decimals so changing the float value into int removes the numbers after the decimal point.
#E. Error - would not cast because the number was not base 10.
#F. 123 - a float value gets evaluated first, and then the int version of that value is interpreted. Inner first, and then outer.
#G. '12' - str changes the number into a string literal.
#H. '12.2' - str change the number into a string literal.
#I. True - Everything other than 0, None, and empty are considered true for bool in Python unless explicitly coded otherwise.
#J. False - bool is a subclass of int and False is set to the value of 0.
#K. True -  Everything other than 0, None, and empty are considered true for bool in Python unless explicitly coded otherwise.

