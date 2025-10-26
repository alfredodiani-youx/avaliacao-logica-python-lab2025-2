def analiseALUNO(nome,notas):
    media = sum(notas) / len(notas) 
    if media >= 7:
        situaçao = "APROVADO"
    else:
        situaçao = "REPROVADO"
    return {"nome" : nome,"media": media, "situaçao": situaçao }  
alunos = []  
while True:
    nome = str(input("digite seu nome: "))
    nota1 = float(input("NOTA1: "))
    nota2 = float(input("NOTA2: "))
    aluno = analiseALUNO(nome,[nota1 , nota2])
    alunos.append(aluno)
    resposta = input("deseja cadastrar outro aluno? [s/n]").lower()
    if resposta == "n":
        break
print("-="*20)    
print("RELATARIO COMPLETO")   
print("-="*20)    
for aluno in alunos:
    print(f"Nome: {aluno['nome']} , Media: {aluno['media']}, Situaçao: {aluno['situaçao']}") 

