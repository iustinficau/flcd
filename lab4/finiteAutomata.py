# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:42:24 2020

@author: ficau
"""


class FiniteAutomata:
    
    def __init__(self,Q,E,q0, F, S):
        self.Q = Q
        self.E = E
        self.q0 = q0
        self.F = F
        self.S = S
        
    def parse_line(line):
        return line.strip().split(' ')[2:]
    
    
    def print_states(self):
        string = ""
        for i in self.Q:
            string+= str(i) + ", "
        print(string)
        
    def print_alphabet(self):
        string = ""
        for i in self.E:
            string+= str(i) + ", "
        print(string)
        
    def print_initial_state(self):
        print(self.q0)
        
    def print_transitions(self):
        string = ""
        for i in self.S:
            string+= "(" + str(i[0][0]) + ", " + str(i[0][1]) + ") " + "-> " +str(i[1]) + "\n" 
        print(string)
        
    def print_final_states(self):
        string = ""
        for i in self.F:
            string+= str(i) + ", "
        print(string)
        
    def read_fa(file):
        with open(file) as f:
            Q = FiniteAutomata.parse_line(f.readline())
            E = FiniteAutomata.parse_line(f.readline())
            q0 = FiniteAutomata.parse_line(f.readline())
            F = FiniteAutomata.parse_line(f.readline())
            
            f.readline()
            
            S = []
            
            for line in f:
                src = line.strip().split('->')[0].strip().replace('(',' ').replace(')',' ').split(',')[0]
                route = line.strip().split('->')[0].strip().replace('(',' ').replace(')',' ').split(',')[1]
                dist = line.strip().split('->')[1].strip()
                
                S.append(((src,route), dist))
                
            return FiniteAutomata(Q,E,q0,F,S)
        
 

    