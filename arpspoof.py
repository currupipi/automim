#! /usr/bin/env python

'''Script para arpspoofing'''

import os, sys, subprocess, socket

#Comprueba si el script lo lanza root
if os.getuid() != 0:
    print "No eres root :( "
    sys.exit(1)

#Activa el port forwarding
print "Activando ip forwarding ... "

if subprocess.call('echo 1 > /proc/sys/net/ipv4/ip_forward', shell=True) != 0:
    print "No se ha podido activar el ip_forward :("
    sys.exit(2)

#Scan de ips de la red
nmap_comando = 'nmap -sS 192.168.1.0/24'

resultado 

