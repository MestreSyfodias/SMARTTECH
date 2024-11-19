#Nome do usuário
nome = input("Insira seu nome:")

#Idade do usuário
idade = int(input("Digite sua idade:"))

#Texto apresentado quando nome e idade são insiridos
print(f"welcome to de matto {nome}, você tem {idade} anos")


print("Gostaria de jogar quais jogos?")
print("1 Minecraft")
print("2 Roblox")
print("3 Identity V")
print("4 Fortnite")

opc_user = int(input("Digite o número da opção desejada:"))

if opc_user == 1:
    print("Temos vários mods e servidores disponíveis")

elif opc_user == 2:
    print("Nessa plataforma tem vários jogos de gênros vareados")
    
elif opc_user == 3:
    print("No jogo temos vários modos sendo eles o duo-hunters")

elif opc_user == 4:
    print("Esse jogo é de fps e de tiro")

else:
    print("Opção incorreta, tente novamente os seguintes n° 1 2 3")
    