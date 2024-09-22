```python
print('Hello World!')
```

    Hello World!
    

# First notebook

# Variables in python




```python
x = 22

print(x)
```

    22
    


```python
type(x)
```




    int




```python
y = 'Vanilla icecream'

print(y)
```

    Vanilla icecream
    


```python
type(y)
```




    str




```python
y = 'chocolate icecream'

Y = 'Vanilla icecream'

print(y)

print(Y)
```

    chocolate icecream
    Vanilla icecream
    


```python
x,y,z = 'chocolate', 'vanilla', 'strawberry'
print(x)
print(y)
print(z)

```

    chocolate
    vanilla
    strawberry
    


```python
x = y = z = 'Tusker lager'
print(x)
print(y)
print(z)

```

    Tusker lager
    Tusker lager
    Tusker lager
    


```python
ice_cream = ['chocolate','vanilla', 'strawberry']

x,y,z = ice_cream

print(x)
print(y)
print(z)
```

    chocolate
    vanilla
    strawberry
    


```python
# camel case

#test variable case

testVariableCase = 'Vanilla'
```


```python
# Pascal case

#test variable case

TestVariableCase = 'Vanilla'
```


```python
# Snake case

#test variable case

test_variable_ case = 'Vanilla'
```


```python

```


```python
testvar = 'Vanilla'
test_var = 'Vanilla'
_test_var = 'Vanilla'
Testvar = 'Vanilla'
TestVar = 'Vanilla'
testVar2 = 'Vanilla'

```


```python
# DO NOT DO THIS AT ALL

2testvar = 'Vanilla'
test-var2 = 'Vanilla'
test Var2 = 'Vanilla'
testVar2 = 'Vanilla'


```


```python

```


```python
x= 'ice cream is my favourite' + '.'
print(x)
```

    ice cream is my favourite.
    


```python

```


```python

```


```python
# DO NOT ADD AN INTEGER TO A STRING
x= 'ice cream is my favorite' + 9
print(x)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[41], line 2
          1 # DO NOT ADD AN INTEGER TO A STRING
    ----> 2 x= 'ice cream is my favorite' + 9
          3 print(x)
    

    TypeError: can only concatenate str (not "int") to str



```python

```


```python

```


```python
Y= 2745654 + 9082643
print(Y)
```

    11828297
    


```python

```


```python
x = 'ice cream' 
y = ' is'
z = ' my favorite.'



print(x+y+z)


```

    ice cream is my favorite.
    


```python

```


```python

```


```python

```


```python
x = 22
y = 96
z = 5



print(x+y+z)


```

    123
    


```python

```


```python

```


```python
# DO NOT DO THIS 

x = 'ice cream'
y = 96


print(x+y)


```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[53], line 5
          1 x = 'ice cream'
          2 y = 96
    ----> 5 print(x+y)
    

    TypeError: can only concatenate str (not "int") to str



```python

```


```python

```


```python
# You can do this 

x = 'ice cream'
y = 96


print(x,y)


```

    ice cream 96
    


```python

```

# Data types in python


```python
type(2334545)
```




    int




```python
type(-2334545)
```




    int




```python
type(-2334545 + 134)
```




    int




```python
# Adding an integer to a decimal number results in a float

type(9.234 + 12)
```




    float




```python
# Only use j for an imaginary number

type(23 + 4j)
```




    complex




```python
# BOOLEAN VALUES

type(True)
```




    bool




```python
# BOOLEAN VALUES

type(False)
```




    bool




```python

```


```python
# BOOLEAN VALUES

type(2 > 6)
```




    bool




```python

```


```python
# BOOLEAN VALUES

2 > 6
```




    False




```python

```


```python
# BOOLEAN VALUES

2 == 2
```




    True




```python
# Strings

'Single Quote'

```




    'Single Quote'




```python
"Double Quote"
```




    'Double Quote'




```python
""" 
The subject was so difficult to understand, 
when the exam was given we failed miserably, 
we have to do the supplementary now.

"""
```




    ' \nThe subject was so difficult to understand, \nwhen the exam was given we failed miserably, \nwe have to do the supplementary now.\n\n'




```python

```


```python

```


```python
multiline = """ 
The subject was so difficult to understand, 
when the exam was given we failed miserably, 
we have to do the supplementary now.

"""

print(multiline)
```

     
    The subject was so difficult to understand, 
    when the exam was given we failed miserably, 
    we have to do the supplementary now.
    
    
    


```python

