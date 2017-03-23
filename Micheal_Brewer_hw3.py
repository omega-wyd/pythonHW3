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


system = sys.argv[0]

def help():
    """
    Help function
    """
    print("Usage is: " + sys.argv[0] + " <file Input>")


def test_arg():
    #url = sys.argv[1]
    
    if isset(sys.argv[1]):
        help()


#Main Function
def main():
    """
    Test Function
    """
    #url = sys.argv[1]
    #print(url)
    test_arg()



if __name__=="__main__":
    # Call Main
    main()

    exit(0)
