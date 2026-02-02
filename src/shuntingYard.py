from lexerToken import *

def preTermParsingCheck(inputTokenList: list[Token|TokenWithPrecedence]) -> list[Token|TokenWithPrecedence]:
    """
    Prüft, ob der Term aufeinanderfolgende Operatoren (außer Funktionen an zweiter Stelle) aufweist --> Fehler \n
    und Minuszeichen ohne vorstehendes Literal wird eine Null vorangefügt

    Args:
        inputTokenQueue (list[Token | TokenWithPrecedence]): _description_

    Returns:
        list[Token|TokenWithPrecedence]: _description_
    """
    # Für jedes Token bis einschließlich des vorletzten wird überprüft, ob es ein Operator ist
    # wenn ja wird das nachfolgende Token ebenfalls geprüft --> Fehler, wenn Operator aber keine Funktion
    count = len(inputTokenList)
    for i in range(count-1):
        if inputTokenList[i].getTokenType() in {TokenType.OPERATOR,TokenType.FUNCTION}:
            # das nachfolgende darf ausschließlich eine Funktion sein, zur Abfrage der Priorität muss erst geprüft werden, ob überhaupt Operator
            if inputTokenList[i+1].getTokenType() in {TokenType.OPERATOR,TokenType.FUNCTION}:
                if not(inputTokenList[i+1].getPrecedence() == 5): # type: ignore
                    raise Exception(f"Syntaxfehler an Position {inputTokenList[i+1].getPosition()}: Operator folgt auf einen anderen Operator.")
    
    # Erstellung des Null-Tokens
    # Position ist egal, da die Positionen für Referenzen in der Originaleingabe verwendet werden
    zeroToken = Token(TokenType.LITERAL, '0', (-1, -1))
    
    # Prüfung, ob das erste Token ein Subtraktions-Operator ist --> wenn ja Null davor setzen
    if inputTokenList[0].getValue() == '-':
        inputTokenList.insert(0, zeroToken)
        count += 1
         
    # Für jedes Token startend beim zweiten bis einschließlich des vorletzten (Minus am Ende dürfte eh nicht sein) wird überprüft, ob es ein Subtraktions-Operator ist
    # wenn ja wird das vorrangehende Token auf eine öffnende Klammer oder ein Argumenttrennzeichen geprüft
    i = 1
    while i<len(inputTokenList)-1:
        if inputTokenList[i].getValue() == '-':
            if inputTokenList[i-1].getTokenType() in {TokenType.PARENTHESIS_OPEN,TokenType.COMMA}:
                inputTokenList.insert(i, zeroToken)
                i+=1
        i += 1
    
    return inputTokenList

def shuntingYardAlgorithm(inputTermTokenQueue: list[Token|TokenWithPrecedence]) -> list[Token|TokenWithPrecedence]:
    """
    Formt einen in Infixnotation gegebenen Term in einen Term in Postfixnotation um.
    Verwendet wird dabei der Shunting-Yard-Algorithmus.

    Args:
        inputTermTokenQueue (list[Token | TokenWithPrecedence]): Termtokenliste in Infixnotation

    Returns:
        list[Token|TokenWithPrecedence]: Termtokenliste in Postfixnotation
    """
    
    # Schlangen und Stapel können in Python über Listen implementiert werden
    # Stapel: hinzufügen: stapel.append(element); entfernen: element=stapel.pop()
    # Schlange: hinzufügen: schlange.append(element); entfernen: element=schlange.pop(0)
    
    operatorStack : list[Token|TokenWithPrecedence] = list()
    outputTermTokenQueue : list[Token|TokenWithPrecedence] = list()
    
    # Iteration über jedes Token der Eingabeschlange solange diese nicht leer ist
    while inputTermTokenQueue != []:
        token = inputTermTokenQueue.pop(0)
        tokenType = token.getTokenType()
        
        # Wenn das Token eine Zahl oder eine Variable ist (hier können Unknown-Ids nur Variablen sein)
        if tokenType in {TokenType.LITERAL, TokenType.UNKNOWN_IDENTIFIER}:
            outputTermTokenQueue.append(token)
            continue
        
        # Wenn das Token ein Operator ist
        if tokenType in {TokenType.OPERATOR,TokenType.FUNCTION}:
            # Solange der Operatorstack nicht leer ist und
            # solange die Stapelspitze ein Operator ist und
            # solange das oberste Token des Operatorstacks ein Operator mit größerer Priorität oder mit gleicher Priorität bei gleichzeitiger Linksassoziativität ist
            abort = False
            while not abort:
                if operatorStack == []:
                    abort = True
                    continue
                if not (operatorStack[-1].getTokenType() in {TokenType.OPERATOR,TokenType.FUNCTION}):
                    abort = True
                    continue
                tokenPrecedence = token.getPrecedence() # type: ignore
                if not(operatorStack[-1].getPrecedence() > tokenPrecedence or (operatorStack[-1].getPrecedence() == tokenPrecedence and token.getAssociativity() == Associativity.LEFT)): # type: ignore
                    abort = True
                    continue
                
                # Wenn alle Bedingungen erfüllt sind
                outputTermTokenQueue.append(operatorStack.pop())
                    
            operatorStack.append(token)
            continue
        
        # Wenn das Token eine öffnende Klammer ist
        if tokenType == TokenType.PARENTHESIS_OPEN:
            operatorStack.append(token)
            continue
        
        # Wenn das Token eine schließende Klammer ist
        if tokenType == TokenType.PARENTHESIS_CLOSE:
            try:
                while operatorStack[-1].getTokenType() != TokenType.PARENTHESIS_OPEN:
                    outputTermTokenQueue.append(operatorStack.pop())
            except IndexError:
                raise Exception(f"Syntaxfehler: Für die schließende Klammer an Position {token.getPosition()} wurde keine öffnende Klammer gefunden.")
            
            # das oberste Token des Operatorstapels müsste jetzt eine öffnende Klammer sein --> verwerfen
            operatorStack.pop()
            continue
        
        # Wenn das Token ein Trennzeichen ist (in Termen nur Kommata)
        if tokenType == TokenType.COMMA:
            try:
                while operatorStack[-1].getTokenType() != TokenType.PARENTHESIS_OPEN:
                    outputTermTokenQueue.append(operatorStack.pop())
            except IndexError:
                raise Exception(f"Syntaxfehler: Für das Argumenttrennzeichen (Komma) an Position {token.getPosition()} wurde keine vorrangehende öffnende Klammer gefunden.")
            
    # Am Ende den Operatorstack in den Output leeren 
    while operatorStack != []:
        token = operatorStack.pop()
        if token.getTokenType() == TokenType.PARENTHESIS_OPEN:
            raise Exception(f"Syntaxfehler: Für die öffnende Klammer an Position {token.getPosition()} wurde keine schließende Klammer gefunden.")
        outputTermTokenQueue.append(token)
    
    
    return outputTermTokenQueue

if __name__ == "__main__":
    from lexer import tokenize
    _, tokenStream, _  = tokenize("-1**loremipsum2(-2+3,42^69-3+5,4)^5")
    print("\nEingabetermtoken in Infixnotation: ")
    tokenStream = preTermParsingCheck(tokenStream)
    for token in tokenStream: print(token)
    print()
    newTokenStream = shuntingYardAlgorithm(tokenStream)
    print("\nAusgabetermtoken in Postfixnotation: ")
    for token in newTokenStream: print(token)