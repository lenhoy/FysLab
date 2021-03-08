import matplotlib.pyplot as plt

filepath = './Data/txy_1.txt'

with open(filepath) as file: 
    lines = file.readlines()
    
#Lagre objekt navn, variabler

name = lines[0].rstrip() # Navnet på objektet
labels = tuple(lines[1].rstrip().split('\t')) #Tuple over kolonnenavn
print('Objectnavn: %s, kolonner: '%(name)+str(labels))

#Lagre verdiene t,x og y i egne lister
t = []; x = []; y = [] #tre tomme lister
for i in range(2, len(lines)):
    l = lines[i].rstrip().split('\t')
    
    t.append(float("{:.5f}".format(float(l[0]))))
    x.append(float("{:.5f}".format(float(l[1]))))
    y.append(float("{:.5f}".format(float(l[2]))))
    
# Plott
fig, ax = plt.subplots(1,1,figsize=(10,6),constrained_layout=True)
ax.scatter(x,y,c='r') #Scatterplot på y(x)
plt.title('Banens form med autotracker', fontsize=16)
ax.set_xlabel('x (m)', fontsize=14)
ax.set_ylabel('y (m)', fontsize=14)
plt.show()