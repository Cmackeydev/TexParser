class WordPosition(object):
    def __init__(self,line:int,column:int) -> None:
        if not isinstance(line,int) or not isinstance(column,int):
            raise TypeError("Position of word (line,col) must be integers")
        self.line = line
        self.column = column
    
    def __str__(self) -> str:
        return f"line : {self.line} - col :{self.column}"
    
    def __repr__(self) -> str:
        return self.__str__()
    

class Word(object):
    def __init__(self,word:str)->None:
        if not isinstance(word,str):
            raise TypeError("word should be a string")
        self.value = word

    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, compare_to: object) -> bool:
        if not isinstance(compare_to,Word):
            raise TypeError("Word object can only be compared to Word object")
        
        if compare_to.value ==self.value:return True
        return False
        
    def __hash__(self) -> int:
        return self.value.__hash__()
    
class ReservedWord(Word):
    def __init__(self, word: str)->None:
        super().__init__(word)
