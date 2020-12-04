# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 01:30:32 2020

@author: ficau
"""

from grammar import Grammar

from parsetable import ParseTable
class Parser:
    
    def __init__(self, grammar):
        self.grammar = grammar
        self.first = dict()
        self.follow = dict()
        self.rules = []
        self.productions = dict()
        self.generate_first()
        self.generate_follow()

        
    def get_first_set(self):
        return self.first
    
    def get_follow_set(self):
        return self.follow
        
    def generate_first(self):
        for non_terminal in self.grammar.N:
            self.first[non_terminal] = self.first_of(non_terminal)
            
    def generate_follow(self):
        for non_terminal in self.grammar.N:
            self.follow[non_terminal] = self.follow_of(non_terminal, non_terminal)
            
    def first_of(self, non_terminal):
        if non_terminal in self.first.keys():
            return self.first[non_terminal]
        
        temp = set()
        
        terminals = set(self.grammar.E)
        productions = self.grammar.get_productions_for_given_nonterminal(non_terminal)
        
        for production in productions:
            rule = production[1]
            first = rule.split(" ")[0].strip()
            if first != non_terminal:
                if first == "*":
                    temp.add("*")
                elif first in terminals:
                    temp.add(first)
                else:
                    for f in self.first_of(first):
                        temp.add(f)
        return temp
        
    def follow_of(self, non_terminal, initial_non_terminal):
        if non_terminal in self.follow.keys():
            return self.follow[non_terminal]
        
        temp = set()
        
        terminals = set(self.grammar.E)
        productions = self.grammar.get_productions_for_given_nonterminal(non_terminal)
        
        if non_terminal == self.grammar.S:
            temp.add("$")
            
        for production in productions:
            start = production[0]
            
            rule = [var for var in production[1].split(" ")]
            
            rule_conflict = [non_terminal]
            
            for r in rule:
                rule_conflict.append(r)
                
            if non_terminal in rule and rule_conflict not in self.rules:
                self.rules.append(rule_conflict)
                index = rule.index(non_terminal)
                
                for operation in self.follow_operation(non_terminal, temp, terminals, start, rule, index ,initial_non_terminal):
                   temp.add(operation)
                sub_list = rule[index + 1:]
                
                if non_terminal in sub_list:
                    for op in self.follow_operation(non_terminal, temp, terminals, start, rule, index + 1 + sub_list.index(non_terminal),initial_non_terminal):
                        temp.add(op)
                self.rules.pop()
        return temp

    def follow_operation(self, non_terminal, temp, terminals, start, rule, index, initial_non_terminal):
        if index == len(rule) - 1:
            if start == non_terminal:
                return temp
            
            if initial_non_terminal != start:
                for follow in self.follow_of(start, initial_non_terminal):
                    temp.add(follow)
        else:
            next_n = rule[index+1]
            if next_n in terminals:
                temp.add(next_n)
            else:
                if initial_non_terminal != next_n:
                    temp_first = set()
                    for first in self.first[next_n]:
                        temp_first.add(first)
                    if "*" in temp_first:
                        for operation in self.folow_of(next_n, initial_non_terminal):
                            temp.add(operation)
                        temp_first.remove("*")
                    for first in temp_first:
                        temp.add(first)
                        
        return temp

   
    