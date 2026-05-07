from LLParserGrammar import *
from lexerToken import *

def LLParser(inputTokenQueue : list[Token | TokenWithPrecedence | TermSubstitutionToken]):
    """
    LL(1)-Parser für die Eingabegrammatik

    Args:
        inputTokenQueue (list[Token  |  TokenWithPrecedence  |  TermSubstitutionToken]): Liste der Token
    """
    # Schlangen und Stapel können in Python über Listen implementiert werden
    # Stapel: hinzufügen: stapel.append(element); entfernen: element=stapel.pop(); Zugriff auf Kopf: stapel[-1]
    # Schlange: hinzufügen: schlange.append(element); entfernen: element=schlange.pop(0); Zugriff auf Kopf: schlange[0]
    stack : list[TokenType | Nonterminals] = [TokenType.EOI, Nonterminals.START]
    inputTokenQueue.append(Token(TokenType.EOI, "", (-1,-1)))
    
    usedRules = []
    
    # Hauptschleife
    # sobald Stapel leer (EOI) kann der Parser nichts mehr machen --> Schleife terminiert
    # danach Überprüfung, ob beide leer --> dann erfolgreich
    while not stack[-1]==TokenType.EOI:
        #print(stack)
        #print(inputTokenQueue)
        stackHead = stack.pop()
        
        # Wenn auf Stapel ein Nichtterminal
        if type(stackHead) == Nonterminals:
            ruleNumber = parseTable[stackHead].get(inputTokenQueue[0].getTokenType())
            if ruleNumber == None:
                raise Exception(f"Im LL-Parser gibt es für das Nichtterminal der Stack-Spitze und das Terminal der Eingabetokenschlange keine Produktionsregel.")
            usedRules.append(ruleNumber)
            productionRuleContent = productionRules[ruleNumber].copy()
            productionRuleContent.reverse()
            stack.extend(productionRuleContent)
        elif type(stackHead) == TokenType:
            token = inputTokenQueue.pop(0)
            if stackHead != token.getTokenType():
                raise Exception(f"Im LL-Parser stimmt das Terminal der Stack-Spitze nicht mit dem der Eingabetokenschlange überein. Position des Tokens: {token.getPosition()}")
    
    if not (stack[-1]==TokenType.EOI and inputTokenQueue[0].getTokenType() == TokenType.EOI):
        print(stack)
        print(inputTokenQueue[0].getTokenType())
        raise Exception("Der LL-Parser ist einseitig terminiert.")
    
    print("Im Parser angewendete Regeln:", usedRules)
    