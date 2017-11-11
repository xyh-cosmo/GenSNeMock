import os,sys,time
from pylab import *
from scipy.linalg import cholesky
from scipy.integrate import quad
from scipy.interpolate import interp1d

NMOCK = 20

# Now add random errors on to the theoretical values:
covmat = loadtxt('../data/snls3_covmat.txt')
snls3 = loadtxt('../data/mock_snls3_amin_1E-6_interpsize_1000.txt')

# use distance / muduls pre-computed with CLASS as the fiducial values.
classmc_z_Dl_mu = loadtxt('../data/classmc_z_Dl_mu_LCDM.txt');

Dl_z_ref = interp1d(classmc_z_Dl_mu[:,0],classmc_z_Dl_mu[:,2],kind='linear')

A = cholesky(covmat,lower=True)

# well, here we need only the redshifts from old mock file 'data/mock_snls3_amin_1E-6_interpsize_1000.txt'
z = snls3[:,0]
# mu = snls3[:,3]  # use the unperturbed distance modulus
err= diag(covmat)**0.5

# r = randn(snls3.shape[0])
# dmu = matmul(A,r)


mu = Dl_z_ref(z)
ran_mu = multivariate_normal(mu,covmat)

for i in range(len(z)):
    # mu = Dl_z_ref(z[i])
    print '%15.10f'%((ran_mu[i]-mu[i])/err[i])


# show()
