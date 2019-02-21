from pylab import *
from scipy.linalg import cholesky
from scipy.integrate import quad
from scipy.interpolate import interp1d

# Now add random errors on to the theoretical values:
covmat = loadtxt('data/JLA_cov.txt')
jla = loadtxt('data/mock_jla_amin_1E-6_interpsize_1000.txt')

print 'saving the inverse covariance matrix ...'
icovmat = inv(covmat)
savetxt('jla_covmat_inv.txt',icovmat,fmt='%15.8E')

A = cholesky(covmat,lower=True)

r = randn(jla.shape[0])
dmu = matmul(A,r)

# plot(z,dmu,'o')

z = jla[:,0]
mu = jla[:,3]  # use the unperturbed distance modulus
err= diag(covmat)**0.5

# Now write mock SN into file
fp = open('jla_mock_amin_1E-6_interpsize_1000_A.txt','w')

for i in range(len(z)):
    print >> fp, '%s %15.10f %15.10f %15.10f %15.10f'%('mock_JLA', z[i],mu[i]+dmu[i],err[i],mu[i])
    print '%s  %15.10f %15.10f %15.10f %15.10f'%('mock_JLA', z[i],mu[i]+dmu[i],err[i],mu[i])

fp.close()


#show()
