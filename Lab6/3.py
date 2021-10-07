import math
import numpy as np 
import scipy
import copy
import itertools
def sistem (n,x):
    if n==1:
        return -0.1*x[1]**2-0.2*x[2]**2+0.3
    elif n==2: 
       return -0.1*x[1]**2 +0.1*x[1]*x[2]+0.7
def mpi (n,m,x, eps= 1e-3):
   k=0
   while True:
       d=0; b=copy.deepcopy(x); a=copy.deepcopy(b)
       a[1]=sistem(1,x)
       x[1]=a[1]
       a[2]=sistem(2,x) 
       x[2]=a[2]
       a=copy.deepcopy(b)
       for i in range(1,n+1):
          d1=abs(x[i]-a[i])
          if d<d1:
             d = d1
             k += 1 
             if d<= eps:
                print ('Solution is',x,'/number of iteration=',k)
                break
             else:
                 a=copy.deepcopy(x)
   if k>m:
      print('Процес розбігається!')
      exit(0)
mpi(2,10,np.array([0.,0.25,0.75]))