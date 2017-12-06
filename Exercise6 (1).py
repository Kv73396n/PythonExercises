
# coding: utf-8

# In[65]:


#Ashley Vargas, Karina Vargas

#exercise 6 a
n = int
x = 2
def isPrime(n):
    if n<2:
        return False
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True 
    #test 
    print(isPrime(7))
    


# In[53]:


#exercise 6b
n = int
x = 5
def isPrime(n):
    if n<2:
        return False
    else:
        while :
            if  n * n <= n:
                return False    
            n += x
            n = 6 - n
            return True  
  


# In[63]:


#exercise 6c
n = int
x = 2
y = int(input("number:"))

def isPrime(n):
    for n in range(1,y+1):  
        if n<2:
            return False
        else:
            for x in range(2,n):
                if(n % x==0):
                    return False
            return n
     

    


# In[ ]:


#exercise 6d

n = int
x = 2
y = int(input("number:"))

def isPrime(n):
    for n in range(1,y+1):  
        if n<2:
            return False
        else:
            for x in range(2,n):
                if(n % x==0):
                    return False
            return n
     

