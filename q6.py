#The formula is based on the centered hexagonal number and a triangular number with its index being n-1
def star(x):
    return( 6*(x**2)-(6*x)+1 )
print(star(10))