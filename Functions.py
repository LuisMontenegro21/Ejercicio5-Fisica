# Funciones para calcular la capacitancia de distintos objetos
import math
#constante dielectrica del pexiglas
k = 3.40    
#constante de permitividad del aire
e = 8.85418*(10**-12)
#constante pi
p = math.pi

def capacitanceParallel(h, l, d , dielectric, quantity, n):
    if(dielectric.lower() == "y" and quantity.lower() == "full"): 
       return (k*e*h*l)/d
    elif(dielectric.lower() == "y" and quantity.lower() == "half"):
        return ((e*h*l)/2*d) + ((k*e*h*l)/2*d)
    elif(dielectric.lower() == "n" and quantity == None):
        return (e*h*l)/d
    elif(n == 0):
        return 0

def capacitanceSphere(r_ext, r_int, dielectric, quantity, n):
    if(dielectric.lower() == "y" and quantity.lower() == "full"): 
        return 4*p*e*k*(r_ext * r_int) / (r_ext - r_int)
    elif(dielectric.lower() == "y" and quantity.lower() == "half"):
        return 2*p*e*(k+1)*(r_ext * r_int) / (r_ext - r_int)
    elif(dielectric.lower() == "n" and quantity == None):
        return 4*p*e*(r_ext * r_int) / (r_ext - r_int)
    elif(n == 0):
        return 0
    
def capacitanceCylinder(r_ext, r_int, l, dielectric, quantity, n):
    if(dielectric.lower() == "y" and quantity.lower() == "full"): 
        return (2*p*e*l*k)/(math.log(r_ext) - math.log(r_int))
    elif(dielectric.lower() == "y" and quantity.lower() == "half"):
        return (p*e*l)/(math.log(r_ext) - math.log(r_int)) + (p*e*l*k)/(math.log(r_ext) - math.log(r_int))
    elif(dielectric.lower() == "n" and quantity == None):
        return (2*p*e*l)/(math.log(r_ext) - math.log(r_int))
    elif(n == 0):
        return 0
    
def capacitanceCharge(C, V):
    return C * V

#dependiendo si C_0 es 0 en caso tenga dielectrico, sino 
def storedEnergy(C, C_0,  V):
    return C*((V/k)**2)/2 + C_0*(V**2)/2
  

def freeCharge(Q, A):
    return Q/A

def bondedCharge(sigma):
    return sigma*(1 - (1/k))


