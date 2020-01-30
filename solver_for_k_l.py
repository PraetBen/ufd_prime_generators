from sympy.ntheory.primetest import isprime
from sympy.solvers.diophantine import diophantine, symbols, diop_solve, cornacchia


Q = 41
c, d = 554, 87
k, l, m, n = symbols("k l m n", integer=True)

print(((k*n-d)-m))



for k in range(1,1000):
    for l in range(1,1000):
        if ((c+d)*l+d*k)/(k**2+k*l+l**2*Q) % 1 == 0:
            print("k,l "+str(k)+" "+str(l))