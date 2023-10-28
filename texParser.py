from fileReader import FileReader
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
class ParserError(Exception):pass

class TexParser(object):
    
    def __init__(self,filename:str) -> None:
        self.content = FileReader(filename).read()
        self.filename = filename
        logging.info(f'content {filename}: {self.content}')
    
    def __str__(self) -> str:
        return  f'Parser of {self.filename}'
    
    def __repr__(self) -> str:
        return self.__str__()
        
    def parse(self)->None:
        pass
