import os
from pdb import set_trace
from ase.io.vasp import read_vasp, write_vasp
import numpy as np


path0 = 'poscar_one_ele'
ele1 = 5
ele2 = 6

min_conc = 1/9
max_conc = 1/8

for ii in range(2,4):
    path1 = os.path.join(path0, 'Nw=%s' % ii)
    dirs = os.listdir(path1)
    for dir in dirs:
        path2 = os.path.join(path1, dir)
        files = os.listdir(path2)
        for jj in range(len(files)):
            path3 = os.path.join(path2, 'POSCAR%s' % jj)
            atom = read_vasp(path3)
            num_all = len(atom.numbers)
            num1 = len(np.where(atom.numbers==ele2)[0])
            conc = num1/num_all
            if conc>=min_conc and conc<=max_conc:
                save_dir = os.path.join('poscar_one_ele_conc_1-9_1-8', 'Nw=%s' % ii, dir)
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                idx = len(os.listdir(save_dir))
                write_vasp(save_dir + '/POSCAR%s' % idx, atom, direct=True, sort=True)







