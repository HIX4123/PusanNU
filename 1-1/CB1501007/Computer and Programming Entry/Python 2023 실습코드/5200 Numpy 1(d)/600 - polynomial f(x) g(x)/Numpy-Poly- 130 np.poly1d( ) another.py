
import numpy as np

ppar = [4, 3, -2, 10] # f(x)= x^3+3x^2-2x +10
p = np.poly1d(ppar)

print ( p(3) )
print ( np.polyval(ppar, 3) )

x = 3
print ( 4*x**3 + 3*x**2 -2*x + 10 )

def myf(z):
    return(4*x**3 + 3*x**2 -2*x + 10 )


# numpy makes it easy to get the derivative and integral of a polynomial.
# Consider: $y = 2x^2 - 1$. We know the derivative is $4x$. Here we compute the derivative and evaluate it at x=4.

p = np.poly1d([2, 0, -1])
p2 = np.polyder(p)
print ( p2 )
print ( p2(4) )


print ( np.roots([2, 0, -1]) )# roots are +- sqrt(2)

# note that imaginary roots exist, e.g. x^2 + 1 = 0 has two roots, +-i
p = np.poly1d([1, 0, 1])
print ( np.roots(p) )


