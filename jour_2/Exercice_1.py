#ecrire un programme qui trouve le plus grand nombre parmi deux nombres en utilisant un prompt
Nombre1=int(input("saisie Nombre1 "))
Nombre2=int(input("Saisie Nombre2"))
#print(type(Nombre1),type(Nombre2))
if Nombre1>Nombre2:
    print("le plus grand nombre est:"+str(Nombre1))
elif Nombre2>Nombre1:
    print("le plus grand nombre est:"+str(Nombre2))
else:
    print("les deux sont egaux:")