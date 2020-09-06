import sys
import re
import subprocess

class Group:

    def __init__(self, name):
        self.name = name
        self.steps = []

class Step:

    def __init__(self, number, start, stop, questions, answers):
        self.number = number
        self.start = start
        self.stop = stop
        self.questions = questions
        self.answers = answers



#------- Functions
def open_csv(fileName):
    print("Opening file: " + fileName)
    try:
        f = open(fileName, "r")
        file_content = f.read().splitlines()
    except IOError:
        print("Error: Invalid file.")
        sys.exit(0)
    return file_content

def write_in_file(string, fileName):
    with open(fileName + ".tex", "w") as f:
        f.write(string)
        f.close()

def parse_line(line):
    res = [p for p in re.split("(,\\\".*?\\\"|,)", line) if p.strip()]
    return list(filter(lambda x : x != ',', res))

def sanitize_blank_answers(string):
    res = string.replace(",,", ",none,")
    if res != string:
        return sanitize_blank_answers(res)
    else:
        return res

def sanitize_multi_quotes(string):
    res = string.replace('"""', '""')
    if res != string:
        return sanitize_multi_quotes(res)
    else:
        return res

def sanitize_double_quotes(string):
    res = string.replace('""', '&&')
    if res != string:
        return sanitize_multi_quotes(res)
    else:
        return res

def sanitize_csv_line(line):
    line = sanitize_blank_answers(line)
    line = sanitize_multi_quotes(line)
    line = sanitize_double_quotes(line)
    return line

def sanitize_csv(csv):
    j = 0
    while j < len(fileContent):
        csv[j] = sanitize_csv_line(csv[j])
        tmp = csv[j].split("\"")

        n = count_char(csv[j], '"')
        if n % 2 != 0:
            csv[j] = csv[j] + "||" + csv[j +1]
            csv.pop(j +1)
        else:
            j += 1

    return csv

def sanitize_q_n_a(qa):
    qa = qa.replace("&&", '"')
    qa = qa.replace("_", "\_")
    qa = qa.replace("||", " ")
    if qa == "none":
        return ""
    elif qa[:2] == ',"':
        return sanitize_q_n_a(qa[2:])
    elif qa[-1] == '"':
        return sanitize_q_n_a(qa[:-1])
    elif qa[0] == '"':
        return sanitize_q_n_a(qa[1:])
    else :
        return qa

def sanitize_groups(groups):
    for g in groups:
        for s in g.steps:
            for i in range(0, len(s.answers)):
                s.answers[i] = sanitize_q_n_a(s.answers[i])
                s.questions[i] = sanitize_q_n_a(s.questions[i])
    return groups

def count_char(string, char):
    res = 0
    for c in string:
        if c == char:
            res = res +1
    return res

def find_if_group_exists(group_list, group_name):
    for g in group_list:
        if g.name == group_name:
            return True
    return False

def get_group_index_by_name(group_list, group_name):
    for i in range(0, len(group_list) +1):
        if group_list[i].name == group_name:
            return i
    return -1



#------ MAIN
groups = []
tex_template = open("template.tex", "r").read()

for i in range(1, 6):
    fileContent = open_csv("step" + str(i) + ".csv")
    fileContent = sanitize_csv(fileContent)

    questions = parse_line(fileContent[0])
    questions = questions[1:len(questions) -4]

    for j in range(1, len(fileContent)):
        answers = parse_line(fileContent[j])
        start = answers[-3]
        stop = answers[-2]
        group_name = answers[-4]
        answers = answers[1:len(answers) -4]

        if not find_if_group_exists(groups, group_name):
            groups.append(Group(group_name))
        
        groups[get_group_index_by_name(groups, group_name)].steps.append(Step(i, start, stop, questions, answers))

groups = sanitize_groups(groups)

for g in groups:
    res = ""
    group_tex = tex_template.split("<group_number>")
    group_tex = str(g.name).join(group_tex)
    for s in g.steps:
        res = res + "\n\n\section{-- Etape " + str(s.number) + "}"
        for i in range(0, len(s.questions)):
            res = res + "\n\\newline\\newline\\textbf{Question " + str(i +1) + ": }" + s.questions[i] + "\n\\newline\\textbf{Reponse: }" + s.answers[i]
    group_tex = group_tex.split("<text>")
    res = res.join(group_tex)

    write_in_file(res + "\n", g.name)

    test = subprocess.Popen(["/Library/TeX/Root/bin/x86_64-darwin/pdflatex", "-interaction=nonstopmode", g.name + ".tex"])
    test.communicate()[0]
