from util.Func_Main import Listaveiculos
from util.Func_ADM import Menu1, cria_veiculo, lista_vendas

if __name__ == '__main__':
    sair = True
    while sair:
        opc = Menu1()
        if opc == 1:
            Listaveiculos()
        elif opc == 2:
            resu = cria_veiculo()
        elif opc == 3:
            lista_vendas()
        elif opc == 4:
            sair = False