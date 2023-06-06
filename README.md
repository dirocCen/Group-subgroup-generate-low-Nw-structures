# Group-subgroup-generate-low-Nw-structures

## 第一步提前准备扩胞后的超胞
可使用http://sagar.compphys.cn/sagar 网站上的 Specific Volume Supercell Generator 功能。


## 第二步生成超胞置换群对应的子群
先安装sage数学软件 https://doc.sagemath.org/html/en/installation/index.html （推荐使用conda安装）。

进入sage的环境后执行第一个脚本：
```
python 1.sage_generate_subgroup.py
```
最终生成的每个超胞对应的子群会被保存在sub_group文件夹下。


注：该示例是遍历按体积扩胞的小胞，如仅需要一些特定形状的超胞，需要自行修改读取extend_cell的路径。


## 第三步根据子群生成结构
注：该步骤不需要使用sage的环境

```
python 2.generate_structureBysubgroup.py
```
参数说明：
num：遍历到最大的超胞体积
ele1：最终结构的元素序号1 （例如：ele1=5 表示第一种元素是B）
ele2：最终结构的元素序号2
considerNw：生成的最大的维克夫位点数的结构

注：ele1/ele2 不能写1（H）,后面运算的时候会使用。
注：该示例是二元体系的例子，三元及以上的需要修改其中排列组合的部分（不太好写），并且没有特殊限制的话结构数会非常多。



# （可选）一些额外的脚本

## 仅指定其中一个元素的维克夫位点生成结构
同样需要先有子群：
```
python 1.sage_generate_subgroup.py
```
再生成结构
```
python generate_structureBysubgroup_one_ele(optional).py
```

参数说明：
considerNw：指的是ele1最大维克夫位点数


## 根据浓度筛选结构
需要前面已经生成好"poscar"这个文件夹后，再执行：
```
python select_concentration_poscar(optional)
```

参数说明：
min_conc：保留的最低浓度
max_conc：保留的最高浓度





