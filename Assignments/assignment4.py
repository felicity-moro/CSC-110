import doctest

def get_factors(n:int)->str:
    '''
    when given an int, returns the factors of that int
    Precondition: n must be greater than zero

    >>> get_factors(4)
    '1,2,4'
    >>> get_factors(1)
    '1'
    >>> get_factors(9)
    '1,3,9'
    >>> get_factors(21)
    '1,3,7,21'
    '''
    factors = ""

    for count in range (1,n+1):
        if (n%count == 0):
            factors += str(count)
            if (count != n):
                factors += ","
    return factors

def get_range_of_factors(start:int,end:int)->str:
    '''
    given a start and an end point, will return the factors of the numbers
    in that range. 
    preconditon: all arguments > 0

    >>> get_range_of_factors(1,3)
    '1
    1,2'

    >>> get_range_of_factors(1,1)
    ''

    >>> get_range_of_factors(3,9)
    '1,3
    1,2,4
    1,5
    1,2,3,6
    1,7
    1,2,4,8'
            
    >>> get_range_of_factors(10,13)
    '1,2,5,10
    1,11
    1,2,3,4,6,12'

    '''
    factors = ""
    for count in range (start,end):
        factors += get_factors(count)
        factors += "\n"
    return factors

def sum_fibonacci_sequence(n:int)->int:
    '''
    when given a value, returns the sum of numbers in a fibonacci sequence until 
    that value.

    >>> sum_fibonacci_sequence(7)
    20
    >>> sum_fibonacci_sequence(0)
    0
    >>> sum_fibonacci_sequence(2)
    1
    >>> sum_fibonacci_sequence(1)
    0
    >>> sum_fibonacci_sequence(5)
    7
    '''
    if n == 0:
        return 0 

    if n == 1:
        return 0
    
    if n == 2:
        return 1
    
    sequence = 1
    prev_value = 0
    value = 1
    holder = prev_value

    for count in range (2,n):
        prev_value = value
        value = holder + value
        holder = prev_value
        sequence += value
    return sequence

#FOR PART TWO

def print_tail(size:int)->None:
    """
    Prints the tail depending on given size

    Precondition: size is not negative
    """
    tail = "//  "

    if size == 0:
        print("//  \\\\") 
        return

    for burst in range (1,size+1):
        tail += "/\\  "
    
    tail += "\\\\"
    print(tail)

def print_booster(size:int)->None:
    """
    Prints the booster depending on given size
    
    Precondition: size is not negative
    """
    booster = "|"
    dot = "."
    triangle = "/\\"
    dot_amm = size
    triangle_amm = 0

    line = "|"
    
    for initial in range (size+1):
        line += (dot)*dot_amm
        line += (triangle)*(triangle_amm+1)
        line += dot*(dot_amm*2)
        line += (triangle)*(triangle_amm+1)

        line += (dot)*dot_amm
        line += "|"
        print(line)
        dot_amm -= 1
        triangle_amm += 1
        line = "|"

    booster = "|"
    dot = "."
    upside_triangle = "\\/"
    dot_amm = 0
    triangle_amm = size

    for second in range (size+1):
        line += (dot)*dot_amm
        line += (upside_triangle)*(triangle_amm+1)
        line += dot*(dot_amm*2)
        line += (upside_triangle)*(triangle_amm+1)

        line += (dot)*dot_amm
        line += "|"
        print(line)
        dot_amm += 1
        triangle_amm -= 1
        line = "|"
    
    last_line = "+"
    for last in range ((size*2)+2):
        last_line += "=*"
    last_line += "+"
    print(last_line)

def print_instrument_unit(size:int)->None:
    """
    Prints the instrument depending on given size
    
    Precondition: size is not negative
    """
    for base in range (2):
        line = "||"
        for mid in range ((size*2)+1):
            line += "~#"
        line += "||"
        print(line)
    
    last_line = "+"
    for last in range ((size*2)+2):
        last_line += "=*"
    last_line += "+"
    print(last_line)

def print_lem_adapter(size:int)-> None:
    """
    Prints the lem adapter depending on given size
    
    Precondition: size is not negative
    """

    
    line1 = " //"

    if size != 0:
            line1 += " "

    for start in range (size*2):
        line1 += "%"
        if start != size*2-1:
            line1 += " "
    line1 += "\\\\"
    print(line1)

    line2 = "// "

    for start in range ((size*2)+1):
        line2 += "%"
        if start != (size*2):
            line2 += " "
    line2 += "\\\\"
    print(line2)

    last_line = "+"
    for last in range ((size*2)+2):
        last_line += "=*"
    last_line += "+"
    print(last_line)

def print_space_craft(size:int)->None:
    """
    Prints the space craft depending on given size
    
    Precondition: size is not negative
    """
    if size == 0:
        print("  ++  ")
        return
    
    spaces = (size*2)
    tip = ""

    for top in range (spaces+2):
        tip += " "

    tip += "**"

    for top in range (spaces):
        tip += " "

    print(tip)

    slash_amm = 1
    spaces -= 1

    for main in range ((size*2)-1):
        line = ''
        counter = 1
        for space in range (spaces+2):
            line += " "

        
        for left in range (slash_amm):
            line += "/"*counter

        line += "**"

        for right in range (slash_amm):
            line += "\\"*counter

        for space in range (spaces):
            line += " "
        
        counter += 1
        slash_amm += 1
        print(line)
        spaces -= 1

    last_line = "  +"
    for last in range (((size)*2)):
        last_line += "=*"
    last_line += "+"
    print(last_line)
    
def print_rocket_ship(size:int, booster:int)->None:
    """
    Prints the rocket ship depending on given size and ammount
    of booster sections to be printed
    
    Precondition: size and booster ammount is not negative
    """
    print_space_craft(size)
    print_lem_adapter(size)
    print_instrument_unit(size)

    for booster_count in range (booster):
        print_booster(size)

    print_tail(size)