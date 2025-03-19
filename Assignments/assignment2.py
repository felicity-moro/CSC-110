import doctest

def check_funds(balance:float,purchase:float):
    '''
    When given balance of credit card and cost of purchase, prints remaining balance.
    >>> check_funds(5,2)
    you will have $ 3.00 left after this purchase
    >>> check_funds(9,18)
    you are short $ 9.00
    >>> check_funds(-1, 5)
    you have a negative balance
    >>> check_funds(4,0)
    you will have $ 4.00 left after this purchase

    '''
    if (balance < 0):
        print("you have a negative balance")
        return
    if (purchase > balance):
        y = (-1)*(balance-purchase)
        print(f"you are short $ {y:.2f}")
        return
    else:
        x = balance - purchase
        print(f"you will have $ {x:.2f} left after this purchase")

def print_biggest(a:float, b:float, c:float):
    '''
    when given three numbers, prints the largest number
    >>> print_biggest(4,5,6)
    6
    >>> print_biggest(7,2,6)
    7
    >>> print_biggest(4,4,4)
    4
    >>> print_biggest(3,9,2)
    9
    >>> print_biggest(3,-1,3)
    3
    '''
    if (a >= b and a >= c):
        print(a)
        return
    elif (b >= a and b >= c):
        print(b)
        return
    else:
        print(c)

def convert_inches(inches: float):
    '''
    when given inches, prints its value in miles, yard, feet and inches

    >>> convert_inches(63409)
    1 mi, 1 yd, 1 ft, 1 in
    >>> convert_inches(12)
    0 mi, 0 yd, 1 ft, 0 in
    >>> convert_inches(36)
    0 mi, 1 yd, 0 ft, 0 in
    >>> convert_inches(1)
    0 mi, 0 yd, 0 ft, 1 in
    >>> convert_inches(789423)
    12 mi, 808 yd, 1 ft, 3 in
    '''

    miles = 0
    yards = 0
    feet = 0

    if(inches >= 63360):
        miles = inches//63360
        inches -= (miles*63360)
    
    if(inches >= 36):
        yards = inches//36
        inches -= (yards*36)
        
    if (inches >= 12):
        feet = inches//12
        inches -= (feet*12)
    
    print(f"{miles} mi, {yards} yd, {feet} ft, {inches} in")
    
def is_multiple_of(a: int, b: int):
    '''
    prints out if first argument is a multiple of second argument
    >>> is_multiple_of(8,2)
    8 is a multiple of 2
    >>> is_multiple_of(9,2)
    9 is not a multiple of 2
    >>> is_multiple_of(0,2)
    0 is not a multiple of 2
    >>> is_multiple_of(4,0)
    4 is not a multiple of 0
    '''
    if (b == 0):
        if (a==0):
            print(f"{a} is a multiple of {b}")
        else:
            print(f"{a} is not a multiple of {b}")
        return
    if (a%b == 0):
        print(f"{a} is a multiple of {b}")
    else:
        print(f"{a} is not a multiple of {b}")
    
def display_charges(purchase:float, taxrate: float, member:bool, discode: str, country: str):
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
    price = purchase
    shipping = 0
    total = 0

    if (country != "Canada" and member == False):
        shipping = price*0.10

    if (discode == "FIRST_PURCHASE"):
        price -= 10
    if (discode == "FREQUENT_BUYER" and member == True):
        price -= 2
    
    if (price < 0):
        price = 0
    tax = price*(taxrate/100)

    total = price + tax + shipping


    print(f"price: $ {price:.2f}")
    print(f"tax: $ {tax:.2f}")
    print(f"shipping: $ {shipping:.2f}")
    print(f"total charge: $ {total:.2f}")






 