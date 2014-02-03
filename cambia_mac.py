#! /usr/bin/env python

'''Script para cambiar la mac'''

import os, sys, subprocess
from termcolor import colored

#Comprueba si eres root
def eresRoot():
    if os.getuid() != 0:
        print colored ('No eres root :-(', 'red')
        sys.exit(1)

#Realiza un rfkill 
def rfkill():
    rfkill_comando = 'rfkill unblock all'
    try:
        subprocess.check_call(rfkill_comando, shell=True)
        return 0
    except:
        return -1
        
#Apaga o enciende la interfaz
def gestionaInterfaz(accion, interfaz=None):
    if interfaz is None:
        interfaz = 'wlan0'
    if accion =='apaga':
        apaga_interfaz = 'ifconfig ' + interfaz + ' down'
        try:
            salida = subprocess.check_output(apaga_interfaz, shell=True)
            return 0
        except:
            return -1
    elif accion == 'enciende':
        enciende_interfaz = 'ifconfig ' + interfaz + ' up'
        try:
            salida = subprocess.check_output(enciende_interfaz, shell=True)
            return 0
        except:
            return -1
        
#Cambia la mac
def cambiaMac(interfaz=None, mac=None):
    if interfaz is None:
        interfaz = 'wlan0'
    if mac is None:
        mac = '00:23:18:69:69:69'
    cambia_mac = 'ifconfig ' + interfaz + ' hw ether ' + mac
    try:
        salida = subprocess.check_call(cambia_mac, shell=True)
        return 0
    except:
        return -1

#Codigo principal
def main():
    eresRoot()
    print colored ( '***************************************************', 'blue')
    if rfkill() != 0:
        print colored ('Problemas con rfkill', 'red') 

    print colored ('Apagando interfaz ...', 'green')
    if gestionaInterfaz('apaga') == 0:
        print colored ('Interfaz apagada!', 'green')
    else:
        print colored ('No se puede apagar la interfaz :-(', 'red')
        sys.exit(2)
    print colored ('Procediendo a cambiar la mac...', 'green')
    if cambiaMac() == 0:
        print colored ('Direccion mac cambiada!', 'green')
    else:
        print colored ('No se ha podido cambiar la direccion mac :-(', 'red')
        sys.exit(3)
    print colored ('Levantando de nuevo la interfaz', 'green')
    if gestionaInterfaz('enciende') == 0:
        print colored ('Interfaz reinicada!', 'green')
    else:
        print colored ('No se ha podido reiniciar la interfaz despues del cambio', 'red')
        sys.exit(4)
    print colored ('****************************************************', 'blue')
if __name__ == "__main__":
    main()
