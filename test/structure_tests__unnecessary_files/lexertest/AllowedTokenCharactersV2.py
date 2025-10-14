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
    
    """
    Gesammelte Buchstabensammlungen für häufige Verwendung
    """
    BRACKETS = {'(', ')', '[', ']', '{', '}'}
    LETTERS = __LETTERS
    DIGITS = {str(i) for i in range(10)}
    DIGITS_DOT = {str(i) for i in range(10)} | {'.'}

print(__COMMON_CHARACTER_SETS.LETTERS)

class TokenCharacterPosition(Enum):
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
    END_CHARACTERS = "end" # Token kann kein weiteres Zeichen haben, es muss also ein End-Zeichen kommen
  
# TODO : Enum für die Positionen
ALLOWED_TOKEN_CHARACTERS = [
    {
        'tokenType' : 'str',
        TokenCharacterPosition.LEADING : __COMMON_CHARACTER_SETS.LETTERS,
        TokenCharacterPosition.FOLLOWING : TokenCharacterPositionPointer.ALL_CHARACTERS,
        TokenCharacterPosition.ALL : __COMMON_CHARACTER_SETS.LETTERS | __COMMON_CHARACTER_SETS.DIGITS,
        'trailing' : {'+','-','*','/','^'} | __COMMON_CHARACTER_SETS.BRACKETS,
        # 'specialExeptions' : None
    },
    {
        'tokenType' : 'nmbr',
        TokenCharacterPosition.LEADING : TokenCharacterPositionPointer.ALL_CHARACTERS,
        TokenCharacterPosition.FOLLOWING : TokenCharacterPositionPointer.ALL_CHARACTERS,
        TokenCharacterPosition.ALL : __COMMON_CHARACTER_SETS.DIGITS_DOT,
        'trailing': __COMMON_CHARACTER_SETS.LETTERS | {'+','-','*','/','^'} | __COMMON_CHARACTER_SETS.BRACKETS,
    },
    {
        'tokenType' : 'add',
        TokenCharacterPosition.LEADING : {'+'},
        TokenCharacterPosition.FOLLOWING : TokenCharacterPositionPointer.END_CHARACTERS,
        TokenCharacterPosition.ALL : TokenCharacterPositionPointer.END_CHARACTERS,
        'trailing' : __COMMON_CHARACTER_SETS.LETTERS | __COMMON_CHARACTER_SETS.DIGITS_DOT | __COMMON_CHARACTER_SETS.BRACKETS,
    },
    {
        'tokenType' : 'sub',
        TokenCharacterPosition.LEADING : {'-'},
        TokenCharacterPosition.FOLLOWING : TokenCharacterPositionPointer.END_CHARACTERS,
        TokenCharacterPosition.ALL : TokenCharacterPositionPointer.END_CHARACTERS,
        'trailing' : __COMMON_CHARACTER_SETS.LETTERS | __COMMON_CHARACTER_SETS.DIGITS_DOT | __COMMON_CHARACTER_SETS.BRACKETS,
    },
    {
        'tokenType' : 'mul',
        TokenCharacterPosition.LEADING : {'*'},
        TokenCharacterPosition.FOLLOWING : TokenCharacterPositionPointer.END_CHARACTERS,
        TokenCharacterPosition.ALL : TokenCharacterPositionPointer.END_CHARACTERS,
        'trailing' : __COMMON_CHARACTER_SETS.LETTERS | __COMMON_CHARACTER_SETS.DIGITS_DOT | __COMMON_CHARACTER_SETS.BRACKETS,
    },
    {
        'tokenType' : 'div',
        TokenCharacterPosition.LEADING : {'/'},
        TokenCharacterPosition.FOLLOWING : TokenCharacterPositionPointer.END_CHARACTERS,
        TokenCharacterPosition.ALL : TokenCharacterPositionPointer.END_CHARACTERS,
        'trailing' : __COMMON_CHARACTER_SETS.LETTERS | __COMMON_CHARACTER_SETS.DIGITS_DOT | __COMMON_CHARACTER_SETS.BRACKETS,
    },
    {
        'tokenType' : 'exp',
        TokenCharacterPosition.LEADING : {'^'},
        TokenCharacterPosition.FOLLOWING : TokenCharacterPositionPointer.END_CHARACTERS,
        TokenCharacterPosition.ALL : TokenCharacterPositionPointer.END_CHARACTERS,
        'trailing' : __COMMON_CHARACTER_SETS.LETTERS | __COMMON_CHARACTER_SETS.DIGITS_DOT | __COMMON_CHARACTER_SETS.BRACKETS | {'-'},
    },
    {
        'tokenType' : 'exp',
        TokenCharacterPosition.LEADING : {'^'},
        TokenCharacterPosition.FOLLOWING : TokenCharacterPositionPointer.END_CHARACTERS,
        TokenCharacterPosition.ALL : TokenCharacterPositionPointer.END_CHARACTERS,
        'trailing' : __COMMON_CHARACTER_SETS.LETTERS | __COMMON_CHARACTER_SETS.DIGITS_DOT | __COMMON_CHARACTER_SETS.BRACKETS | {'-'},
    },
]
"""
Gibt für eine bestimmte Position eines Tokens des Typs TokenType die erlaubten Zeichen zurück.
>>> ALLOWED_TOKEN_CHARACTERS[TokenTypeID][Position] -> re.Pattern[str] | SpecialCharacterTypes

class CharacterPositionNode():
    def """