#!/usr/bin/env python

import os
import numpy

data = numpy.loadtxt(fname='housing.data.txt',delimiter='   ')

print(data.type)