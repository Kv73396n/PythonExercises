
# coding: utf-8

# In[9]:


#Ashley Vargas, Karina Vargas

list1 = [[1, 2, 3], [4, 5, 6]]
list2 = [ item for sublist in list1 for item in sublist]

for sublist in list1:
    for item in sublist:
        list2.append(list2)
print(list2)

#result: [1, 2, 3, 4, 5, 6, [...], [...], [...], [...], [...], [...]]

