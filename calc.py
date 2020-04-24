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


# Newton's Method to approximate sqrt 2
def newtons(prev_solution):
    return float(prev_solution + float(2 / prev_solution)) / 2

def recursive_sequence(n, f_x):
    if n == 1:
        # a_1 = 1
        return 1
    prev_solution = recursive_sequence(n - 1, f_x)
    return f_x(prev_solution)




print("sqrt 2 is approximately: ", recursive_sequence(10, newtons))    

#print("dydt: ", dydt(4.7, 16))
#eulers(16, .2, 4.7, 5.7)
