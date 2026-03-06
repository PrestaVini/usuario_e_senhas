
#def main():
#se usuário não encontrado, pedir novamente
#adicionar o nome do usuário na linha 34

def senha_do_usuario():

    senhas = {
         "vinicius": "geladeira",
         "melissa": "abelinha",
         "davi": "lion"
        } 
                
    usuario = (input("Digite seu usuário: "))

    if usuario in senhas:
        return senhas[usuario]
    else:
        print("Usuário não encontado ❌")
        return None

def verificador_senha():
     senha_correta = senha_do_usuario()
     tentativas = 0
     limite = 3

     if senha_correta is None:
         return

     while tentativas < limite:
        senha = input("Digite sua senha: ")

        if senha == senha_correta:
            print(f"✅ Acesso liberado! Bem vindo!")
            break
        else:
            tentativas += 1
            print (f"❌ Acesso negado! Você tem {limite - tentativas} tentativas restantes")

     if tentativas == limite:
        print("🔒 Você esgotou suas tentativas, tente novamente mais tarde")

def main():
    verificador_senha()

if __name__ == "__main__":
    main()