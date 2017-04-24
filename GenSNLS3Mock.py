from pylab import *
from scipy.linalg import cholesky
from scipy.integrate import quad
from scipy.interpolate import interp1d

# Now add random errors on to the theoretical values:
covmat = loadtxt('data/snls3_covmat.txt')
snls3 = loadtxt('data/mock_snls3_amin_1E-6_interpsize_1000.txt')

A = cholesky(covmat,lower=True)

r = randn(snls3.shape[0])
dmu = matmul(A,r)

# plot(z,dmu,'o')

z = snls3[:,0]
mu = snls3[:,3]  # use the unperturbed distance modulus
err= diag(covmat)**0.5

# Now write mock SN into file
fp = open('snls3_mock_amin_1E-6_interpsize_1000.txt','w')

for i in range(len(z)):
    print >> fp, '%s %15.10f %15.10f %15.10f %15.10f'%('mock_SNLS3', z[i],mu[i]+dmu[i],err[i],mu[i])
    print '%s  %15.10f %15.10f %15.10f %15.10f'%('mock_SNLS3', z[i],mu[i]+dmu[i],err[i],mu[i])

fp.close()


show()
