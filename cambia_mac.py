#! /usr/bin/env python

'''Script para cambiar la mac'''

import os, sys, subprocess
from termcolor import colored
from time import sleep

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
    elif accion == 'mimac':
        mac = '00:23:18:69:69:69'
        indica_mac = "ifconfig wlan0 | grep HWaddr | cut -d ' ' -f10 | tr a-z A-Z"
        salida = subprocess.check_output(indica_mac, shell=True)
        salida = salida.rstrip('\n')
        if  salida != mac :
            print colored ('no se ha podido cambiar la mac :-(', 'red')
            return 1
        else:
            return 0

    else:
        print colored ('Error desconocido en la llamada a gestionaInterfaz :-(', 'red')
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

#Lanza DHCP
def dhcp():
    pide_dhcp = 'dhclient wlan0'
    try:
        salida = subprocess.check_call(pide_dhcp, shell=True)
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
        print colored ('Interfaz reinicada! esto tarda unos segundos...', 'green')
        sleep(10)
        if gestionaInterfaz('mimac') == 1:
            print colored ('Pero finalente no se ha cambiado correctamente la mac ...', 'red')
    else:
        print colored ('No se ha podido reiniciar la interfaz despues del cambio', 'red')
        sys.exit(4)
    if dhcp() != 0:
        print colored ('ERROR al pedir dhcp','red')
    
    print colored ('****************************************************', 'blue')
if __name__ == "__main__":
    main()
