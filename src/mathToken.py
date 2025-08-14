from enum import Enum
import numpy

import globalVariables

PREDEFINED_CONSTANTS = {
    "pi" : numpy.pi,
    "Pi" : numpy.pi,
    "π" : numpy.pi,
    "euler" : numpy.e,
    "Euler" : numpy.e
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
    Klasse für ein Token mit Typ, Inhalt, Assoziativität, Priorität  und Position
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

class TokenFactory():
    """
    Klasse für die Erzeugung von Tokens aus den Endzuständen
    """
    def __init__(self):
        self.__variables = set()
    
    def generateToken(self, endState : str, lexem: str, position: tuple[int, int]) -> Token | TokenWithPrecedence:
        """
        Funktion, welche aus einem Endzustand und dem zukünftigen Inhalt des Tokens ein Token generiert und zurückgibt

        Args:
            endState (str): Die Id des Endzustandes
            lexem (str): Das Lexem / die Zeichenkette, welches/welche die Grundlage für das zu generierende Token ist
            position (tuple[int, int]): Die Position des Tokens im Eingabestring

        Returns:
            Token | TokenWithPrecedence: Gibt ein Objekt der Klasse Token oder einer der davon erbenden Klassen zurück
        """
        
        match endState:
            case 'E_add' | 'E_sub':
                return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 1, position)
            case 'e_nmbr':
                return Token(TokenType.LITERAL, lexem, position)
            case 'e_str':
                return self.__severalStrings(lexem, position)
                # return Token(TokenType.LITERAL, lexem, position)
            case 'e_mul' | 'E_div':
                return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 3, position)
            case 'E_mod':
                return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 2, position)
            case 'E_exp':
                return TokenWithPrecedence(TokenType.OPERATOR, '^', Associativity.LEFT, 4, position)
            case 'E_ka_r':
                return TokenWithPrecedence(TokenType.PARENTHESIS, lexem, Associativity.LEFT, 5, position)
            case 'E_ka_e':
                return TokenWithPrecedence(TokenType.RANGE, lexem, Associativity.LEFT, 5, position)
            case 'E_ka_g':
                return TokenWithPrecedence(TokenType.SET, lexem, Associativity.LEFT, 5, position)
            case 'E_kz_r':
                return TokenWithPrecedence(TokenType.PARENTHESIS, lexem, Associativity.RIGHT, 5, position)
            case 'E_kz_e':
                return TokenWithPrecedence(TokenType.RANGE, lexem, Associativity.RIGHT, 5, position)
            case 'E_kz_g':
                return TokenWithPrecedence(TokenType.SET, lexem, Associativity.RIGHT, 5, position)
            case 'e_eq' | 'e_les' | 'e_gre' |  'E_leq' | 'E_geq' | 'neq':
                return Token(TokenType.RELATIONAL_OPERATOR, lexem, position)
            case 'E_cma' | 'E_smc':
                return Token(TokenType.SEPERATOR, lexem, position)
            case 'E_asgn':
                return Token(TokenType.ASSIGNMENT, lexem, position)
            case 'e_dpkt':
                return Token(TokenType.PART_OF, lexem, position)
            case 'E_vln':
                return Token(TokenType.WITH, lexem, position)
            case 'E_grLet':
                return self.__severalStrings(lexem, position)
            case 'E_smpr':
                raise NotImplementedError()
            case _:
                raise Exception("Unerwarteter Endzustand")
        
        
    
    def __severalStrings(self, lexem: str, position: tuple[int, int]) -> Token | TokenWithPrecedence:
        """
        Funktion, welche für jegliche unbekannte Zeichenketten das jeweilige Token generiert,
        also für Konstanten, Funktionen, Variablen und Befehle

        Args:
            lexem (str): Die Zeichenkette, welche der Tokenizer extrahiert hat
            position (tuple[int, int]): Start und Endposition des Lexems/Tokens im Ausgangsstring

        Raises:
            NotImplementedError: _description_
            NotImplementedError: _description_

        Returns:
            Token | TokenWithPrecedence: Gibt das entsprechende Token zurück
        """
        global PREDEFINED_CONSTANTS
        global PREDEFINED_FUNCTIONS
        
        if lexem in PREDEFINED_CONSTANTS:
            return Token(TokenType.LITERAL, PREDEFINED_CONSTANTS.get(lexem), position) # type: ignore --> Vorhandensein mit if-Bedingung geprüft
        
        if lexem in globalVariables.getSelfdefinedConstants():
            return Token(TokenType.LITERAL, globalVariables.getSelfdefinedConstants().get(lexem), position) # type: ignore --> siehe oben
        
        if lexem in PREDEFINED_FUNCTIONS:
            raise NotImplementedError
        
        if lexem in globalVariables.getSelfdefinedFunctions():
            raise NotImplementedError
        
        # Sonst muss die Zk eine Variable sein (wird dem Set hinzugefügt, doppelt macht eh nichts)
        self.__variables.add(lexem)
        return Token(TokenType.VARIABLE, lexem, position)
    
    def getVariables(self):
        return self.__variables
        