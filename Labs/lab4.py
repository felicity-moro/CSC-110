import doctest
def compute_harmonic_series(n:int)->float:

    '''
    computes the harmonic series starting at one until
    the given int

    >>> compute_harmonic_series(0)
    0
    >>> compute_harmonic_series(2)
    1.5
    >>> compute_harmonic_series(3)
    1.8333333333333333
    '''
    total = 0

    if (n == 0):
        return 0

    for count in range (1,n+1):
        total += 1/count

    return total

def get_fibonacci_sequence(n:int)->str:
    '''
    gives the fibonacci sequence until the given int
    precondition: n is not negative
    >>> get_fibonacci_sequence(0)
    ''
    >>> get_fibonacci_sequence(1)
    '0'

    >>> get_fibonacci_sequence(2)
    '0,1'

    >>> get_fibonacci_sequence(9)
    '0,1,1,2,3,5,8,13,21'

    >>> get_fibonacci_sequence(10)
    '0,1,1,2,3,5,8,13,21,34'
    '''

    if n == 0:
        return ''

    if n == 1:
        return "0"
    
    if n == 2:
        return "0,1"
    
    sequence = "0,1,"

    prev_value = 0
    value = 1
    holder = prev_value


    for count in range (2,n):
        prev_value = value
        value = holder + value
        holder = prev_value
        sequence += str(value)

        if (count != n-1):
            sequence += ','
            
    return sequence
        



    # sequence = ''
    # if (n == 0):
    #     return sequence
    
    # prev_value = 0
    # value = 0

    # if n >= 1:
    #     value = 0
    #     sequence += '0'
    # if n >= 2:
    #     prev_value = value
    #     value = 1
    #     sequence += ',1'
    #     if n != 2:
    #             sequence += ','

            
    # if n > 2:
    #     for count in range (1, n+1):
    #         prev_value = value
    #         value = count
    #         sequence += str(prev_value+value)
    #         if (count < n):
    #             sequence += ','
    
    # return sequence

def print_pattern(height:int, width:int, a:str, b:str)->None:
    '''
    prints pattern a and b for specified ammount of times for specificed ammount of rows
    
    precondition: height and width are more than zero

    >>> print_pattern(4,3,"!@","$$$")
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@

    >>> print_pattern(1,1,"!@","$$$")
    !@$$$

    >>> print_pattern(1,1,"","")
    <BLANKLINE>

    >>> print_pattern(1,4,"hello","<3")
    hello<3hello<3hello<3hello<3

    >>> print_pattern(2,4,"hello","<3")
    hello<3hello<3hello<3hello<3
    <3hello<3hello<3hello<3hello
    '''
    row1 = ""
    row2 = ""
    
    for count in range (1,(width*2)+1):
        if (count%2 != 0):
            row1 += a
        if (count%2 == 0):
            row1 += b

    for count in range (1,(width*2)+1):
        if (count%2 != 0):
            row2 += b
        if (count%2 == 0):
            row2 += a

    for count in range (1,height+1):
        if (count%2 != 0):
            print(row1)
        if (count%2 == 0):
            print(row2)
    


