import doctest
def get_biggest(a:int, b:int, c:int)->int:
    '''
    returns biggest of three integers
    >>> get_biggest(7,8,9)
    9
    >>> get_biggest(4,2,3)
    4
    >>> get_biggest(2,0,2)
    2
    >>> get_biggest(7,7,7)
    7
    '''
    if (a>=b) and (a>=c):
        return a
    elif (b>=c):
        return b
    else:
        return c
    
def get_smallest(a:int, b:int, c:int)->int:
    '''
    returns smallest of three integers
    >>> get_smallest(7,8,9)
    7
    >>> get_smallest(4,2,3)
    2
    >>> get_smallest(2,0,2)
    0
    >>> get_smallest(7,7,7)
    7
    '''
    if (a<=b) and (a<=c):
        return a
    elif (b<=c):
        return b
    else:
        return c

def is_multiple_of(n1:int, n2:int)-> bool:
    '''
    returns whether or not argument one is a multiple of arument two
    >>> is_multiple_of(4,2)
    True
    >>> is_multiple_of(7,4)
    False
    >>> is_multiple_of(0,2)
    True
    >>> is_multiple_of(5,5)
    True
    '''
    if (n2 == 0):
        if n1 == 0:
            return True
        else:
            return False
    return (n1%n2 == 0)

def is_biggest_multiple_of_smallest(a: int, b:int, c:int)->bool:
    '''
    takes the biggest value and returns if it is a multiple of 
    the smallest given value

    >>> is_biggest_multiple_of_smallest(6,4,3)
    True
    >>> is_biggest_multiple_of_smallest(2,5,3)
    False
    >>> is_biggest_multiple_of_smallest(0,5,8)
    False
    >>> is_biggest_multiple_of_smallest(6,6,6)
    True
    >>> is_biggest_multiple_of_smallest(18,4,4)
    False
    '''
    big = get_biggest(a,b,c)
    small = get_smallest(a,b,c)
    return is_multiple_of(big,small)

def get_discount(code:str,membership:bool)->float:
    '''
    retuns the ammount of disount depending on
    discount codes and buyer's membership

    >>> get_discount("FREQUENT_BUYER",True)
    2
    >>> get_discount("FREQUENT_BUYER",False)
    0
    >>> get_discount("FIRST_PURCHASE",True)
    10
    >>> get_discount("FIRST_PURCHASE",False)
    10
    >>> get_discount("sdvjdjv",True)
    0
    '''
    if (code == "FIRST_PURCHASE"):
        return 10
    elif (membership and (code == "FREQUENT_BUYER")):
        return 2
    else:
        return 0
    
def get_discounted_price(code:str,price: float,membership:bool)->float:
    '''
    returns the discounted price of purchase

    >>> get_discounted_price("FREQUENT_BUYER", 16, True)
    14
    >>> get_discounted_price("FREQUENT_BUYER", 16, False)
    16
    >>> get_discounted_price("FIRST_PURCHASE", 16, True)
    6
    >>> get_discounted_price("FIRST_PURCHASE", 16, False)
    6
    >>> get_discounted_price("vkajva", 16, True)
    16

    '''
    discount = get_discount(code,membership)
    total = price - discount
    if (total < 0):
        return 0
    else:
        return total

def get_shipping(membership:bool,country:str,price:float)->float:
    '''
    returns shipping price of an order

    >>> get_shipping_price(True,"Uruguay",16)
    0
    >>> get_shipping_price(True,"Canada",16)
    0
    >>> get_shipping_price(False,"Uruguay",16)
    1.6
    >>> get_shipping_price(False,"Canada",16)
    0
    >>> get_shipping_price(False,"Uruguay",0)
    0.0
    

    '''
    if (membership or country == 'Canada'):
        return 0
    else:
        return price*0.1
    
def display_charges(price:float, tax:float, membership: bool, code:str, country: str)-> None:
    '''
    Displays bill for online website.
    >>> display_charges(22.0, 8, False, 'FIRST_PURCHASE', 'Mexico')
    price: $ 12.00
    tax: $ 0.96
    shipping: $ 2.20
    total charge: $ 15.16

    >>> display_charges(0, 5, False, 'NO_DISCOUNT', 'Mexico')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00

    >>> display_charges(10, 50, False, 'FREQUENT_BUYER', 'Mexico')
    price: $ 10.00
    tax: $ 5.00
    shipping: $ 1.00
    total charge: $ 16.00

    >>> display_charges(10, 50, True, 'FREQUENT_BUYER', 'Mexico')
    price: $ 8.00
    tax: $ 4.00
    shipping: $ 0.00
    total charge: $ 12.00
'''
    total = get_discounted_price(code,price,membership)
    tot_tax = total*(tax/100)
    
    print(f"price: $ {get_discounted_price(code,price,membership):.2f}")
    print(f"tax: $ {tot_tax:.2f}")
    print(f"shipping: $ {get_shipping(membership,country,price):.2f}")
    print(f"total charge: $ {total+get_shipping(membership,country,price)+tot_tax:.2f}")

