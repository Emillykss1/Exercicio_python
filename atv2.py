# 1
palavras = ["codigo", "linguagem", "web"]
numeros = [18, 123]
vazia = []
lista_mista = ["oi", 2.0, 5*2, [10, 20]]

# 2

numeros = [1, 2, 3]
lista_mista = [4, 'cinco', 6]
palavras = ['sete', 'oito', 'nove']
uma_lista = [10, 11, 12]

print(numeros)
print(lista_mista)
nova_lista = [numeros, palavras]
print(nova_lista + uma_lista)

# 3

numeros = [18, 424, 86, 13, 66, 8338, 74]
print(numeros[2])
print(numeros[9-8])
print(numeros[-2])

# 4

uma_lista = [3, 5, "Cibele", 3.14, False]
print(len(uma_lista))

# 5

uma_lista = [3, 5, "Cibele", [88, 99, "Suely"], [ ], 3.14, False]
print(len(uma_lista))

# 6

uma_lista = [3, 5, "Cibele", [88, 99, "Suely"], [ ], 3.14, False]
print(uma_lista[5])

# 7

uma_lista = [3, 5, "Cibele", [88, 99, "Suely"], [ ], 3.14, False]
print(uma_lista[2].upper())

# 8

uma_lista = [3, 5, "Cibele", [88, 99, "Suely"], [ ], 3.14, False]
print(uma_lista[2][0])

# 9

uma_lista = [3, 5, "Cibele", [88, 99, "Suely"], [ ], 3.14, False]
print(3.14 in uma_lista)

# 10

uma_lista = [3, 5, "Cibele", [88, 99, "Suely"], [ ], 3.14, False]
print(88 in uma_lista)

# 11

uma_lista = [1, 3, 5]
outra_lista = [2, 4, 6]
print(uma_lista + outra_lista)

# 12

uma_lista = [1, 3, 5]
print(uma_lista * 3)

# 13

uma_lista = [3, 5, "Cibele", [88, 99, "Suely"], [ ], 3.14, False]
print(uma_lista[4:])

# 14

uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']
uma_lista[1:3] = ['x', 'y']
print(uma_lista)

# 15 

uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']
uma_lista[1:3] = []
print(uma_lista)

# 16

uma_lista = ['a', 'd', 'f']
uma_lista[1:1] = ['b', 'c']
print(uma_lista)
uma_lista[4:4] = ['e']
print(uma_lista)

# 17

uma_lista = [4, 1, 8, 6, 3]
uma_lista[2] = True
print(uma_lista)

# 18

a = ['um', 'dois', 'três']
del a[1]
print(a)
lista = ['a', 'b', 'c', 'd', 'e', 'f']
del lista[1:5]
print(lista)

# 19

lista_a = [4, 1, 8, 6, 3]
lista_b = lista_a
lista_b[3] = 22
print(lista_a)

# 20

lista_original = [5, 6, 7, 8]
print(lista_original*3)

# 21

lista_original = [5, 6, 7, 8]
print(lista_original*3)
lista_nova = [lista_original] * 3
print(lista_nova)

# 22

lista_original = [5, 6, 7, 8]
lista_nova = [lista_original] * 3
print(lista_nova)
lista_original[1] = 22
print(lista_nova)

# 23

lista_a = [4, 1, 8, 6, 3]
lista_b = lista_a * 2
lista_b[3] = 35
print(lista_a)

# 24

lista_a = [4, 1, 8, 6, 3]
lista_b = [lista_a] * 2
lista_a[3] = 35
print(lista_b)

# 25

uma_lista = [4, 1, 8, 6, 3]
uma_lista.append(True)
uma_lista.append(False)
print(uma_lista)

# 26

uma_lista = [4, 1, 8, 6, 3]
uma_lista.insert(2,True)
uma_lista.insert(0,False)
print(uma_lista)

# 27

uma_lista = [4, 1, 8, 6, 3]
temp = uma_lista.pop(2)
temp = uma_lista.pop()
print(uma_lista)

# 28

uma_lista = [4, 1, 8, 6, 3]
uma_lista = uma_lista.pop(0)
print(uma_lista)
