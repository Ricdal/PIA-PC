def Desencriptar(palabra):
    abc = {
    'A':'E', 'B':'F', 'C':'G', 'D':'H', 'E':'I',
    'F':'J', 'G':'K', 'H':'L', 'I':'M', 'J':'N',
    'K':'O', 'L':'P', 'M':'Q', 'N':'R', 'O':'S',
    'P':'T', 'Q':'U', 'R':'V', 'S':'W', 'T':'X',
    'U':'Y', 'V':'Z', 'W':'A', 'X':'B', 'Y':'C',
    'Z':'D'
    }
    palabra = palabra.upper()
    FraseDes = ''
    for letra in palabra:
        encontrado = False
        for x,y in abc.items():
            if letra == y:
                FraseDes += x #fraseEnc.append(x)
                encontrado = True
        if not encontrado: #if encontrado == False
            FraseDes += letra
    print (FraseDes)
    return FraseDes
