from model.to_JSON import Repositorio as rp
from model.Carro import Carro
from model.Moto import Moto

def Menu1():
    try:
        opc = int(input(f"""
            {30*'_'}Menu Principal{30*'_'}
            1 - Listar Veiculos
            2 - Cadastrar Veiculo
            3 - Visualizar vendas
            4 - Sair
        
            Digite o numero de uma das opções do menu!!
            OPÇÃO >> """))
    except:
        print("Dado inserido invalido!!")
        Menu1()

    if 0 < opc < 5 and opc is not None:
        return opc
    else:
        print("Valor informado não consta no Menu!!")
        Menu1()

def gera_id(Lista):
    l = 0
    if Lista:
        id = Lista[l]['id']+1
        while True:
            if l == len(Lista):
                break
            if id == Lista[l]['id']:
                id+=1
            l+=1
    else:
        id = 1

    return id

def cria_veiculo():
    try:
        opc = int(input(f'''
                    {20 * '_'}Qual Veiculo quer cardastrar!{20 * '_'}
                    1 -> Carro
                    2 -> Moto
                    3 -> Voltar
                    Opção >> '''))
    except:
        print('opção invalida!!')
        resu = cria_veiculo()
        return resu

    if opc == 1:
        rep = rp('RepositorioBD', 'CarroBD')
        Lista = rep.load()
    elif opc == 2:
        rep = rp('RepositorioBD', 'MotoBD')
        Lista = rep.load()
    else:
        return False

    id = gera_id(Lista)
    veiculo = {}
    try:
        veiculo['id'] = id
        veiculo['marca'] = input('Informe a marca: ')
        veiculo['modelo'] = input('Informe a modelo: ')
        veiculo['motor'] = input('Informe o motor: ')
        veiculo['cor'] = input('Informe a cor: ')
        veiculo['ano'] = int(input('Informe o ano: '))
        veiculo['valor']= float(input('Informe o preço: '))
    except:
        print("Erro nos dados informados!! Por Favor!! Informe os dados corretamente!! ")
        resu = cria_veiculo()
        return resu

    if opc == 1:
        car = Carro(veiculo['id'], veiculo['marca'], veiculo['modelo'], veiculo['motor'], veiculo['ano'], veiculo['cor'], veiculo['valor'])
        rep.saveVeiculo(car.to_json())
        return car
    elif opc == 2:
        mot = Moto(veiculo['id'], veiculo['marca'], veiculo['modelo'], veiculo['motor'], veiculo['ano'], veiculo['cor'], veiculo['valor'])
        rep.saveVeiculo(mot.to_json())
        return True

def lista_vendas():
    rep = rp('RepositorioBD', 'VendasBD')
    Lista = rep.load()

    if Lista is not None:
        print(f"{20*'#'} Lista de Vendas {20*'#'}")
        for vendas in Lista:
            print(f'''
            Dados do Cliente :
            Nome = {vendas['nome_cliente']} 
            CPF  = {vendas['cpf_cliente']}
            _______________________________________________________
            Produto(s) :
            
            Codigo = {vendas['produto']['id']}
            marca = {vendas['produto']['marca']}
            modelo = {vendas['produto']['modelo']}
            motor  = {vendas['produto']['motor']}
            ano    = {vendas['produto']['ano']}
            cor    = {vendas['produto']['cor']}
            valor  = R$ {vendas['produto']['valor']:.2f}
            ________________________________________________________
            Informações da Venda:
            Valor total = {vendas['valor_total']}
            Data = {vendas['data_venda']}
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$''')
        print(f"{60*'#'}")
    else:
        print('Não foi encontrado nenhum, veiculo cadastrado!!')




