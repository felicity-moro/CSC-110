import doctest
Person = tuple[str,float]
NAME = 0
AGE = 1

people = [("tokyo",4),("Rupert baby",4),("Ian",14)]

def file_to_person_list(filepath:str)->list[Person]:
    '''
    Reads a file with names and ages and creates and returns a
    list of tuples with their information
    
    >>> file_to_person_list("lab8-name-age.txt")
    [('Lynden', 6.0), ('Tian', 27.0), ('Daljit', 18.0), ('Jose', 53.0), ('Jingwen', 17.0), ('Rajan', 65.0)]
    '''

    file_handle = open(filepath , 'r')
    line = file_handle.readline()
    people = []
    while line != '':

        info = line.split(' ')
        name = info[NAME]
        age = float(info[AGE])
        person = (name,age)
        people.append(person)

        line = file_handle.readline()

    file_handle.close()
    return people

def get_average_age(people:list[Person])->int:
    '''
    takes a list of people and returns the average age between them
    Precondion: list is not empty.

    >>> people = file_to_person_list("lab8-name-age.txt")
    >>> get_average_age(people)
    31

    >>> get_average_age([('a',5),('a',5),('a',5),('a',5)])
    5
    '''

    total_age = 0.0
    total_people = 0
    for person in people:
        total_age += person[AGE]
        total_people += 1

    average_age = total_age//total_people
    return int(average_age)

def get_above_age(people:list[Person],threshold:int)->list[Person]:
    '''
    takes a list of people tuples and a threshold and returns a new
    list of people whos ages are over the given threshold

    >>> people = file_to_person_list("lab8-name-age.txt")
    >>> get_above_age(people,19)
    [('Tian', 27.0), ('Jose', 53.0), ('Rajan', 65.0)]

    >>> get_above_age(people,5)
    [('Lynden', 6.0), ('Tian', 27.0), ('Daljit', 18.0), ('Jose', 53.0), ('Jingwen', 17.0), ('Rajan', 65.0)]

    >>> get_above_age(people,42)
    [('Jose', 53.0), ('Rajan', 65.0)]
    
    >>> get_above_age(people,100)
    []

    '''
    older_people = []

    for person in people:
        if person[AGE] > threshold:
            older_people.append(person)

    return older_people

def to_file(people:list[Person],filename:str)->None:
    '''
    takes a list of people and puts their names and ages
    neatly into a file
    
    '''
    
    file_handle = open(filename,'w')

    for person in people:

        file_handle.write(person[NAME])
        file_handle.write(",")
        file_handle.write(str(int(person[AGE])))
        file_handle.write("\n")

    file_handle.close()
    

def write_names_above_avg_age(input:str,output:str)->None:
    '''
    Takes a file of people information and outputs those who are
    above the average age into a separate(given) file.
    '''

    people = file_to_person_list(input)
    if len(people)!=0:
        average_age = get_average_age(people)
        older_people = get_above_age(people, average_age)
        to_file(older_people,output)
    else:
        to_file([],output)








