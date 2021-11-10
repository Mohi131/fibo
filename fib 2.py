#!/usr/bin/env python
# coding: utf-8

# In[11]:


n=int(input("enter n: "))
def fibnacci(n):
    a=0
    b=1
    if n < 0:
        print("incorrect input")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if c>50:
                break
            print(c)
fibnacci(n)
            


# In[ ]:





# In[ ]:




