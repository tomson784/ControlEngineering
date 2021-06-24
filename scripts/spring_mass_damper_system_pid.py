import numpy as np
import control.matlab as ctrl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

m = 1    # 質量 [kg] 非負
c = 1    # 減衰係数 [N/m] 非負
k = 10   # バネ係数 [Ns/m] 非負

sys = ctrl.tf((1),(m,c,k)) # 伝達関数
print(sys)

t_range = (0,10)
y, t = ctrl.impulse(sys, T=np.arange(*t_range, 0.01))

fig, ax = plt.subplots(2, 1)

ax[0].hlines(0,*t_range,colors='gray',ls=':')
ax[0].plot(t,y)
ax[0].grid()

ax[1].set_xlim((y.min()-1, y.max()+1))
ax[1].set_ylim((0, 0.5))
ax[1].grid()
ax[1].set_aspect("equal")

for i in range(len(t)):
    r = patches.Rectangle(xy=(y[i]-0.2, 0.1), width=0.4, height=0.25, ec='black', fill=False)
    c_f = patches.Circle(xy=(y[i]-0.1, 0.05), radius=0.05, ec='black', fill=False)
    c_b = patches.Circle(xy=(y[i]+0.1, 0.05), radius=0.05, ec='black', fill=False)
    x = ax[0].scatter(t[i], y[i], color="red")
    ax[1].add_patch(r)
    ax[1].add_patch(c_f)
    ax[1].add_patch(c_b)
    plt.pause(0.01)
    r.remove()
    c_f.remove()
    c_b.remove()
    x.remove()
