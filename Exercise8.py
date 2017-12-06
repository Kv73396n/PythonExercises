
# coding: utf-8

# In[12]:


#Ashley Vargas, Karina Vargas

#8a
a = [1, 2, 3, 4]

#8b
b = a

#8c
b[1] = 5

#8d 
print(a)
print(b)
#result: a: [1, 5, 3, 4]
#b :[1, 5, 3, 4]
#a had a value changed to the value listed for b[1]. 

#8e
c = a[:]

#8f 
c[1] = 7

#8g
print(a)
print(c)
# result: a: [1, 5, 3, 4]
# c: [1, 7, 3, 4]
#Now only c had a value changed to 7 instead. List a stayed the same as before.

def set_first_element_to_zero(list):
    d = a
    d[0] = 1
    print(set_first_element_to_zero(a))
    



