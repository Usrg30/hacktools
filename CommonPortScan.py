import socket as sk
lista=[21,22,23,25,49,53,67,68,69,80,88,110,111,123,135,137,138,139,143,161,179,201,389,443,445,500,514,520,546,547,587,902,1080,1194,1433,1434,1521,1629,2049,3128,3306,3389,5060,5222,5432,5666,5900,6000,6129,6667,9001,9090,9091,9100,8080]

for port in lista:
    try:
        s=sk.socket(sk.AF_INET, sk.SOCK_STREAM) #predeterminados (familia de direcciones Af_inet) y (tipo de conector sock-stream)
        s.settimeout(50) #tiempo de espera
        s.connect(('127.0.0.1', port)) #direccion y puerto(local host por defecto, modificar con el de la maquina a escanear)
        print('Port - %d: Open' % (port)) #imprime el resultado
        s.close()
    except:
        pass

