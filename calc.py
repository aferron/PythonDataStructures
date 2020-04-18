# Calculus III 


import math


def dydt(t, y):
    return  t * math.sin(y)

def eulers(y, h, t_start, t_end):
    n = 0
    t = t_start
    y_values = [y]
    F = 0
    print("n: ", n, "t: ", t, "y: ", y)
    while t < t_end:
        y += h * dydt(t, y) 
        y_values.append(y)
        t += h
        n += 1
        print("n:", n, "\tt:{:.4}".format(t), "\ty:{:.6}".format(y))


    

#print("dydt: ", dydt(4.7, 16))
eulers(16, .2, 4.7, 5.7)
