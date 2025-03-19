import doctest

def sum_even_values(values:list[int])->int:
    '''
    returns the summed value of the even values in a list of integers.

    >>> sum_even_values([1,2,3,4,5])
    6
    >>> sum_even_values([])
    0
    >>> sum_even_values([5,7,9,7])
    0
    >>> sum_even_values([4,8,4,2])
    18
    '''
    total = 0

    if (len(values) == 0):
        return total
    
    for index in range (len(values)):
        if (values[index]%2 == 0):
            total += values[index]
    
    return total

def count_above(values:list[int],threshold:int)->int:
    '''
    counts ammount of integers that are above the given threshold
    in the given list.

    >>> count_above([1,2,3,4,5,6,7,8,9],5)
    4
    >>> count_above([0,2,3],5)
    0
    >>> count_above([],3)
    0
    >>> count_above([10,11,12,13],9)
    4
    >>> count_above([5,5,5,5,5],4)
    5
    >>> count_above([5,5,5,5,5],5)
    0
    '''

    count = 0
    if (len(values) == 0):
        return count
    
    for index in range (len(values)):
        if (values[index] > threshold):
            count += 1
    
    return count

def add1(values:list[int])->list[int]:
    '''
    adds one to all the integers in the given list.

    >>> add1([2,3,4,5])
    [3, 4, 5, 6]

    >>> add1([])
    []

    >>> add1([-1,-2,-3])
    [0, -1, -2]

    >>> add1([1,1,1,1])
    [2, 2, 2, 2]
    
    '''
    new_values = []
    if (len(values) == 0):
        return new_values
    
    for index in range (len(values)):
        new_values.append(values[index]+1)

    return new_values

def are_all_even(values:list[int])->bool:
    '''
    determines whether or not all integers in a given
    list are even.

    >>> are_all_even([1,2,3,4,5])
    False
    >>> are_all_even([])
    True
    >>> are_all_even([2,2,2,2,2])
    True
    >>> are_all_even([2,4,6,8])
    True
    >>> are_all_even([1,3,5,7])
    False
    '''

    if (len(values) == 0):
        return True
    
    for index in range (len(values)):
        if values[index]%2 != 0:
            return False
    
    return True