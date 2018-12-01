#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 09:53:58 2018

@author: hannaholdorf
"""

#%% Copy Files (HW Session 18 - Black Belt)

def copy_file(origin, destination):
    
    try:
        origin_file = open(origin)
        destination_file = open(destination, "w")
        
#        if len(origin_file.read()) == 0 
            
        for line in origin_file:
            destination_file.write(line)
        
        destination_file.close()
        
    except Exception:
        print("oups,something went wrong")

copy_file("data.txt", "copy_data.text")