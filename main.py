import random
letras = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
largo = int(input("Introduzca la longitud de la contraseña"))
contraseña = ("")
for i in range (largo):
   contraseña = contraseña + random.choice(letras)

print(contraseña)
