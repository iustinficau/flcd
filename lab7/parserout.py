# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:38:13 2020

@author: ficau
"""
from functools import reduce

class ParserOutput:
    
    def __init__(self, parser):
        self.parser = parser
        
    def parse_pif(self):
        result = self.parser.parse_pif()
        if result is True:
            print("PIF has been parsed succesfully. Parsing tree is: ")
            self.print_derivations_strings()
    
    def print_derivations_strings(self):
        productions_number = self.parser.pi
        my_productions = []
        for number in productions_number[1:]:
            for key, value in self.parser.productions.items():
                if value == number:
                    my_productions.append(key)      
        my_productions = list(reversed(my_productions))
        first, rhs = my_productions.pop()
        s = first + '->' + rhs + "->"
        print(s)
        derivation = rhs.split()
        while len(my_productions) > 0:
            lhs, rhs = my_productions.pop()
            position = next(i for i, v in enumerate(derivation) if lhs == v)
            derivation = derivation[:position] + rhs.split() + derivation[position + 1:]
            s = "->" + reduce(lambda x, y : x + " " + y, filter(lambda x: x != "*", derivation))
            
            print(s, end = " ")
        print('*')