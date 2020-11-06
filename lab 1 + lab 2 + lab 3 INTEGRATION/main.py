# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:58:51 2020

@author: ficau
"""

from symboltable import SymTable
from scanner import Scanner

def read_tokens():
        tokens_table = {}
        tokens = []
        with open("tokens.in", 'r') as f:
            for line in f.readlines():
                row = line.strip().split(',')
                tokens_table[row[0]] = row[1]
                tokens.append(row[0])
        return tokens_table,tokens

def write_pif(data):
    f = open("pif.out","w")
    for i in data:
            f.write(i[0])
            f.write(" -> ")
            f.write(str(i[1]))
            f.write("\n")
    f.close()
    
def write_sym(data):
    f = open("symboltable.out","w")
    f.write("The symtable is represented on a hash table using separate chaining as a resolution method")
    f.write("\n")
    f.write(repr(data))
    f.close()
    
if __name__ == "__main__":
    
     file = open('pr1.txt','r')
     symbolTable = SymTable()
     pif = []
     tokens_table,tokens = read_tokens()
     
     index = 0
     
    
            
     for line in file:
         
         if line[-1] == '\n':
            line = line[0:-1] 
         index += 1
      
         for token in Scanner.get_tokens(line):
             if token in tokens:
                 pif.append([token,-1])
             elif Scanner.check_identifier(token):
                 pif.append([token,symbolTable.insert(token)])
                 
             elif Scanner.check_constant(token):
                 pif.append([token,symbolTable.insert(token)])
             else:
                 print("Unknown token: "  + token + " at line " + str(index))
    
     print(pif)
     print("\n")
     print(symbolTable)
     write_pif(pif)
     write_sym(symbolTable)
     
    
        

        
    
