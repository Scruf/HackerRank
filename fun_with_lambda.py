#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr.sort()
print n
while len(arr) > 1:
    arr = filter(lambda x: x-arr[0], arr)
    counter = len(arr)
    if counter is not 0:
        print counter

