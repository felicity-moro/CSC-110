import doctest

def print_name_age_v1()->None:
    """
    asks for your name and age and prints out a greeting, your name, 
    and age category.

    """

    name = str(input('Enter your name: '))
    age = int(input('Enter your age: '))
    acat = ""
    if (age < 18 ):
        acat = "child"
    elif (age >= 18 and age < 65):
        acat = "adult"
    else:
        acat = "senior"

    print(f"hello {name} {acat}")

def print_name_age_v2()->None:

    """
    asks for your name and age and prints out a greeting, your name, 
    and age category.

    """
    name = str(input('Enter your name: '))
    str_age = str(input('Enter your age: '))
    acat = ""

    if (str_age.isdigit() == False):
        print ("you are lying about your age")
        return
    
    age = int(str_age)

    if age < 0:
        print ("you are lying about your age")
    elif (age < 18 ):
        acat = "child"
    elif (age >= 18 and age < 65):
        acat = "adult"
    else:
        acat = "senior"

    print(f"hello {name} {acat}")

def get_num(n: int, prompt:str)->int:
    """
    will ask for an integer that is more than the given integer with the 
    given promt. Will print the first integer that meets this condition.

    """
     
    correct = False

    while not correct:
        input_str = str(input('{prompt} '))
        if (input_str.isdigit() == True):
            value = int(input_str)
            if value >= n:
                return value
            else:
                correct = False

def print_name_age_v3()->None:

    """
    asks for your name and age and prints out a greeting, your name, 
    and age category.

    """
    
    name = str(input('Enter your name: '))
    age = get_num(0,"Enter your age:")
    acat = ""

    if age < 0:
        print ("you are lying about your age")
    elif (age < 18 ):
        acat = "child"
    elif (age >= 18 and age < 65):
        acat = "adult"
    else:
        acat = "senior"

    print(f"hello {name} {acat}")
