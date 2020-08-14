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
        self.mentorId = -1

    def __str__(self):
        return "Name: " + self.firstName + " " + self.lastName + "\nMail: " + self.mail + "\nGroup: " + self.groupNumber + "\nLanguage: " + self.language + "\nMembers: " + str(self.groupMembers) + "\nMentorId: " + str(self.mentorId)
    
    def addStudentToGroup(self, name):
        self.groupMembers.append(name)

    def toCSV(self):
        return self.lastName + "," + self.firstName + "," + self.mail + "," + get_random_string(6) + "," + self.groupNumber + "," + self.language + "," + "|".join(self.groupMembers) + "," + str(self.mentorId) + ",5cdf36776b1c26001793aea3"

###################################
# Mentor class
###################################
class Mentor:
    def __init__(self, lastName, firstName, language, groups, mentorId):
        self.lastName = lastName
        self.firstName = firstName
        self.language = language
        self.groups = groups
        self.mentorId = mentorId

    def __str__(self):
        return "Name: " + self.lastName + " " + self.firstName + " Id: " + str(self.mentorId) + " Language: " + self.language

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

def create_mentors_array(parsed_file):
    mentors = []
    mentor_id = 0

    for l in parsed_file:
        sl = l.split(",")
        groups = []
        groups_index = sl[3].split("-")
        for j in range(int(groups_index[0]), int(groups_index[1]) +1):
            groups.append(j)
        mentors.append(Mentor(sl[0], sl[1], sl[2], groups, mentor_id))
        
        mentor_id += 1

    return mentors

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

def assign_mentor_to_student(students_dict, mentors_array):
    for g in students_dict:
        i = 0
        while i < len(mentors_array):
            if int(g) in mentors_array[i].groups:
                for s in students_dict.get(g):
                    s.mentorId = mentors_array[i].mentorId
            i += 1

def print_groups_dict(groups_dict):
    print "\nGROUPS : "
    for g in groups_dict:
        print("\n------ Group " + g)
        for s in groups_dict.get(g):
            print(s)

def print_mentors(mentors_array):
    print "\nMENTORS : "
    for m in mentors_array:
        print(m)
        print(m.groups)

def show_help():
    print "How to use :\n"
    print "python create_csv.py <students data CSV file> <mentors data CSV file>\n"
    print "Exemple : python create_csv.py students.csv mentors.csv"

def check_arguments(argv):
    if len(argv) < 3:
        show_help()
        sys.exit(0)
    else:
        main_process(argv[1], argv[2])

def main_process(students_csv_file, mentors_csv_file):
    students_array = create_students_array(open_csv(students_csv_file))
    mentors_array = create_mentors_array(open_csv(mentors_csv_file))

    dict_students_by_group = create_students_group(students_array)
    create_group_members_list(dict_students_by_group)

    assign_mentor_to_student(dict_students_by_group, mentors_array)

    csv_string = ""
    for g in dict_students_by_group:
        for s in dict_students_by_group.get(g):
            csv_string = csv_string + "\n" + s.toCSV()

    csv_string = "Prénom,Nom,Email,Password,Numéro de groupe,Langue,Membres de Groupe,Mentor,Membership ID\n" + csv_string[1:] + "\n"
    write_in_file(csv_string)

###########################
# Program
###########################
check_arguments(sys.argv)
