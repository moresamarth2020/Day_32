#!/usr/bin/env python
# coding: utf-8

# # If ... Else in One Line
# There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short. Here's an example:

# In[1]:


a = 2
b = 330
print("A") if a > b else print("B")


# In[2]:


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# In[3]:


result = value_if_true if condition else value_if_false


# In[ ]:




