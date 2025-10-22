listaNumeros=[]
for i in range(5):
    resposta=int(input('Digite um numero: '))
    listaNumeros.append(resposta)
    
    
maximo=max(listaNumeros)
minimo=min(listaNumeros)
media=sum(listaNumeros)/len(listaNumeros)
crescente=listaNumeros.sort()
decrescente=listaNumeros.sorted(reverse=True)



print(f'os numeros são {resposta}')