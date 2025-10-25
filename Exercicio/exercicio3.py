boletim = []


while True:
    aluno = str(input('Digite seu nome: '))
    nota1 = int(input('Digite sua nota: '))
    nota2 = int(input('Digite a segunda nota: '))
    boletim.append([aluno, [nota1, nota2]])

    while True:
        continuar = str(input('Você quer continuar digitando?[S/N]')).upper()
        if continuar == 'S':
            break
        elif continuar == 'N':
            break
        else :
            print (f'ERROR: Você não digitou nenhuma das opções ("S" ou "N"), digite novamente')
    if continuar == 'N':
        break


print("\n=== BOLETIM ===")
print(f"{'Nº':<4}{'NOME':<15}{'MÉDIA':>8}")
print("-" * 30)

for i, a in enumerate(boletim):
    media = sum(a[1]) / 2
    print(f"{i:<4}{a[0]:<15}{media:>8.2f}")

while True:
    opc = int(input('De qual aluno você deseja mostrar as notas?(999 encerra o programa): '))
    if opc == 999:
        print (f'Encerrar programa')
        break
    if 0 <= opc <len(boletim):
        print (f'Notas de {boletim[opc][0]}: {boletim[opc][1]}')
    else:
        print (f'Número inválido, tente de novo')