import numpy as np
from sagar.io.vasp import read_vasp
from utils import get_perms
import os
from pdb import set_trace


num=32
for n in range(2, num):
    files = os.listdir("extend_cell/extend_cell-%s" % n)
    for file in files:
        print("run in %s" % file )    
        poscar = os.path.join("extend_cell/extend_cell-%s" % n, file)
        safe_name = os.path.splitext(file)[0]
        
        cell = read_vasp(poscar)

        perms = get_perms(cell).astype(np.int64) +1


        P = []
        for line in perms:
            P.append(Permutation(line))
        G = PermutationGroup(P)

        F=G.conjugacy_classes_subgroups()

        res=[]
        for line in F:
            res.append(line.list())


        perms_sub = []
        for line in res:
            tmp_perms = []
            for ll in line:
                tmp1 = list(ll.tuple())
                tmp_perms.append(tmp1)
            perms_sub.append(np.array(tmp_perms))


        save_dir = 'sub_group/extend_cell-%s' % n
        try:
            os.makedirs(save_dir)
        except:
            pass
        np.savez(save_dir + '/resultSubgroup_%s_perms_sub.npz' % safe_name , perms_sub=perms_sub)

