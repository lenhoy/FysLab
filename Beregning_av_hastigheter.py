import matplotlib.pyplot as plt
import numpy as np

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
    return t, x, y
    
# Plott
def plotBaneForm(x, y):
    """Plotter en scatterplot basert på 2 arrays

    Args:
        x (array): posisjoner i x retning
        y (array): tilhørende posisjoner i y retning
    """
    
    fig, ax = plt.subplots(1,1,figsize=(10,6),constrained_layout=True)
    ax.scatter(x,y,c='r') #Scatterplot på y(x)
    plt.title('Banens form med autotracker', fontsize=16)
    ax.set_xlabel('x (m)', fontsize=14)
    ax.set_ylabel('y (m)', fontsize=14)
    plt.show()

def observertHastighet(t, x, y):
    """Beregner observert hastighet ved å se på de to siste posisjonene

    Args:
        t (np array): tider
        x (np array): x
        y (np array): y

    Returns:
        float: farten basert på siste to målte pkt
    """
    
    v_e = np.sqrt(abs(((y[-2] - y[-1])**2 + (x[-2] - x[-1])**2) / (t[-2] - t[-1])))
    
    return v_e
    
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

def Gjennomsnitt(v):
    return round(np.average(v), 3)

def StandardAvvik(v):
    return round(np.std(v), 4)

def StandardFeil(v):
    return round(StandardAvvik(v)/np.sqrt(len(v)), 5)



def main():
    t, x, y = HentDataFraFil('./Data/txy_1.txt')
    #plotBaneForm(x, y)
    v = BeregnHastighet(y)
    print("v",v)
    print("y0",y)
    print("Gjennomsnitt", Gjennomsnitt(v))
    print("StdAvvik", StandardAvvik(v))
    print("StdFeil", StandardFeil(v))

#main()
