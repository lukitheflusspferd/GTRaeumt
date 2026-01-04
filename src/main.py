import lexer
import prepareTokenstream

# Dies ist die Hauptdatei, welche alle Algorithmen zusammenfasst

inputString = input("Bitte einen Befehl oder eine Definition eingeben:\n")

# Lexikalische Analyse
lexemList, tokenList, unknownIdentifiers = lexer.tokenize(inputString)
print("\nListe der Lexeme", lexemList, " \n")
print("Liste der Token:")
for t in tokenList: print(t)
print("\nGefundene unbekannte Bezeichnungen:", unknownIdentifiers)

# Syntaktische Analyse: Shunting-Yard-Algorithmus und Substitution
newTokenList = prepareTokenstream.prepareTokenstram(tokenList)
print("\nNeue Liste der Token:")
for t in newTokenList: print(t)

# Hier würde der LL(1)-Parser folgen