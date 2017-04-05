#!/usr/bin/env python3

def find_missing(list_1, list_2):
    '''
    input -> two lists
    output -> list_2[index] != list_1[index]
    '''
        
    hashTable = {}
    hashTable_2 = {}
    #insert everything in list_1 into hashTable(elminates any duplicates)
    hashTable = { x : x for x in list_1 if x not in hashTable}
    
    #insert everything in list_2 into hashTable_2(eliminates any duplicates)
    hashTable_2 = { x : x for x in list_2 if x not in hashTable_2}
    
    #make sure hashTable is the largest dictionary
    if len(hashTable_2) > len(hashTable):
        hashTable, hashTable_2 = (hashTable_2, hashTable)
        
    #search for elements in hashTable that are missing in hashTable_2
    for elem in hashTable:
        if elem not in hashTable_2:
            return elem
            
    return 0
