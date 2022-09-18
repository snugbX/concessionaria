from util.Func_Main import Listaveiculos
from util.Func_ADM import Menu1, cria_veiculo, lista_vendas, up_veiculo

if __name__ == '__main__':
    sair = True
    while sair:
        opc = Menu1()
        if opc == 1:
            Listaveiculos()
        elif opc == 2:
            resu = cria_veiculo()
        elif opc == 3:
            up_veiculo()
        elif opc == 4:
            lista_vendas()
        elif opc == 5:
            sair = False