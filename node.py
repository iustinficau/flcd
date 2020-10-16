# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:49:38 2020

@author: ficau
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None