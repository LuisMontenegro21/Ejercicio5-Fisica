#Programa principal para correr las cosas
import Functions



print("Ingrese qué tipo de capacitor es")
print("1. Placas paralelas \n2. Esfera \n3. Cilindro")
option = int(input())
dielectric = str(input("¿Contiene dielectrico? y/n: "))
if(dielectric.lower() == "y"):
    quantity = str(input("full/half:" ))
    n = 1
elif(dielectric.lower() == "n"):
    quantity = None
    n = 0
#para las placas paralelas
if(option == 1):
    h = float(input("Ingrese altura (m): "))
    l = float(input("Ingrese largo (m): "))
    d = float(input("Ingrese la distancia entre placas (m): "))
    v = float(input("Ingrese voltaje: "))
    C_0 = Functions.capacitanceParallel(h, l, d, dielectric, quantity, n)
    C = Functions.capacitanceParallel(h, l, d, dielectric, quantity, n)
    Q = Functions.capacitanceCharge(C, v)
    U = Functions.storedEnergy(C, C_0, v)
    print("C: ", C, "F")
    print("Q: ", Q , "C")
    print("U: ", U, "J")
    if(quantity.lower() == "y"):
        sigma = Functions.freeCharge(Q, v)
        sigma_i = Functions.bondedCharge(sigma)
        print("σ: ", sigma, "C")
        print("σi: ", sigma_i, "C")
    

#para la esfera
elif(option == 2):
    r_ext = float(input("Ingrese el radio exterior (m): "))
    r_int = float(input("Ingrese el radio interior (m): "))
    v = float(input("Ingrese voltaje: "))
    
    C_0 = Functions.capacitanceSphere(r_ext, r_int, dielectric, quantity, n)
    C = Functions.capacitanceSphere(r_ext, r_int, dielectric, quantity, n)
    Q = Functions.capacitanceCharge(C, v)
    U = Functions.storedEnergy(C, C_0, v)
    print("C: ", C, "F")
    print("Q: ", Q , "C")
    print("U: ", U, "J")
    if(quantity.lower() == "y"):
        print("σ: ", "C")
        print("σi: ", "C")
    

#para el cilindro
elif(option == 3):
    r_ext = float(input("Ingrese el radio exterior (m): "))
    r_int = float(input("Ingrese el radio exterior (m): "))
    l = float(input("Ingrese el largo (m): "))
    v = float(input("Ingrese voltaje: "))
    
    C_0 = Functions.capacitanceCylinder(r_ext, r_int, l, dielectric, quantity, n)
    C = Functions.capacitanceCylinder(r_ext, r_int, l, dielectric, quantity, n)
    Q = Functions.capacitanceCharge(C, v)
    U = Functions.storedEnergy(C, C_0, v)
    print("C: ", C, "F")
    print("Q: ", Q , "C")
    print("U: ", U, "J")
    if(quantity.lower() == "y"):
        print("σ: ", "C")
        print("σi: ", "C")
    