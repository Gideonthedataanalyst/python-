#!/usr/bin/env python
# coding: utf-8

# # Functions

# In[14]:


def first_func():
    print('We did it!')


# In[16]:


first_func()


# In[30]:


def number_squared(number):
    print(number**2)
    


# In[32]:


number_squared(7)


# In[34]:


number_squared(12)


# In[ ]:





# In[36]:


def number_squared_cust(number,power):
    print(number**power)


# In[38]:


number_squared_cust(3,5)


# In[ ]:





# # Arbitrary arguments

# In[45]:


def number_args(*number):
    print(number[0]*number[1])


# In[47]:


number_args(5,12,1,5,8)


# In[ ]:





# In[53]:


args_tuple = (5,12,1,5,8)

def number_args(*number):
    print(number[0]*number[1])



# In[55]:


number_args(5,12,1,5,8)


# In[ ]:





# In[57]:


args_tuple = (5,12,1,5,8)

def number_args(*number):
    print(number[0]*number[1])


# In[59]:


number_args(*args_tuple)


# # keyword argument

# In[62]:


def number_squared_cust(number,power):
    print(number**power)


# In[66]:


number_squared_cust(power = 3,number = 4)


# In[76]:


def number_kwarg(**number):
    print('My number is: '+ number['integer'])


# In[78]:


number_kwarg(integer = '2450')


# In[ ]:





# In[92]:


def number_kwarg(**number):
    print('My number is: '+ number['integer'] + 'My other number is: ' + number['integer2'])


# In[94]:


number_kwarg(integer = '2450', integer2 = '1890')


# # converting data types in python

# In[97]:


num_int = 9
type(num_int)


# In[103]:


num_string = '8'
type(num_string)


# In[107]:


num_string_conv = int(num_string)

type(num_string_conv)


# In[ ]:





# In[105]:


num_sum = num_int + num_string #cannot add string to integer


# In[ ]:





# In[111]:


num_sum = num_int + (num_string_conv)

print(num_sum)


# # converting lists, sets and tuples

# In[115]:


list_type = [1,5,9]

type(list_type)


# In[119]:


tuple(list_type)


# In[121]:


type(tuple(list_type))


# In[129]:


list_type = [1,5,9,5,1,9,1,5,9]


# In[131]:


set(list_type)


# In[133]:


type(set(list_type))


# # dictionaries

# In[141]:


dict_type = {'Name': 'Gideon Simiyu','Age': 25, 'Hair': 'N/A'}

type(dict_type)


# In[143]:


dict_type.items()


# In[145]:


dict_type.values()


# In[149]:


dict_type.keys()


# In[151]:


list(dict_type.keys())


# In[153]:


type(list(dict_type.keys()))


# In[ ]:





# In[155]:


type(list(dict_type.values()))


# In[157]:


long_str = 'I like to go out and hangout with my friends'

list(long_str)


# In[ ]:





# In[159]:


long_str = 'I like to go out and hangout with my friends'

set(long_str)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




