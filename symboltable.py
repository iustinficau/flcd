# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 13:17:37 2020

@author: ficau
"""
from node import Node

#Symbol table represented as Hash table with separate chaining

class SymTable:
    
	# Initialize hash table
	def __init__(self):
		self.capacity = 50
		self.size = 0
		self.buckets = [None]*self.capacity
        
	# Generate a hash for a given key
	def hash(self, key):
		hashsum = 0
		
		for idx, c in enumerate(key):
			
			hashsum += (idx + len(key)) ** ord(c)
		
			hashsum = hashsum % self.capacity
		return hashsum

	# Insert a key,value pair to the hashtable
	def insert(self, key, value):
		
		self.size += 1

		index = self.hash(key)
		
		node = self.buckets[index]
		
		if node is None:
			
			self.buckets[index] = Node(key, value)
			return
		
		prev = node
		while node is not None:
			prev = node
			node = node.next
		
		prev.next = Node(key, value)

	# Find a data value based on key
	def find(self, key):
		
		index = self.hash(key)
		values = []
		node = self.buckets[index]
	
		while node is not None and node.key != key:
			node = node.next
	
		if node is None:
			return None
		
		while node is not None:
			values.append(node.value)
			node = node.next
            
		return index,values

	# Remove node stored at key
	def remove(self, key):

		index = self.hash(key)
		node = self.buckets[index]
		prev = None
		
		while node is not None and node.key != key:
			prev = node
			node = node.next

		if node is None:
	
			return None
		else:

			self.size -= 1
			result = node.value

			if prev is None:
				self.buckets[index] = node.next
			else:
				prev.next = prev.next.next  
			return result