from util.Func_Main import Menu1, Menu2, Listaveiculos, add_ClienteBD, Login, Comprar, Cria_Cliente, up_cliente

# Lembrar de Fazer o CRUD pelomenos dos veiculos
#
if __name__ == '__main__':
    sair = True
    while sair:
        opc = Menu1()
        if opc == 1:
            Listaveiculos()

        elif opc == 2:

            add_ClienteBD(Cria_Cliente())

        elif opc == 3:
            resu = Login()
            if not resu:
                continue
            Logado = True
            while Logado:

                opc = Menu2(resu)

                if opc == 1:

                    Listaveiculos()

                elif opc == 2:

                    produto = Comprar(resu)

                elif opc == 3:
                    re = up_cliente(resu)
                    if re == 1:
                        break
                    elif not re:
                        continue
                elif opc == 4:
                    break
        elif opc == 4:
            sair = False