import doctest
import math

def print_longer(a:str, b:str):
    '''
    when given two strings will return the longer string
    >>> print_longer("hat","mouse")
    mouse
    >>> print_longer("shadowman","mouse")
    shadowman
    '''
    if (len(a) >= len(b)):
        print(a) 
    else:
        print(b)

def print_real_roots(a:float, b:float, c:float):
    '''
    Prints the roots of a quadratic equation when given three values.
    Value a must be more than 0.
    >>> print_real_roots(1,6,5)
    -5.000,-1.000
    >>> print_real_roots(0,5,6)
    ERROR
    >>> print_real_roots(5,1,18)
    NO REAL ROOTS
    '''

    if (a == 0):
        print("ERROR")
        return

    discriminant = (b**2) - 4*a*c

    if (discriminant < 0):
        print("NO REAL ROOTS")
        return

    minroot = ((b*-1) - math.sqrt(discriminant))/(2*a)
    addroot = ((b*-1) + math.sqrt(discriminant))/(2*a)
    print(f"{minroot:.3f},{addroot:.3f}")

def print_zodiac_sign(month:str,day:int):
    '''
    when given a month and day, prints out the star sign of the day
    >>> print_zodiac_sign("August",23)
    Virgo
    >>> print_zodiac_sign("November",26)
    Sagittarius
    >>> print_zodiac_sign("January",20)
    Aquarius
    >>> print_zodiac_sign("February",18)
    Aquarius
    >>> print_zodiac_sign("February",19)
    Pisces
    >>> print_zodiac_sign("February",20)
    Pisces
    >>> print_zodiac_sign("March",21)
    Aries
    >>> print_zodiac_sign("April",19)
    Aries
    >>> print_zodiac_sign("April",20)
    Taurus
    >>> print_zodiac_sign("May",21)
    Gemini
    >>> print_zodiac_sign("June",21)
    Cancer
    '''
    if (month == "January"):
        if (day < 20):
            print("Capricorn")
        else:
            print("Aquarius")

    if (month == "February"):
        if (day < 19):
            print("Aquarius")
        else:
            print("Pisces")
    
    if (month == "March"):
        if (day < 21):
            print("Pisces")
        else:
            print("Aries")

    if (month == "April"):
        if (day < 20):
            print("Aries")
        else:
            print("Taurus")
    
    if (month == "May"):
        if (day < 21):
            print("Taurus")
        else:
            print("Gemini")
    
    if (month == "June"):
        if (day < 21):
            print("Gemini")
        else:
            print("Cancer")
    
    if (month == "July"):
        if (day < 23):
            print("Cancer")
        else:
            print("Leo")
    
    if (month == "August"):
        if (day < 23):
            print("Leo")
        else:
            print("Virgo")
    
    if (month == "September"):
        if (day < 23):
            print("Virgo")
        else:
            print("Libra")

    if (month == "October"):
        if (day < 23):
            print("Libra")
        else:
            print("Scorpio")

    if (month == "November"):
        if (day < 22):
            print("Scorpio")
        else:
            print("Sagittarius")

    if (month == "December"):
        if (day < 22):
            print("Sagittarius")
        else:
            print("Capricorn")

            