from enum import Enum

from lexerToken import *

class Nonterminals(Enum):
    """
    Enum, welches sämtliche in der LL(1)-Grammatik verwendeten Nichtterminale vereinheitlicht
    """
    START = "Start",
    PLOT_LEADING = "PlotLeading"
    PLOT_MIDDLE = "PlotMiddle",
    PLOT_TRAILING = "PlotTrailing",
    MIN_LEADING = "MinLeading",
    MIN_TRAILING = "MinTrailing",
    MAX_LEADING = "MaxLeading",
    MAX_TRAILING = "MaxTrailing",
    WENDE_LEADING = "WendeLeading",
    WENDE_TRAILING = "WendeTrailing",
    ABLEITUNG_LEADING = "AbleitungLeading",
    ABLEITUNG_MIDDLE = "AbleitungMiddle",
    ABLEITUNG_TRAILING = "AbleitungTrailing",
    DEFINITION_LEADING = "DefinitionLeading",
    DEFINITION_MIDDLE = "DefinitionMiddle",
    ARGUMENTS = "Arguments",
    ARGUMENTS_FOLLOWING = "ArgumentsFollowing",
    DEFINITION_TRAILING = "DefinitionTrailing",
    CONDITIONS = "Conditions",
    CONDITIONS_FOLLOWING = "ConditionsFollowing",
    SINGLE_CONDITION = "SingleCondition",
    BERECHNE_LEADING = "BerechneLeading",
    BERECHNE_TRAILING = "BerechneTrailing",
    LITERALS = "Literals",
    LITERALS_FOLLOWING = "LiteralsFollowing"

    

parseTable : dict[Nonterminals,dict[TokenType,int]] = {
    Nonterminals.START : {
        TokenType.COMMAND_PLOT : 2,
        TokenType.COMMAND_MIN : 3,
        TokenType.COMMAND_MAX : 4,
        TokenType.COMMAND_WENDE : 5,
        TokenType.COMMAND_ABLEITUNG : 6,
        TokenType.COMMAND_BERECHNE : 7,
        TokenType.UNKNOWN_IDENTIFIER : 8,
        },
    Nonterminals.PLOT_LEADING : {TokenType.COMMAND_PLOT : 9},
    Nonterminals.PLOT_MIDDLE : {
        TokenType.TERM_SUBSTITUTION : 10,
        TokenType.FUNCTION : 11
        },
    Nonterminals.PLOT_TRAILING : {
        TokenType.PARENTHESIS_CLOSE : 12,
        TokenType.ARGUMENTSEPERATOR : 13
        },
    Nonterminals.MIN_LEADING : {TokenType.COMMAND_MIN : 14},
    Nonterminals.MIN_TRAILING : {
        TokenType.TERM_SUBSTITUTION : 15,
        TokenType.FUNCTION : 16
        },
    Nonterminals.MAX_LEADING : {TokenType.COMMAND_MAX : 17},
    Nonterminals.MAX_TRAILING : {
        TokenType.TERM_SUBSTITUTION : 18,
        TokenType.FUNCTION : 19
        },
    Nonterminals.WENDE_LEADING : {TokenType.COMMAND_WENDE : 20},
    Nonterminals.WENDE_TRAILING : {
        TokenType.TERM_SUBSTITUTION : 21,
        TokenType.FUNCTION : 22
        },
    Nonterminals.ABLEITUNG_LEADING : {TokenType.COMMAND_ABLEITUNG : 23},
    Nonterminals.ABLEITUNG_MIDDLE : {
        TokenType.TERM_SUBSTITUTION : 24,
        TokenType.FUNCTION : 25
        },
    Nonterminals.ABLEITUNG_TRAILING : {
        TokenType.PARENTHESIS_CLOSE : 27,
        TokenType.ARGUMENTSEPERATOR : 26
        },
    Nonterminals.DEFINITION_LEADING : {TokenType.UNKNOWN_IDENTIFIER : 28},
    Nonterminals.DEFINITION_MIDDLE : {
        TokenType.PARENTHESIS_OPEN : 30,
        TokenType.ASSIGNMENT : 29
        },
    Nonterminals.ARGUMENTS : {TokenType.UNKNOWN_IDENTIFIER : 31},
    Nonterminals.ARGUMENTS_FOLLOWING : {
        TokenType.PARENTHESIS_CLOSE : 33,
        TokenType.COMMA : 32
        },
    Nonterminals.DEFINITION_TRAILING : {
        TokenType.ARGUMENTSEPERATOR : 34,
        TokenType.EOI : 35
        },
    Nonterminals.CONDITIONS : {TokenType.UNKNOWN_IDENTIFIER : 36},
    Nonterminals.CONDITIONS_FOLLOWING : {
        TokenType.PARENTHESIS_CLOSE : 38,
        TokenType.SEPERATOR : 37,
        TokenType.EOI : 38,
        },
    Nonterminals.SINGLE_CONDITION : {TokenType.UNKNOWN_IDENTIFIER : 39},
    Nonterminals.BERECHNE_LEADING : {TokenType.COMMAND_BERECHNE : 40},
    Nonterminals.BERECHNE_TRAILING : {
        TokenType.TERM_SUBSTITUTION : 41,
        TokenType.FUNCTION : 42
        },
    Nonterminals.LITERALS : {TokenType.LITERAL : 43},
    Nonterminals.LITERALS_FOLLOWING : {
        TokenType.PARENTHESIS_CLOSE : 45,
        TokenType.COMMA : 44
        },
}
"""
# Parsetabelle\n
Wörterbuch 'aktuelles Nichtterminal' -> (Wörterbuch 'aktueller Tokentyp' -> 'anzuwendende Regel')
"""

