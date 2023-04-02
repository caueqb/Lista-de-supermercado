listaSupermercado = []
x = 0
while(x == 0):
    listaSupermercado.append(input('Digite o nome do produto que deseja acrescentar na lista: '))
    print('Deseja adicionar mais um produto? Se sim digite 0, se não digite 1')
    x = int(input())

print(listaSupermercado)
print()
print('Deseja retirar algum produto? Se sim digite 0, se não digite 1')
x = int(input())

while(x == 0):
    itemRetirado = int(input('Digite o número do item que deseja retirar: '))
    del listaSupermercado[itemRetirado - 1]
    print(listaSupermercado)
    print('Deseja retirar mais algum produto? Se sim digite 0, se não digite 1')
    x = int(input())