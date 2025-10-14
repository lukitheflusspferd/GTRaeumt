from enum import Enum
from Tests.lexertest.AllowedTokenCharactersV1 import *
import re


class Parenthesis(Enum):
    """
    Enum für die Assoziativitätstypen
    """
    RIGHT = "right"
    LEFT = "left"
  

class TokenType:
    def __init__(
        self,
        init_tokentypeid : str,
        init_name: str,
        init_firstCharacter : re.Pattern[str],
        init_secondCharacter : re.Pattern[str] | TokenCharacterpositionPointer,
        init_allCharacters : re.Pattern[str],
        init_trailingCharacter : re.Pattern[str],
        init_parenthesis: Parenthesis,
    ):
        self.__tokentypeid = init_tokentypeid
        self.__name = init_name
        self.__firstCharacter = init_firstCharacter
        self.__secondCharacter = init_secondCharacter
        self.__allCharacters = init_allCharacters
        self.__trailingCharacter = init_trailingCharacter
        self.__parenthesis = init_parenthesis
    
    def getTokenid(self) -> str:
        return self.__tokentypeid
    
    def getName(self) -> str:
        return self.__name
    
    def getFirstCharacter(self) -> str:
        return self.__firstCharacter
    
    def getSecondCharacter(self) -> str:
        return self.__secondCharacter
    
    def getMiddleCharacters(self) -> str:
        return self.__allCharacters
    
    def getLastCharacter(self) -> str:
        return self.__trailingCharacter
    
    def getParenthesis(self) -> Parenthesis:
        return self.__parenthesis    
    
class TokenStr(TokenType):
    def __init__(self):
        super().__init__(
            "str", "String", 
            re.compile(""), 
            re.compile([]), 
            re.compile([]), 
            re.compile([]), 
            Parenthesis.RIGHT
        )

def tokenize(expression: str) -> list:
    """
    Zerlegt einen Ausdruck in eine Liste von Tokens
    """
    pass