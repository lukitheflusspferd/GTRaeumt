from enum import Enum
import numpy

import globalVariables

PREDEFINED_CONSTANTS = {
    "pi" : numpy.pi,
    "e" : numpy.e
}

PREDEFINED_FUNCTIONS = {
    "LoremIpsum1" : None
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
    PARENTHESIS = "parenthesis"
    RANGE = "range"
    SET = "set"
    PART_OF = "partOf"
    RELATIONAL_OPERATOR = "relationalOperator"
    WITH = "with"
    SEPERATOR = "seperator"
    ASSIGNMENT = "assignment"

class Token():
    """
    Klasse für ein Token mit Typ und Inhalt
    """
    def __init__(self, tokenType : TokenType, lexem : str):
        self._tokenType = tokenType
        self._lexem = lexem
        
    def getTokenType(self):
        return self._tokenType
    
    def getValue(self):
        return self._lexem
    
    def __str__(self):
        return f"Tokenobjekt ->  Typ: {self._tokenType},   Inhalt: {self._lexem}"
        
class TokenWithPrecedence(Token):
    """
    Klasse für ein Token mit Typ, Inhalt, Assoziativität und Priorität
    """
    def __init__(self, tokenType : TokenType, lexem : str, associativity : Associativity, precedence : int):
        super().__init__(tokenType, lexem)
        self.__associativity = associativity
        self.__precedence = precedence
        
    def getAssociativity(self):
        return self.__associativity
    
    def getPrecedence(self):
        return self.__precedence
    
    def __str__(self):
        return f"Tokenobjekt ->  Typ: {self._tokenType},   Inhalt: {self._lexem},   Assoziativität: {self.__associativity},   Priorität: {self.__precedence}"

class TokenFactory():
    """
    Klasse für die Erzeugung von Tokens aus den Endzuständen
    """
    def __init__(self):
        self.__variables = set()
    
    def generateToken(self, endState : str, lexem: str) -> Token | TokenWithPrecedence:
        """
        Funktion, welche aus einem Endzustand und dem zukünftigen Inhalt des Tokens ein Token generiert und zurückgibt

        Args:
            endState (str): Die Id des Endzustandes
            value (str): Der zukünftige Inhalt des Strings

        Returns:
            Token | TokenWithPrecedence: Gibt ein Objekt der Klasse Token oder einer der davon erbenden Klassen zurück
        """
        
        match endState:
            case 'E_add' | 'e_sub':
                return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 1)
            case 'e_nmbr':
                return Token(TokenType.LITERAL, lexem)
            case 'e_str':
                return Token(TokenType.LITERAL, lexem)
            case 'e_mul' | 'E_div':
                return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 3)
            case 'E_mod':
                return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 2)
            case 'E_exp':
                return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 4)
            case 'E_ka_r':
                return TokenWithPrecedence(TokenType.PARENTHESIS, lexem, Associativity.LEFT)
            case 'E_ka_e':
                return TokenWithPrecedence(TokenType.RANGE, lexem, Associativity.LEFT)
            case 'E_ka_g':
                return TokenWithPrecedence(TokenType.SET, lexem, Associativity.LEFT)
            case 'E_kz_r':
                return TokenWithPrecedence(TokenType.PARENTHESIS, lexem, Associativity.RIGHT)
            case 'E_kz_e':
                return TokenWithPrecedence(TokenType.RANGE, lexem, Associativity.RIGHT)
            case 'E_kz_g':
                return TokenWithPrecedence(TokenType.SET, lexem, Associativity.RIGHT)
            case 'e_eq' | 'e_les' | 'e_gre' |  'E_leq' | 'E_geq' | 'neq':
                return Token(TokenType.RELATIONAL_OPERATOR, lexem)
            case 'E_cma' | 'E_smc':
                return Token(TokenType.SEPERATOR, lexem)
            case 'E_asgn':
                return Token(TokenType.ASSIGNMENT, lexem)
            case 'e_dpkt':
                return Token(TokenType.PART_OF, lexem)
            case 'E_vln':
                return Token(TokenType.WITH, lexem)
            case _:
                raise Exception("Unerwarteter Endzustand")
        
        
    
    def __severalStrings(self, lexem : str):
        global PREDEFINED_CONSTANTS
        global PREDEFINED_FUNCTIONS
        
        if lexem in PREDEFINED_CONSTANTS:
            return Token(TokenType.LITERAL, PREDEFINED_CONSTANTS.get(lexem))
        
        if lexem in PREDEFINED_FUNCTIONS:
            raise NotImplementedError
        
        if lexem in globalVariables.getSelfdefinedConstants():
            return Token(TokenType.LITERAL, globalVariables.getSelfdefinedConstants().get(lexem))
        
        if lexem in globalVariables.getSelfdefinedFunctions():
            raise NotImplementedError
        
        # Sonst muss die Zk eine Variable sein (wird dem Set hinzugefügt, doppelt macht eh nichts)
        self.__variables.add(lexem)
        return Token(TokenType.VARIABLE, lexem)
        