#Code made by HonorioCode
print('**************************************************************')
print(""" _   _                 _ 
| | | | ___   ___   __| |
| |_| |/ _ \ / _ \ / _` |
|  _  | (_) | (_) | (_| |
|_| |_|\___/ \___/ \__,_|
                         
 ____             _                ____  _                 
| __ )  __ _ _ __| |__   ___ _ __ / ___|| |__   ___  _ __  
|  _ \ / _` | '__| '_ \ / _ \ '__|\___ \| '_ \ / _ \| '_ \ 
| |_) | (_| | |  | |_) |  __/ |    ___) | | | | (_) | |_) |
|____/ \__,_|_|  |_.__/ \___|_|___|____/|_| |_|\___/| .__/ 
                             |_____|                |_|   """)
print('**************************************************************')

escolha = None
decorator = '***************************************'
cadastros = {}

while escolha != '3':

    def menu():
        print('Bem vindo ao sistema da Hood Barber_Shop')
        print('1 - Clique 1 para realizar o seu Log In')
        print('2 - Clique 2 para se cadastrar')
        print('3 - Clique 3 para sair e finalizar o programa')


    menu()
    escolha = input('Digite o número entre 1, 2 e 3: ')

    if escolha == '2':
        while True:
                nomecad = input('Crie um nome de usuário : ')
                senhacad = input('Crie uma senha para cadastro : ')
                qtde_senha = len(senhacad)
                if 8 < qtde_senha > 16:
                    print('Senha inválida! Crie uma senha com no mínimo 8 caracteres')

                else:
                    cadastros[nomecad] = senhacad
                    print(cadastros)
                    print('Senha cadastrada com sucesso!')
                    break
    elif escolha == '1':
        i = 3
        while i != 0:
            user = input('Informe o nome de usuário : ')
            senha = input('Informe a senha : ')
            if user == cadastros.keys() and senha == cadastros.values():
                print('Acesso liberado!')
                print(decorator)
                print('Contabilidade Hood Barber_Shop')
                valorcorte = float(input('Informe o valor de cada corte : '))
                qtdecortes = int(input('Informe a quantidade cortes no dia : '))
                valordiario = qtdecortes * valorcorte
                print(f'Quantidade de cortes realizados no dia : {qtdecortes}')
                print(f'Valor Total dos cortes realizados no dia : {valordiario}')
            else:
                i = i - 1
                print(f"Usuário ou senha incorretos, você ainda tem {i} tentativas. ")
                continue
        print("Demasiadas tentativas incorretas, programa finalizado.")

        restart = print(input("Você gostaria de reiniciar? Sim/ Não: "))
        if restart != "não":
            continue


print('\n Sessão Finalizada! Volte Sempre')