```


```python
# if you have a single quote in a sentence, always use a double quote for it to work well

"I've always wanted to eat chapati and kuku."
```




    "I've always wanted to eat chapati and kuku."




```python

```


```python
# if you have a double quote in a sentense, always use a triple quote for it to work well

""" 
I've always wanted to eat "chapati and kuku." 

"""
```




    ' \nI\'ve always wanted to eat "chapati and kuku." \n\n'




```python

```


```python
# If you have a double quote in a sentence, always use a triple quote for it to work well

multiline = """ 
I've always wanted to eat "chapati and kuku." 

"""

print(multiline)

type(multiline)

```

     
    I've always wanted to eat "chapati and kuku." 
    
    
    




    str




```python

```


```python
a = 'Hello World!'
```


```python
print(a)
```

    Hello World!
    


```python

```


```python
a = 'Hello World!'

print(a[:5])
```

    Hello
    


```python

```


```python
a = 'Hello World!'

print(a[3])
```

    l
    


```python

```


```python
# starts from zero moving forward

a = 'Hello World!'

print(a[8])
```

    r
    


```python

```


```python
# starts from negative (-1) moving backwords

a = 'Hello World!'

print(a[-4])
```

    r
    


```python

```


```python
# starts from negative (-1) moving backwords

a = 'Hello World!'

print(a[-8])
```

    o
    


```python

```


```python

```


```python
a = 'Hello World!'

print(a[3:8])
```

    lo Wo
    


```python
# Multiply strings

a*5
```




    'Hello World!Hello World!Hello World!Hello World!Hello World!'




```python
# add strings 

a + a
```




    'Hello World!Hello World!'




```python

```


```python
# LIST
[1,2,3,4,5,6,7,8,9]
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
['chapati','kuku','omena','ugali','sukuma','nyama','chips','mayai','rice']
```




    ['chapati',
     'kuku',
     'omena',
     'ugali',
     'sukuma',
     'nyama',
     'chips',
     'mayai',
     'rice']




```python
['ice cream',3, ['spoon','scoop','plate'],True]
```




    ['ice cream', 3, ['spoon', 'scoop', 'plate'], True]




```python

```


```python
#append is to add to an existing list 
ice_cream = ['chocolate','vanilla','strawberry']

ice_cream.append('salted caramel')

ice_cream
```




    ['chocolate', 'vanilla', 'strawberry', 'salted caramel']




```python

```


```python
# to change from chocolate to buttermilk pecan
ice_cream[0] = 'buttermilk pecan'
ice_cream
```




    ['buttermilk pecan', 'vanilla', 'strawberry', 'salted caramel']




```python

```


```python
#nest_list arranges the order of details from 0

nest_list = ['ice cream',3, ['spoon','scoop','plate'],True]
```


```python
nest_list[0]
```




    'ice cream'




```python
nest_list[1]
```




    3




```python
nest_list[2]
```




    ['spoon', 'scoop', 'plate']




```python
nest_list[2][1]
```




    'scoop'




```python
nest_list[2][2]
```




    'plate'




```python

```

# Tuples




```python
#tuple

tuple_scoops = (1,2,3,2,1)

type(tuple_scoops)
```




    tuple




```python

```


```python
tuple_scoops[0]
```




    1




```python
tuple_scoops[2]
```




    3




```python
tuple_scoops[4]
```




    1




```python
# for a tuple, you cannot change or append anything 
#tuples are used when data will never change at all

tuple_scoops.append(2)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[192], line 4
          1 # for a tuple, you cannot change or append anything 
          2 #tuples are used when data will never change at all
    ----> 4 tuple_scoops.append(2)
    

    AttributeError: 'tuple' object has no attribute 'append'



```python

```

# Sets




```python
# Do not have any duplicates 

daily_shows = {1,2,3,4}
```


```python
type(daily_shows)
```




    set




```python
print(daily_shows)
```

    {1, 2, 3, 4}
    


```python

```


```python

```


```python
# Do not have any duplicates 

daily_shows_log = {1,2,31,2,31,80,0,4,67,89,2,58,80,9,4,67}
```


```python
#unique values are only shown here

print(daily_shows_log)
```

    {0, 1, 2, 67, 4, 9, 80, 89, 58, 31}
    


```python

```


```python
wifes_daily_log = {1,3,7,9,7,3,1,2}
```


