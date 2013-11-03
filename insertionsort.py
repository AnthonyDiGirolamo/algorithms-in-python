#!/usr/bin/env python
# coding: utf-8

def insertionsort(array):
    for i in range(1, len(array)):
        value_to_insert = array[i]
        hole_index = i
        while hole_index > 0 and value_to_insert < array[hole_index - 1]:
            array[hole_index] = array[hole_index - 1]
            hole_index -= 1
        array[hole_index] = value_to_insert

