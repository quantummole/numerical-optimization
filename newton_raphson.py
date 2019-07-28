# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 09:40:32 2019

@author: quantummole
"""

import numpy as np
from matplotlib import pyplot as plt
class NewtonRaphson :
    def __init__(self,function,derivative,epsilon=1e-3) :
        self.func = function
        self.derivative = derivative
        self.eps = epsilon
    def search(self,x_0,max_epochs) :
        epochs = max_epochs
        f_0 = self.func(x_0)
        while epochs > 0 and np.abs(f_0)>self.eps :
            f1_0 = self.derivative(x_0)
            x_0 = x_0 - f_0/f1_0
            f_0 = self.func(x_0)
        return x_0,f_0
    
if __name__ == '__main__' :
    func = lambda x : x**4-x**2-2
    derivative = lambda x : 4*x**3 -2*x
    solver = NewtonRaphson(func,derivative)
    x,f = solver.search(3.1,100)
    print(x,f)
    xs = np.linspace(x-1,x+1,100)
    ys = [func(x) for x in xs]
    plt.plot(xs,ys)
    plt.show()
    
    