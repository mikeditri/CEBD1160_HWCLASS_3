#!/usr/bin/env python

#import os
#
#
#if os.path.isfile(myfilename):
#    print('yay, I have a file')
#else:
#    print('Boo, I dont have')

myfilename = "housing.data.txt"

with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ',' ').replace('  ',' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        print(values)
        for value in values:
            print(float(value))
        
    print('Finished')
