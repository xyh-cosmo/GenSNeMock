import sys
import numpy as np
import matplotlib.pylab as plt

# data format:
# SN_name z   mu   dmu   mu_ref

def read_snls3_mock( mock_filename ):
	fp = open(mock_filename,'r')
	lines = fp.readlines()
	fp.close()

	snls3 = []
	for line in lines:
		sn = line.split()
		temp = []
		temp.append(float(sn[1]))
		temp.append(float(sn[2]))
		temp.append(float(sn[3]))
		temp.append(float(sn[4]))
		snls3.append(temp)

	return np.array(snls3)

def main():
	if len(sys.argv) < 2:
		print 'usage: %s snls3_mock.txt'%(sys.argv[0])
		sys.exit(0)

	mock_num = len(sys.argv) - 1
	snls3 = read_snls3_mock(sys.argv[1])
	z = snls3[:,0]
	dmu = (snls3[:,1]-snls3[:,3])/snls3[:,2]
	# dmu = (snls3[:,1]-snls3[:,3])

	nbin_all = 15
	nbin_1 = 10
	nbin_2 = 10
	z1 = 0.4
	z2 = 0.6
	
	plt.figure()
	# plt.errorbar(snls3[:,0],snls3[:,1],yerr=snls3[:,2])
	ID1 = (z <  z1 )
	ID2 = (z >= z2 )
	plt.hist(dmu, bins=nbin_all, histtype='step',label=r'ALL')
	plt.hist(dmu[ID1], bins=nbin_1, histtype='step', label=r'$z < 0.3$')
	plt.hist(dmu[ID2], bins=nbin_2, histtype='step', label=r'$z >= 0.8$')

	plt.legend(loc='upper left')
	plt.show()

if __name__ == '__main__':
	main()