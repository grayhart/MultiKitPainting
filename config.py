# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:18:30 2021

@author: graham
"""

SIBLING_LIST = ['Alan J D Hart', 'Brian F Hart', 'Kenneth Leslie HART']

# Set use names to True to use names rather than Ids for the match lists. 
# If you use names, then a check will be made that there is only one of that name and processing will 
# stop otherwise
USE_NAMES=True

# Example with USE_NAME=False
#BOTH_LIST = ['D-F13C8F58-A50F-498B-8844-A4D74EA40E74', 'D-8FE030CD-9545-4220-B1C6-FA0D853F9B0D', 'D-CC3A5967-8A51-4B85-B7E6-2C24D1F780F6', 
#              'D-FC5DE884-8932-4C50-A07A-7F97CCB7CB0A', 'D-D7958A02-69A3-470D-A066-9FCA0D077D6C' ]
#MATERNAL_LIST = ['D-5CC0AFE3-1301-4CEF-9C76-F457F6F34EA1']
#PATERNAL_LIST = ['D-34A434EA-EE7A-4930-BAAE-1BC3BB8E7FF9']
#ANCESTOR_LIST = ['D-34A434EA-EE7A-4930-BAAE-1BC3BB8E7FF9','D-5CC0AFE3-1301-4CEF-9C76-F457F6F34EA1']

# Example with USE_NAME=True
BOTH_LIST = ['Lesley Ann', 'Graham Michael Hart', 'Rosemary Ann Hart', 'Patrick Kenneth Kehoe', 'Roisin Frances Kehoe']
MATERNAL_LIST = ['Beryl M Martell']
PATERNAL_LIST = ['Lyn Steele']
ANCESTOR_LIST = ['Lyn Steele','Beryl M Martell']


INPUT_FOLDER = 'InputData'
OUTPUT_FOLDER = 'OutputFolder'
