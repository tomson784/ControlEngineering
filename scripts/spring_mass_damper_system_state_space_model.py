# 参考サイト
# - [バネ・マス・ダンパ系の伝達関数・状態空間モデルとPythonによるシミュレーション](https://qiita.com/code0327/items/10fb56090a1e56046fa4)

import numpy as np
import control.matlab as ctrl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

m = 1    # 質量 [kg] 非負
c = 1    # 減衰係数 [N/m] 非負
k = 10   # バネ係数 [Ns/m] 非負

A = [[0,1],[-k/m, -c/m]]
B = [[0],[1/m]]
C = [[1,0],[0,1]]
D = 0

# 状態空間モデル
sys = ctrl.ss(A,B,C,D)
print(sys)

t_range = (0,10)

# x1（=変位）の初期値を 0.1 に設定。x2（=速度）の初期値は 0 に設定
y, t = ctrl.impulse(sys, T=np.arange(*t_range, 0.05), X0=[0.1, 0.0])

fig, ax = plt.subplots(3, 1)

ax[0].hlines(0,*t_range,colors='gray',ls=':')
ax[0].plot(t,y[:,0])
ax[0].grid()
ax[1].hlines(0,*t_range,colors='gray',ls=':')
ax[1].plot(t,y[:,1])
ax[1].grid()

ax[2].set_xlim((y.min()-1, y.max()+1))
ax[2].set_ylim((0, 0.5))
ax[2].grid()
ax[2].set_aspect("equal")

for i in range(len(t)):
    r = patches.Rectangle(xy=(y[i,0]-0.2, 0.1), width=0.4, height=0.25, ec='black', fill=False)
    c_f = patches.Circle(xy=(y[i,0]-0.1, 0.05), radius=0.05, ec='black', fill=False)
    c_b = patches.Circle(xy=(y[i,0]+0.1, 0.05), radius=0.05, ec='black', fill=False)
    x = ax[0].scatter(t[i], y[i,0], color="red")
    v = ax[1].scatter(t[i], y[i,1], color="red")
    ax[2].add_patch(r)
    ax[2].add_patch(c_f)
    ax[2].add_patch(c_b)
    plt.pause(0.01)
    r.remove()
    c_f.remove()
    c_b.remove()
    x.remove()
    v.remove()
