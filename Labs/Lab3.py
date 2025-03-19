
import math
import doctest
GST = 0.05
PST = 0.10
def get_longer(a:str, b:str)->str:
    '''
    when given two strings, returns the longer string
    >>> get_longer("strawberry","pear")
    'strawberry'
    >>> get_longer("cube","pear")
    'cube'
    >>> get_longer("cube","tuberculosis")
    'tuberculosis'
    '''
    if (len(a) >= len(b)):
        return a
    return b
def get_tax(food:float, alcohol:float)->float:
    '''
    calculates and returns owed tax on food and alcohol purchases
    >>> get_tax(0,0)
    0.0
    >>> get_tax(5,10)
    1.75
    >>> get_tax(20,10)
    2.5
    >>> get_tax(20,0)
    1.0
    '''
    total_tax = (food*GST) + (alcohol*PST)
    return total_tax
def get_bill_share(food:float, alcohol:float, people:int)->float:
    ''''
    returns the price of an evenly split restaurant bill
    
    >>> get_bill_share(0,0,1)
    0.0
    >>> get_bill_share(5,10,1)
    16.75
    >>> get_bill_share(5,10,2)
    8.375
    >>> get_bill_share(20,10,3)
    10.833333333333334
    >>> get_bill_share(20,0,2)
    10.5
    '''
    total_price = food + alcohol + get_tax(food,alcohol)
    return total_price/people