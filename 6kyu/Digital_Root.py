#El objetivo de este reto es a partir de un número positivo entero realizar
#la sumatoria de cada uno de sus dígitos hasta que el resultado sea un 
#número de un dígito.

#Esta fue la solución que propuse...

def digital_root(n):
    str_n = str(n)
    length_n = len(str_n)
    y=n
    while length_n > 1:
        y=0
        for x in range(length_n):
            y = int(str_n[x]) + y
        str_n = str(y)
        length_n = len(str_n)
    return y    

# Esta es una de las propuestas de la comunidad, utilización de la función map

def digital_root_comunity(n):
    while n>9:
        n=sum(map(int,str(n)))
    return n

print(digital_root(493193))
print(digital_root_comunity(493193))

