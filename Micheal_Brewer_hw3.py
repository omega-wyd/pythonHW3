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


# http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test


def help():
    """
    Help function
    """
    print("Usage is: " + sys.argv[0] + " <file Input>")
    exit(1)

def test_arg():
    if len(sys.argv) > 1:
            url = sys.argv[1]
            return url
    else:
        help()
    
def get_words(url):
    #urlopen(url)
    with urlopen(url) as lines: 
        story_words = []

#Main Function
def main():
    """
    Test Function
    """
    url = test_arg()
    print(url)
    get_url(url)


if __name__=="__main__":
    # Call Main
    main()

    exit(0)
