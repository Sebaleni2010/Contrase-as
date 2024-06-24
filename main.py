import random
letras = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
largo = int(input("Introduzca la longitud de la contraseña"))
newpass = ("")
for i in range (largo):
   newpass = newpass + random.choice(letras)

print(newpass)
