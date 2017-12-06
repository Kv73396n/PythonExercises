
# coding: utf-8

# In[1]:


#Ashley Vargas, Karina Vargas

def fib(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    else:
        return (fib(n-1) + fib(n-2))
    
print(fib(10))

#Output is 55

