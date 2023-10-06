# Funciones para calcular la capacitancia de distintos objetos
import math
#constante dielectrica del pexiglas
k = 3.40    
#constante de permitividad del aire
e = 8.85418*(10**-12)
#constante pi
p = math.pi

#arreglos para guardar las densidades de cargas
freeCharges = [0,0,0,0]
bondedCharges = [0,0,0,0]
#para los emisferios de las cargas libres

def hasDielectric(dielectric):
    if(dielectric == "y"):
        quantity = str(input("full/half:" ))
        return quantity
    elif(dielectric == "n"):
        quantity = None
        return quantity
        

def capacitanceParallel(h, l, d):
    return (e*h*l)/d

def capacitanceSphere(r_ext, r_int):
    return 4*p*e*(r_ext * r_int) / (r_ext - r_int)

def capacitanceCylinder(r_ext, r_int, l):
    return (2*p*e*l)/(math.log(r_ext) - math.log(r_int))

def capacitanceParallelDielectric(h, l, d , dielectric, quantity):
    if(dielectric == "y" and quantity == "full"): 
       return (k*e*h*l)/d
    elif(dielectric == "y" and quantity == "half"):
        return ((e*h*l)/2*d) + ((k*e*h*l)/2*d)   
    else:
        return 0     

def capacitanceSphereDielectric(r_ext, r_int, dielectric, quantity):
    if(dielectric == "y" and quantity == "full"): 
        return 4*p*e*k*(r_ext * r_int) / (r_ext - r_int)
    elif(dielectric == "y" and quantity == "half"):
        return 2*p*e*(k+1)*(r_ext * r_int) / (r_ext - r_int)
    else:
        return 0
    
def capacitanceCylinderDielectric(r_ext, r_int, l, dielectric, quantity):
    if(dielectric == "y" and quantity == "full"): 
        return (2*p*e*l*k)/(math.log(r_ext) - math.log(r_int))
    elif(dielectric == "y" and quantity == "half"):
        return (p*e*l)/(math.log(r_ext) - math.log(r_int)) + (p*e*l*k)/(math.log(r_ext) - math.log(r_int))
    else:
        return 0
#para calcular la carga
def capacitanceCharge(C, V):
    return C * V

#dependiendo si C_0 es 0 en caso tenga dielectrico, sino 
def storedEnergy(C, C_0,  V, quantity):
    if(quantity == "half"):
        return C*((V/k)**2)/2 + C_0*(V**2)/2
    elif(quantity == "full"):
        C_0 = 0
        return C*((V/k)**2)/2 + C_0*(V**2)/2
    else:
        C = 0
        return C*((V/k)**2)/2 + C_0*(V**2)/2
    
############################################
# Para calcular las densidades
############################################

# para la carga libre paralela
def freeChargeParallel(Q, h, l, quantity):
    if(quantity == "full"):
        freeCharges[0] = Q/(h*l)
        return freeCharges
    elif(quantity == "half"):
        #dos densidades
        freeCharges[0] = (2*Q)/(h*l)
        freeCharges[1] = (2*Q*k)/(h*l)
        return freeCharges

# para la carga ligada paralela
def bondedChargeParallel(Q, h, l, quantity):
    if(quantity == "full"):
        bondedCharges[0] = (Q/(h*l)) * (1-(1/k))
        return bondedCharges
    elif(quantity == "half"):
        bondedCharges[0] = (2*Q*k/(h*l) * (1-(1/k))) 
        return bondedCharges

# para la carga libre esferica
def freeChargeSphere(Q, r_ext, r_int, quantity):

    if(quantity == "full"):
        #dos densidades de carga libre
        freeCharges[0] = (k*Q)/(4*p*(r_int**2)*(1+k))
        freeCharges[1] = (k*Q)/(4*p*(r_ext**2)*(1+k))
        return freeCharges
    elif(quantity == "half"):
        #cuatro densidades de carga libre
        freeCharges[0] = Q/(2*p*(r_int**2)*(1+k))
        freeCharges[1] = Q/(2*p*(r_ext**2)*(1+k))
        freeCharges[2] = (k*Q)/(2*p*(r_int**2)*(1+k))
        freeCharges[3] = (k*Q)/(2*p*(r_ext**2)*(1+k))
        return freeCharges

# para la carga ligada esferica
def bondedChargeSphere(Q, r_ext, r_int, quantity):
    
    if(quantity == "full"):
        bondedCharges[0] = ((k-1)*Q) / (4*p*(r_int**2)*(1+k))
        bondedCharges[1] = ((k-1)*Q) / (4*p*(r_ext**2)*(1+k))
        return bondedCharges
    elif(quantity == "half"):
        
        bondedCharges[0] =  ((k-1)*Q) / (2*p*(r_int**2)*(1+k))
        bondedCharges[1] =  ((k-1)*Q) / (2*p*(r_ext**2)*(1+k))
        return bondedCharges

# para la carga libre cilindrica
def freeChargeCylinder(Q, r_ext, r_int, l, quantity):
    if(quantity == "full"):
        freeCharges[0] = Q/(p*l*r_int**2)
        freeCharges[1]
        return freeCharges
    elif(quantity == "half"):
        return freeCharges

# para la carga ligada cilindrica
def bondedChargeCylinder(quantity):
    if(quantity == "full"):
        bondedCharges[0]
        bondedCharges[1]
        return bondedCharges
    elif(quantity == "half"):
        return bondedCharges