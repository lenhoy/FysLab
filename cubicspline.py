# TFY41xx Fysikk vaaren 2021.
#
# Programmet tar utgangspunkt i hoeyden til de 8 festepunktene.
# Deretter beregnes baneformen y(x) ved hjelp av 7 tredjegradspolynomer, 
# et for hvert intervall mellom to festepunkter, slik at baade banen y, 
# dens stigningstall y' = dy/dx og dens andrederiverte
# y'' = d2y/dx2 er kontinuerlige i de 6 indre festepunktene.
# I tillegg velges null krumning (andrederivert) 
# i banens to ytterste festepunkter (med bc_type='natural' nedenfor).
# Dette gir i alt 28 ligninger som fastlegger de 28 koeffisientene
# i de i alt 7 tredjegradspolynomene.

# De ulike banene er satt opp med tanke paa at kula skal 
# (1) fullfoere hele banen selv om den taper noe mekanisk energi underveis;
# (2) rulle rent, uten aa gli ("slure").

#Importerer noedvendige biblioteker:
from Beregning_av_hastigheter import BeregnHastighet
import matplotlib.pyplot as plt
import numpy as np
import Beregning_av_hastigheter as funk
from scipy.interpolate import CubicSpline
import math

#Horisontal avstand mellom festepunktene er 0.200 m
h = 0.200
xfast=np.asarray([0,h,2*h,3*h,4*h,5*h,6*h,7*h])
#Skriv inn y-verdiene til banens 8 festepunkter i tabellen yfast.
#Et vilkaarlig eksempel:
yfast = np.asarray([0.399, 0.310, 0.261, 0.254, 0.248, 0.211, 0.165, 0.105])
#Erstatt med egne tallverdier avlest i tracker.
#Programmet beregner de 7 tredjegradspolynomene, et
#for hvert intervall mellom to festepunkter,
#med funksjonen CubicSpline:
cs = CubicSpline(xfast, yfast, bc_type='natural')
#Funksjonen cs kan naa brukes til aa regne ut y(x), y'(x) og y''(x)
#for en vilkaarlig horisontal posisjon x, eventuelt for mange horisontale
#posisjoner lagret i en tabell:
#cs(x)   tilsvarer y(x)
#cs(x,1) tilsvarer y'(x)
#cs(x,2) tilsvarer y''(x)
#Her lager vi en tabell med x-verdier mellom 0 og 1.4 m
xmin = 0.000
xmax = 1.401
dx = 0.001
x = np.arange(xmin, xmax, dx)   
#Funksjonen arange returnerer verdier paa det "halvaapne" intervallet
#[xmin,xmax), dvs slik at xmin er med mens xmax ikke er med. Her blir
#dermed x[0]=xmin=0.000, x[1]=xmin+1*dx=0.001, ..., x[1400]=xmax-dx=1.400, 
#dvs x blir en tabell med 1401 elementer
Nx = len(x)
y = cs(x)       #y=tabell med 1401 verdier for y(x)
dy = cs(x,1)    #dy=tabell med 1401 verdier for y'(x)
d2y = cs(x,2)   #d2y=tabell med 1401 verdier for y''(x)


######################################################################

# Helning

def helning(dx, dy):
    
    Theta = np.array([])
    
    for i in range(1400):
        
        #theta = math.asin(dy[i]/dx)
        #Theta = np.append(Theta, theta)
        
    
    print("Helningsutvikling")
    print(Theta)
    
    return Theta

helning(dx, dy)

###################################################################

# Beregning av krumning

def krumning(d2y, dy):
    """[summary]

    Args:
        d2y ([type]): [description]
        dy ([type]): [description]

    Returns:
        array: Krumningen
    """
    
    k = (d2y)/(1+dy**2)**(3/2)
    
    return k
  
print("Krumning: ")  
k = krumning(d2y, dy)
print(k)
funk.plotBaneForm(x, k, "Krumning", "x(m) (m)", "k (1/m)", "Krumning", -2, 2)


####################################################################

# Fart over tid 


# Beregnet Hastighetsutvikling
v = funk.BeregnHastighet(y)
print("Teoretisk beregnet slutthastighet")
print(v[-1])


def v_x(v, theta):
    return "Hei"

def fartOverTid():

    for i in range(1400):
        
        res = (2*dx[i])/(v_x[i-1]+v_x[i])






##########################################################################

# Henter ut Observert data
t_obs, x_obs, y_obs = funk.HentDataFraFil('./Data/txy_1.txt')
    


#########################################################################

#Plotteeksempel: Banens form y(x)


baneform = plt.figure('y(x)',figsize=(12,6))
plt.plot(x,y, label="Beregnet")
plt.plot(xfast,yfast,'*', label="Festepunkter")
plt.plot(x_obs, y_obs, label="Observert")
plt.title('Banens form')
plt.xlabel('$x$ (m)',fontsize=20)
plt.ylabel('$y(x)$ (m)',fontsize=20)
plt.ylim(0.10,0.40)
plt.legend()
plt.grid()


#Figurer kan lagres i det formatet du foretrekker:
#baneform.savefig("baneform.pdf", bbox_inches='tight')
#baneform.savefig("baneform.png", bbox_inches='tight')
#baneform.savefig("baneform.eps", bbox_inches='tight')


####################################################################

# Hastighetsutvikling uten festepunkter i plot




# Observert Hastighetsutvikling
#v_obs = BeregnHastighet(y_obs) 
v_obs = funk.observerteHastigheter(x_obs, y_obs)
print("Observerte hastigheter: ")
print(v_obs)

beregnethastighet = plt.figure('v(x)',figsize=(12,6))
plt.plot(x,v, label="Beregnet")
plt.plot(x_obs[1:],v_obs, label="Observert")
#plt.plot(xfast,yfast,'*', label="Festepunkter")
plt.title('Hastighetsutvikling')
plt.xlabel('$x$ (m)',fontsize=20)
plt.ylabel('$v(x)$ (m/s)',fontsize=20)
plt.ylim(0,2.1)
plt.grid()
plt.legend()
#plt.show()



#######################################################################


# Hastighetsutvikling med festpunkter i plot

fig, ax1 = plt.subplots()
color="tab:red"
ax1.set_xlabel("$x$ (m)", fontsize=20)
ax1.set_ylabel('$y(x)$ (m)', fontsize=20, color=color)
ax1.plot(xfast, yfast, '*', label="Festepunkter")
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color="tab:blue"
ax2.set_ylabel("$v(x)$ (m/s)", fontsize=20, color=color)
ax2.plot(x,v, label="Beregnet", color=color)
ax2.plot(x_obs[1:],v_obs, label="Observert", color="orange")
ax2.tick_params(axis='y', labelcolor=color)

plt.title("Hastighetsutvikling")
plt.legend()
plt.grid()
fig.tight_layout()
#plt.show()

#fig.savefig("HastighetsutviklingDualAxis.png", bbox_inches="tight")

#beregnethastighet.savefig("Hastighetsutvikling.png", bbox_inches='tight')
