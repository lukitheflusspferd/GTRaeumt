import lexer
import prepareTokenstream
import lexerToken

# Dies ist die Hauptdatei, welche alle Algorithmen zusammenfasst

print("Gekürzte Ausgabe...\n")

inputString = input("Bitte einen Befehl oder eine Definition eingeben:\n")

# Lexikalische Analyse
print("\n-> Ausführung der Lexikalischen Analyse")
lexemList, tokenList, unknownIdentifiers = lexer.tokenize(inputString)
print("Token:", lexemList, " \n")
#print("\nGefundene unbekannte Bezeichner:", unknownIdentifiers)

# Syntaktische Analyse: Shunting-Yard-Algorithmus und Substitution
newTokenList = prepareTokenstream.prepareTokenstram(tokenList)
output = list()
for t in newTokenList:
    if t.getTokenType() == lexerToken.TokenType.TERM_SUBSTITUTION:
        temp = ">>> "
        for st in t.getTokenlist(): # type: ignore
            temp = temp + ' '+str(st.getValue())
        temp += '  <<<'
        output.append(temp)
        continue
    output.append(t.getValue())
    
print("-> Ausführung des Shunting-Yard-Algorithmus")
print("Neue Token:", output)

# Hier würde der LL(1)-Parser folgen