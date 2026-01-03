selfdefinedConstants = dict()

selfdefinedConstants["bsp_konst"] = 17

def getSelfdefinedConstants():
    return selfdefinedConstants

# Bezeichner und Stelligkeiten von selbstdefinierten Funktionen
# die Bezeichner müssen vollständig klein geschrieben sein
selfdefinedFunctionsIdentifier = {
    "loremipsum2",
    "beispielfunktion"
}

def getSelfdefinedFunctionIdentifier():
    return selfdefinedFunctionsIdentifier

selfdefinedFunctionsArity = {
    "loremipsum2" : 42,
    "beispielfunktion" : 3,
    "f": 2
}

def getSelfdefinedFunctionArity(functionIdentifier):
    return selfdefinedFunctionsArity[functionIdentifier]