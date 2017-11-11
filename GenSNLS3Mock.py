import os,sys,time
from pylab import *
from scipy.linalg import cholesky
from scipy.integrate import quad
from scipy.interpolate import interp1d

NMOCK = 20

# Now add random errors on to the theoretical values:
covmat = loadtxt('data/snls3_covmat.txt')
snls3 = loadtxt('data/mock_snls3_amin_1E-6_interpsize_1000.txt')

# use distance / muduls pre-computed with CLASS as the fiducial values.
classmc_z_Dl_mu = loadtxt('data/classmc_z_Dl_mu_LCDM.txt');

Dl_z_ref = interp1d(classmc_z_Dl_mu[:,0],classmc_z_Dl_mu[:,2],kind='linear')

A = cholesky(covmat,lower=True)

# well, here we need only the redshifts from old mock file 'data/mock_snls3_amin_1E-6_interpsize_1000.txt'
z = snls3[:,0]
# mu = snls3[:,3]  # use the unperturbed distance modulus
err= diag(covmat)**0.5


# check dir
if os.path.isdir('./snls3_mock'):
    print('directory ./snls3_mock already exist!')
else:
    print('directory ./snls3_mock not found, so I create it for you!')
    os.mkdir('snls3_mock')

for n in range(1,1+NMOCK):
    fp = open('snls3_mock/snls3_mock_CLASSMC_'+str(n)+'.txt','w')
    print '--> %3d th mock sample ...'%(n)

    r = randn(snls3.shape[0])
    dmu = matmul(A,r)
    time.sleep(0.5);
    
    for i in range(len(z)):
        mu = Dl_z_ref(z[i])
        print >> fp, '%s %15.10f %15.10f %15.10f %15.10f'%('mock_SNLS3', z[i],mu+dmu[i],err[i],mu)
        # print '%s  %15.10f %15.10f %15.10f %15.10f'%('mock_SNLS3', z[i],mu+dmu[i],err[i],mu)
        # print 'z = %10.8f\tmu = %15.10f'%(z[i], mu[i]-Dl_z_ref(z[i]))

    fp.close()


show()
