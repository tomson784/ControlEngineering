# 参考サイト
# https://tajimarobotics.com/kalman-filter-localization/

import numpy as np
import matplotlib.pyplot as plt

def StateEquation(x, u, w):
    return x + u + np.random.normal(0, w, x.shape)

def OutputEquation(x, v):
    return x + np.random.normal(0, v, x.shape)

t = 1
u = np.array([0.2, 0.1])

w_ = 0.2
v_ = 0.3

F = np.eye(2) # State Matrix
H = np.eye(2) # Output Matrix

u = [0.2,0.1] # Input Signal Vector

w = [w_**2, w_**2] # Input Gaussian noise
v = [v_**2, v_**2] # Output Gaussian noise
Q = np.diag(w) # Covariance Matrix
R = np.diag(v) # Covariance Matrix

ideal_robot_state = np.array([[0,0]])
robot_state = np.array([[0,0]])
observe_state = np.array([[0,0]])
estimate_state = np.array([[0,0]])

P = np.eye(2); # Initialize Covariance Matrix

ideal_x = np.array([0, 0])
x = np.array([0, 0])
z = np.array([0, 0])
x_est = np.array([0, 0])

plt.plot(ideal_robot_state[:,0], ideal_robot_state[:,1], color="black", label="ideal robot pos")
plt.plot(robot_state[:,0], robot_state[:,1], color="blue", label="true robot pos")
plt.plot(observe_state[:,0], observe_state[:,1], color="red", label="sensing robot pos")
plt.plot(estimate_state[:,0], estimate_state[:,1], color="green", label="estimate robot pos")
plt.legend()
plt.grid()

for _ in range(50):
    ideal_x = StateEquation(ideal_x, u*t, 0)
    x = StateEquation(x, u*t, w_)
    z = OutputEquation(x, v_)
    x_est = F @ x_est + u           # Predicted State Estimate
    P = F @ P @ F.T + Q             # Predicted Error Covariance
    y = z - H @ x_est               # Innovation or Measurement Pre-fit Residual
    S = R + H @ P @ H.T             # Innovation or Pre-fit Residual Covariance
    K = P @ H.T @ np.linalg.inv(S)  # Optimal Kalman Gain
    x_est = x_est + K @ y           # Updated State Estimate
    P = (np.eye(2) - K @ H) @ P     # Updated Estimate Corvariance

    ideal_robot_state = np.vstack((ideal_robot_state, np.array([ideal_x]).reshape(1,2)))
    robot_state = np.vstack((robot_state, np.array([x]).reshape(1,2)))
    observe_state = np.vstack((observe_state, np.array([z]).reshape(1,2)))
    estimate_state = np.vstack((estimate_state, np.array([x_est]).reshape(1,2)))
    plt.plot(ideal_robot_state[:,0], ideal_robot_state[:,1], color="black", label="ideal robot pos")
    plt.plot(robot_state[:,0], robot_state[:,1], color="blue", label="true robot pos")
    plt.plot(observe_state[:,0], observe_state[:,1], color="red", label="sensing robot pos")
    plt.plot(estimate_state[:,0], estimate_state[:,1], color="green", label="estimate robot pos")
    plt.pause(0.1)

plt.show()
