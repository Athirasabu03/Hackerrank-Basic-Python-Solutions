#!/usr/bin/env python
# coding: utf-8

# In[2]:


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400==0:
        leap=True
    elif year%4==0 and year%100!=0:
        leap=True
    return leap

year = int(input())
print(is_leap(year))


# In[ ]:




