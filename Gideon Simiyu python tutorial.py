#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello World!')


# # First notebook

# # Variables in python
# 
# 

# In[7]:


x = 22

print(x)


# In[9]:


type(x)


# In[11]:


y = 'Vanilla icecream'

print(y)


# In[13]:


type(y)


# In[23]:


y = 'chocolate icecream'

Y = 'Vanilla icecream'

print(y)

print(Y)


# In[25]:


x,y,z = 'chocolate', 'vanilla', 'strawberry'
print(x)
print(y)
print(z)


# In[27]:


x = y = z = 'Tusker lager'
print(x)
print(y)
print(z)


# In[29]:


ice_cream = ['chocolate','vanilla', 'strawberry']

x,y,z = ice_cream

print(x)
print(y)
print(z)


# In[ ]:


# camel case

#test variable case

testVariableCase = 'Vanilla'


# In[ ]:


# Pascal case

#test variable case

TestVariableCase = 'Vanilla'


# In[ ]:


# Snake case

#test variable case

test_variable_ case = 'Vanilla'


# In[ ]:





# In[ ]:


testvar = 'Vanilla'
test_var = 'Vanilla'
_test_var = 'Vanilla'
Testvar = 'Vanilla'
TestVar = 'Vanilla'
testVar2 = 'Vanilla'


# In[ ]:


# DO NOT DO THIS AT ALL

2testvar = 'Vanilla'
test-var2 = 'Vanilla'
test Var2 = 'Vanilla'
testVar2 = 'Vanilla'



# In[ ]:





# In[33]:


x= 'ice cream is my favourite' + '.'
print(x)


# In[ ]:





# In[ ]:





# In[41]:


# DO NOT ADD AN INTEGER TO A STRING
x= 'ice cream is my favorite' + 9
print(x)


# In[ ]:





# In[ ]:





# In[45]:


Y= 2745654 + 9082643
print(Y)


# In[ ]:





# In[49]:


x = 'ice cream' 
y = ' is'
z = ' my favorite.'



print(x+y+z)



# In[ ]:





# In[ ]:





# In[ ]:





# In[51]:


x = 22
y = 96
z = 5



print(x+y+z)



# In[ ]:





# In[ ]:





# In[53]:


# DO NOT DO THIS 

x = 'ice cream'
y = 96


print(x+y)



# In[ ]:





# In[ ]:





# In[55]:


# You can do this 

x = 'ice cream'
y = 96


print(x,y)



# In[ ]:





# # Data types in python

# In[60]:


type(2334545)


# In[62]:


type(-2334545)


# In[68]:


type(-2334545 + 134)


# In[76]:


# Adding an integer to a decimal number results in a float

type(9.234 + 12)


# In[74]:


# Only use j for an imaginary number

type(23 + 4j)


# In[78]:


# BOOLEAN VALUES

type(True)


# In[80]:


# BOOLEAN VALUES

type(False)


# In[ ]:





# In[82]:


# BOOLEAN VALUES

type(2 > 6)


# In[ ]:





# In[84]:


# BOOLEAN VALUES

2 > 6


# In[ ]:





# In[86]:


# BOOLEAN VALUES

2 == 2


# In[88]:


# Strings

'Single Quote'


# In[90]:


"Double Quote"


# In[94]:


""" 
The subject was so difficult to understand, 
when the exam was given we failed miserably, 
we have to do the supplementary now.

"""


# In[ ]:





# In[ ]:





# In[96]:


multiline = """ 
The subject was so difficult to understand, 
when the exam was given we failed miserably, 
we have to do the supplementary now.

"""

print(multiline)


# In[ ]:





# In[98]:


# if you have a single quote in a sentence, always use a double quote for it to work well

"I've always wanted to eat chapati and kuku."


# In[ ]:





# In[102]:


# if you have a double quote in a sentense, always use a triple quote for it to work well

""" 
I've always wanted to eat "chapati and kuku." 

"""


# In[ ]:





# In[106]:


# If you have a double quote in a sentence, always use a triple quote for it to work well

multiline = """ 
I've always wanted to eat "chapati and kuku." 

"""

print(multiline)

type(multiline)


# In[ ]:





# In[108]:


a = 'Hello World!'


# In[110]:


print(a)


# In[ ]:





# In[112]:


a = 'Hello World!'

print(a[:5])


# In[ ]:





# In[118]:


a = 'Hello World!'

print(a[3])


# In[ ]:





# In[120]:


# starts from zero moving forward

a = 'Hello World!'

print(a[8])


# In[ ]:





# In[122]:


# starts from negative (-1) moving backwords

a = 'Hello World!'

print(a[-4])


# In[ ]:





# In[124]:


# starts from negative (-1) moving backwords

a = 'Hello World!'

print(a[-8])


# In[ ]:





# In[ ]:





# In[126]:


a = 'Hello World!'

print(a[3:8])


