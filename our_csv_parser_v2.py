#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        value = [] 
        value.append([float(values[0])])
        value.append([float(values[1])])
        value.append([float(values[2])])
        value.append([int(values[3])])
        value.append([float(values[4])])
        value.append([float(values[5])])
        value.append([float(values[6])])
        value.append([float(values[7])])
        value.append([int(values[8])])
        value.append([float(values[9])])
        value.append([float(values[10])])
        value.append([float(values[11])])
        value.append([float(values[12])])
        value.append([float(values[13])])
        print(value)


        #newlist = [t(x) for t,x in zip(value,values)]
       