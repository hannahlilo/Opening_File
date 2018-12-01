# -*- coding: utf-8 -*-

#%% Opening Files

file = open("data.txt")

for line in file:
    print(line)    # without int double space is printed between lines



#%% 

try:
    file = open("data.txt")
    
    for line in file:
        print(line * 2)

except Exception:
    print("File doesn't exist")
    

#%%

try:
    file = open("data.txt")
    
    for line in file:
        print(int(line) * 2)

except Exception:
    print("File doesn't exist")


#%% Print in Upper Letters (HW Session 17 - Blue Belt)

def print_file_uppercase(filename):
    try:
        file = open(filename)
        
        for line in file:
            print(line.upper().strip())         #.strip() to eliminate double lines and white spaces
    
    except Exception:
        print("File doesn't exist")


print_file_uppercase("data.txt")

#%% Parse CSV

def parse_csv(filename, separator = ","):
    try:
        file = open(filename)
        csv = []
            
        for line in file:               # line is a string containing all the row (i.e pepe, garcia, 28, spain)
            csv.append(line.strip().split(separator))
    
        return csv

    except Exception:
        print("something went wrong")

csv = parse_csv("data.txt")

def sum_age(filename):
    
    age = 0
    
    for line in csv :
        age += int(line[2])


parse_csv("data.txt")










