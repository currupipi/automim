#! /usr/bin/env python

'''Script para cambiar la mac'''

import os, sys, subprocess

#Comprueba si eres root
def eresRoot():
    if os.getuid() != 0:
        print 'No eres root :-('
        sys.exit(1)

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
    print '***************************************************'
    print 'Apagando interfaz ...'
    if gestionaInterfaz('apaga') == 0:
        print 'Interfaz apagada!'
    else:
        print 'No se puede apagar la interfaz :-('
        sys.exit(2)
    print 'Procediendo a cambiar la mac...'
    if cambiaMac() == 0:
        print 'Direccion mac cambiada!'
    else:
        print 'No se ha podido cambiar la direccion mac :-('
        sys.exit(3)
    print 'Levantando de nuevo la interfaz'
    if gestionaInterfaz('enciende') == 0:
        print 'Interfaz reinicada!'
    else:
        print 'No se ha podido reiniciar la interfaz despues del cambio'
        sys.exit(4)
    print '****************************************************'

if __name__ == "__main__":
    main()
