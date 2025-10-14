import time

class speedTestPublicVariablesClass():
    """
    Einfache Klasse mit drei öffentlichen Attributen zum Vergleich mit anderen Strukturen
    """
    def __init__(self) -> None:
        self.a = 1
        self.b = 2
        self.c = 3

class speedTestGetMethodClass():
    """
    Einfache Klasse mit drei privaten Attributen und den zugehörigen get-Methoden zum Vergleich mit anderen Strukturen
    """
    def __init__(self) -> None:
        self.__a = 1
        self.__b = 2
        self.__c = 3

    def get_a(self): return self.__a
    
    def get_b(self): return self.__b
    
    def get_c(self): return self.__c
    
# Wörterbuch mit drei Einträgen zum Vergleich mit anderen Strukturen
speedTestDict = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

if __name__ == "__main__":
    startzeit = time.time()
    Klasse = speedTestPublicVariablesClass()
    for _ in range(100000000):
        _ = Klasse.a
        _ = Klasse.b
        _ = Klasse.c
    print(f"Die Zeit für das 100 Mio.-fache Abrufen aus einer Klasse mit public-Variablen beträgt {time.time()-startzeit} Sekunden.")
    
    startzeit = time.time()
    Klasse = speedTestGetMethodClass()
    for _ in range(100000000):
        _ = Klasse.get_a
        _ = Klasse.get_b
        _ = Klasse.get_c
    print(f"Die Zeit für das 100 Mio.-fache Abrufen aus einer Klasse mit get-Methoden beträgt {time.time()-startzeit} Sekunden.")
    
    startzeit = time.time()
    for _ in range(100000000):
        _ = speedTestDict["a"]
        _ = speedTestDict["b"]
        _ = speedTestDict["c"]
    print(f"Die Zeit für das 100 Mio.-fache Abrufen aus einem Wörterbuch beträgt {time.time()-startzeit} Sekunden.")
    
else:
    raise Exception("Datei soll nicht importiert werden!")