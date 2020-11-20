# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:29:00 2020

@author: ficau
"""

from grammar import Grammar
def print_menu():
    print("0. Exit")
    print("1. Show non terminals")
    print("2. Show terminals")
    print("3. Show productions")
    print("4. Production for a given nonterminal")
    
    
if __name__ == '__main__':
    
    grammar = Grammar.read_file("g2.txt")
    
    while True:
        print_menu()
        x = int(input())
        if x == 1:
            grammar.print_non_terminals()
        elif x == 2:
            grammar.print_terminals()
        elif x == 3:
            grammar.print_productions()
        elif x == 4:
             n = str(input("Enter non-terminal: "))
             grammar.print_productions_for_given_nonterminal(n)
        else:
            break
    
    
    