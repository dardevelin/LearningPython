from matplotlib.pyplot import plot, show, subplot, legend, grid
from numpy import pi, linspace, sin, cos, tan, tanh

x = linspace(0, 2*pi, 50)

subplot(2,2,1)
plot(x, sin(x), "r+", label='sin')
legend(loc='best')

subplot(2,2,2)
plot(x, cos(x), "b+", label='cos')
legend(loc='best')

subplot(2,2,3)
plot(x, tan(x), "g+", label='tan')
legend(loc='best')

subplot(2,2,4)
plot(x, tanh(x), "y+", label='tanh')
legend(loc='best')
grid()

show()