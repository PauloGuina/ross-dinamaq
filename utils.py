from matplotlib import pyplot as plt

def Plot(bearing):
    kxx_plot, kyy_plot = bearing.plot(['kxx', 'kyy']).data

    kxx_x, kxx_y = kxx_plot.x, kxx_plot.y
    kyy_x, kyy_y = kyy_plot.x, kyy_plot.y

    plt.plot(kxx_x,kxx_y,label='kxx')
    plt.plot(kyy_x,kyy_y,label='kyy')
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Coefficient (N/m)')
    plt.title('TOMAR NO CU')
    plt.grid()
    plt.legend()
    plt.show()