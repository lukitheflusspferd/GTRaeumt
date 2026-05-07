import lexer
import prepareTokenstream
import LLParser

# Dies ist die Hauptdatei, welche alle Algorithmen zusammenfasst

inputString = input("Bitte einen Befehl oder eine Definition eingeben:\n")

# Lexikalische Analyse
lexemList, tokenList, unknownIdentifiers = lexer.tokenize(inputString)
print("\nListe der Lexeme", lexemList, " \n")
print("Liste der Token:")
for t in tokenList: print(t)
#print("\nGefundene unbekannte Bezeichner:", unknownIdentifiers)

# Syntaktische Analyse: Shunting-Yard-Algorithmus und Substitution
newTokenList = prepareTokenstream.prepareTokenstram(tokenList)
print("\nNeue Liste der Token:")
for t in newTokenList: print(t)

print()
print("-> Ausführung des LL-Parsers")
LLParser.LLParser(newTokenList)
print()