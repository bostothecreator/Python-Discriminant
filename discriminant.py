from math import sqrt   

def discriminant(a,b,c):

    d = b**2 - 4*a*c 

    if d < 0:
        return "idinaxui aramodis"
    elif d == 0:
        x= -b / (2*a)
        return x
    else:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)

    return x1, x2 

print(discriminant(1, 5, 3))
 
