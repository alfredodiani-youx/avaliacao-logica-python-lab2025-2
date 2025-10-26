lista = []
for i in range(0,5):
    numero1 = int(input("digite um numero inteiro: ")) 
    lista.append(numero1)
maior_numero = max(lista)
menor_numero = min(lista)
media = sum(lista) / len(lista)
print(f"O maior numero e {maior_numero} o menor e {menor_numero} ea media e {media}")
lista.sort()
print(lista)
lista_decresente = sorted(lista,reverse=True)
print(lista_decresente)
numero2 = int(input("digite um numero: ")) 
if numero2 in lista:
        print(f"o numero {numero2} esta na lista e sua posiçao e {lista.index(numero2)}")
else:
      print("esse numero nao existe na lista")        
