#Programa principal para correr las cosas
import Functions



print("Ingrese qué tipo de capacitor es")
print("1. Placas paralelas \n2. Esfera \n3. Cilindro")
option = int(input())
dielectric = str(input("¿Contiene dielectrico? y/n: ")).lower()
quantity = Functions.hasDielectric(dielectric)
#para las placas paralelas
if(option == 1):
    h = float(input("Ingrese altura (m): "))
    l = float(input("Ingrese largo (m): "))
    d = float(input("Ingrese la distancia entre placas (m): "))
    v = float(input("Ingrese voltaje: "))
    C_0 = Functions.capacitanceParallel(h, l, d)
    C = Functions.capacitanceParallelDielectric(h, l, d, dielectric, quantity)
    Q = Functions.capacitanceCharge(C, v)
    Q_0 = Functions.capacitanceCharge(C, v)
    U = Functions.storedEnergy(C, C_0, v, quantity)
    
    if(dielectric == "y"):
        sigma = Functions.freeChargeParallel(Q, h, l, quantity)
        sigma_i = Functions.bondedChargeParallel(Q, h, l, quantity)
        print("C: ", C, "F")
        print("Q: ", Q , "C")
        print("U: ", U, "J")
        print("σ: ", sigma, "C/m^2")
        print("σi: ", sigma_i, "C/m^2")
    else:
        print("C: ", C_0, "F")
        print("Q: ", Q_0 , "C")
        print("U: ", U, "J")

#para la esfera
elif(option == 2):
    r_ext = float(input("Ingrese el radio exterior (m): "))
    r_int = float(input("Ingrese el radio interior (m): "))
    v = float(input("Ingrese voltaje: "))
    
    C_0 = Functions.capacitanceSphere(r_ext, r_int)
    C = Functions.capacitanceSphereDielectric(r_ext, r_int, dielectric, quantity)
    Q = Functions.capacitanceCharge(C, v)
    Q_0 = Functions.capacitanceCharge(C_0, v)
    U = Functions.storedEnergy(C, C_0, v, quantity)
    
    if(dielectric == "y"):
        sigma = Functions.freeChargeSphere(Q, r_ext, r_int, quantity)
        sigma_i = Functions.bondedChargeSphere(Q, r_ext, r_int, quantity)
        print("C: ", C, "F")
        print("Q: ", Q , "C")
        print("U: ", U, "J")
        print("σ: ",sigma, "C/m^2")
        print("σi: ", sigma_i, "C/m^2")
    else:
        print("C: ", C_0, "F")
        print("Q: ", Q_0 , "C")
        print("U: ", U, "J")
        
    
    

#para el cilindro
elif(option == 3):
    r_ext = float(input("Ingrese el radio exterior (m): "))
    r_int = float(input("Ingrese el radio exterior (m): "))
    l = float(input("Ingrese el largo (m): "))
    v = float(input("Ingrese voltaje: "))
    
    C_0 = Functions.capacitanceCylinder(r_ext, r_int)
    C = Functions.capacitanceCylinderDielectric(r_ext, r_int, l, dielectric, quantity)
    Q = Functions.capacitanceCharge(C, v)
    Q_0 = Functions.capacitanceCharge(C_0, v)
    U = Functions.storedEnergy(C, C_0, v, quantity)
    
    if(dielectric == "y"):
        sigma = Functions.freeChargeCylinder(r_ext, r_int, l, quantity)
        sigma_i = Functions.bondedChargeCylinder(r_ext, r_int, l, quantity)
        print("C: ", C, "F")
        print("Q: ", Q , "C")
        print("U: ", U, "J")
        print("σ: ", sigma, "C/m^2")
        print("σi: ", sigma_i, "C/m^2")
    else:
        print("C: ", C_0, "F")
        print("Q: ", Q_0, "C")
        print("U: ", U, "J")
    