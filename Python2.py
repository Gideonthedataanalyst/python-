#!/usr/bin/env python
# coding: utf-8

# # Comparison Operators

# In[2]:


#equal to 

#you can't say 10 = 10

10 = 10


# In[4]:


10  == 10


# In[6]:


50 == 10


# In[8]:


23 != 10


# In[ ]:





# In[12]:


'Vanilla' == 'Chocolate'


# In[ ]:





# In[14]:


'Vanilla' == 'Vanilla'


# In[16]:


x = 'Vanilla'
y = 'Chocolate'

x == y


# In[ ]:





# In[18]:


x = 'Vanilla'
y = 'Chocolate'

x != y


# In[ ]:





# In[20]:


50 < 10


# In[22]:


12 < 60


# In[24]:


10 < 10


# In[26]:


10 <= 10


# In[28]:


10 >= 10


# In[30]:


23>= 16


# In[ ]:





# # Logical operators
# 
# 
# 
# 

# In[35]:


12 > 45


# In[37]:


(10 > 70) and (70 > 10)


# In[39]:


(70 > 10) and ( 60 > 23)


# In[ ]:





# In[41]:


(10 > 70) or (70 > 10)


# In[ ]:





# In[43]:


('Vanilla' > 'Chocolate') and ( 60 > 23)


# In[ ]:





# In[45]:


('Vanilla' > 'Chocolate') or ( 60 > 23)


# In[47]:


not(65 > 23)


# In[ ]:





# # Membership operators

# In[54]:


ice_cream = 'I love chocolate ice cream'


'love' in ice_cream


# In[ ]:





# In[56]:


ice_cream = 'I love chocolate ice cream'


'love' in 'I love chocolate ice cream'


# In[58]:


scoops = [1,2,3,4,5,6,7]

2 in scoops


# In[ ]:





# In[60]:


scoops = [1,2,3,4,5,6,7]

9 not in scoops


# In[ ]:





# In[64]:


scoops = [1,2,3,4,5,6,7]
wanted_scoops = 8

wanted_scoops not in scoops


# In[ ]:





# In[ ]:





# In[66]:


scoops = [1,2,3,4,5,6,7]
wanted_scoops = 8

wanted_scoops in scoops


# In[ ]:





# # If - Elif - Else - Statement
# 
# 
# 
# 

# In[70]:


if 23 > 12:
    
    print('It worked')
    


# In[ ]:





# In[72]:


if 23 < 12:
    
    print('It worked')
    


# In[ ]:





# In[80]:


if 23 < 12:
    print('It worked')
else: 
    print('It did not work....')
    


# In[ ]:





# In[ ]:





# In[82]:


if 23 > 12:
    print('It worked')
else: 
    print('It did not work....')
    


# In[ ]:





# In[ ]:





# In[90]:


if 23 < 12:
    print('It worked')
elif 25 < 90:
    print('elif worked!')
    
else: 
    print('It did not work....')
    


# In[94]:


if 25 < 12:
    print('It worked')
elif 25 < 20:
    print('elif worked!')
elif 25 < 22:
    print('elif 2 worked!')
elif 25 < 46:
    print('elif 3 worked!')
elif 25 < 57:
    print('elif 4 worked!')
else: 
    print('It did not work....')
    


# In[ ]:





# In[ ]:





# In[96]:


if (25 < 12) or (2 < 7):
    print('It worked')
elif 25 < 20:
    print('elif worked!')
elif 25 < 22:
    print('elif 2 worked!')
elif 25 < 46:
    print('elif 3 worked!')
elif 25 < 57:
    print('elif 4 worked!')
else: 
    print('It did not work....')
    


# In[98]:


print('It worked') if 10 > 23 else print('it did not work')


# In[ ]:





# In[ ]:





# In[102]:


if (25 < 12) or (2 < 7):
    print('It worked')
    if 10 > 5:
        print('The nested if statement worked')
elif 25 < 20:
    print('elif worked!')
elif 25 < 22:
    print('elif 2 worked!')
elif 25 < 46:
    print('elif 3 worked!')
elif 25 < 57:
    print('elif 4 worked!')
else: 
    print('It did not work....')
    


# In[ ]:





# # For loops
# 
# 

# In[ ]:


integers = [1,2,3,4,5,6]


# In[123]:


integers = [1,2,3,4,5,6]
for numbers in integers:
    print(numbers)


# In[ ]:





# In[127]:


integers = [1,2,3,4,5,6]
for numbers in integers:
    print('yes!')


# In[ ]:





# In[ ]:





# In[131]:


integers = [1,2,3,4,5,6]
for numbers in integers:
    print('integers')


# In[ ]:





# In[ ]:





# In[ ]:


integers = [1,2,3,4,5,6]


# In[133]:


for any in integers:
    print(any + any)


# In[ ]:





# In[ ]:





# In[ ]:


integers = [1,2,3,4,5,6]


# In[135]:


for any in integers:
    print(any + any + any + any)


# In[ ]:





# In[137]:


ice_cream_dict = {'name': 'Gideon Simiyu Wafula', 'weekly intake': '8 scoops per week', 'favourite ice cream': ['blue berry', 'Vanilla', 'Strawberry']}


# In[139]:


for cream in ice_cream_dict.values():
    print(cream)


# In[ ]:





# In[141]:


for key, value in ice_cream_dict.items():
    print(key, '->', value)


# In[ ]:





# # Nested for loops
# 
# 

# In[145]:


flavours = ['Vanilla', 'Stawberry', 'Chocolate']
toppings = ['Hot fudge','oreos', 'mashmellow']


# In[147]:


for one in flavours:
    for two in toppings:
        print(one, 'topped with', two)


# # while loop
# 
# 

# In[154]:


number = 0

while number < 31:
    print(number)
    number = number + 1


# In[ ]:





# In[ ]:





# In[156]:


number = 0

while number < 31:
    print(number)
    if number == 10:
        break
    number = number + 1


# In[ ]:





# In[ ]:





# In[ ]:





# In[160]:


number = 0

while number < 7:
    print(number)
    if number == 8:
        break
    number = number + 1
else:
    print('No longer < 7') 


# In[ ]:





# In[ ]:





# In[ ]:





# In[182]:


number = 0

while number < 7:
    print(number)
    if number == 4:
        continue
    number = number + 1
else:
    print('No longer < 7') 


# In[ ]:





# In[ ]:





# In[184]:


number = 0

while number < 7:
    number = number + 1
    if number == 4:
        continue
    print(number)
    
else:
    print('No longer < 7') 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




