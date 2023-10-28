#Author: Mackey CHARLES
#Abstract : This module helps to read files
from os import path
import re

class FileReader(object):
	#This pbject represents the file reader

	def __init__(self,filename=""):
		if not filename or not isinstance(filename,str):pass
		elif not path.isfile(filename):pass
		if not self.__valid__():pass
		self.file_stream = open(filename,'r')
	
	def __valid__(self,filename):
		if not re.search(r'\.tex$',filename):return False
		return True

	def read(self):
		if not self.__valid__():return None
		return self.file_stream.read()

		


if __name__=="__main__":print("This is a module")