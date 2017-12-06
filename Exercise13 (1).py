
# coding: utf-8

# In[3]:


#Ashley Vargas, Karina Vargas
#Used https://www.guru99.com/reading-and-writing-files-in-python.html for help

f = open("emails.txt", "r")
if f.mode == 'r':
    content = f.read()
    print(content)

