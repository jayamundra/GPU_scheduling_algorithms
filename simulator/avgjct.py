# import csv
import sys


inputF = sys.argv[1]

with open(inputF) as file:
    lines = file.readlines()
    lines = lines[1:]

    totalJCT = 0
    for l in lines:
        arr = l.split(",")
        totalJCT += int(arr[7])
    print(inputF, totalJCT/len(lines))