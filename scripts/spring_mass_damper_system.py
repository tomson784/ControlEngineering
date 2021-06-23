import numpy as np
import control.matlab as ctrl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

m = 1    # 質量 [kg] 非負
c = 1    # 減衰係数 [N/m] 非負
k = 10   # バネ係数 [Ns/m] 非負

sys = ctrl.tf((1),(m,c,k)) # 伝達関数
print(sys)

t_range = (0,10) # 0～10秒の範囲をシミュレーション
y, t = ctrl.impulse(sys, T=np.arange(*t_range, 0.01))

plt.figure(figsize=(7,4),dpi=120,facecolor='white')
plt.hlines(0,*t_range,colors='gray',ls=':')
plt.plot(t,y)
plt.xlim(*t_range)
plt.show()

fig, ax = plt.subplots(1, 1)
ax.set_aspect('equal')
ax.grid()

for i in y:
    r = patches.Rectangle(xy=(i, 0.1), width=0.4, height=0.25, ec='black', fill=False)
    c_f = patches.Circle(xy=(i+0.1, 0.05), radius=0.05, ec='black', fill=False)
    c_b = patches.Circle(xy=(i+0.3, 0.05), radius=0.05, ec='black', fill=False)
    ax.add_patch(r)
    ax.add_patch(c_f)
    ax.add_patch(c_b)
    plt.pause(0.01)
    r.remove()
    c_f.remove()
    c_b.remove()
