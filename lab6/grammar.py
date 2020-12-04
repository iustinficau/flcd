# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:07:29 2020

@author: ficau
"""
class Grammar:
    def __init__(self, N,E,P,S):
        self.N = N # Non-terminals
        self.E = E # Terminals
        self.P = P # Productions
        self.S = S # Starting point
        
    def parse_line(line):
        
        #return what comes after =
        return line.strip().split(' ')[2:]


    def read_file(file):
        with open(file) as f:
            N = Grammar.parse_line(f.readline())
            E = Grammar.parse_line(f.readline())
            S = Grammar.parse_line(f.readline())[0] 
            
            f.readline() 
            
            P = []
            
            for line in f:
                lhs, rhs = line.split('::=')
                lhs = lhs.strip()
                rhs = [value.strip() for value in rhs.split('|')]
                
                for value in rhs:
                    P.append((lhs,value))
                    
        return Grammar(N,E,P,S)
    
    def get_non_terminals(self):
        return self.N
    
    def get_terminals(self):
        return self.E
    
    def get_productions(self):
        return self.P
    
    def get_starting_point(self):
        return self.S
    
    def get_rules_for_production(self, prod_key):
        rules_list = []
        for i in self.P:
            if prod_key == i[0]:
                rules_list.append(i[1])
                
        return rules_list
            
    
    def get_productions_for_given_nonterminal(self, n):
        productions_list = []
        for i in self.P:
           lhs, rhs = i
           if lhs == n:
              productions_list.append(i)
                
        return productions_list
    
    def print_productions_for_given_nonterminal(self, n):
        for i in self.P:
            if i[0] == n:
                print(i)
        

        
            