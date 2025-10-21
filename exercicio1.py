nome = str(input("digite seu nome: "))
idade = int(input("digite sua idade: "))
nota_media = float(input("digite sua media: "))
demora100 = 100
demora_para_os_100anos = demora100 - idade
print(f"falta {demora_para_os_100anos} para chegar em 100 anos")
if nota_media < 7.0:
    print( "voce nao passou de ano")
else:
    print("voce passou de ano")    
