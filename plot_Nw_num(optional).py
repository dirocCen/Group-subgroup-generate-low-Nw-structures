import numpy as np
# import h5py
from pdb import set_trace
from scipy import io
import matplotlib.pyplot as plt



def main():
    data = np.load('Nw_2_8_num_1_80_Nw_num.npz')['Nw_num']
    x = range(1, len(data)+1)

    plt.figure(figsize=(7,5))
    plt.rc('font', family='Times New Roman')
    plt.plot(x, data[:, 0], 'o-', label=r'$N_{\rm W} = 2$')
    plt.plot(x, data[:, 1], 'D-', label=r'$N_{\rm W} = 3$')
    plt.plot(x, data[:, 2], 'v-', label=r'$N_{\rm W} = 4$')
    plt.plot(x, data[:, 3], '*-', label=r'$N_{\rm W} = 5$')
    plt.plot(x, data[:, 4], '.-', label=r'$N_{\rm W} = 6$')
    plt.plot(x, data[:, 5], 'k-', label=r'$N_{\rm W} = 7$')
    plt.plot(x, data[:, 6], 'p-', label=r'$N_{\rm W} = 8$')


#    plt.plot(x, N_conv[3, :], '*-', label='l=4')

#    new_ticks = np.linspace(0, 20, 11)  # 重新设置坐标轴的取值范围
#    plt.xticks(new_ticks)

    plt.xlabel(r"Number of atoms in the cell", size=16)
    plt.ylabel(r"Structures number", size=16)

    plt.legend(loc=0, prop={'size': 12, 'family':'Times New Roman','style':'italic'})
    plt.tick_params(labelsize=14)
    plt.title('Triangle Lattice - Binary', size=16)

    plt.savefig('structnum-num.png', dpi=400)
#    plt.show()



if __name__ == '__main__':
    main()

