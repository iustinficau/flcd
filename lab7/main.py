# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:29:00 2020

@author: ficau
"""

from grammar import Grammar
from parser2 import Parser
from parserout import ParserOutput
from parsetable import ParseTable
import re
import json
class FA:
    def __init__(self, fileIn):
        f = open(fileIn, "r")
        lines = f.readlines()
        self._Q = lines[0].split("\n")[0].split(" ")
        self._E = lines[1].split("\n")[0].split(" ")
        self._q0 = lines[2].split("\n")[0]
        self._F = lines[3].split("\n")[0].split(" ")
        D0 = lines[4].split("\n")[0].split("|")
        self._P = []
        self._isDFA = True
        self._table = {}

        for rule in D0:

            x = rule.split(" ")
            self._P.append(x)
            if (x[0], x[1]) in self._table:
                self._isDFA = False
            self._table[(x[0], x[1])] = x[2]


    @staticmethod
    def printState(list):
        x = "{ "
        for el in list:
            x += el + ", "
        x += "}"
        return x

    def isAccepted(self,seq):
        if not self._isDFA:
            return False
        else:
            curState = self._q0
            for i in seq:
                if (curState, i) in self._table:
                    curState = self._table[(curState, i)]
                else:
                    return False
            if not curState in self._F:
                return False
            return True
class HashTable:

    def __init__(self, initial_size=32):
        self._capacity = initial_size
        self._data = [""] * self._capacity
        self._size = 0

    # initial_hash_function
    # input : key - String
    # output : suma % self.capacity - int
    # effect : it returns the hash value of the string 'key'
    def initial_hash_function(self, key):
        suma = 0
        for charx in key:
            suma += ord(charx)
        return suma % self._capacity

    # add
    # input : key - String
    # output : None
    # effect : it adds the string 'key' in the hashtable
    def add(self, key):

        maybeIn = self.lookup(key)
        if maybeIn != -1:
            return maybeIn

        if self._size / self._capacity > 0.7:
            self._capacity = self._capacity * 2
            self._size = 0
            data = self._data
            self._data = [""] * self._capacity
            for oldKey in data:
                self.add(oldKey)
        index = self.initial_hash_function(key)
        while index < self._capacity and self._data[index] != "":
            index += 1
        if index == self._capacity:
            index = 0
        while index < self._capacity and self._data[index] != "":
            index += 1
        self._data[index] = key
        self._size += 1
        return index

    # lookup
    # input : key - String
    # output : index - int
    # effect : returns the index of the string 'key' from the hashtable
    def lookup(self, key):
        index = self.initial_hash_function(key)
        while index < self._capacity and self._data[index] != key:
            index += 1
        if index == self._capacity:
            index = 0
        while index < self._capacity and self._data[index] != key:
            index += 1
        if index == self._capacity:
            return -1
        return index

    def __str__(self):
        result = "["
        for i in self._data:
            result += " " + i + ", "
        result += "]"
        return result

def scan(file1,file2):
        f = open(file1, "r", encoding="utf8")
        d = open(file2, "r", encoding="utf8")

        FaIntegers = FA("integers.in")
        FaIdentifiers = FA("identifier.in")
        tokens = []
        for line in d.readlines():
            tokens.append(line.split("#")[0])
        pif = []
        parseTokens = []
        errors = []
        lines = f.readlines()
        beforeMinus = ["==", "=", "+", "-", "*", "/", ">", "<", "<=", ">=", "%"]
        lastToken = ""
        for k in range(len(lines)):
            line = lines[k]
            quotesNr = 0
            newLine = ""
            for i in range(len(line)):
                ch = line[i]
                if line[i] == ' ' and quotesNr % 2 != 0:
                    ch = "#space#"
                if line[i] == '\n' and quotesNr % 2 != 0:
                    ch = "#enter#"
                if line[i] == '\t' and quotesNr % 2 != 0:
                    ch = "#tab#"
                if line[i] == '"':
                    quotesNr += 1
                    if (quotesNr % 2 == 1):
                        if newLine.rfind('"') == -1:
                            for i in range(len(tokens)):
                                newLine = newLine.replace(tokens[i], ' #' + str(i) + '# ')
                        else:
                            lastSubstring = newLine[newLine.rfind('"') + 1:]
                            for i in range(len(tokens)):
                                lastSubstring = lastSubstring.replace(tokens[i], ' #' + str(i) + '# ')
                            newLine = newLine[:newLine.rfind('"') + 1] + lastSubstring
                newLine += ch
            if newLine.rfind('"') == -1:
                for i in range(len(tokens)):
                    newLine = newLine.replace(tokens[i], ' #' + str(i) + '# ')
            elif quotesNr % 2 == 0:
                lastSubstring = newLine[newLine.rfind('"') + 1:]
                for i in range(len(tokens)):
                    lastSubstring = lastSubstring.replace(tokens[i], ' #' + str(i) + '# ')
                newLine = newLine[:newLine.rfind('"') + 1] + lastSubstring
            line = newLine
            for i in range(len(tokens)):
                line = line.replace('#' + str(i) + '#', tokens[i])
            x = re.split('\s', line)

            x = list(filter(None, x))
            for i in range(len(x)):
                token = x[i]
                if lastToken != "":
                    token = lastToken + token
                    lastToken = ""
                if token == "-" and (x[i - 1] in beforeMinus):
                    lastToken = token
                    continue

                token = token.replace("#space#", " ")
                token = token.replace("#tab#", "\t")
                token = token.replace("#enter#", "\n")
                if token.lower() in tokens:
                    parseTokens.append(token)
                elif FaIdentifiers.isAccepted(token) :
                    parseTokens.append("IDENTIFIER")
                elif FaIntegers.isAccepted(token):
                    parseTokens.append("NUM")

                elif re.findall(
                        '^".*"$|^\'.\'$', token):

                    parseTokens.append("STR")

                else:
                    errors.append("Lexical error at line " + str(k) + " at token :" + token)
        return parseTokens

def print_menu():
    print("0. Exit")
    print("1. Show non terminals")
    print("2. Show terminals")
    print("3. Show productions")
    print("4. Production for a given nonterminal")
    print("5. First Set ")
    print("6. Follow set")
    print("7. Parse PIF")
    
    
if __name__ == '__main__':

  
    grammar = Grammar.read_file("g2.txt")
    pif = scan("text.in","token.in")
    parser = Parser(grammar,pif)
    parser_output = ParserOutput(parser)

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
        elif x == 7:
            parser_output.parse_pif()
        else:
            break
    
    
    