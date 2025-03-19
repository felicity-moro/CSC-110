import doctest
from student import Student

def get_students(filename:str)->list[Student]:
    """
    creates student objects from a file and returns them as a list
    """
    student_lst = []
    file_handle = open(filename,'r')
    for line in file_handle:
        line = line.strip()
        info = line.split(',')
        if len(info) != 0:
            s = Student(info[0],info[1])
            student_lst.append(s)
    
    file_handle.close()
    return student_lst

def get_classlist(enrolled:list[Student])->list[str]:
    '''
    takes a list of student onjects and returns a list of their ids
    '''
    student_ids = []
    for person in enrolled:
        student_ids.append(person.get_sid())
    
    return student_ids

def count_above(class_list:list[Student],threshold:int)->int:
    '''
    takes a list of student objects and returns the number of 
    students above a given grade threshold
    '''
    counter = 0

    for person in class_list:
        if person.is_grade_above(threshold):
            counter += 1

    return counter

def get_average_grade(class_list:list[Student])->float:
    '''
    calculates the average grade of students in a given student list
    '''
    total_grade = 0.0
    for person in class_list:
        total_grade += person.get_grade()
    
    return total_grade/len(class_list)