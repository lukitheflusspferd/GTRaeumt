from enum import Enum
import re

class RE_P(Enum):
    """
    Gesammelte RexEx-Muster für häufige Verwendung
    """
    BRACKETS = r'[()\[\]{}]'
    LETTERS = r'[A-Za-z]'
    DIGITS_DOT = r'[0-9.]'
    

class TokenCharacterpositionPointer(Enum):
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
        'leading' : re.compile(RE_P.LETTERS),
        'following' : TokenCharacterpositionPointer.ALL_CHARACTERS,
        'all' : re.compile(RE_P.LETTERS | r'[0-9]'),
        'trailing' : re.compile(r'[+\-*/^]' | RE_P.BRACKETS),
        #'specialExeptions' : None
    },
    {
        'tokenType' : 'nmbr',
        'leading' : TokenCharacterpositionPointer.ALL_CHARACTERS,
        'following' : TokenCharacterpositionPointer.ALL_CHARACTERS,
        'all' : re.compile(RE_P.DIGITS_DOT),
        'trailing': re.compile(RE_P.LETTERS | r'[+\-*/^]' | RE_P.BRACKETS),
    },
    {
        'tokenType' : 'add',
        'leading' : re.compile(r'+'),
        'following' : TokenCharacterpositionPointer.END_CHARACTERS,
        'all' : TokenCharacterpositionPointer.END_CHARACTERS,
        'trailing' : re.compile(RE_P.LETTERS | RE_P.DIGITS_DOT | RE_P.BRACKETS),
    },
    {
        'tokenType' : 'sub',
        'leading' : re.compile(r'-'),
        'following' : TokenCharacterpositionPointer.END_CHARACTERS,
        'all' : TokenCharacterpositionPointer.END_CHARACTERS,
        'trailing' : re.compile(RE_P.LETTERS | RE_P.DIGITS_DOT | RE_P.BRACKETS),
    },
    {
        'tokenType' : 'mul',
        'leading' : re.compile(r'*'),
        'following' : TokenCharacterpositionPointer.END_CHARACTERS,
        'all' : TokenCharacterpositionPointer.END_CHARACTERS,
        'trailing' : re.compile(RE_P.LETTERS | RE_P.DIGITS_DOT | RE_P.BRACKETS),
    },
    {
        'tokenType' : 'div',
        'leading' : re.compile(r'/'),
        'following' : TokenCharacterpositionPointer.END_CHARACTERS,
        'all' : TokenCharacterpositionPointer.END_CHARACTERS,
        'trailing' : re.compile(RE_P.LETTERS | RE_P.DIGITS_DOT | RE_P.BRACKETS),
    },
    {
        'tokenType' : 'exp',
        'leading' : re.compile(r'^'),
        'following' : TokenCharacterpositionPointer.END_CHARACTERS,
        'all' : TokenCharacterpositionPointer.END_CHARACTERS,
        'trailing' : re.compile(RE_P.LETTERS | RE_P.DIGITS_DOT | RE_P.BRACKETS | r'[-]'),
    },
    {
        'tokenType' : 'exp',
        'leading' : re.compile(r'^'),
        'following' : TokenCharacterpositionPointer.END_CHARACTERS,
        'all' : TokenCharacterpositionPointer.END_CHARACTERS,
        'trailing' : re.compile(RE_P.LETTERS | RE_P.DIGITS_DOT | RE_P.BRACKETS | r'[-]'),
    },
]
"""
Gibt für eine bestimmte Position eines Tokens des Typs TokenType die erlaubten Zeichen zurück.
>>> ALLOWED_TOKEN_CHARACTERS[TokenTypeID][Position] -> re.Pattern[str] | SpecialCharacterTypes
"""