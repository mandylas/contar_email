import os
import json

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER + '/DB/' 'db.json')
with open (my_file, "r") as f:
    datos = json.load(f)
datos_personas = datos['Personas']
f.close()
lista_corros = []
cantidad_correos = 0
mostrar = ""
print("\nDatos del Estudianten\n".center(88, "-"))
for persona in datos_personas:
    #print(persona)
    for i,j in persona.items():
        for h in j:    
            if type(h) == str and "@" in h:
                lista_corros.append(h)
                cantidad_correos += 1
        #.ljust(15, " ")
        if i == "datos":
            for nombre_e in j[0:1]:
                pass
            for edad in j[1:2]:
                pass
            for ciudad in j[2:3]:
                pass
            print(f"Nombre:   {nombre_e} | Edad: {edad} | Ciudad: {ciudad}")
        elif i == "Materias":
            for m1 in j[0:1]:
                pass
            for m2 in j[1:2]:
                pass
            for m3 in j[2:3]:
                pass
            for m4 in j[3:4]:
                pass

            print(f"Materias: {m1.ljust(15, " ")} {m2.ljust(15, " ")} {m3.ljust(15, " ")} {m4.ljust(15, " ")}")
        elif i == "Notas":
            for n1 in j[0:1]:
                pass
            for n2 in j[1:2]:
                pass
            for n3 in j[2:3]:
                pass
            for n4 in j[3:4]:
                pass
            print(f"Notas:    {str(n1).ljust(15, " ")} {str(n2).ljust(15, " ")} {str(n3).ljust(15, " ")} {str(n4).ljust(15, " ")}")

            promedio = sum(j) / len(j)
            print(f"Promedio: {promedio}")
    print("\n--------------------------------------------\n")
        
print("Direcciones de correos:")
for dir in lista_corros:
    print(f"{dir}")
print(f"Camtidad de direcciones de correo: {cantidad_correos}")