# In[128]:


# Multiply strings

a*5


# In[130]:


# add strings 

a + a


# In[ ]:





# In[132]:


# LIST
[1,2,3,4,5,6,7,8,9]


# In[138]:


['chapati','kuku','omena','ugali','sukuma','nyama','chips','mayai','rice']


# In[144]:


['ice cream',3, ['spoon','scoop','plate'],True]


# In[ ]:





# In[146]:


#append is to add to an existing list 
ice_cream = ['chocolate','vanilla','strawberry']

ice_cream.append('salted caramel')

ice_cream


# In[ ]:





# In[150]:


# to change from chocolate to buttermilk pecan
ice_cream[0] = 'buttermilk pecan'
ice_cream


# In[ ]:





# In[160]:


#nest_list arranges the order of details from 0

nest_list = ['ice cream',3, ['spoon','scoop','plate'],True]


# In[154]:


nest_list[0]


# In[156]:


nest_list[1]


# In[158]:


nest_list[2]


# In[162]:


nest_list[2][1]


# In[164]:


nest_list[2][2]


# In[ ]:





# # Tuples
# 
# 

# In[178]:


#tuple

tuple_scoops = (1,2,3,2,1)

type(tuple_scoops)


# In[ ]:





# In[180]:


tuple_scoops[0]


# In[186]:


tuple_scoops[2]


# In[188]:


tuple_scoops[4]


# In[192]:


# for a tuple, you cannot change or append anything 
#tuples are used when data will never change at all

tuple_scoops.append(2)


# In[ ]:





# # Sets
# 
# 

# In[195]:


# Do not have any duplicates 

daily_shows = {1,2,3,4}


# In[197]:


type(daily_shows)


# In[199]:


print(daily_shows)


# In[ ]:





# In[ ]:





# In[205]:


# Do not have any duplicates 

daily_shows_log = {1,2,31,2,31,80,0,4,67,89,2,58,80,9,4,67}


# In[209]:


#unique values are only shown here

print(daily_shows_log)


# In[ ]:





# In[211]:


wifes_daily_log = {1,3,7,9,7,3,1,2}


# In[215]:


#compare the unique values between wifes daily log and daily shows

print(daily_shows | wifes_daily_log)


# In[ ]:





# In[ ]:





# In[217]:


#compare the values between wifes daily log and daily shows
#shows the values that show up in both sets


print(daily_shows & wifes_daily_log)


# In[ ]:





# In[ ]:





# In[219]:


#compare the values between wifes daily log and daily shows
#shows the values that do not match.


print(daily_shows - wifes_daily_log)


# In[ ]:





# In[221]:


#compare the values between daily shows minus wifes daily log
#shows the values that do not match.



print(wifes_daily_log - daily_shows)


# In[ ]:





# In[ ]:





# In[223]:


#compare the values between daily shows minus wifes daily log
#shows the values that are either on one or the other but not in both.



print(wifes_daily_log ^ daily_shows)


# In[ ]:





# In[ ]:





# # Dictionaries
# 
# 

# In[ ]:





# In[228]:


# dictionaries

# key/value pair

dict_cream = {'name': 'Gideon Simiyu', 'weekly intake': 6, 'favourite ice creams': ['Chocolate','vanilla','strawberry']}


# In[232]:


type(dict_cream)


# In[234]:


print(dict_cream)


# In[236]:


dict_cream.values()


# In[ ]:





# In[ ]:





# In[238]:


dict_cream.keys()


# In[ ]:





# In[ ]:





# In[240]:


dict_cream.items()


# In[ ]:





# In[244]:


dict_cream['name']


# In[ ]:





# In[ ]:





# In[246]:


dict_cream['weekly intake']


# In[ ]:





# In[252]:


# updates a name 

dict_cream['name'] = 'Caroline Kamau Mbuo'

print(dict_cream)


# In[ ]:





# In[256]:


# It didn't delete the other keywords
#It just added to it



dict_cream.update({'name': 'Caroline Kamau Mbuo', 'weekly intake': 6, 'weight': ['450 pounds']})



print(dict_cream)


# In[ ]:


{'name': 'Caroline Kamau Mbuo', 'weekly intake': 6, 'favourite ice creams': ['Chocolate', 'vanilla', 'strawberry']}


# In[ ]:





# In[ ]:





# In[292]:


dict_cream.update({'name': 'Caroline Kamau Mbuo', 'weekly intake': 6, 'favorite ice creams': ['Chocolate', 'vanilla', 'strawberry']})

print(dict_cream)


# In[288]:


del dict_cream['name']

print(dict_cream)


# In[ ]:





# In[294]:


dict_cream.update({'name': 'Caroline Kamau Mbuo', 'weekly intake': 6, 'weight': ['349 pounds']})

print(dict_cream)                                                                                 


# In[296]:


del dict_cream['weight']

print(dict_cream)


# In[ ]:




