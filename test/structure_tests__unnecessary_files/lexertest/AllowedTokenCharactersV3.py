from enum import Enum

class __COMMON_CHARACTER_SETS():
    """
    Generierung der Buchstabenliste
    """
    __LETTERS = set()
    for i in range(65, 91):
        __LETTERS.add(chr(i))
    for i in range(97, 123):
        __LETTERS.add(chr(i))
    
    __LETTERS = __LETTERS | {'Ä', 'Ö', 'Ü', 'ä', 'ö', 'ü', 'ß'}
    
    """
    Gesammelte Buchstabensammlungen für häufige Verwendung
    """
    BRACKETS = {'(', ')', '[', ']', '{', '}'}
    LETTERS = __LETTERS
    DIGITS = {str(i) for i in range(10)}
    DIGITS_DOT = {str(i) for i in range(10)} | {'.'}

'''class TokenCharacterPosition(Enum):
    """
    Namen der möglichen Positionstypen eines Zeichens
    """
    LEADING = "leading"
    FOLLOWING = "following"
    ALL = "all"
    TRAILING = "trailing"
    
class TokenCharacterPositionPointer(Enum):
    """
    Besondere Zeiger, welche als Inhalt einer Zeichenposition eines Tokentyps
    auf eine andere Zeichenposition des Tokentyps verweisen
    """
    ALL_CHARACTERS = "allCharacters"
    END = "end" # Token kann kein weiteres Zeichen haben, es muss also beendet werden'''
  
# TODO : Enum für die Positionen
ALLOWED_TOKEN_CHARACTERS = [
    {   # Zeichenkette
        'tokenType' : 'str',
        'characters' : [
            (__COMMON_CHARACTER_SETS.LETTERS, __COMMON_CHARACTER_SETS.LETTERS),
            (__COMMON_CHARACTER_SETS.LETTERS | __COMMON_CHARACTER_SETS.DIGITS, set()),
        ],
    },
    {   # Zahl
        'tokenType' : 'nmbr',
        'characters' : [
            (__COMMON_CHARACTER_SETS.DIGITS | {'.'}, {'.'}),
            (__COMMON_CHARACTER_SETS.DIGITS, set()),
        ],
    },
    # Operatoren
    {   # Addition
        'tokenType' : 'add',
        'characters' : [
            ({'+'}, {'+'}),
        ],
    },
    {   # Subtraktion
        'tokenType' : 'sub',
        'characters' : [
            ({'-'}, {'-'}),
        ],
    },
    {   # Multiplikation
        'tokenType' : 'mul',
        'characters' : [
            ({'*'}, {'*'}),
        ],
    },
    {   # Division
        'tokenType' : 'div',
        'characters' : [
            ({'/'}, {'/'}),
        ],
    },
    {   # Potenz 1
        'tokenType' : 'exp',
        'characters' : [
            ({'^'}, {'^'}),
        ],
    },
    {   # Potenz 2
        'tokenType' : 'exp',
        'characters' : [
            ({'*'}, {'*'}),
            ({'*'}, {'*'}),
        ],
    },
    # Klammern
    {   # Klammer auf rund
        'tokenType' : 'ka_r',
        'characters' : [
            ({'('}, {'('}),
        ],
    },
    {   # Klammer auf eckig
        'tokenType' : 'ka_e',
        'characters' : [
            ({'['}, {'['}),
        ],
    },
    {   # Klammer auf geschweift
        'tokenType' : 'ka_g',
        'characters' : [
            ({'{'}, {'{'}),
        ],
    },
    {   # Klammer zu rund
        'tokenType' : 'kz_r',
        'characters' : [
            ({')'}, {')'}),
        ],
    },
    {   # Klammer zu eckig
        'tokenType' : 'kz_e',
        'characters' : [
            ({']'}, {']'}),
        ],
    },
    {   # Klammer zu geschweift
        'tokenType' : 'kz_g',
        'characters' : [
            ({'}'}, {'}'}),
        ],
    },
    # Relationszeichen
    {   # Gleich
        'tokenType' : 'eq',
        'characters' : [
            ({'='}, {'='}),
        ],
    },
    {   # Ungleich
        'tokenType' : 'neq',
        'characters' : [
            ({'!'}, {'!'}),
            ({'='}, {'='}),
        ],
    },
    {   # Größer
        'tokenType' : 'gre',
        'characters' : [
            ({'>'}, {'>'}),
        ],
    },
    {   # Größergleich
        'tokenType' : 'geq',
        'characters' : [
            ({'>'}, {'>'}),
            ({'='}, {'='}),
        ],
    },
    {   # Größergleich
        'tokenType' : 'geq',
        'characters' : [
            ({'='}, {'='}),
            ({'>'}, {'>'}),
        ],
    },
    {   # Kleiner
        'tokenType' : 'sml',
        'characters' : [
            ({'<'}, {'<'}),
        ],
    },
    {   # Kleinergleich
        'tokenType' : 'seq',
        'characters' : [
            ({'<'}, {'<'}),
            ({'='}, {'='}),
        ],
    },
    {   # Kleinergleich
        'tokenType' : 'seq',
        'characters' : [
            ({'='}, {'='}),
            ({'<'}, {'<'}),
        ],
    },
    # Spezielle Zeichen
    {   
        'tokenType' : 'vln',
        'characters' : [
            ({'|'}, {'|'}),
        ],
    },
    {   
        'tokenType' : 'dpkt',
        'characters' : [
            ({':'}, {':'}),
        ],
    },
    {   
        'tokenType' : 'smc',
        'characters' : [
            ({';'}, {';'}),
        ],
    },
    {   
        'tokenType' : 'cma',
        'characters' : [
            ({','}, {','}),
        ],
    },
]
"""
Gibt für eine bestimmte Position eines Tokens des Typs TokenType die erlaubten Zeichen zurück.
>>> ALLOWED_TOKEN_CHARACTERS[TokenTypeID][Position] -> set of allowed Characters
"""


'''class State():
    """
    Klasse für einen Zustand des Automaten für die Generierung der Token
    """
    def __init__(self, stateID, nextStatesByCharacter : dict):
        self.__stateID = stateID
        self.__nextStatesByCharacter = nextStatesByCharacter
        # Endzustand wenn Menge der Folgezustände leer
        if self.__nextStatesByCharacter == dict():
            self.__isFinalState = True
        else:
            self.__isFinalState = False
    
    """
    Gibt den nächsten Zustand für den gegebenen Buchstaben zurück
    """
    def getNextStateByCharacter(self, character):
        return self.__nextStatesByCharacter.get(character)
    
    """
    Getter-Methode für isFinalState
    """
    def getIsFinalState(self):
        return self.__isFinalState
        '''

class State():
    """
    Klasse für einen Zustand des Automaten für die Generierung der Token
    """
    def __init__(self, nextStatesByCharacter : dict): # stateID,
        #self.__stateID = stateID
        self.__nextStatesByCharacter = nextStatesByCharacter
        # Endzustand wenn Menge der Folgezustände leer
    
    """
    Gibt den nächsten Zustand für den gegebenen Buchstaben zurück
    """
    def getNextStateByCharacter(self, character):
        return self.__nextStatesByCharacter.get(character)
    
# Generierung des Automaten
Alphabet = set(' ') # Menge der Buchstaben, außerdem das Leerzeichen, damit bei diesem als unbekanntem Symbol nicht geworfen wird, stattdessen wird das Token beendet
States = dict()