productionRules : dict[int,list[Nonterminals|TokenType]] = {
    2  : [Nonterminals.PLOT_LEADING],
    3  : [Nonterminals.MIN_LEADING],
    4  : [Nonterminals.MAX_LEADING],
    5  : [Nonterminals.WENDE_LEADING],
    6  : [Nonterminals.ABLEITUNG_LEADING],
    7  : [Nonterminals.BERECHNE_LEADING],
    8  : [Nonterminals.DEFINITION_LEADING],
    9  : [TokenType.COMMAND_PLOT, TokenType.PARENTHESIS_OPEN, Nonterminals.PLOT_MIDDLE],
    10 : [TokenType.TERM_SUBSTITUTION, Nonterminals.PLOT_TRAILING],
    11 : [TokenType.FUNCTION, Nonterminals.PLOT_TRAILING],
    12 : [TokenType.PARENTHESIS_CLOSE],
    13 : [TokenType.ARGUMENTSEPERATOR, Nonterminals.CONDITIONS, TokenType.PARENTHESIS_CLOSE],
    14 : [TokenType.COMMAND_MIN, TokenType.PARENTHESIS_OPEN, Nonterminals.MIN_TRAILING],
    15 : [TokenType.TERM_SUBSTITUTION, TokenType.PARENTHESIS_CLOSE],
    16 : [TokenType.FUNCTION, TokenType.PARENTHESIS_CLOSE],
    17 : [TokenType.COMMAND_MAX, TokenType.PARENTHESIS_OPEN, Nonterminals.MAX_TRAILING],
    18 : [TokenType.TERM_SUBSTITUTION, TokenType.PARENTHESIS_CLOSE],
    19 : [TokenType.FUNCTION, TokenType.PARENTHESIS_CLOSE],
    20 : [TokenType.COMMAND_WENDE, TokenType.PARENTHESIS_OPEN, Nonterminals.WENDE_TRAILING],
    21 : [TokenType.TERM_SUBSTITUTION, TokenType.PARENTHESIS_CLOSE],
    22 : [TokenType.FUNCTION, TokenType.PARENTHESIS_CLOSE],
    23 : [TokenType.COMMAND_ABLEITUNG, TokenType.PARENTHESIS_OPEN, Nonterminals.ABLEITUNG_MIDDLE],
    24 : [TokenType.TERM_SUBSTITUTION, TokenType.ARGUMENTSEPERATOR, TokenType.UNKNOWN_IDENTIFIER, Nonterminals.ABLEITUNG_TRAILING],
    25 : [TokenType.FUNCTION, TokenType.ARGUMENTSEPERATOR, TokenType.UNKNOWN_IDENTIFIER, Nonterminals.ABLEITUNG_TRAILING],
    26 : [TokenType.ARGUMENTSEPERATOR, TokenType.UNKNOWN_IDENTIFIER, TokenType.PARENTHESIS_CLOSE],
    27 : [TokenType.PARENTHESIS_CLOSE],
    28 : [TokenType.UNKNOWN_IDENTIFIER, Nonterminals.DEFINITION_MIDDLE],
    29 : [TokenType.ASSIGNMENT, TokenType.TERM_SUBSTITUTION, Nonterminals.DEFINITION_TRAILING],
    30 : [TokenType.PARENTHESIS_OPEN, Nonterminals.ARGUMENTS, TokenType.PARENTHESIS_CLOSE, TokenType.ASSIGNMENT, TokenType.TERM_SUBSTITUTION, Nonterminals.DEFINITION_TRAILING],
    31 : [TokenType.UNKNOWN_IDENTIFIER, Nonterminals.ARGUMENTS_FOLLOWING],
    32 : [TokenType.COMMA, TokenType.UNKNOWN_IDENTIFIER, Nonterminals.ARGUMENTS_FOLLOWING],
    33 : [],
    34 : [TokenType.ARGUMENTSEPERATOR, Nonterminals.CONDITIONS],
    35 : [],
    36 : [Nonterminals.SINGLE_CONDITION, Nonterminals.CONDITIONS_FOLLOWING],
    37 : [TokenType.SEPERATOR, Nonterminals.SINGLE_CONDITION, Nonterminals.CONDITIONS_FOLLOWING],
    38 : [],
    39 : [TokenType.UNKNOWN_IDENTIFIER, TokenType.RELATIONAL_OPERATOR, TokenType.LITERAL],
    40 : [TokenType.COMMAND_BERECHNE, TokenType.PARENTHESIS_OPEN, Nonterminals.BERECHNE_TRAILING],
    41 : [TokenType.TERM_SUBSTITUTION, TokenType.PARENTHESIS_CLOSE],
    42 : [TokenType.FUNCTION, TokenType.PARENTHESIS_OPEN, Nonterminals.LITERALS, TokenType.PARENTHESIS_CLOSE, TokenType.PARENTHESIS_CLOSE],
    43 : [TokenType.LITERAL, Nonterminals.LITERALS_FOLLOWING],
    44 : [TokenType.COMMA, TokenType.LITERAL, Nonterminals.LITERALS_FOLLOWING],
    45 : []
}