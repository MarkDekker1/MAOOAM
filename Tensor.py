# --------------------------------------------------------------------------- #
# TENSOR FUNCTIONS USED IN AOTensor.py
# --------------------------------------------------------------------------- #
from Parameters import ndim
import numpy as np

real_eps = 2.2204460492503131e-16

def copy_tensor(src,dst):
    for i in range(0,ndim):
        for j in range(0,len(src[i])):
            dst[i,j,0]=src[i,j,0]
            dst[i,j,1]=src[i,j,1]
            dst[i,j,2]=src[i,j,2]
    return dst

def mat_to_coo(src,dst):
    for i in range(0,ndim):
        nl=0
        for j in range(0,ndim):
            if np.abs(src[i,j])>real_eps:
                nl=nl+1
        if len(dst[i])!=0:
            print 'mat_to_coo: desination coolist not empty!'
        nl=0
        for j in range(0,ndim):
            if np.abs(src[i,j])>real_eps:
                nl=nl+1
                dst[i,nl,0]=j
                dst[i,nl,1]=0
                dst[i,nl,2]=src[i,j]
    return dst

def sparse_mul3(coolist_ijk,arr_j,arr_k,res):    
    for i in range(0,ndim):
        for nl in range(0,len(coolist_ijk[i])):
            j = np.int(coolist_ijk[i][nl][0])
            k = np.int(coolist_ijk[i][nl][1])
            res[i]=res[i]+coolist_ijk[i][nl][2]*arr_j[j]*arr_k[k]
    return res

def sparse_mul2(coolist_ij,arr_j,res):
    #res=0.
    for i in range(0,ndim):
        for nl in range(0,len(coolist_ij[i])):
            j=coolist_ij[i,nl,0]
            res[i]=res[i]+coolist_ij[i,nl,2]*arr_j[j]
    return res