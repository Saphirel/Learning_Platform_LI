import sys
import random
import string
from math import *

def write_in_file(string):
    with open('generated_test_csv.csv', 'w') as f:
        f.write(string)
        f.close()

def get_random_string(length):
    letters = string.ascii_lowercase
    return''.join(random.choice(letters) for i in range(length))

n = sys.argv[1]
res = ""

for i in range(0, 4):
    for j in range(0, 20 +i):
      fn = "P " + str(i) + "-" + str(j)
      ln = "N"
      res = res + fn + "," + ln + "," + fn + ln + "@truc.com," + chr(65 + i) + ",fr\n"

write_in_file(res)
