#Programa principal para correr las cosas
import Functions



print("Ingrese qué tipo de capacitor es")
print("1. Placas paralelas \n2. Esfera \n3. Cilindro")
option = int(input())
dielectric = str(input("¿Contiene dielectrico? y/n: "))
if(dielectric.lower() == "y"):
    quantity = str(input("full/half:" ))
else:
    quantity = None

#para las placas paralelas
if(option == 1):
    h = float(input("Ingrese altura (m): "))
    l = float(input("Ingrese largo (m): "))
    d = float(input("Ingrese la distancia entre placas (m): "))
    v = float(input("Ingrese voltaje: "))
    C = Functions.capacitanceParallel(h, l, d, dielectric, quantity)
    Q = Functions.capacitanceCharge(C, v)
    U = Functions.storedEnergy(Q, v)
    print("C: ", C, "F")
    print("Q: ", Q , "C")
    print("U: ", U, "J")

#para la esfera
elif(option == 2):
    r_ext = float(input("Ingrese el radio exterior (m): "))
    r_int = float(input("Ingrese el radio interior (m): "))
    v = float(input("Ingrese voltaje: "))
    
    C = Functions.capacitanceSphere(r_ext, r_int, dielectric, quantity)
    Q = Functions.capacitanceCharge(C, v)
    U = Functions.storedEnergy(Q, v)
    print("C: ", C, "F")
    print("Q: ", Q , "C")
    print("U: ", U, "J")

#para el cilindro
elif(option == 3):
    r_ext = float(input("Ingrese el radio exterior (m): "))
    r_int = float(input("Ingrese el radio exterior (m): "))
    l = float(input("Ingrese el largo (m): "))
    v = float(input("Ingrese voltaje: "))
    
    C = Functions.capacitanceCylinder(r_ext, r_int, l, dielectric, quantity)
    Q = Functions.capacitanceCharge(C, v)
    U = Functions.storedEnergy(Q, v)
    print("C: ", C, "F")
    print("Q: ", Q , "C")
    print("U: ", U, "J")