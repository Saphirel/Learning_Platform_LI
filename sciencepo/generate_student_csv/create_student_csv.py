# coding=UTF-8

import sys
import random
import string

##################################
# Student class
##################################
class Student:

    def __init__(self, lastName, firstName, mail, classNumber, language):
        self.lastName = lastName
        self.firstName = firstName
        self.mail = mail
        self.classNumber = classNumber
        self.language = language
        self.groupNumber = ""

    def __str__(self):
        return "Name: " + self.firstName + " " + self.lastName + "\nMail: " + self.mail + "\nClass:" + self.classNumber + "\nGroup: " + str(self.groupNumber) + "\nLanguage: " + self.language + "\n"
    
    def toCSV(self):
        return self.lastName + "," + self.firstName + "," + self.mail + "," + get_random_string(8) + "," + str(self.groupNumber +1) + self.classNumber + "," + self.language + ",<memberId>"

class Promo:

    def __init__(self, students, classNumber):
        self.students = students
        self.classNumber = classNumber

###################################
# File functions
###################################
def open_csv(fileName):
    try:
        f = open(fileName, "r")
        file_content = f.read().splitlines()
    except IOError:
        print("Error : Invalid file.")
        sys.exit(0)
    return file_content

def open_and_split_csv(fileName):
    try:
        f = open(fileName, "r")
        file_content = f.read().splitlines()[0]
    except IOError:
        print("Error : Invalid file.")
        sys.exit(0)
    return file_content.split(",")

def write_in_file(string):
    with open('processed_students.csv','w') as f:
        f.write(string)
        f.close()

####################################
# Usefull functions
####################################
def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def create_students_array(parsed_file):
    students = []
    
    for l in parsed_file:
        sl = l.split(",")
        tmp_student = Student(sl[0], sl[1], sl[2], sl[3], sl[4])
        students.append(tmp_student)

    return students

def create_students_promos_dict(students_array):
    students_dictionnary = {}

    for s in students_array:
        if s.classNumber in students_dictionnary:
            students_dictionnary[s.classNumber].append(s)
        else:
            students_dictionnary[s.classNumber] = [s]
    
    return students_dictionnary

def create_groups_for_promo(classNumber, students):
    groups = {}
    n = len(students) /4
    for i in range(0, 4):
        groups[i] = []
        for j in range(5*i, i*5+n):
            students[j].groupNumber = i
            groups[i].append(students[j])

    spare = len(students) -4*n
    for i in range(0, spare):
        students[i + 4*n].groupNumber = i
        groups.get(i).append(students[i + 4*n])

def print_groups_dict(groups_dict):
    print "\nGROUPS : "
    for g in groups_dict:
        print("\n------ Group " + str(g))
        for s in groups_dict.get(g):
            print(s)

def show_help():
    print "How to use :\n"
    print "python create_csv.py <students data CSV file>\n"
    print "Exemple : python create_csv.py students.csv"

def check_arguments(argv):
    if len(argv) < 2:
        show_help()
        sys.exit(0)
    else:
        main_process(argv[1])

def main_process(students_csv_file):
    students_array = create_students_array(open_csv(students_csv_file))

    dict_students_by_promo = create_students_promos_dict(students_array)
    for p in dict_students_by_promo:
        create_groups_for_promo(p, dict_students_by_promo.get(p))

    csv_string = ""
    for g in dict_students_by_promo:
        for s in dict_students_by_promo.get(g):
            csv_string = csv_string + "\n" + s.toCSV()

    csv_string = "Prénom,Nom,Email,Password,Numéro de groupe,Langue,Membership ID\n" + csv_string[1:] + "\n"
    write_in_file(csv_string)

###########################
# Program
###########################
check_arguments(sys.argv)
