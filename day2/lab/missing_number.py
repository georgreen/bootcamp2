#!/usr/bin/env python3

def find_missing(list_1, list_2):
    '''
    input -> two lists
    output -> list_2[index] != list_1[index]
    '''
    hashTable = {}
    hashTable_2 = {}
    #insert everything in hashTable(elminates any duplicates)
    for elem in list_1:
        if elem not in hashTable:
            hashTable[elem] = elem

    for elem in list_2:
        if elem not in hashTable_2:
            hashTable_2[elem] = elem
    #search for elements in hashTable that are missing in hashTable_2
    for elem in hashTable:
        if elem not in hashTable_2:
            return elem
    #search hashTable for elem in hashTable_2 :return any missing
    for elem in hashTable_2:
        if elem not in hashTable:
            return elem
    return 0
