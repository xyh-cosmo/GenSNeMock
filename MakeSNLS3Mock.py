import sys as sys
import numpy as np
import scipy.stats as stats
from scipy.interpolate import interp1d

# load LCDM fiducial distance mudulus
z_dl_mu = np.loadtxt('classmc_z_Dl_mu_LCDM.txt')
fun_mu = interp1d(z_dl_mu[:,0],z_dl_mu[:,2])

# load SNLS3 redshifts
snls3 = np.loadtxt('data/mock_snls3_amin_1E-6_interpsize_1000.txt')
z_snls3 = snls3[:,0]

# load covariance matrix
covmat = np.loadtxt('data/snls3_covmat.txt')
var_snls3 = covmat.diagonal()**0.5


# set the random number seed
np.random.seed(1234567890)


def gen_err(covmat=None,use_full_cov=True):
	if covmat is None:
		print('covmat is not set, exit!')
		sys.exit(0)
	
	ndim = covmat.shape[0]
	mean = np.zeros(covmat.shape[0])
	if use_full_cov is False:
		covtemp = covmat.copy()
		covmat.fill(0.)
		for i in range(ndim):
			covmat[i,i] = covtemp[i,i]
	
	err = np.random.multivariate_normal(mean,covmat)
	return err

num_of_mocks = 10

cnt = 0
while cnt < 10:
	mu = fun_mu(z_snls3)
	mu_err = gen_err(covmat,use_full_cov=False)
	ks_stats, pvalue = stats.kstest(mu_err/covmat.diagonal()**0.5,cdf='norm')
	if pvalue > 0.5:
		print 'yeap! got a good mock sample! pvalue = %g'%(pvalue)
		fname = 'MOCK_SNLS3_'+str(cnt+1)+'.txt'
		fp = open(fname,'w')
		for i in range(len(mu)):
			print >> fp, '%10s %8.6f %10.8f %10.8f %10.8f'%('snls3_mock',z_snls3[i],mu[i]+mu_err[i],var_snls3[i],mu[i])
		fp.close()
		cnt += 1
