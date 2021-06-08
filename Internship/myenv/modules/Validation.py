# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:04:56 2019

@author: elh
"""

import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import sys
import numpy as np
from openpyxl import Workbook

import xlrd
from openpyxl import load_workbook# set file path

'''
#Read the validation data with openpyxl

filepath="H:/Ali/_Internship/Validation/Anzeigen_Scheibe1_Segment1_Komponente1_2018-06-06.xlsx"# load demo.xlsx 
wb=load_workbook(filepath)# select demo.xlsx
sheet = wb["ESE_Nr.1"]

#sheet=sheet.active# get b1 cell value

for cell in source['A']:
    print(cell.value)
'''

'''Read the validation data with pandas'''

filepath="H:/Ali/_Internship/Validation/Anzeigen_Scheibe1_Segment1_Komponente1_2018-06-06.xlsx"# load demo.xlsx 
dataFrame = pd.read_excel(filepath, sheet_name = 'ESE_Nr.1')

xy = dataFrame.iloc[112:,1:3].copy()
print(xy.as_matrix())
