import numpy as np
import Beregning_av_hastigheter as funk


result = np.array([])
result2 = np.array([])

# Henter hastighetene 
for i in range(10):
    
    
    t, x, y = funk.HentDataFraFil(
        './Data/txy_' + str((i+1)) + '.txt')
    
    v = funk.observerteHastigheter(x, y)
    v_e = funk.observertHastighet_old(t, x, y)
    
    #legger til de to siste hastighetene fra hvert
    # dataset i result arrayen
    result = np.append(result, v_e)
    result2 = np.append(result2, v[-1])
    
print(result)
print("Gjennomsnitt", funk.getGjennomsnitt(result))
print("StandardAvvik", funk.getStandardAvvik(result))
print("StandardFeil", funk.getStandardFeil(result))
print("Gjennomsnitt2", funk.getGjennomsnitt(result2))
print("StandardAvvik2", funk.getStandardAvvik(result2))
print("StandardFeil2", funk.getStandardFeil(result2))

