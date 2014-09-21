#! /usr/bin/env python

'''Networking framework'''

import os, sys, subprocess

#Gets the ip address of the specified interface, if not specified by default is wlan0
def get_ip(interface=None):
    import netifaces
    if interface is None:
        interface = 'wlan0'
    myaddress = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]
    #my_ip = myaddress.get('addr')
    #my_netmask = myaddress.get('netmask')
    return myaddress


def main():
    print "testing values of my address"
    my_addr = get_ip()
    my_ip = my_addr.get('addr')
    my_netmask = my_addr.get('netmask')
    print "My ip is: ", my_ip , " and my netmask is: ", my_netmask

if __name__ == "__main__":
    main()
