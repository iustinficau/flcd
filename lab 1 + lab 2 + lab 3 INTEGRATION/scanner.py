# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:00:34 2020

@author: ficau
"""
import re

class Scanner:
    
    
    def get_tokens(line):
        separators = ['{','}',';','(',')',':','[',']',' ',',', '"']
        token = ''
        i = 0
        while i < len(line):
            
            if line[i] == '"':
                if token:
                    yield token
                token,i= Scanner.get_string(line,i )
                yield token
                token = ''
                
            elif line[i] in separators:
                if token:
                    yield token
                token, i = line[i], i + 1
                if token == ";":
                    yield token
                token =  ''
            elif Scanner.check_operator(line[i]):
               # if token:
              #      yield token
                token,i = Scanner.get_operator(line,i)
                yield token
                token = ''
            else:
                token += line[i]
                i += 1
        
        if token:
            yield token
                
    
    def check_identifier(token):
        return re.match(r"^[a-zA-Z]([a-zA-Z]|[0-9]|_){,15}$", token) is not None
        
    def check_constant(token):
        return re.match('^(0|[+-]?[1-9][0-9]*)$', token) is not None or re.match('^\".*\"$', token) is not None
    
    def check_operator(token):
        operators = ['*','+','+=','>=','=','==','<=','<','>','-=','*=','/','%']
        return token in operators
    
    def get_string(line, index):
        
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '"':
                quotes += 1
            token += line[index]
            index += 1

        return token, index
    
    def get_operator(line,index):
        
        token = ''
        
        while index < len(line) and Scanner.check_operator(line[index]):
            token += line[index]
            index += 1

        return token, index