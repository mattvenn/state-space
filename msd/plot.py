import control
import numpy as np
from matplotlib.pyplot import * # Grab MATLAB plotting functions
"""
* x : position of mass [m] at time t [s]
* m : mass [kg]
* c  : viscous damping coefficient [N s / m]
* k  : spring constant [N / m]
* u : force input [N]
"""
k = 10.0
m = 3.0
c = 3.0

A = np.matrix([[0, 1],[-k/m, -c/m]])
B = np.matrix([[0],[1/m]])

C = np.matrix([1,0])
D = 0

sys = control.StateSpace(A,B,C,D)

clf(); 
suptitle("MSD responses")
(Ys, Ts) = control.step(sys, T=np.linspace(0,20,100));
(Yi, Ti) = control.impulse(sys, T=np.linspace(0,20,100));
subplot(211)
plot( Ts.T, Ys.T)
title('step')
ylabel('x')
xlabel('time')
subplot(212)
ylabel('x')
title('impulse')
plot( Ti.T, Yi.T)
show()
