# 参考
# - [長いむだ時間をもつプロセス制御: スミス予測器](https://jp.mathworks.com/help/control/ug/control-of-processes-with-long-dead-time-the-smith-predictor.html)
# - [一次遅れ＋むだ時間系のモデルと数値シミュレーション（ステップ応答編）](https://hi-ctrl.hatenablog.com/entry/2017/11/07/033829)
# - [【PID制御】PID制御をPythonで実装](https://shizenkarasuzon.hatenablog.com/entry/2018/08/27/002812)

import matplotlib.pyplot as plt
import numpy as np

import time

class PID:
    def __init__(self, P=0.2, I=0.0, D=0.0):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.targetPos=0.
        self.clear()
