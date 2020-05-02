from math import sqrt, sin

a11 = 3
a12 = -7
a13 = 2.44
a14 = -3.141592
a15 = 2.8
a21 = 0
a22 = 7.22
a23 = -0.2
a24 = sqrt(2)   # raíz cuadrada de dos
a25 = (1+sqrt(5))/2
a31 = 2.22
a32 = 3.2
a33 = sin(45*3.1415/180)  # 45 se pasa a radianes y se le aplica el seno
a34 = sqrt(a33)
a35 = a25

# ahora vamos a imprimirlo como una matriz

print("{:6.2f}{:6.2f}{:6.2f}{:6.2f}{:6.2f}".format(float(a11), float(a12), a13, a14, a15))
print(("{:6.2f}"*5).format(float(a21), a22, a23, a24, a25))
print(("{:6.2f}"*5).format(a31, a32, a33, a34, a35))
