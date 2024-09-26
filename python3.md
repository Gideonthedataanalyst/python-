# Functions


```python
def first_func():
    print('We did it!')
```


```python
first_func()
```

    We did it!
    


```python
def number_squared(number):
    print(number**2)
    
```


```python
number_squared(7)
```

    49
    


```python
number_squared(12)
```

    144
    


```python

```


```python
def number_squared_cust(number,power):
    print(number**power)
```


```python
number_squared_cust(3,5)
```

    243
    


```python

```

# Arbitrary arguments


```python
def number_args(*number):
    print(number[0]*number[1])
```


```python
number_args(5,12,1,5,8)
```

    60
    


```python

```


```python
args_tuple = (5,12,1,5,8)

def number_args(*number):
    print(number[0]*number[1])


```


```python
number_args(5,12,1,5,8)
```

    60
    


```python

```


```python
args_tuple = (5,12,1,5,8)

def number_args(*number):
    print(number[0]*number[1])

```


```python
number_args(*args_tuple)
```

    60
    

# keyword argument


```python
def number_squared_cust(number,power):
    print(number**power)
```


```python
number_squared_cust(power = 3,number = 4)
```

    64
    


```python
def number_kwarg(**number):
    print('My number is: '+ number['integer'])
```


```python
number_kwarg(integer = '2450')
```

    My number is: 2450
    


```python

```


```python
def number_kwarg(**number):
    print('My number is: '+ number['integer'] + 'My other number is: ' + number['integer2'])
```


```python
number_kwarg(integer = '2450', integer2 = '1890')
```

    My number is: 2450My other number is: 1890
    

# converting data types in python


```python
num_int = 9
type(num_int)
```




    int




```python
num_string = '8'
type(num_string)
```




    str




```python
num_string_conv = int(num_string)

type(num_string_conv)
```




    int




```python

```


```python
num_sum = num_int + num_string #cannot add string to integer
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[105], line 1
    ----> 1 num_sum = num_int + num_string
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'



```python

```


```python
num_sum = num_int + (num_string_conv)

print(num_sum)
```

    17
    

# converting lists, sets and tuples


```python
list_type = [1,5,9]

type(list_type)
```




    list




```python
tuple(list_type)
```




    (1, 5, 9)




```python
type(tuple(list_type))
```




    tuple




```python
list_type = [1,5,9,5,1,9,1,5,9]
```


```python
set(list_type)
```




    {1, 5, 9}




```python
type(set(list_type))
```




    set



# dictionaries


```python
dict_type = {'Name': 'Gideon Simiyu','Age': 25, 'Hair': 'N/A'}

type(dict_type)
```




    dict




```python
dict_type.items()

```




    dict_items([('Name', 'Gideon Simiyu'), ('Age', 25), ('Hair', 'N/A')])




```python
dict_type.values()
```




    dict_values(['Gideon Simiyu', 25, 'N/A'])




```python
dict_type.keys()
```




    dict_keys(['Name', 'Age', 'Hair'])




```python
list(dict_type.keys())
```




    ['Name', 'Age', 'Hair']




```python
type(list(dict_type.keys()))
```




    list




```python

```


```python
type(list(dict_type.values()))
```




    list




```python
long_str = 'I like to go out and hangout with my friends'

list(long_str)
```




    ['I',
     ' ',
     'l',
     'i',
     'k',
     'e',
     ' ',
     't',
     'o',
     ' ',
     'g',
     'o',
     ' ',
     'o',
     'u',
     't',
     ' ',
     'a',
     'n',
     'd',
     ' ',
     'h',
     'a',
     'n',
     'g',
     'o',
     'u',
     't',
     ' ',
     'w',
     'i',
     't',
     'h',
     ' ',
     'm',
     'y',
     ' ',
     'f',
     'r',
     'i',
     'e',
     'n',
     'd',
     's']




```python

```


```python
long_str = 'I like to go out and hangout with my friends'

set(long_str)
```




    {' ',
     'I',
     'a',
     'd',
     'e',
     'f',
     'g',
     'h',
     'i',
     'k',
     'l',
     'm',
     'n',
     'o',
     'r',
     's',
     't',
     'u',
     'w',
     'y'}




```python

```


```python

```


```python

```


```python

```
