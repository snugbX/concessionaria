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

def criaVeiculo(Lista:list):
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
        criaVeiculo(Lista)
    return veiculo

def Listaeiculos(Veic:str):
    rep = rp('RepositorioBD',Veic)
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
            marca = {veiculo['marca']}
            modelo= {veiculo['modelo']}
            motor = {veiculo['motor']}
            ano   = {veiculo['ano']}
            cor   = {veiculo['cor']}
            valor = R$ {veiculo['valor']:.2f} ''')
        print(f"{61*'#'}")
    else:
        print('Não foi encontrado nenhum, veiculo cadastrado!!')


if __name__ == '__main__':
    sair = True
    while sair:
        opc = Menu1()
        if opc == 1:
            try:
                opc = int(input(f'''
                    {20*'_'}Quer ver qual lista?{20*'_'}
                    1 -> Carro
                    2 -> Moto
                    Opção >> '''))
            except:
                print('opção invalida!!')
                continue

            if opc == 1:
                Listaeiculos('CarroBD')
            elif opc == 2:
                Listaeiculos('MotoBD')
            else:
                print('Opção não encontrada!!!')

        elif opc == 2:
            try:
                opc = int(input(f'''
                    {20*'_'}Qual Veiculo quer cardastrar!{20*'_'}
                    1 -> Carro
                    2 -> Moto
                    Opção >> '''))
            except:
                print('opção invalida!!')
                continue
            if opc == 1:
                rep = rp('RepositorioBD', 'CarroBD')
                veiculos = rep.load()
                resu = criaVeiculo(veiculos)
                car = Carro(resu['id'], resu['marca'], resu['modelo'], resu['motor'], resu['ano'], resu['cor'], resu['valor'])
                rep.saveVeiculo(car.to_json())
            elif opc == 2:
                rep = rp('RepositorioBD', 'MotoBD')
                veiculos = rep.load()
                resu = criaVeiculo(veiculos)
                mot = Moto(resu['id'], resu['marca'], resu['modelo'], resu['motor'], resu['ano'], resu['cor'], resu['valor'])
                rep.saveVeiculo(mot.to_json())
            else:
                print('Opção não encontrada!!!')

        elif opc == 4:
            sair = False