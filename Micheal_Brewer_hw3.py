#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 student1 <student1@CS3030_87>
#


#===========================================================================
#
#       File: Micheal_Brewer_hw3.py 
#
#       Usage: ./Micheal_Brewer_hw3.py
#
#   Description:
#
#       Options: ---
#       ReqOPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Micheal Brewer (), mbrewerramirez@mail.weber.edu
#  ORGANIZATION:
#       CREATED: 03/03/2017 14:27
#      REVISION:  ---
#===========================================================================

import sys
from urllib.request import urlopen
import re

from collections import Counter
# http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test


def help():
    """
    Help function
    """
    print("Usage is: " + sys.argv[0] + " <file Input>")
    exit(1)

def test_arg():
    """
    Test if arguments was entered into cmd
    if there is a file continue
    if not use help()
    """
    if len(sys.argv) > 1:
            url = sys.argv[1]
            return url
    else:
        help()
    
def get_words(url):
    """
    Takes the file inputed by user and decodes it to utf-8
    Then goes through each line of the file and matches to 4 critiria types.
    it then saves the found matches to a list which is then counted.
    Returns print of top 25 errors found and how many times occured. 
    """
    #urlopen(url)
    with urlopen(url) as log_file: 
        readable_log = []
        for line in log_file:
            readable_log.append(line.decode('utf-8'))
            #print(readable_log)

    errors = []
    for line in readable_log:
        m1 = re.match(r"^.* '(/.*)'.*$", line)
        m2 = re.match(r"^.* (/.*):.*,.*$", line)
        m3 = re.match(r"^.* (/.*), .*$", line)
        m4 = re.match(r"^.*: (/.*)$", line)
        if m1:
            errors.append(str(m1.group(1)))
        elif m2:
            errors.append(str(m2.group(1)))
        elif m3:
            errors.append(str(m3.group(1)))
        elif m4:
            errors.append(str(m4.group(1)))
    topErrs = Counter(errors).most_common(25)                       
    print ("*** Top 25 page errors ***")                
    for x in topErrs:
        print("Count: " + str(x[1]) + "\tPage: " + x[0])



#Main Function
def main():
    """
    Test Function
    """
    url = test_arg()
    #print(url)
    get_words(url)


if __name__=="__main__":
    # Call Main
    main()

    exit(0)
