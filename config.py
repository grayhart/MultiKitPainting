# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:18:30 2021

@author: graham
"""

SIBLING_LIST = ['Alan Smith', 'Brian Smith', 'Kenneth Smith']

# Set use names to True to use names rather than Ids for the match lists. 
# If you use names, then a check will be made that there is only one of that name and processing will 
# stop otherwise
USE_NAMES=True

# Example with USE_NAME=False
#BOTH_LIST = ['D-F13C8F58-A50F-498B-8844-A4D74EA434E5', 'D-8FE030CD-8763-4220-B1C6-FA0D853F9B0D', 'D-CC3A5967-3215-4B85-B7E6-2C24D1F780F6', 
#              'D-FC5DE884-9893-4C50-A07A-7F97CCB7CB0A', 'D-D7958A02-9876-470D-A066-9FCA0D077D6C' ]
#MATERNAL_LIST = ['D-5CC0AFE3-2342-4CEF-9C76-F457F6F34EA1']
#PATERNAL_LIST = ['D-34A434EA-2312-4930-BAAE-1BC3BB8E7FF9']
#ANCESTOR_LIST = ['D-34A434EA-3453-4930-BAAE-1BC3BB8E7FF9','D-5CC0AFE3-3211-4CEF-9C76-F457F6F34EA1']

# Example with USE_NAME=True
BOTH_LIST = ['Lesley Ann', 'Graham Jones', 'Marvin Hart']
MATERNAL_LIST = ['Beryl French']
PATERNAL_LIST = ['Lyn Bottle']
ANCESTOR_LIST = ['Lyn Bottle','Beryl French']


INPUT_FOLDER = 'InputData'
OUTPUT_FOLDER = 'OutputFolder'
