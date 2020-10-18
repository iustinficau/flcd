# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:58:51 2020

@author: ficau
"""


from symboltable import SymTable

if __name__ == "__main__":   
        
    test_symTable = SymTable()
    
    test_symTable.insert("something",34)
    test_symTable.insert("something", 49)
    test_symTable.insert("somethingElse", 47)
    test_symTable.insert("something", 345)
    index, values = test_symTable.find("something")
    print("Position: " + str(index) + " Values: " + str(values)  )
    

    test_symTable.remove("something")
