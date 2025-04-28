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
    LETTERS = __LETTERS
    DIGITS = {str(i) for i in range(10)}
  

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
    
# Generierung des Automaten
# Menge der Buchstaben, außerdem das Leerzeichen, damit bei diesem als unbekanntem Symbol nicht geworfen wird, stattdessen wird das Token beendet
Alphabet = {
    '+', '-', '*', '/', '^', '(', ')', '{', '}', '[', ']', '<', '>', '=', '!', '|', ',', ';', ':', '.', ' ', '_', '%'
} | __COMMON_CHARACTER_SETS.LETTERS | __COMMON_CHARACTER_SETS.DIGITS


__PreStates = {
    'start' : {
        ' ' : 'start',
        '+' : 'E_add',
        '-' : 'sub',
        '.' : 'nmbr_2',
        'DIGITS' : 'nmbr_1',
        'LETTERS' : 'str',
        '_' : 'str',
        '*' : 'mul',
        '^' : 'E_exp',
        '/' : 'E_div',
        '(' : 'E_ka_r',
        '[' : 'E_ka_e',
        '{' : 'E_ka_g',
        ')' : 'E_kz_r',
        ']' : 'E_kz_e',
        '}' : 'E_kz_g',
        '=' : 'eq',
        '<' : 'les',
        '>' : 'gre',
        '!' : 'neq',
        ',' : 'E_cma',
        ';' : 'E_smc',
        ':' : 'dpkt',
        '|' : 'E_vln',
        '%' : 'E_mod',
    },
    'E_add' : None,
    'sub' : {
        'DIGITS' : 'nmbr_1',
        '.' : 'nmbr_2',
        'ELSE' : 'e_sub',
    },
    'e_sub' : None,
    'nmbr_1' : {
        'DIGITS' : 'nmbr_1',
        '.' : 'nmbr_2',
        'ELSE' : 'e_nmbr',
    },
    'nmbr_2' : {
        'DIGITS' : 'nmbr_2',
        'ELSE' : 'e_nmbr',
    },
    'e_nmbr' : None,
    'str' : {
        'LETTERS' : 'str',
        'DIGITS' : 'str',
        '_' : 'str',
        'ELSE' : 'e_str',
    },
    'e_str' : None,
    'e_mul' : None,
    'E_exp' : None,
    'mul' : {
        '*' : 'E_exp',
        'ELSE' : 'e_mul'
    },
    'E_div' : None,
    'E_ka_r' : None,
    'E_ka_e' : None,
    'E_ka_g' : None,
    'E_kz_r' : None,
    'E_kz_e' : None,
    'E_kz_g' : None,
    'eq' : {
        '<' : 'E_leq',
        '>' : 'E_geq',
        'ELSE' : 'e_eq'
    },
    'les' : {
        '=' : 'E_leq',
        'ELSE' : 'e_les'
    },
    'gre' : {
        '=' : 'E_geq',
        'ELSE' : 'e_gre'
    },
    'e_eq' : None,
    'e_les' : None,
    'e_gre' : None,
    'E_leq' : None,
    'E_geq' : None,
    'neq' : {
        '=' : 'E_neq'
    },
    'E_neq' : None,
    'dpkt' : {
        '=' : 'E_asgn',
        'ELSE' : 'e_dpkt'
    },
    'E_cma' : None,
    'E_smc' : None,
    'E_asgn' : None,
    'e_dpkt' : None,
    'E_vln' : None,
    'E_mod' : None
}

# print(__PreStates)

"""
Auflösen der vorläufigen Relationen zu vollständig verwendbaren Relationen
Da die PreStates in einem Dict gespeichert sind, in welchem für normale Zustände ein weiteres Dict gespeichert ist, genügt eine einfache Schleife, um alle Relationen zu erfassen
Es werden die reservierten Schlüsselwörter 'LETTERS', 'DIGITS' und 'ELSE' ersetzt.
Dabei muss 'ELSE' in PreStates immer als letztes stehen, damit dafür korrekt der Rest des Alphabets eingesetzt werden kann
"""
STATES = dict()
# Für jede Liste von Folgezuständen der Zustände in den vorläufigen Zuständen
for state, value in __PreStates.items():
    # Wenn Endzustand, dann ist nichts zu tun
    if value == None: 
        STATES[state] = value
        continue
    a = Alphabet.copy()
    valueWorkingCopy = value.copy()
    # Für jede Relation in dem ausgewählten Zustand
    for character, nextState in value.items():
        if character == 'LETTERS':
            valueWorkingCopy.pop(character)
            for letter in __COMMON_CHARACTER_SETS.LETTERS: 
                valueWorkingCopy[letter] = nextState
                a.remove(letter)
        elif character == 'DIGITS':
            valueWorkingCopy.pop(character)
            for digit in __COMMON_CHARACTER_SETS.DIGITS: 
                valueWorkingCopy[digit] = nextState
                a.remove(digit)
        elif character == 'ELSE':
            valueWorkingCopy.pop(character)
            for element in a: 
                valueWorkingCopy[element] = nextState
        else:
            a.remove(character)
    STATES[state] = valueWorkingCopy
    
# print(States)

print("Initialized the Lexer Automaton")