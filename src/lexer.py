from copy import deepcopy

from lexerAutomaton import STATES
import mathToken

def tokenize(expression: str) -> list:
    """
    Zerlegt einen Ausdruck in eine Liste von Tokens

    Args:
        expression (str): Eingabeausdruck

    Raises:
        Exception: Unerwarteter Buchstabe

    Returns:
        list: Liste der Tokenobjekte
    """
    
    tokenFaktory = mathToken.TokenFactory()
    
    # Hinzufügen eines Endleerzeichens, um das letzte Token in jedem Fall zu beenden
    expression += ' '
    
    index = 0
    repeatLetterFlag = False
    # Char auf einen unsinnigen Wert setzen, damit in dem (eigentlich unmöglichen) Fall, dass Char nicht belegt wird,
    # die Anwendung über nextStateID = None in die "Unerwarteter Buchstabe"-Exception läuft
    char = ""
    expressionLength = len(expression)
    nextPossibleStates : dict = deepcopy(STATES["start"])
    currentTokenString = ""
    # Index des Beginns des TokenStrings (aufgrund der Zählweise in Python beginnend bei 0)
    startIndex = 0
    
    tokenList = []
    tokenStringList = []
    
    while index < expressionLength:
        # Nächsten Buchstaben auslesen, wenn das Flag 'repeatLetter' nicht gesetzt ist
        if not repeatLetterFlag:
            char = expression[index]
        
        # In jedem Fall den Folgezustand des Buchstabens auslesen, da sich dieser auch mit Wiederholung geändert hat
        # Hier Abruf mit .get(), da der Buchstabe evtl. ungültig ist
        nextStateID = nextPossibleStates.get(char)
        
        # Das Flag 'repeatLetter' zurücksetzen
        repeatLetterFlag = False
        
        # Prüfen, ob der ausgelesene Buchstabe zu einem Zustand geführt hat
        if nextStateID != None: 
            # print(nextStateID)
            # Wenn der zweite Buchstabe der ID des nächsten Zustands ein Unterstrich ist, ist dieser ein Endzustand
            if nextStateID[1] == '_':
                if nextStateID[0] == 'e':
                    repeatLetterFlag = True
                # Wenn das Zeichen dazugehört, wird es dem String hinzugefügt und der Index erhöht
                # Hier kann das Zeichen kein Leerzeichen sein, da es sich immer im Sonst-Fall befindet
                else: 
                    currentTokenString += char
                    index += 1
                # Der Index ist hier in jedem Fall stellvertretend für das nächste Zeichen, für den Endindex wird daher eins abgezogen    
                print("Endzustand:", nextStateID, "mit Inhalt [{}]".format(currentTokenString))
                tokenList.append(tokenFaktory.generateToken(nextStateID, currentTokenString, (startIndex, index -1)))
                tokenStringList.append(currentTokenString)
                nextPossibleStates = deepcopy(STATES["start"])
                nextStateID = ""
                currentTokenString = ""
                # index steht hier definitiv für den (theoretischen) Beginn des nächsten Tokens -> wird deswegen gespeichert
                startIndex = index
                continue
            else:
                # Hier Abruf mit [], da der State in jedem Fall vorhanden sein sollte
                nextPossibleStates = deepcopy(STATES[nextStateID])
        # Sonst Fehler "Unerwarteter Buchstabe"
        else: raise Exception("Unerwarteter Buchstabe")
        
        # Da 'repeatLetter' hier definitiv nicht gesetzt ist, da nach einem Endzustand die Schleife wiederholt wird, wird der Index erhöht
        index += 1
        
        # Leerzeichen sollen übersprungen werden, wenn ein Leerzeichen erkannt wird, ist definitiv kein Token aktiv und der startIndex muss nach dem Leerzeichen folgen
        # --> dieser wird also auf den gerade berechneten neuen Index gesetzt
        if char != ' ': currentTokenString += char
        else: startIndex = index
        
        print(char, nextStateID)
    
    # TODO: Rückgabe der in der Tokenfactory gesammelten Variablen
    return tokenStringList, tokenList
        
#zk = "Hallo_Welt314Pi_dfs$s"
#zk = "-3.1414.55"
a, b = tokenize("Hallo, Welt: =><>-314*Pi_dfss -3.1414.55/ 69--42")
print("Liste der Lexeme", a, " \n")
print("Liste der Token:")
for t in b: print(t)
