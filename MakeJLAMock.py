import sys as sys
import numpy as np
import scipy.stats as stats
from scipy.interpolate import interp1d

# load LCDM fiducial distance mudulus
z_dl_mu = np.loadtxt('classmc_z_Dl_mu_LCDM.txt')
fun_mu = interp1d(z_dl_mu[:,0],z_dl_mu[:,2])

# load JLA redshifts
z_jla = np.loadtxt('jla_z.txt')

# load covariance matrix
covmat = np.loadtxt('data/JLA_cov.txt')
var_jla = covmat.diagonal()**0.5


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
	mu = fun_mu(z_jla)
	mu_err = gen_err(covmat,use_full_cov=False)
	ks_stats, pvalue = stats.kstest(mu_err/covmat.diagonal()**0.5,cdf='norm')
	if pvalue > 0.5:
		print 'yeap! got a good mock sample! pvalue = %g'%(pvalue)
		fname = 'MOCK_JLA_'+str(cnt+1)+'.txt'
		fp = open(fname,'w')
		for i in range(len(mu)):
			print >> fp, '%10s %8.6f %10.8f %10.8f %10.8f'%('jla_mock',z_jla[i],mu[i]+mu_err[i],var_jla[i],mu[i])
		fp.close()
		cnt += 1
