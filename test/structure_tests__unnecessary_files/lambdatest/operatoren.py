def sum() -> lambda func1, func2: lambda x: int:
    """
    Addiert zwei Lambda-Funktionen und gibt die neue Lambda-Funktion zurück.
    """
    return lambda func1, func2: lambda x: func1(x) + func2(x)

def sub() -> lambda func1, func2: lambda x: int:
    """
    Subtrahiert zwei Lambda-Funktionen und gibt die neue Lambda-Funktion zurück.
    """
    return lambda func1, func2: lambda x: func1(x) - func2(x)

def mul() -> lambda func1, func2: lambda x: int:
    """
    Multipliziert zwei Lambda-Funktionen und gibt die neue Lambda-Funktion zurück.
    """
    return lambda func1, func2: lambda x: func1(x) * func2(x)

def div() -> lambda func1, func2: lambda x: int:
    """
    Dividiert zwei Lambda-Funktionen und gibt die neue Lambda-Funktion zurück.
    """
    return lambda func1, func2: lambda x: func1(x) / func2(x)

def pot() -> lambda basisfkt, exponentfkt: lambda x: int:
    """
    Potenziert zwei Lambda-Funktionen und gibt die neue Lambda-Funktion zurück.
    """
    return lambda basisfkt, exponentfkt: lambda x: basisfkt(x) ** exponentfkt(x)