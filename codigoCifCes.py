def Encriptar(palabra):
    abc = {
    'A':'E', 'B':'F', 'C':'G', 'D':'H', 'E':'I',
    'F':'J', 'G':'K', 'H':'L', 'I':'M', 'J':'N',
    'K':'O', 'L':'P', 'M':'Q', 'N':'R', 'O':'S',
    'P':'T', 'Q':'U', 'R':'V', 'S':'W', 'T':'X',
    'U':'Y', 'V':'Z', 'W':'A', 'X':'B', 'Y':'C',
    'Z':'D'
    }
    palabra = palabra.upper()
    FraseEnc = '' #str vacio
    for letra in palabra: #recorro Frase letra por letra
        encontrado = False
        for x,y in abc.items():
            if letra == x:
                FraseEnc += y #fraseEnc.append(y)
                encontrado = True
        if not encontrado: #if encontrado == False
                            # if encontrado != True
            FraseEnc += letra
    print (FraseEnc)
    return FraseEnc
    
