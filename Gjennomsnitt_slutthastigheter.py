import numpy as np
import Beregning_av_hastigheter as funk


result = np.array([])

# Henter hastighetene 
for i in range(10):
    
    
    t, x, y = funk.HentDataFraFil(
        './Data/txy_' + str((i+1)) + '.txt')
    
    
    v_e = funk.observertHastighet(t, x, y)
    
    #legger til de to siste hastighetene fra hvert
    # dataset i result arrayen
    result = np.append(result, v_e)
    
print(result)
print("Gjennomsnitt", funk.Gjennomsnitt(result))
print("StandardAvvik", funk.StandardAvvik(result))
print("StandardFeil", funk.StandardFeil(result))

