from enum import Enum
import numpy

PREDEFINED_CONSTANTS = {
    "pi" : numpy.pi,
    "π" : numpy.pi,
    "euler" : numpy.e,
}

PREDEFINED_FUNCTIONS = {
    "loremipsum1" : None
}

COMMAND_IDENTIFIER = {
    "plot" : "commandPlot",
    "min" : "commandMin",
    "max" : "commandMax",
    "wende" : "commandWende",
    "ableitung" : "commandAbleitung"
}

NUMBER_RANGES = {
    "int",
    "real"
}

class Associativity(Enum):
    """
    Enum für die Assoziativitätstypen
    """
    RIGHT = "right"
    LEFT = "left"

class TokenType(Enum):
    LITERAL = "literal"
    VARIABLE = "variable"
    
    OPERATOR = "operator"
    FUNCTION = "function"
    
    PARENTHESIS_OPEN = "parenthesis"
    PARENTHESIS_CLOSE = "parenthesis"
    RANGE_OPEN = "range"
    RANGE_CLOSE = "range"
    SET_OPEN = "set"
    SET_CLOSE = "set"
    
    PART_OF = "partOf"
    NUMBER_RANGE = "numberRange"
    RELATIONAL_OPERATOR = "relationalOperator"
    ARGUMENTSEPERATOR = "argumentSeperator"
    SEPERATOR = "seperator"
    ASSIGNMENT = "assignment"
    
    
    COMMAND_PLOT = "commandPlot"
    COMMAND_MIN = "commandMin"
    COMMAND_MAX = "commandMax"
    COMMAND_WENDE = "commandWende"
    COMMAND_ABLEITUNG = "commandAbleitung"
    
    TEMP_SUBSTITUTION = "tempSubstitution"
    UNKNOWN_IDENTIFIER = "unknownIdentifier"

class Token():
    """
    Klasse für ein Token mit Typ, Inhalt und Position
    """
    def __init__(self, tokenType : TokenType, lexem : str | int | float, position : tuple[int, int]):
        self._tokenType = tokenType
        self._lexem = lexem
        self._position = position
        
    def getTokenType(self):
        return self._tokenType
    
    def getValue(self):
        return self._lexem
    
    def getPosition(self):
        return self._position
    
    def __str__(self):
        return f"Tokenobjekt ->  Typ: {self._tokenType},   Inhalt: {self._lexem},   Position: {self._position[0]}..{self._position[1]}"
        
class TokenWithPrecedence(Token):
    """
    Klasse für ein Token mit Typ, Inhalt, Assoziativität, Priorität und Position
    """
    def __init__(self, tokenType : TokenType, lexem : str, associativity : Associativity, precedence : int, position : tuple[int, int]):
        super().__init__(tokenType, lexem, position)
        self.__associativity = associativity
        self.__precedence = precedence
        
    def getAssociativity(self):
        return self.__associativity
    
    def getPrecedence(self):
        return self.__precedence
    
    def __str__(self):
        return f"Tokenobjekt ->  Typ: {self._tokenType},   Inhalt: {self._lexem},   Assoziativität: {self.__associativity},   Priorität: {self.__precedence},   Position: {self._position[0]}..{self._position[1]}"
        
class TempSubstitionToken(Token):
    def __init__(self, tokens: list[Token]):
        self.__tokenlist = tokens
        assert len(tokens)!=0
        overallPosition = (tokens[0].getPosition()[0], tokens[len(tokens)-1].getPosition()[1])
        super().__init__(TokenType.TEMP_SUBSTITUTION, "", overallPosition)
    
    def getTokenlist(self):
        return self.__tokenlist
    
    def __str__(self):
        return f"Temporäres Tokenobjekt mit substituierten Tokens ->  Typ: {self._tokenType},   Inhalt der Substitution: {self.__tokenlist},   Position: {self._position[0]}..{self._position[1]}"