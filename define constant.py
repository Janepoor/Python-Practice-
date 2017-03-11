#! /usr/bin/env python
#coding=utf-8

### python define constant

import sys

class const(obejct):
	class Consterror(TypeException):
		"""docstring for Consterror"""
		def __init__(self, arg):
			super(Consterror, self).__init__()
			self.arg = arg

		pass
			

	def __set__(self, key, value):
		if self.__dict__.has_key(key):
			raise self.Consterror,"Changing the Constan.%s", %key
		else:
			self.__dict__[key]=value

	def __get__(self, key):
		if self.__dict__.has_key(key):
			return self.key
		else:
			return None		