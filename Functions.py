# Funciones para calcular la capacitancia de distintos objetos
import math
#constante dielectrica del pexiglas
k = 3.40    
#constante de permitividad del aire
e = 8.85418*(10**-12)
#constante pi
p = math.pi

def capacitanceParallel(h, l, d , dielectric, quantity):
    if(dielectric.lower() == "y" and quantity.lower() == "full"): 
       return (k*e*h*l)/d
    elif(dielectric.lower() == "y" and quantity.lower() == "half"):
        return ((e*h*l)/2*d) + ((k*e*h*l)/2*d)
    elif(dielectric.lower() == "n" and quantity == None):
        return (e*h*l)/d

def capacitanceSphere(r_ext, r_int, dielectric, quantity):
    if(dielectric.lower() == "y" and quantity.lower() == "full"): 
        return 4*p*e*k*(r_ext * r_int) / (r_ext - r_int)
    elif(dielectric.lower() == "y" and quantity.lower() == "half"):
        return 2*p*e*(k+1)*(r_ext * r_int) / (r_ext - r_int)
    elif(dielectric.lower() == "n" and quantity == None):
        return 4*p*e*(r_ext * r_int) / (r_ext - r_int)
    
def capacitanceCylinder(r_ext, r_int, l, dielectric, quantity):
    if(dielectric.lower() == "y" and quantity.lower() == "full"): 
        return (2*p*e*l*k)/(math.log(r_ext) - math.log(r_int))
    elif(dielectric.lower() == "y" and quantity.lower() == "half"):
        return (p*e*l)/(math.log(r_ext) - math.log(r_int)) + (p*e*l*k)/(math.log(r_ext) - math.log(r_int))
    elif(dielectric.lower() == "n" and quantity == None):
        return (2*p*e*l)/(math.log(r_ext) - math.log(r_int))
    
def capacitanceCharge(C, V):
    return C * V

def storedEnergy(Q, V):
    return Q*V/2



