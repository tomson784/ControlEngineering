# 参考サイト
# https://tajimarobotics.com/kalman-filter-localization/

import numpy as np
import matplotlib.pyplot as plt

def StateEquation(x, u, w):
    x_ = x + u + np.random.normal(0,w,1)
    return x_

def OutputEquation(x, v):
    z = x + np.random.normal(0,v,1)
    return z

t = 1
u = [0.2, 0.1]
ideal_x = [0, 0]
x = [0, 0]
z = [0, 0]
F = np.eye(2) # State Matrix
H = np.eye(2) # Output Matrix

u = [0.2,0.1] # Input Signal Vector

w = [0.04,0.04] # Input Gaussian noise
v = [0.09,0.09] # Output Gaussian noise
Q = np.diag(w) # Covariance Matrix
R = np.diag(v) # Covariance Matrix

# xDes = [0,0] # Desired Trajectory
# xAct = [0,0] # Actual Trajcectory
# xEst = [0,0] # Estimated Trajectory

P = np.eye(2); # Initialize Covariance Matrix
ideal_robot_state = np.array([[0,0]])
robot_state = np.array([[0,0]])
observe_state = np.array([[0,0]])

for _ in range(50):
    ideal_x[0] = StateEquation(ideal_x[0], u[0]*t, 0)
    ideal_x[1] = StateEquation(ideal_x[1], u[1]*t, 0)
    x[0] = StateEquation(x[0], u[0]*t)
    x[1] = StateEquation(x[1], u[1]*t)
    z[0] = OutputEquation(x[0])
    z[1] = OutputEquation(x[1])
    ideal_robot_state = np.vstack((ideal_robot_state, np.array([ideal_x]).reshape(1,2)))
    robot_state = np.vstack((robot_state, np.array([x]).reshape(1,2)))
    observe_state = np.vstack((observe_state, np.array([z]).reshape(1,2)))

plt.plot(ideal_robot_state[:,0], ideal_robot_state[:,1], color="black", label="ideal robot pos")
plt.plot(robot_state[:,0], robot_state[:,1], color="blue", label="true robot pos")
plt.plot(observe_state[:,0], observe_state[:,1], color="red", label="sensing robot pos")
plt.legend()
plt.grid()
plt.show()


xEst = F*xEst + u; % Predicted State Estimate
P = F*P*F' + Q; % Predicted Error Covariance