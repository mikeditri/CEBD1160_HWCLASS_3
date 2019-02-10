#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        value = []
        value.extend([float(values[0])])
        value.extend([float(values[1])])
        value.extend([float(values[2])])
        value.extend([int(values[3])])
        value.extend([float(values[4])])
        value.extend([float(values[5])])
        value.extend([float(values[6])])
        value.extend([float(values[7])])
        value.extend([int(values[8])])
        value.extend([float(values[9])])
        value.extend([float(values[10])])
        value.extend([float(values[11])])
        value.extend([float(values[12])])
        value.extend([float(values[13])])
        thelist = list(value)
        print(value)


        #newlist = [t(x) for t,x in zip(value,values)]
       