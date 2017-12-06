
# coding: utf-8

# In[6]:


#Ashley Vargas, Karina Vargas

n=[]
for x in range(1, 8000):
    if (x%5==0) and (x%7==0) and (x%11==0):
        n.append(str(x))
print (','.join(n))

#result: 385,770,1155,1540,1925,2310,2695,3080,3465,3850,4235,4620,5005,5390,5775,6160,6545,6930,7315,7700

