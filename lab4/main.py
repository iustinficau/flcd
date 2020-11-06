# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:42:03 2020

@author: ficau
"""
from finiteAutomata import FiniteAutomata

def print_menu():
    
    print("1. Show the set of states")
    print("2. Show the alphabet")
    print("3. Show the transitions")
    print("4. Show the final states")
    print("0. Exit")
    
    
if __name__ == "__main__":
    fa = FiniteAutomata.read_fa("FA.in")
    
    while(True):
        print_menu()
        i = int(input())
        if i == 1:   
            fa.print_states()
        elif i == 2:
            fa.print_alphabet()
        elif i == 3:
            fa.print_transitions()
        elif i == 4:
            fa.print_final_states()
        elif i == 0:
            break
        