#Author: Mackey CHARLES
#Abstract : This module helps to read files
from os import path
import re

class FileReaderError(Exception):
	pass

class FileReader(object):
	#This pbject represents the file reader

	def __init__(self,filename=""):
		if not filename or not isinstance(filename,str):raise FileReaderError('You should provide a non empty string')
		elif not path.isfile(filename) or not self.__valid__(filename):raise FileReaderError(f'{filename} is not found or not a tex file')
		self.file_stream = open(filename,'r')

	def __str__(self) -> str:
		return f'fichier {self.file_stream.name}'
	def __valid__(self,filename:str)->bool:
		if not re.search(r'\.tex$',filename):return False
		return True

	def read(self)->str:
		if not self.__valid__():return None
		return self.file_stream.read()
