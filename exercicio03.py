continuar = 'S'
aluno = []
listadenotas = []
listadealunos = []
i = 0
while continuar != 'N':
    aluno.clear()
    nome = str(input('Digite o nome do aluno: '))
    aluno.append(nome)
    listadenotas.clear()
    continuar_notas = 'S'
    while continuar_notas != 'N':
        nota = float(input('Digite a nota do aluno: '))
        listadenotas.append(nota)
        continuar_notas = input('Deseja adicionar mais notas [S/N]?: ').upper()

    aluno.append(listadenotas)
    listadealunos.append(aluno.copy())
    continuar = input('Deseja adicionar mais alunos [S/N]?: ').upper()

print(' REGISTRO DE ALUNOS')
print(listadealunos) 

while i < len(listadealunos):
        aluno_dado = listadealunos[i]
        nome = aluno_dado[0]
        notas = aluno_dado[1]
        
        media = 0
        if notas:
            media = sum(listadenotas) / len(listadenotas)
            print(f'{i, nome, media}')
        i += 1         
consultar = 'S'
while consultar == 'S':
        consulta = input("Digite o NÚMERO de índice do aluno para ver as notas: ")
        indice = int(consulta)

        if 0 <= indice < len(listadealunos):
            aluno_dado = listadealunos[indice]
            nome = aluno_dado[0]
            notas = aluno_dado[1]

            print(f"--- NOTAS DO ALUNO: {nome.upper()} ---")
            print(f'Media {media}')
            j = 0
            while j < len(notas):
                print(f"Nota {j+1}: {notas[j]:.2f}")
                j += 1
            
            print("-" * 40)
        consultar = input("Deseja consultar outro aluno? (S/N): ").upper()
        print("-" * 40)       
print("Fim da consulta.")