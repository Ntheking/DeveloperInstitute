#Exersize2

# class Currency():
# 	type = ""
# 	val = 0
# 	def __init__(self, type, val):
# 		self.type = type
# 		self.val = val
# 	def __str__(self):
# 		return(val.str() + " " + type)
# 	def __int__(self):
# 		return(val)
# 	def __add__(self, other):
# 		if isinstance(other,Currency()):
# 			if self.type != other.type:
# 				raise TypeError("Cannot add different types")
# 			return self.val + other.val
# 		return self.val + other
# 	def __iadd__(self, other):
# 		if isinstance(other,Currency()):
# 			if self.type != other.type:
# 				raise TypeError("Cannot add different types")
# 			return self.val + other.val
# 		return self.val + other.val
# 	def __repr__(self):
# 		self.__str__()
#Excersize3

import datetime

def two_num_sum():
	