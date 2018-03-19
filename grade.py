#!/usr/bin/python
# To call this from the command line:
# python grade.py

from subprocess import call
from subprocess import STDOUT
from collections import OrderedDict
from getopt import getopt
import os
import sys
import json
import random

def usage():
    print("grade.py [-n] some_test_binary")
    print("")
    print("    -n : non-interactive. supresses color. meant for autograders.")
    print("")
    print("Examples:")
    print(" $ python grade.py hello_test")
    print(" $ python grade.py -n linked_list_test")

# Be sure the user gave us a binary to test.
if len(sys.argv) < 2:
    usage()
    sys.exit(-1)

# Get the command line arguments and process them.
argv = sys.argv[1:]
try:
    opts, args = getopt(argv, "n")
except(e):
    print(e)
    usage()
    sys.exit(2)

noninteractive = False # default to interactive mode
for opt, arg in opts:
    if opt == '-n':
        print("Non-interactive mode engaged.")
        noninteractive = True # means supress color
binary = args[0]

# Set up some colorization definitions and color printer.
class termcolors:
    CYAN = '\033[36m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @staticmethod
    def get(color, n):
        if n:
            return ''
        else:
            return color

# Load test tags and point values from points.json    
tests = OrderedDict()
try:
    with open('points.json') as point_file:
        top = json.load(point_file)
        points = top['points']
        for entry in points:
            for k in entry.keys():
                tests[k] = entry[k]        
except:
    print ('Couldn\'t open or parse points.json')
    sys.exit(-1)

# Invoke each test tag and record the exit status code    
results = OrderedDict()
failedTests = []
DN = open(os.devnull, 'w')
total_points = 0
try:
    for key, val in tests.items():
        status = call(["./" + binary, "[" + key + "]"], stdout=DN, stderr=STDOUT)
        if status != 0:
            failedTests.append("./" + binary + " \"[" + key + "]\"")
        results[key] = status
        total_points += val
    DN.close()
    print ("")
except:
    print ("Couldn't invoke the unit tests. Did it compile? (hint: type 'make' in your terminal)")
    sys.exit(-1)

# In the event the student has full points, show a happy emoji at the end
def choose_happygram(n):
    if n:
        return '' # return empty string if we're non-interactive
    # choose among the following at random
    happygrams = [
        u'\U0001F389', # party popper
        u'\U0001f604', # grin
        u'\U0001F308', # rainbow
        u'\U0001F60E', # sunglasses
    ]
    idx = random.randint(0, len(happygrams) - 1)
    hg = happygrams[idx]
    return hg.encode('utf-8')

# Tally points earned and print stuff out    
earned_points = 0
for key in results:
    this_points = 0
    if results[key] == 0:
        this_points = tests[key]
    earned_points += this_points
    # chk = ''
    col = termcolors.get(termcolors.WARNING, noninteractive)
    if this_points > 0:
        col = termcolors.get(termcolors.CYAN, noninteractive)
    #     chk = u'\u2713'.encode('utf-8')
    line = "{:<20} {:2} / {:2} ".format(key, str(this_points), str(tests[key])) # + chk
    print(col, line)
print ("===============================")
col = termcolors.get(termcolors.FAIL, noninteractive)
full = False
happygram = ''
if earned_points > 0:
    col = termcolors.get(termcolors.WARNING, noninteractive)
if earned_points == total_points:
    col = termcolors.get(termcolors.OKGREEN, noninteractive)
    happygram = choose_happygram(noninteractive)
    full = True
line = '{:<20} {:2} / {:2} {}'.format('TOTAL', str(earned_points), str(total_points), happygram)
print(line)

# Show a parting message to either submit or how to troubleshoot.
print ("")
if full:
    print ("You should be good to submit your assignment now!")
else:
    print ("Command line(s) to invoke specific failed unit tests follow this message. They")
    print ("will give you much more detailed information about what's wrong with your program.")
    print ("")

for f in failedTests:
    print (f)

# Add final output for the grade. This is for the inginious callback. 
epf = float(earned_points)
tpf = float(total_points)
grade = int((epf / tpf) * 100)
print (str(grade))
