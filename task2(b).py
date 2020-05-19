#!/usr/bin/env python
# coding: utf-8

# In[1]:


ls=[]
ls=input().split(',')
print(ls)


# In[20]:



for i in range(0, 4):
           for j in range(0, i + 1):
                print("* ", end="")
           print("\r")
for i in range(4, -1 , -1):
          for j in range(0, i + 1):
               print("* ", end="")
          print("\r")
 


# In[22]:


st=input()
s=''
for i in st:
    s=i+s
print(s)


# In[40]:


st=list(input().split(','))
print(st[0],st[1])
print('   ',st[2],'!')
print('     ',st[3],st[4])
print('      ',st[5])

    


# In[ ]:





# In[ ]:




