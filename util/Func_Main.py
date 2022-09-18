import datetime as dt

from model.to_JSON import Repositorio as rp
from model.Cliente import Cliente
from model.Venda import Venda

def Valida_CPF(cpf):
    #Limpa os caracteres indesejados
    cpf = [int(char) for char in cpf if char.isdigit()]

    #Verifica se a quantidade de digitos bate
    if len(cpf) != 11:
        return False

    #Verifica se todos os numeros do cpf são iguais
    if cpf == cpf[::-1]:
        return False

    # Para só usar Cpfs Validos descomenta essa parte !!!
    # Valida os dois dígitos Verificadores do cpf
    #for i in range(9,11):
    #    valor = sum((cpf[num] * ((i+1) - num) for num in range(0,i)))
    #    digito = ((valor * 10) % 11) % 10

    #    if digito != cpf[i]:
    #        return False
    return True

def Valida_CPF2():
    rep = rp('RepositorioBD', 'ClienteBD')
    data = rep.load()

    cpf = input("Informe o cpf: ")
    #Limpa os caracteres indesejados
    cpf = [int(char) for char in cpf if char.isdigit()]

    #Verifica se a quantidade de digitos bate
    if len(cpf) != 11:
        return False

    #Verifica se todos os numeros do cpf são iguais
    if cpf == cpf[::-1]:
        return False

    # Para só usar Cpfs Validos descomenta essa parte !!!
    # Valida os dois dígitos Verificadores do cpf
    #for i in range(9,11):
    #    valor = sum((cpf[num] * ((i+1) - num) for num in range(0,i)))
    #    digito = ((valor * 10) % 11) % 10

    #    if digito != cpf[i]:
    #        return False

    for i in data:
        if cpf == i['cpf']:
            try:
                opcao = int(input(f"""
                    CPF já exite deseja informar outro?
                    1 > Sim
                    2 > Não
                """))

                if opcao == 1:
                    Valida_CPF2()
                elif opcao == 2:
                    return False
                else:
                    print("Opção inalida!!")
                    return False
            except:
                print('Ocorreu um erro!!')
                return False
    cpf = str(cpf).strip('[]')
    cpf = cpf.replace(',', '')
    cpf = cpf.replace(' ', '')
    return str(cpf)

def Cria_Cliente():
    rep = rp('RepositorioBD', 'ClienteBD')
    bdLista = rep.load()
    try:
        cpf = input('Informe um CPF: ')
        while not Valida_CPF(cpf):
            cpf = input('''Informe um CPF valido: ''')
        if bdLista:
            for i in bdLista:
                if cpf == i['cpf']:
                    print("CPF já existente!!")
                    resu = Cria_Cliente()
                    if resu:
                        return resu
            nome = input('Digite seu Nome: ')
            for i in bdLista:
                if nome == i['nome']:
                    print("Nome já existente!!")
                    resu = Cria_Cliente()
                    if resu:
                        return resu
        else:
            nome = input('Digite seu Nome: ')
        cli = Cliente(
            nome,
            cpf,
            input('Digite uma senha: ')
        )
    except:
        print("Erro nos dados informados!! Por Favor!! Informe os dados corretamente!! ")
        resu = Cria_Cliente()
        if resu:
            return resu
    return cli

def Menu1():
    try:
        opc = int(input(f"""
            {20*'_'}Menu Principal{20*'_'}
            1 - Listar Veiculos
            2 - Cadastrar-se
            3 - Fazer Login
            4 - Sair
        
            Digite o número de uma das opções do menu!!
            OPÇÃO >> """))
    except:
        print("Dado inserido invalido!!")
        Menu1()

    if 0 < opc < 5 and opc is not None:
        return opc
    else:
        print("Valor informado não consta no Menu!!")
        Menu1()

def Menu2(User: dict):
    try:
        op = int(input(f"""
            {20*'_'}Bém Vindo!! {User['nome']} {20*'_'}
            1 - Listar Veiculos
            2 - Comprar Veiculo
            3 - Alterar Dados do Perfil
            4 - Sair da Conta
            Digite o número de uma das opções do menu!!
            OPÇÃO >> """))
    except:
        print("Dado inserido invalido!!")
        Menu2(User)

    if 0 < op < 5 and op is not None:
        return op
    else:
        print("Valor informado não consta no Menu!!")

def up_cliente(user):
    rep = rp('RepositorioBD', 'ClienteBD')
    data = rep.load()
    cpf_antigo = user['cpf']
    volta = True
    while volta:
        try:
            opcao = int(input(f"""
                1 > Alterar Nome
                2 > Alterar Senha
                3 > Alterar CPF
                4 > Salvar Alterações
                5 > Deletar conta
                6 > Voltar
                opção > """))

            for i, item in enumerate(data):
                if cpf_antigo == item['cpf']:
                    pos = i

            if opcao == 1:
                user['nome'] = input("Informe seu novo nome: ")
            elif opcao == 2:
                user['senha'] = input("Informe sua nova senha: ")
            elif opcao == 3:
                cpf = Valida_CPF2()
                if cpf:
                    user['cpf'] = cpf
                else:
                    print("Erro no cpf ")
                    continue
            elif opcao == 4:
                data[pos] = user
                rep.AtualizaBD(data)
                print("Alterações Realizadas com sucesso!!")
            elif opcao == 5:
                op = int(input(f"""
                        Deseja realmente apagar esse veiculo? {data[pos]['nome']}
                        1 -> Sim
                        2 -> Não
                        Opção >> """))

                if op == 1:
                    del(data[pos])
                    rep.AtualizaBD(data)
                    print("Cliente removido com sucesso!!")
                    return 1
            elif opcao == 6:
                return False
            else:
                print("Opção invalida tente novamente!!")
                continue
        except:
            print('Ocorreu um erro!!')
            up_cliente(user)

def Listaveiculos():
    try:
        opc = int(input(f'''
        {20*'_'}Quer ver qual lista?{20*'_'}
        1 -> Carro
        2 -> Moto
        3 -> Voltar
        Opção >>'''))
    except:
        print('Opção invalida!!')
        return False
    if opc == 1:
        Veic = 'CarroBD'
    elif opc == 2:
        Veic = 'MotoBD'
    elif opc == 3:
        return False

    rep = rp('RepositorioBD', Veic)
    veiculos = rep.load()
    if Veic == 'CarroBD':
        tipo = 'Carros'
    else:
        tipo = 'Motos'
    if veiculos is not None:
        print(f"{20*'#'} Lista de {tipo} {20*'#'}")
        for veiculo in veiculos:
            print(f'''
            Código = {veiculo['id']} 
            marca  = {veiculo['marca']}
            modelo = {veiculo['modelo']}
            motor  = {veiculo['motor']}
            ano    = {veiculo['ano']}
            cor    = {veiculo['cor']}
            valor  = R$ {veiculo['valor']:.2f}
            status = {veiculo['status']} ''')
        print(f"{60*'#'}")
    else:
        print('Não foi encontrado nenhum, veiculo cadastrado!!')

def add_ClienteBD(Novo_Cliente):
    rep = rp('RepositorioBD', 'ClienteBD')
    clie = Novo_Cliente.to_json()
    rep.saveCliente(clie)
    print("Cliente cadastrado com sucesso!!!")

def Login():
    rep = rp('RepositorioBD', 'ClienteBD')
    data = rep.load()
    Nome = input('Nome: ')
    senha = input('Senha: ')

    for i in data:
        if Nome == i['nome']:
            if i['senha'] == senha:
                return i
            else:
                print(f'A senha {senha} não conferi!!')
                try:
                    opc = int(input('''
                            1 > Tentar novamente?
                            2 > Voltar para o menu principal
                            opção >> '''))
                except:
                    print('Valor informado invalido!\nsera direcionado para o menu principal')
                    return False
                if opc == 1:
                    t = Login()
                    if t:
                        return t

                elif opc == 2:
                    return False
                else:
                    print('Valor informado invalido!\nsera direcionado para o menu principal')
                    return False
            print('Cliente não encontrado')
            return False

    print('Cliente não encontrado')
    return False

def Comprar(cliente):
    try:
        opc_compra = int(input(f'''
        {20 * '_'}Qual tipo de veículo deseja Comprar?{20 * '_'}
        1-> Carro
        2-> Moto
        3-> Voltar
        Opção >> '''))
    except:
        print('Ocorreu um erro!!')
        return False
    if opc_compra == 1:
        ver = 'CarroBD'
    elif opc_compra == 2:
        ver = 'MotoBD'
    elif opc_compra == 3:
        return False
    else:
        print("Opção inválida!!")

    rep = rp('RepositorioBD', ver)
    produtos = rep.load()

    id_compra = int(input("Digite o Código do veículo que deseja comprar: "))

    for i, item in enumerate(produtos):
        if id_compra == item['id']:
            compra = item
            posi = i
            break

    produtos[posi]['status'] = 'Vendido'

    rep = rp('RepositorioBD', 'ClienteBD')
    cli = rep.load()

    compra['status'] = 'Comprado'

    for i, item in enumerate(cli):
        if cliente['cpf'] == item['cpf']:
            posi = i
            break

    if cliente['compras'] == None:
        cli[posi]['compras'] = [compra]
    else:
        cli[posi]['compras'].append(compra)

    #######Cria Venda#######

    vd = Venda(cli[posi]['nome'], cli[posi]['cpf'], compra, 0.0, dt.date.today().strftime('%d - %m - %Y'), 0.0)
    vd.calcula_desconto()

    # Resumo da Compra
    if ver == 'CarroBD':
        ver = "Carro"
    else:
        ver = "Moto"
    print(f"""
        {20 * '#'} Resumo da compra {20 * '#'}
            Nome: {vd.nome_cliente}
            CPF : {vd.cpf_cliente}
            Data da Compra: {vd.data_venda}
                    
            Informações do Produto Comprado:
                Produto: {ver}
                        
                Marca = {compra['marca']}
                Modelo = {compra['modelo']}
                Ano = {compra['ano']}
                        
                Valor à Pagar = {vd.valor_total}
                """)

    ####################

    sair = True
    while sair:
        try:
            validacao = int(input('''Deseja finalizar a compra?
                1-> Finalizar
                2-> Cancelar compra
                Opção >> '''))
        except:
            print("Dado informado não valido!!")
            continue

        if 0 < validacao < 3 and validacao is not None:
            if validacao == 1:
                r = rp('RepositorioBD', 'VendasBD')
                vendas = r.load()


                if vendas is not None:
                    vendas.append(vd.to_JSON())
                else:
                    vendas = [vd.to_JSON()]

                r.AtualizaBD(vendas)
                rep.AtualizaBD(produtos)
                rep.AtualizaBD(cli)
                break
            elif validacao == 2:
                break
            else:
                print("Opção inválida!!")
                continue

##Teste
client_Teste = {
    "nome": "juca",
    "cpf": "12345678935",
    "senha": "123456",
    "compras": None
}
if __name__ == '__main__':
    pass
    #up_cliente(client_Teste)
    #print(Login())
    #add_ClienteBD()
