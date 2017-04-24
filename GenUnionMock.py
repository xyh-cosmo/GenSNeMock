from pylab import *

# Union2.1 (inv-) covariance matrix
#icovmat = loadtxt('data/Union2.1/sn_wmat_nosys_union2.1.txt')
icovmat = loadtxt('data/Union2.1/sn_wmat_sys_union2.1.txt')
lcfile = open('data/Union2.1/sn_z_mu_dmu_plow_union2.1.txt','r')

######################################################################
# NOTE: if using inv(icovmat), the chol-decompsition would fail !!!
#  so I choose to use decompose icovmat, then use inv(L), it WORKS!!!
# L = cholesky(icovmat,lower=True)
# iL = inv(L)

# generate the random errors
# r = randn(580)
# dmu = matmul(iL,r)

######################################################################
# Now add random errors on to the theoretical values:
sn_data = loadtxt('data/Union2.1/z_mu_dmu_plow_union2.1.txt')
sn_mock = loadtxt('LCDM_SN_union.txt')

# sn_name = open('data/Union2.1/sn_names.txt')
# names = sn_name.readlines()

z = sn_data[:,0]
mu = sn_mock[:,3]  # use the unperturbed distance modulus
err= sn_data[:,2]
plow=sn_data[:,3]

# Now write mock SN into file
fp = open('mock_union2.1.txt','w')

n_want = 5000
cnt = 0

while cnt < n_want:
    i = randint(0,580)
    print 'I = ',i
    print >> fp, '%15.10f %15.10f %15.10f %15.10f'%(z[i],mu[i]+randn()*err[i],err[i],mu[i])
    cnt += 1

fp.close()