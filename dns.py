#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
#import sys #descomentar para ocupar variable de sistema

#el puerto en que se escucharán paquetes UDP debe ser especificado al iniciar la ejecución del programa
port = input("Ingrese el número de puerto en que desea escuchar paquetes UDP")
#port = sys.argv[0] #descomentar para ocupar puerto como variable de la llamada de sistema, y comentar la linea anterior

#ip de la maquina en que se está corriendo el programa (self) para retorno
ip = '127.0.0.1'

#configurar un socket que envia paquetes UDP (SOCK_DGRAM) usando protocolo IPv4 (AF_INET)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#iniciar el socket asociando su configuración al ip y puerto especificado
s.bind((ip,port))

#programa principal
#se mantiene iterando mientras el programa esté corriendo
while True:
    data, address = s.recvfrom(512)
    print("hola.com")
    #resolve(data, address)

def resolve(data, address):
    return