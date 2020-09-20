# coding=UTF-8

import sys
import random
import string

##################################
# Student class
##################################
class Student:

    def __init__(self, lastName, firstName, mail, groupNumber, language):
        self.lastName = lastName
        self.firstName = firstName
        self.mail = mail
        self.groupNumber = groupNumber
        self.language = language
        self.groupMembers = []

    def __str__(self):
        return "Name: " + self.firstName + " " + self.lastName + "\nMail: " + self.mail + "\nGroup: " + self.groupNumber + "\nLanguage: " + self.language + "\nMembers: " + str(self.groupMembers)
    
    def addStudentToGroup(self, name):
        self.groupMembers.append(name)

    def toCSV(self):
        if (self.language == "fr"):
            return self.lastName + "," + self.firstName + "," + self.mail + "," + get_random_string(8) + "," + self.groupNumber + "," + self.language + "," + "|".join(self.groupMembers) + ",5f5dff3aff2c620004579e5d"
        else:
            return self.lastName + "," + self.firstName + "," + self.mail + "," + get_random_string(8) + "," + self.groupNumber + "," + self.language + "," + "|".join(self.groupMembers) + ",5f5dff3aff2c620004579e5d"

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
    return file_content.split(";")

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

def create_students_group(students_array):
    students_dictionnary = {}

    for s in students_array:
        if s.groupNumber in students_dictionnary:
            students_dictionnary[s.groupNumber].append(s)
        else:
            students_dictionnary[s.groupNumber] = [s]
    
    return students_dictionnary

def create_group_members_list(dict_students_by_group):
    for g in dict_students_by_group:
        students = dict_students_by_group.get(g)
        i = 0
        for s in students:
            for j in range(0, len(students)):
                if j != i:
                    s.addStudentToGroup(students[j].firstName + " " + students[j].lastName)
            i += 1

def print_groups_dict(groups_dict):
    print "\nGROUPS : "
    for g in groups_dict:
        print("\n------ Group " + g)
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

    dict_students_by_group = create_students_group(students_array)
    create_group_members_list(dict_students_by_group)

    csv_string = ""
    for g in dict_students_by_group:
        for s in dict_students_by_group.get(g):
            csv_string = csv_string + "\n" + s.toCSV()

    csv_string = "Prénom,Nom,Email,Password,Numéro de groupe,Langue,Membres de Groupe,Membership ID\n" + csv_string[1:] + "\n"
    write_in_file(csv_string)

###########################
# Program
###########################
check_arguments(sys.argv)
