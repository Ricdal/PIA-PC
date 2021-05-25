import argparse


def main():
    examples = """Ejemplos de uso:
            -main.py -hash -file pengu.jpeg
            -main.py -m -target 192.168.0.1 -begin 1 -end 84
            -main.py -mt -ruta c://Desktop
            -main.py -cif -palabra Hola
            -main.py -des -palabra LSPE
            -main.py -cor -r TUCORREO -d DESTINO -s ASUNTO -c MENSAJE
                    """
    parser = argparse.ArgumentParser(description = """
                    Bienvenido al menú de funciones de ciberseguridad en Python, para utilizarlo
                    deberá de agregar el argumento necesario para indicar qué módulo desea usar
                    así como los argumentos necesarios para que dicho módulo funcione""", epilog = examples, formatter_class = argparse.RawDescriptionHelpFormatter)
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-m', '--ModMap', action = 'store_true',
                       help = 'Modulo de Mapeo para hacer un mapeo de red')
    group.add_argument('-mt', '--ModMeta', action = 'store_true',
                       help = 'Modulo de Metadata para obtener la metadata de un directorio de imagenes')
    group.add_argument('-cif', '--ModCif', action = 'store_true',
                       help = 'Modulo de Cifrado para cifrar una palabra con cifrado Cesar')
    group.add_argument('-des', '--ModDes', action = 'store_true',
                       help = 'Modulo de Descifrado para descifrar una palabra con cifrado Cesar')
    group.add_argument('-cor', '--ModCorreo', action = 'store_true',
                       help = 'Modulo de envio de correos de un remitente a un destinatario')
    group.add_argument('-hash', '--ModClaveHash', action = 'store_true',
                       help = 'Modulo para obtener la clave hash de un archivo (en la misma carpeta)')
    parser.add_argument("-target", dest = "target", metavar='', help = "Dirección IP")
    parser.add_argument("-begin", dest = "begin", metavar='', help = "Inicio del rango de puertos a escanear")
    parser.add_argument("-end", dest = "end", metavar='', help = "Final del rango de puertos")
    parser.add_argument("-ruta", dest = "ruta", metavar='', help = "Dirección de la carpeta")
    parser.add_argument("-palabra", dest = "palabra", metavar='', help = "Palabra que desee cifrar con cifrado Cesar")
    parser.add_argument('-r', dest = 'remitente', metavar='', type=str, help='Correo de la persona que envía el mensaje')
    parser.add_argument('-d', dest = 'destinatario', metavar='', type=str, help='Correo de la persona a la que se le va a enviar el mensaje')
    parser.add_argument('-s', dest = 'asunto', metavar='', type=str, help='Asunto del Correo')
    parser.add_argument('-c', dest = 'cuerpo', metavar='', type=str, help='Cuerpo del Correo')
    parser.add_argument("-file", dest = "file", metavar='', help = "Nombre del archivo")
    args = parser.parse_args()
    
    if args.ModMap:
        while not(args.target and args.begin and args.end):
            parser.error("--ModMap requires --target --begin --end")
        if args.target and args.begin and args.end:
            import codigoMapeored
            codigoMapeored.mapeo(args.target, args.begin, args.end)
        
        
    elif args.ModMeta:
        while not(args.ruta):
            parser.error("--ModMeta requires --ruta")
        if args.ruta:
            import codigoMetadata
            codigoMetadata.metaData(args.ruta)

    elif args.ModCif:
        while not (args.palabra):
            parser.error("--ModCif requires --palabra")
        if args.palabra:
            import codigoCifCes
            codigoCifCes.Encriptar(args.palabra)

    elif args.ModDes:
        while not (args.palabra):
            parser.error("--ModDes requires --palabra")
        if args.palabra:
            import codigoDesCes
            codigoDesCes.Desencriptar(args.palabra)

    elif args.ModCorreo:
        while not(args.remitente and args.destinatario and args.asunto and args.cuerpo):
            parser.error("--ModCorreo requires --r --d --s --c")
        if args.remitente and args.destinatario and args.asunto and args.cuerpo:
            import codigoCorreo
            codigoCorreo.correo(args.remitente, args.destinatario, args.asunto, args.cuerpo)

    elif args.ModClaveHash:
        while not (args.file):
            parser.error("--ModClaveHash requires --file")
        if args.file:
            import codigoHash
            codigoHash.hash_archivo(args.file)
        


if __name__ == "__main__":
    try:
        main()
    except ImportError:
        import os
        print("Error en paquetes","Instalando paquetes")
        os.system('pip install -r requierements.txt')
        print("Paquetes instalados","ReRun")
        exit()
