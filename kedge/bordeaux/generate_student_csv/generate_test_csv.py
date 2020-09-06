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

for i in range(0, int(n) -1):
    fn = get_random_string(5)
    ln = get_random_string(10)
    res = res + fn + "," + ln + "," + fn + ln + "@truc.com," + str(random.randint(1, ceil(int(n)/5))) + ",fr\n"

write_in_file(res)
