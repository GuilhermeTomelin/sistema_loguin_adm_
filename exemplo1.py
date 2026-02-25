print("=" * 30)
print("SISTEMA DE LOGIN ADM")
print("=" * 30)
print("Admin: Valentim | Senha: 1234")
print("=" * 30)
while True:
    try:
        usuario = str(input("Digite o usuário: "))
        if usuario == "Valentim":
            break
        else:
         print("Usuario incorreto")
    except ValueError:
        print("Invalido")
while True:
    try:      
        senha = int(input("Digite sua senha: "))
        if senha == 1234:
            break
        else:
         print("Senha incorreto")
    except ValueError:
        print("Invalido")
for i in range(3):   
    if usuario == "Valentim" and senha == 1234:
        print("=" * 30)
        print(f"BEM-VINDO À ÁREA DE ADM {usuario}")
        print("=" * 30)
        break
    else:
        print("Usuário ou senha incorretos! Tente novamente.")
else:
    print("Número máximo de tentativas excedido.")