# Este programa contém um lista chamada valores onde armazena 5 valores e mostra ao final, o maior valor da lista e o menor,
# a média, mostra a lista em ordem crescente e decrescente com os comandos sorted() e sorted/True e também mostra em qual posição está o número que
# o úsuario desejar procurar.




valores = []

for numeros in range(5):
    valor = int(input('Digite um valor: '))
    valores.append(valor)

media = sum(valores) / len(valores)
print(valores)
print(f'O maior valor da lista é: {max(valores)}')
print(f'E o menor valor é: {min(valores)}')
print(f'A media dos valores é: {media}')

crescente = sorted(valores)
decrescente = sorted(valores, reverse=True)
print(f'A lista em ordem crescente é: {crescente}, e a lista em ordem decrescente é {decrescente}')

numero_buscar = int(input("Qual numero deseja procurar?: "))

if numero_buscar in valores:
    posicao = valores.index(numero_buscar)
    print(f'O número buscado está na posição: {posicao}')
else:
    print("Este numero não existe na lista!")