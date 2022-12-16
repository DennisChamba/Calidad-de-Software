def retornarDigito(numero:int) -> int:
    longitud = len(str(numero))
    return numero // 10**(longitud-1)


numero = input('Ingrese un numero: ')
if len(numero) > 4 or int(numero) > 3999:
    print('no se puede traducir el numero ingresado')
else:
    numero = int(numero)
    salida = ''

    while(numero > 0):
        digito = 0
    # unidades de mil
        if (len(str(numero)) == 4):
            digito = retornarDigito(numero)
            if(digito == 3):
                salida += 'MMM'
            elif(digito == 2):
                salida += 'MM'
            elif(digito == 1):
                salida += 'M'
            numero = numero - digito * 10 ** (len(str(numero))-1)
    # centenas
        elif(len(str(numero)) == 3):
            digito = retornarDigito(numero)
            if(digito == 9):
                salida += 'CM'
            elif(digito == 8):
                salida += 'DCCC'
            elif(digito == 7):
                salida += 'DCC'
            elif(digito == 6):
                salida += 'DC'
            elif(digito == 5):
                salida += 'D'
            elif(digito == 4):
                salida += 'CD'
            elif(digito == 3):
                salida += 'CCC'
            elif(digito == 2):
                salida += 'CC'
            elif(digito == 1):
                salida += 'C'
            numero = numero - digito * 10 ** (len(str(numero))-1)
    #decenas
        elif(len(str(numero)) == 2):
            digito = retornarDigito(numero)
            if(digito == 9):
                salida += 'XC'
            elif(digito == 8):
                salida += 'LXXX'
            elif(digito == 7):
                salida += 'LXX'
            elif(digito == 6):
                salida += 'LX'
            elif(digito == 5):
                salida += 'L'
            elif(digito == 4):
                salida += 'XL'
            elif(digito == 3):
                salida += 'XXX'
            elif(digito == 2):
                salida += 'XX'
            elif(digito == 1):
                salida += 'X'
            numero = numero - digito * 10 ** (len(str(numero))-1)
    #unidades
        elif(len(str(numero)) == 1):
            digito = retornarDigito(numero)
            if(digito == 9):
                salida += 'IX'
            elif(digito == 8):
                salida += 'VIII'
            elif(digito == 7):
                salida += 'VII'
            elif(digito == 6):
                salida += 'VI'
            elif(digito == 5):
                salida += 'V'
            elif(digito == 4):
                salida += 'IV'
            elif(digito == 3):
                salida += 'III'
            elif(digito == 2):
                salida += 'II'
            elif(digito == 1):
                salida += 'I'
            numero = numero - digito * 10 ** (len(str(numero))-1)

    # salida de trasnformacion
    print(f'Numero en romano: {salida}')
