#	show redshift distribution of JLA for 4 sets
#	1 - SNLS, 2 - SDSS, 3 - low-z, 4 - Riess HST

from numpy import *
from pylab import *

f = open('sn_z_mu_dmu_plow_union2.1.txt')

text = f.readlines()
z = []
for line in text:
    data = line.split()
    #print data[1]
    z.append(double(data[1]))
    
#zz = zeros(size(z))
#for i in range(size(z)):
#    zz[i] = z[i]

zz = array(z)

#h,e=histogram(zz, 10)

#print h
#print e
#show()
print 'zmin = ', zz.min()
print 'zmax = ', zz.max()
