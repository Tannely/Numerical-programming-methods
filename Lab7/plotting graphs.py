# 1
import matplotlib.pyplot as plt
from numpy import *  # для використання функцій exp та linspace
plt.plot([1, 3, 2, 4])
plt.show()


#2
def f(t):
  return t ** 2 * exp(-t ** 2)
t = linspace(0, 3, 51)  # 51 точка між 0 та 3
y = f(t)
plt.plot(t, y)
plt.show()


# 3
t = linspace(0, 3, 51)
y = t ** 2 * exp(-t ** 2)
plt.plot(t, y, 'g--', label='t^2*exp(-t^2)')
plt.axis([0, 3, -0.05, 0.5]) # [xmin, xmax, ymin, ymax]plt.xlabel('t')  # позначення вісі абсцисplt.ylabel('y')  # позначення е вісі ординатplt.title('My first normal plot')  # назва графіка
plt.legend()  # вставка легенди (тексту в label)
plt.show()


# 4
t = linspace(0, 3, 51)
y1 = t ** 2 * exp(-t ** 2)
y2 = t ** 4 * exp(-t ** 2)
y3 = t ** 6 * exp(-t ** 2)
plt.plot(t, y1, 'g^',  # маркери із зелених трикутників
         t,y2, 'b--',  # синя штриховая
         t, y3, 'ro-')  # червоні круглі маркери
# з'єднані суцільною лінією
plt.xlabel('t')
plt.ylabel('y')
plt.title('Plotting with markers')
plt.legend(['t^2*exp(-t^2)',
            't^4*exp(-t^2)',
            't^6*exp(-t^2)'],  # список легенди
           loc='upper left')  # положення легенди
plt.show()


#5
#Y(x)=5*cos(10*x)*sin(3*x)/(x^(1/2)), x=[0...5] 
def f(t):
  return  5 * cos(10*t) * sin(3*t) / (t**(1/2))
t = linspace(0, 5)
plt.plot(t, f(t), 'ro-', label ='5 * sin(10*x) * sin(3*x) / (x**(1/2))')
plt.axis([1, 4, -7, 6])
plt.grid(color = 'k', 
         linestyle = '-')
plt.xlabel(' вісь абсцис x')
plt.ylabel('вісь ординат y')
plt.title('Графік функції')
plt.legend(loc = 'upper right')
plt.show()