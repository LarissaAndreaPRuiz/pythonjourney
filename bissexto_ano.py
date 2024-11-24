def verificador_ano_bissexto():
    ano = int(input("Insira um ano: "))
    if ano % 4 == 0:
        print('SIM')
    elif ano % 100 != 0:
        print('NÃO')

verificador_ano_bissexto()
