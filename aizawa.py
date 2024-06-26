import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

a = 0.95
b = 0.7
c = 0.6
d = 3.5
e = 0.25


def differential(xyz, t, a, b, c, d, e,):
    x, y, z = xyz
    
    dxdt = (y - b) * x - d * z
    dydt =  (c - a * x**2 - y**2 - z**2) * y + x    
    dzdt =  d * x + (z * (x - e))
    return [dxdt, dydt, dzdt]

position0 = [0.1, 0.1, 0.1]
position2 = [3.0, 6.1, 1.0] 

time = np.linspace(0, 100, 1001)

positions = odeint(differential, position0, time, args=(a, b, c, d, e))
xsol, ysol, zsol = positions[:, 0], positions[:, 1], positions[:, 2]
    
positions_2 = odeint(differential, position2, time, args=(a, b, c, d, e))
x_sol_2, y_sol_2, z_sol_2 = positions_2[:, 0], positions_2[:, 1], positions_2[:, 2]



# combined_solution = np.column_stack((time, xsol, ysol, zsol, x_sol_2, y_sol_2, z_sol_2))

# print("Time\t\tx0\t\ty0\t\tz0\t\tx2\t\ty2\t\tz2")
# for row in combined_solution:
#     print(f"{row[0]:.2f}\t\t{row[1]:.4f}\t\t{row[2]:.4f}\t\t{row[3]:.4f}\t\t{row[4]:.4f}\t\t{row[5]:.4f}\t\t{row[6]:.4f}")


fig, ax = plt.subplots(subplot_kw={'projection': '3d'}, figsize=(10, 8))

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
