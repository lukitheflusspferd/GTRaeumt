from lexerToken import *
from shuntingYard import*

def prepareTokenstram(tokenList: list[Token|TokenWithPrecedence]) -> list[Token|TokenWithPrecedence|TermSubstitutionToken]:
    """
    Extrahiert die Terme und substituiert diese zu TermSubstitutionToken

    Args:
        tokenList (list[Token | TokenWithPrecedence]): Tokenstrom des Lexers

    Returns:
        list[Token|TokenWithPrecedence|TermSubstitionToken]: Gibt den modifizierten Tokenstrom zurück
    """
    if tokenList[0].getTokenType().value.startswith("command"):
        # Befehl
        
        # zweites Token muss öffnende Klammer sein
        if tokenList[1].getTokenType() != TokenType.PARENTHESIS_OPEN:
            raise Exception("Syntaxfehler: Nach einem Befehlstoken keine öffnende Klammer gefunden!")
        
        # wenn drittes Token Funktionsidentifier und danach Klammer oder senkrechter Strich, dann wird nichts substituiert --> liste unverändert zurückgeben
        if tokenList[2].getTokenType() == TokenType.FUNCTION:
            if tokenList[3].getTokenType() == TokenType.PARENTHESIS_CLOSE or tokenList[3].getTokenType() == TokenType.ARGUMENTSEPERATOR:
                return tokenList
        
        # nach erstem Auftreten von senkrechtem Strich suchen suchen
        seperatorPosition = -1
        i = 3 # drittes darf kein Seperator sein, da jetzt eig. Teil eines Terms --> mit viertem Token starten (in Python mit 4->3)
        while seperatorPosition == -1 and i<len(tokenList):
            if tokenList[i].getTokenType() == TokenType.ARGUMENTSEPERATOR:
                seperatorPosition = i
            i += 1
            
        # Wenn kein Seperator, dann bis zum vorletzen Token substituieren (letztes müsste Klammer sein) (y bei list[x:y] nicht inkludiert)
        if seperatorPosition == -1:
            termTokenListToSubstitute = tokenList[2:len(tokenList)-1]
            termTokenListToSubstitute = preTermParsingCheck(termTokenListToSubstitute)
            termTokenListToSubstitute = shuntingYardAlgorithm(termTokenListToSubstitute)
            tokenList = tokenList[0:2] + [TermSubstitutionToken(termTokenListToSubstitute)] + [tokenList[len(tokenList)-1]]
            return tokenList
        
        # Jetzt bis zum Seperator substituieren
        termTokenListToSubstitute = tokenList[2:seperatorPosition]
        termTokenListToSubstitute = preTermParsingCheck(termTokenListToSubstitute)
        termTokenListToSubstitute = shuntingYardAlgorithm(termTokenListToSubstitute)
        tokenList = tokenList[0:2] + [TermSubstitutionToken(termTokenListToSubstitute)] + tokenList[seperatorPosition:len(tokenList)]
        return tokenList
    
    else:
        # Sollte dann Definition sein
        
        # nach erstem Auftreten von := suchen suchen
        assignmentPosition = -1
        i = 1 # frühestens zweites Token, da erstes Bezeichner ist
        while assignmentPosition == -1 and i<len(tokenList):
            if tokenList[i].getTokenType() == TokenType.ASSIGNMENT:
                assignmentPosition = i
            i += 1
            
        # Wenn := nicht existiert, dann Fehler:
        if assignmentPosition == -1:
            raise Exception("Syntaxfehler: Befehlstoken am Anfang oder ':=' irgendwo außer am Anfang erwartet, aber nicht gefunden.")
        
        # nach erstem Auftreten von senkrechtem Strich suchen suchen
        seperatorPosition = -1
        i = 3 # drittes darf kein Seperator sein, da jetzt eig. Teil eines Terms --> mit viertem Token starten (in Python mit 4->3)
        while seperatorPosition == -1 and i<len(tokenList):
            if tokenList[i].getTokenType() == TokenType.ARGUMENTSEPERATOR:
                seperatorPosition = i
            i += 1
        
        # Wenn kein Seperator, dann bis zum letzen Token substituieren
        if seperatorPosition == -1:
            termTokenListToSubstitute = tokenList[assignmentPosition+1:len(tokenList)]
            termTokenListToSubstitute = preTermParsingCheck(termTokenListToSubstitute)
            termTokenListToSubstitute = shuntingYardAlgorithm(termTokenListToSubstitute)
            tokenList = tokenList[0:assignmentPosition+1] + [TermSubstitutionToken(termTokenListToSubstitute)]
            return tokenList
        
        # Jetzt bis zum Seperator substituieren
        
        termTokenListToSubstitute = tokenList[assignmentPosition+1:seperatorPosition]
        termTokenListToSubstitute = preTermParsingCheck(termTokenListToSubstitute)
        termTokenListToSubstitute = shuntingYardAlgorithm(termTokenListToSubstitute)
        tokenList = tokenList[0:assignmentPosition+1] + [TermSubstitutionToken(termTokenListToSubstitute)] + tokenList[seperatorPosition:len(tokenList)]
        return tokenList
        
        