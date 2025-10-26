numeros=[]
maior=0
menor=1
numero=1
numeroMedia=0
contadorMedia=0

for c in range(0, 5):
    numero=int(input('Digite um número: '))
    numeros.append(numero)
    contadorMedia+=1

    numeroMedia =numeroMedia+numero

    media=numeroMedia/contadorMedia
    
    if numeroMedia ==1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero 
            
print(f'Lista de números: {numeros}')
print(f'A média é {media}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

