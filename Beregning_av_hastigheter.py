import matplotlib.pyplot as plt
import numpy as np
from numpy.core.defchararray import array


def HentDataFraFil(filepath):
    """Leser txt datafil fra tracker.

    Args:
        filepath (string): fra workingdir filepath til datafilen

    Returns:
        touple: returnerer arrays t, x og y. Der t er tiden, x er posisjon
        i x retning og y tilhørende posisjon i y retning.
    """
    
    print("Henter data fra fil", filepath)
    
    #filepath = './Data/txy_1.txt'

    with open(filepath) as file: 
        lines = file.readlines()
        
    #Lagre objekt navn, variabler

    name = lines[0].rstrip() # Navnet på objektet
    labels = tuple(lines[1].rstrip().split('\t')) #Tuple over kolonnenavn
    
    #print('Objectnavn: %s, kolonner: '%(name)+str(labels))

    #Lagre verdiene t,x og y i egne lister
    t = []; x = []; y = [] #tre tomme lister
    for i in range(2, len(lines)):
        l = lines[i].rstrip().split('\t')
        
        t.append(float("{:.5f}".format(float(l[0]))))
        x.append(float("{:.5f}".format(float(l[1]))))
        y.append(float("{:.5f}".format(float(l[2]))))
    
    t, x, y = np.array(t), np.array(x), np.array(y)
    
    print("Innlasting ferdig")
    
    return t, x, y
    
# Plott
def plotBaneForm(x, y, title, xlabel, ylabel, legendLabel, ylabelMin, ylabelMax):
    """Plotter en scatterplot basert på 2 arrays

    Args:
        x (array): posisjoner i x retning
        y (array): tilhørende posisjoner i y retning
    """
    
    baneform = plt.figure('y(x)',figsize=(12,6))
    plt.plot(x, y, label=legendLabel)
    plt.title(title)
    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel ,fontsize=20)
    plt.ylim(ylabelMin, ylabelMax)
    plt.legend()
    plt.grid()
    plt.show()

def observertHastighet_old(t, x, y):
    """Beregner observert hastighet ved å se på de to siste posisjonene

    Args:
        t (np array): tider
        x (np array): x
        y (np array): y

    Returns:
        float: farten basert på siste to målte pkt
    """
    
    v_e = np.sqrt(abs(((y[-2] - y[-1])**2 + abs(x[-2] - x[-1])**2) / abs(t[-2] - t[-1])))
    
    return v_e
    
def observerteHastigheter(x, y):
    """Beregner observert hastighet ved å fortløpende se på 2 tracker-posisjoner

    Args:
        x (np array): x posisjoner
        y (np array): y posisjoner

    Returns:
        Array: farten basert på 2 målepunkter av gangen
    """
    
    # Kamera filmer ved 30fps.
    diffT = 1/30
    
    diffX = np.diff(x)
    diffY = np.diff(y)
    
    dist = np.sqrt(diffX**2 + diffY**2)
    
    velocity = dist/diffT
    
    return velocity

def BeregnHastighet(y):
    """
    Beregner hastigheten
    Formelen antar bevart mekanisk energi og en kompakt kule.
     

    Args:
        y (np.array): posisjoner av kule langs bane
        
    Returns:
        numpy array: array med hastigheter i punktene
    """
    
    #definere konstanter
    g = 9.81
    c = 2/5 #konstant for en kompakt kule
    y0 = y[0] #starthøyde
    
    #beregne hastigheten med utgangspunkt i total mekanisk 
    #energi og energibevaring
    v = np.sqrt((2*g*(abs(y0-y)))/(1+c))
    
    
    return v

def getGjennomsnitt(v):
    return round(np.average(v), 3)

def getStandardAvvik(v):
    return round(np.std(v), 4)

def getStandardFeil(v):
    return round(getStandardAvvik(v)/np.sqrt(len(v)), 5)



def main():
    
    
    ###########################
    
    
    # Konstanter
    xmin = 0.000
    xmax = 1.401
    dx = 0.001
    
    #Horisontal avstand mellom festepunktene er 0.200 m
    h = 0.200
    xfast=np.asarray([0,h,2*h,3*h,4*h,5*h,6*h,7*h])
    
    #y-verdiene til de 8 festepunktene
    yfast = np.asarray([0.399, 0.310, 0.261, 0.254, 0.248, 0.211, 0.165, 0.105])
    
    
    ##########################
    
    
    t, x, y = HentDataFraFil('./Data/txy_1.txt')
    
    #plotBaneForm(x, y)
    
    v = BeregnHastighet(y)
    
    #Plot Observert hastighet
    observertHastighet = plt.figure('v(x)',figsize=(12,6))
    plt.plot(x,v,xfast,yfast,'*')
    plt.title('Banens form')
    plt.xlabel('$x$ (m)',fontsize=20)
    plt.ylabel('$v(x)$ (m)',fontsize=20)
    plt.ylim(0.0,2.1)
    plt.grid()
    plt.show()
    
    
    #Printer beregnede gjennomsnittsverdier
    print("v",v)
    print("y0",y)
    print("Gjennomsnitt", getGjennomsnitt(v))
    print("StdAvvik", getStandardAvvik(v))
    print("StdFeil", getStandardFeil(v))

#main()
