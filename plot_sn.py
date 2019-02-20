import os, sys
from pylab import *

def read_sn(snfile):
	sn = []
	fp = open(snfile,'r')
	lines = fp.readlines()
	for i in range(len(lines)):
		line = lines[i].split()
		tmp = [float(line[1]),float(line[2]),float(line[3]),float(line[4])]
		sn.append(tmp)
	fp.close()

	return array(sn)



if len(sys.argv) <= 1:
	print('usage: %s'%(sys.argv[0]), 'sn_1.txt sn_2.txt ...')

sn = []

for i in range(1,len(sys.argv)):
	sn.append(read_sn(sys.argv[i]))
	# errorbar(sn[i-1][:,0],sn[i-1][:,1]-sn[i-1][:,3],yerr=sn[i-1][:,2],fmt='.')
	# scatter(sn[i-1][:,0],(sn[i-1][:,1]-sn[i-1][:,3])/sn[i-1][:,2],marker='.')
	scatter(sn[i-1][:,2],(sn[i-1][:,1]-sn[i-1][:,3])/sn[i-1][:,2],marker='.')
	xlabel(r'$\sigma_{\mu}$')
	ylabel(r'$\frac{\Delta\mu}{\sigma\mu}$')

show()