import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

s = 10
r = 28 
b = 8.0/3.0

def differential(xyz, t, s, r, b):
    x, y, z = xyz
    dxdt = s * (y - x)
    dydt = x * (r - z) - y
    dzdt = x * y - b * z
    return [dxdt, dydt, dzdt]

position0 = [0.0, 1.0, 1.0]
position2 = [20.0, 6.1, 21.0] 

time = np.linspace(0, 40, 1001)

positions = odeint(differential, position0, time, args=(s, r, b))
xsol, ysol, zsol = positions[:, 0], positions[:, 1], positions[:, 2]
    
positions_2 = odeint(differential, position2, time, args=(s, r, b))
x_sol_2, y_sol_2, z_sol_2 = positions_2[:, 0], positions_2[:, 1], positions_2[:, 2]



# combined_solution = np.column_stack((time, xsol, ysol, zsol, x_sol_2, y_sol_2, z_sol_2))

# print("Time\t\tx0\t\ty0\t\tz0\t\tx2\t\ty2\t\tz2")
# for row in combined_solution:
#     print(f"{row[0]:.2f}\t\t{row[1]:.4f}\t\t{row[2]:.4f}\t\t{row[3]:.4f}\t\t{row[4]:.4f}\t\t{row[5]:.4f}\t\t{row[6]:.4f}")


fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

lorenz_plt_1, = ax.plot(xsol, ysol, zsol, 'red', label=f'Position 0 of 1st: {position0}')
lorenz_plt_2, = ax.plot(x_sol_2, y_sol_2, z_sol_2, 'blue', label=f'Position 0 of 2nd: {position2}')

plt.legend()


def update(frame):
    lower_lim = max(0, frame - 100)

    x_current_1 = xsol[lower_lim:frame+1]
    y_current_1 = ysol[lower_lim:frame+1]
    z_current_1 = zsol[lower_lim:frame+1]

    x_current_2 = x_sol_2[lower_lim:frame+1]
    y_current_2 = y_sol_2[lower_lim:frame+1]
    z_current_2 = z_sol_2[lower_lim:frame+1]

    lorenz_plt_1.set_data(x_current_1, y_current_1)
    lorenz_plt_1.set_3d_properties(z_current_1)

    lorenz_plt_2.set_data(x_current_2, y_current_2)
    lorenz_plt_2.set_3d_properties(z_current_2)

    return lorenz_plt_1, lorenz_plt_2

animation = FuncAnimation(fig, update, frames=len(time), interval=30, blit=True)
# animation.save('lorenz_animation.mp4', writer='ffmpeg')
plt.show()
