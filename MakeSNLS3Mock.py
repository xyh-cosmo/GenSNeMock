import numpy as np
import scipy.stats as stats

# load LCDM fiducial distance mudulus


# load covariance matrix



# set the random number seed
np.random.seed(1234567890)


num_of_mocks = 10

for i in range(num_of_mocks):
	# x = np.random.randn(500)
	x = np.random.normal(size=500)
	ks1,ks2 = stats.kstest(x,cdf='norm')
	nt1,nt2 = stats.normaltest(x)
	# print '--> KS: ks1 = %10.8f\tks2 = %10.8f'%(ks1,ks2)
	print '++> NT: nt1 = %10.8f\tnt2 = %10.8f'%(nt1,nt2)
	# print 'ks2 / nt2 = %10.8f'%(ks2/nt2)
