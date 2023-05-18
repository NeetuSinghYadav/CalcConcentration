import pandas as pd
import numpy as np
import sys


edge_length=15*10**(-9)
NPeptide=72
Avagadronumber= 6.023 *10**23
volume=(edge_length*edge_length*edge_length)
Conc= (NPeptide/(Avagadronumber * volume ))/1000

#print (Avagadronumber, "\n", edge_length, "\n", Conc, volume)
concentartion=np.round(Conc,3)
concentartion=concentartion*1000
print (f'concentration (mM)=',concentartion)

particle=Conc*Avagadronumber*volume

print ("Number of particles=",particle*1000)



