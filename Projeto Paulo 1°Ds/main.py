    # aqui, o sistema pede o nome do usuário
nome = input("insira seu nome:")
   
    # aqui, o sistema pede o nome do usuário
idade = int(input("digite sua idade:"))

    # aqui, o sistema imprime uma mensagem


print(f"cavalo {nome}, você tem {idade} anos!")

print("Como posso te ajudar hoje?")
print("1 - salgados")
print("2 - bebidas")
print("3 - doces")

opc_user = int(input("digite o número da opção desejada:"))

if opc_user == 1:
        print("Temos enroladinho de vina, salsichão, coxinha e risolis")

elif opc_user == 2:
        print("Temos coca, fanta, guaraná e sukita, e cini")

elif opc_user == 3:
        print("Temos docinho, bolo e pudim")

else: print("Opção incorreta, tente novamente os seguintes n° 1 2 3")



































