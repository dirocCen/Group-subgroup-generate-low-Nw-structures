import numpy as np
from pdb import set_trace
import itertools
import math
from ase.io.vasp import read_vasp, write_vasp
from sagar.io.vasp import read_vasp as read
from utils import get_perms
from spglib import find_primitive
import os
import spglib as spg

def sortrows(mat):
    n = np.shape(mat)[1]
    idx = np.lexsort(tuple(mat[:, i] for i in range(n - 1, -1, -1)))
    return mat[idx]


num=31
ele1 = 6
ele2 = 5
considerNw = 3
tol_Nw_num = np.zeros((1, considerNw), dtype=np.int32)
save_based_poscarAndNw = True

for atom_num in range(2, num):
    maxNw = min(considerNw, atom_num)
    path0 = "extend_cell/extend_cell-%s" % atom_num
    files = os.listdir(path0)
    tmp_tol_Nw_num = np.copy(tol_Nw_num[-1])
    for file in files:
        print("now run in %s" % file)
        poscar = os.path.join(path0, file)
        cell = read(poscar)
        perms = get_perms(cell).astype(np.int64)
        sub_name = os.path.splitext(file)[0]
        subg = np.load('sub_group/extend_cell-%s/resultSubgroup_%s_perms_sub.npz' % (atom_num, sub_name), allow_pickle=True)['perms_sub'] - 1
        #####
        pos_mat = []
        pos_num = []
        for line in subg:
            if len(line)==1:
                tmp = line[0]
                tmp = tmp.reshape(tmp.shape[0],1)
                pos_mat.append(tmp)
                pos_num.append(len(tmp))
            else:
                tmp = np.sort(line.T)
                tmp = np.unique(tmp,axis=0)
                tmp = np.unique(tmp, axis=1)
                pos_mat.append(tmp)
                pos_num.append(len(tmp))
        pos_num = np.array(pos_num)
        pos_mat = np.array(pos_mat)
        

        ######
        pos_all = np.array([])
        Nw_num = []
        for ii in range(1, maxNw+1):

            print('now run in class:%d' % ii)
            itp1 = np.where(pos_num>ii)[0]
            pos_mat1 = pos_mat[itp1]
            for pos_mat2 in pos_mat1:
                tmp_num = len(pos_mat2)
                itp2 = list(itertools.combinations(range(tmp_num), ii))
                cob = []
                for kk in itp2: 
                    itp3 = list(set(list(range(tmp_num))).difference(set(kk)))
                    cob.append([pos_mat2[list(kk)].flatten(), pos_mat2[itp3].flatten()])

                for ll in cob:
                    idx1 = np.unique(ll[0])
                    idx2 = np.unique(ll[1])
                    tmp_pos = np.zeros((1, atom_num))[0].astype(np.int32)
                    tmp_pos[idx1] = ele1
                    tmp_pos[idx2] = ele2
                    tmp1 = sortrows(tmp_pos[perms])[0]
                    if pos_all.size==0:
                        pos_all = tmp1
                    else:
                        pos_all = np.vstack((pos_all, tmp1))
                #set_trace()
            pos_all = np.unique(pos_all ,axis=0)

            atom = read_vasp(poscar)
            tmp_idx = []
            for jj, line in enumerate(pos_all):
                atom.numbers = line
                lattice, scaled_positions, numbers = find_primitive(atom)
                if len(numbers) != atom_num:
                    tmp_idx.append(jj)
            pos_all = np.delete(pos_all, tmp_idx, axis=0)
            if len(Nw_num)==0:
                Nw_num.append(len(pos_all))
                print('Nw=%d: %s' % (ii, len(pos_all)))
            else:
                tmp1 = len(pos_all)
                for tmp in Nw_num:
                    tmp1 = tmp1 - tmp
                Nw_num.append(tmp1)
                print('Nw=%d: %s' % (ii, tmp1))

        Nw_num = np.array(Nw_num)
        tmp_tol_Nw_num[:len(Nw_num)] = tmp_tol_Nw_num[:len(Nw_num)] + Nw_num
#        print("%s:tmp_tol_Nw_num=%s" %(sub_name, tmp_tol_Nw_num))

        pos_all = np.unique(pos_all ,axis=0)
        atom = read_vasp(poscar)
        for ii, line in enumerate(pos_all):
            atom.numbers = line
            tmp1 = spg.get_symmetry(atom, symprec=1e-3)['equivalent_atoms']
            tmp2 = np.where(atom.numbers==ele1)[0]
            res_Nw = len(np.unique(tmp1[tmp2]))

            save_dir = "poscar_one_ele/Nw=" + str(res_Nw) + '/' + file
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            idx = len(os.listdir(save_dir))
            write_vasp(save_dir + '/POSCAR%s' % idx, atom, direct=True, sort=True)

    tol_Nw_num = np.vstack((tol_Nw_num, tmp_tol_Nw_num))
print(tol_Nw_num)

np.savez('Nw_2_%s_num_1_%s_Nw_num_one_ele.npz' % (considerNw, num) , Nw_num=tol_Nw_num)

set_trace()
