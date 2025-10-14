import operatoren as op

import matplotlib.pyplot as plt
import numpy as np
import time

def fkonst(k : int) -> lambda x: int:
    """
    Erstellt eine Lambda-Funktion, die eine Konstante zurückgibt.
    """
    return lambda x: k 

def freturn() -> lambda x: int:
    """
    Gibt den Parameter direkt als Lambda-Funktion zurück.
    """
    return lambda x: x


def createLambdaExpression(TermInPräfixnotation : list) -> lambda x: int:
    """
    Erstellt eine Lambda-Funktion aus einem gegebenen Term in Präfixnotation.
    """
    return

if __name__ == "__main__":
    #TermInPräfixnotation = "x y z + *"
    """a = freturn()
    b = fkonst(3)
    f = op.mul()(a, a)
    f2 = op.mul()(f, a)"""
    #print(f(14))
    x5 = op.pot()(freturn(), fkonst(5))
    x4 = op.pot()(freturn(), fkonst(4))
    x4 = op.mul()(fkonst(-12), x4)
    x3 = op.pot()(freturn(), fkonst(3))
    x3 = op.mul()(fkonst(35), x3)
    x2 = op.pot()(freturn(), fkonst(2))
    x2 = op.mul()(fkonst(20), x2)
    x1 = op.mul()(fkonst(-156), freturn())
    f = op.sum()(x5, x4)
    f = op.sum()(f, x3)
    f = op.sum()(f, x2)
    f = op.sum()(f, x1)
    f = op.sum()(f, fkonst(112))
    f = op.div()(f, fkonst(56))
    
    # Zeitmessung unter Lambda-Schreibweise
    Zeit = time.time()
    for i in range(-2000000, 2000001):
        n = f(i/100)
    print("Zeit: ", time.time() - Zeit)
    
    # Zeitmessung mit "normaler" Schreibweise
    Zeit = time.time()
    for i in range(-2000000, 2000001):
        #n =(i ** 5 - 12 * i ** 4 + 35 * i ** 3 + 20 * i ** 2 - 156 * i + 112 )/ 56
        x5 = i**5
        x4 = i**4
        x4 = -12 * x4
        x3 = i**3
        x3 = 35 * x3
        x2 = i**2
        x2 = 20 * x2
        x1 = -156 * i
        fkt = x5 + x4
        fkt = fkt + x3
        fkt = fkt + x2
        fkt = fkt + x1
        fkt = fkt + 112
        ftk = fkt / 56  
    print("Zeit: ", time.time() - Zeit)
        
    print(str(f))
    
    # Data for plotting
    t = np.arange(-2.0, 7.0, 0.1)

    fig, ax = plt.subplots()
    ax.plot(t, f(t))

    ax.set(xlabel='x', ylabel='y',
           title='About as simple as it gets, folks')
    ax.grid()

    #fig.savefig("test.png")
    plt.show()