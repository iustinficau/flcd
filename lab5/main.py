# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:29:00 2020

@author: ficau
"""

from grammar import Grammar
from parser2 import Parser
from parsetable import ParseTable
    
    
def print_menu():
    print("0. Exit")
    print("1. Show non terminals")
    print("2. Show terminals")
    print("3. Show productions")
    print("4. Production for a given nonterminal")
    print("5. First Set ")
    print("6. Follow set")

    
if __name__ == '__main__':

  
    grammar = Grammar.read_file("g1.txt")
    parser = Parser(grammar)

    while True:
        print_menu()
        x = int(input())
        if x == 1:
            print(grammar.get_non_terminals())
        elif x == 2:
            print(grammar.get_terminals())
        elif x == 3:
            print(grammar.get_productions())
        elif x == 4:
             n = str(input("Enter non-terminal: "))
             grammar.print_productions_for_given_nonterminal(n)
        elif x == 5:
            print(parser.get_first_set())
        elif x == 6:
            print(parser.get_follow_set())

        else:
            break
    
    
    