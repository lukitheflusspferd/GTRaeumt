from LLParserGrammar import *
from lexerToken import *

def LLParser(inputTokenQueue : list[Token | TokenWithPrecedence | TermSubstitutionToken]):
    """
    LL(1)-Parser für die Eingabegrammatik

    Args:
        inputTokenQueue (list[Token  |  TokenWithPrecedence  |  TermSubstitutionToken]): Liste der Token
    """
    # Schlangen und Stapel können in Python über Listen implementiert werden
    # Stapel: hinzufügen: stapel.append(element); entfernen: element=stapel.pop()
    # Schlange: hinzufügen: schlange.append(element); entfernen: element=schlange.pop(0)
    stack = [Token(TokenType.EOI, "", (-1,-1)), Nonterminals.START]
    inputTokenQueue.append(Token(TokenType.EOI, "", (-1,-1)))
    
    # Hauptschleife
    pass