```python
#compare the unique values between wifes daily log and daily shows

print(daily_shows | wifes_daily_log)
```

    {1, 2, 3, 4, 7, 9}
    


```python

```


```python

```


```python
#compare the values between wifes daily log and daily shows
#shows the values that show up in both sets


print(daily_shows & wifes_daily_log)
```

    {1, 2, 3}
    


```python

```


```python

```


```python
#compare the values between wifes daily log and daily shows
#shows the values that do not match.


print(daily_shows - wifes_daily_log)
```

    {4}
    


```python

```


```python
#compare the values between daily shows minus wifes daily log
#shows the values that do not match.



print(wifes_daily_log - daily_shows)
```

    {9, 7}
    


```python

```


```python

```


```python
#compare the values between daily shows minus wifes daily log
#shows the values that are either on one or the other but not in both.



print(wifes_daily_log ^ daily_shows)
```

    {4, 7, 9}
    


```python

```


```python

```

# Dictionaries




```python

```


```python
# dictionaries

# key/value pair

dict_cream = {'name': 'Gideon Simiyu', 'weekly intake': 6, 'favourite ice creams': ['Chocolate','vanilla','strawberry']}
```


```python
type(dict_cream)
```




    dict




```python
print(dict_cream)
```

    {'name': 'Gideon Simiyu', 'weekly intake': 6, 'favourite ice creams': ['Chocolate', 'vanilla', 'strawberry']}
    


```python
dict_cream.values()
```




    dict_values(['Gideon Simiyu', 6, ['Chocolate', 'vanilla', 'strawberry']])




```python

```


```python

```


```python
dict_cream.keys()
```




    dict_keys(['name', 'weekly intake', 'favourite ice creams'])




```python

```


```python

```


```python
dict_cream.items()
```




    dict_items([('name', 'Gideon Simiyu'), ('weekly intake', 6), ('favourite ice creams', ['Chocolate', 'vanilla', 'strawberry'])])




```python

```


```python
dict_cream['name']
```




    'Gideon Simiyu'




```python

```


```python

```


```python
dict_cream['weekly intake']
```




    6




```python

```


```python
# updates a name 

dict_cream['name'] = 'Caroline Kamau Mbuo'

print(dict_cream)
```

    {'name': 'Caroline Kamau Mbuo', 'weekly intake': 6, 'favourite ice creams': ['Chocolate', 'vanilla', 'strawberry']}
    


```python

```


```python
# It didn't delete the other keywords
#It just added to it



dict_cream.update({'name': 'Caroline Kamau Mbuo', 'weekly intake': 6, 'weight': ['450 pounds']})



print(dict_cream)

```

    {'name': 'Caroline Kamau Mbuo', 'weekly intake': 6, 'favourite ice creams': ['Chocolate', 'vanilla', 'strawberry'], 'weight': ['450 pounds']}
    


```python
{'name': 'Caroline Kamau Mbuo', 'weekly intake': 6, 'favourite ice creams': ['Chocolate', 'vanilla', 'strawberry']}

```


```python

```


```python

```


```python
dict_cream.update({'name': 'Caroline Kamau Mbuo', 'weekly intake': 6, 'favorite ice creams': ['Chocolate', 'vanilla', 'strawberry']})

print(dict_cream)

```

    {'weekly intake': 6, 'favourite ice creams': ['Chocolate', 'vanilla', 'strawberry'], 'name': 'Caroline Kamau Mbuo', 'favorite ice creams': ['Chocolate', 'vanilla', 'strawberry']}
    


```python
del dict_cream['name']

print(dict_cream)
```

    {'weekly intake': 6, 'favourite ice creams': ['Chocolate', 'vanilla', 'strawberry']}
    


```python

```


```python
dict_cream.update({'name': 'Caroline Kamau Mbuo', 'weekly intake': 6, 'weight': ['349 pounds']})

print(dict_cream)                                                                                 

```

    {'weekly intake': 6, 'favourite ice creams': ['Chocolate', 'vanilla', 'strawberry'], 'name': 'Caroline Kamau Mbuo', 'favorite ice creams': ['Chocolate', 'vanilla', 'strawberry'], 'weight': ['349 pounds']}
    


```python
del dict_cream['weight']

print(dict_cream)
```

    {'weekly intake': 6, 'favourite ice creams': ['Chocolate', 'vanilla', 'strawberry'], 'name': 'Caroline Kamau Mbuo', 'favorite ice creams': ['Chocolate', 'vanilla', 'strawberry']}
    


```python

```
