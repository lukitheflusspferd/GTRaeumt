from lexerToken import *
import globalVariables

class TokenFactory():
    """
    Klasse für die Erzeugung von Tokens aus den Endzuständen
    """
    def __init__(self):
        self.__unknownIdentifiers = set()
    
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
                return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 1, 2, position)
            case 'e_nmbr':
                return Token(TokenType.LITERAL, lexem, position)
            case 'e_str':
                return self.__severalStrings(lexem, position)
                # return Token(TokenType.LITERAL, lexem, position)
            case 'e_mul' | 'E_div':
                return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 3, 2, position)
            case 'E_mod':
                return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 2, 2, position)
            case 'E_exp':
                return TokenWithPrecedence(TokenType.OPERATOR, '^', Associativity.RIGHT, 4, 2, position)
            case 'E_ka_r':
                return Token(TokenType.PARENTHESIS_OPEN, lexem, position)
            case 'E_ka_e':
                return Token(TokenType.RANGE_OPEN, lexem, position)
            case 'E_ka_g':
                return Token(TokenType.SET_OPEN, lexem, position)
            case 'E_kz_r':
                return Token(TokenType.PARENTHESIS_CLOSE, lexem, position)
            case 'E_kz_e':
                return Token(TokenType.RANGE_CLOSE, lexem, position)
            case 'E_kz_g':
                return Token(TokenType.SET_CLOSE, lexem, position)
            case 'e_eq' | 'e_les' | 'e_gre' |  'E_leq' | 'E_geq' | 'neq':
                return Token(TokenType.RELATIONAL_OPERATOR, lexem, position)
            case 'E_cma':
                return Token(TokenType.COMMA, lexem, position)
            case 'E_smc':
                return Token(TokenType.SEPERATOR, lexem, position)
            case 'E_asgn':
                return Token(TokenType.ASSIGNMENT, lexem, position)
            case 'e_dpkt':
                return Token(TokenType.PART_OF, lexem, position)
            case 'E_vln':
                return Token(TokenType.ARGUMENTSEPERATOR, lexem, position)
            case 'E_grLet':
                return self.__severalStrings(lexem, position)
            case 'E_smpr':
                return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 5, 3, position)
            case _:
                raise Exception("Unbekannter Endzustand")
        
        
    
    def __severalStrings(self, lexem: str, position: tuple[int, int]) -> Token | TokenWithPrecedence:
        """
        Funktion, welche für jegliche unbekannte Zeichenketten das jeweilige Token generiert,
        also für Konstanten, Funktionen, Variablen und Befehle

        Args:
            lexem (str): Die Zeichenkette, welche der Tokenizer extrahiert hat
            position (tuple[int, int]): Start und Endposition des Lexems/Tokens im Ausgangsstring

        Returns:
            Token | TokenWithPrecedence: Gibt das entsprechende Token zurück
        """
        global PREDEFINED_CONSTANTS
        global PREDEFINED_FUNCTIONS_IDENTIFIER
        
        lexem = lexem.lower()
        
        if lexem in PREDEFINED_CONSTANTS:
            return Token(TokenType.LITERAL, PREDEFINED_CONSTANTS[lexem], position)
        
        if lexem in globalVariables.getSelfdefinedConstants():
            return Token(TokenType.LITERAL, globalVariables.getSelfdefinedConstants()[lexem], position)
        
        if lexem in PREDEFINED_FUNCTIONS_IDENTIFIER:
            return TokenWithPrecedence(TokenType.OPERATOR, lexem, Associativity.LEFT, 5, PREDEFINED_FUNCTIONS_ARITY[lexem], position)
        
        if lexem in globalVariables.getSelfdefinedFunctionIdentifier():
            return TokenWithPrecedence(TokenType.FUNCTION, lexem, Associativity.LEFT, 5, globalVariables.getSelfdefinedFunctionArity(lexem), position)
        
        if lexem in COMMAND_IDENTIFIER:
            tokenType = TokenType(COMMAND_IDENTIFIER[lexem])
            return Token(tokenType, lexem, position)
        
        if lexem in NUMBER_RANGES:
            return Token(TokenType.NUMBER_RANGE, lexem, position)
        
        # Sonst ist der Bezeichner noch unbekannt
        self.__unknownIdentifiers.add(lexem)
        return Token(TokenType.UNKNOWN_IDENTIFIER, lexem, position)
    
    def getUnknownIdentifiers(self):
        return self.__unknownIdentifiers
        