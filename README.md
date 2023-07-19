# Group-subgroup-generate-low-Nw-structures

## The first step is to prepare the expanded supercell in advance
It can use the function of "Specific Volume Supercell Generator" on website http://sagar.compphys.cn/sagar.


## The second step is to generate the subgroup corresponding to the supercell permutation group
Using the software of sage( https://doc.sagemath.org/html/en/installation/index.html ).

Execute the first script after entering the sage environment:
```
python 1.sage_generate_subgroup.py
```
The subgroup corresponding to each supercell generated in the end will be saved in the sub_group folder.

Note: This example is for traversing small cells that are expanded by volume. If you only need some supercells of specific shapes, you need to modify the path to read extend_cell yourself.

## The third step is to generate the structure according to the subgroup
Note: This step does not need to use the sage environment

```
python 2.generate_structureBysubgroup.py
```

Parameter Description:
num：Traversing to the largest supercell volume
ele1：Element number 1 of the final structure （e.g. ele1=5 Indicates that the first element is B）
ele2：Element number 2 of the final structure
considerNw：Generated structures with the largest number of Wikoff sites

Note: ele1/ele2 cannot write 1 (H), and it will be used in subsequent operations.
Note: This example is an example of a binary system. For ternary and above, the part of the arrangement and combination needs to be modified (not easy to write), and the number of structures will be very large if there are no special restrictions.


## (optional) some additional scripts

## Wickoff site generation structure specifying only one of its elements
Also need to have subgroups first:
```
python 1.sage_generate_subgroup.py
```
regeneration structure
```
python generate_structureBysubgroup_one_ele(optional).py
```

Parameter Description:
considerNw：Refers to the maximum number of Vickers points in ele1


## Screen structures by concentration
After the "poscar" folder has been generated before, execute:
```
python select_concentration_poscar(optional)
```

Parameter Description:
min_conc：minimum concentration retained
max_conc：maximum concentration retained




