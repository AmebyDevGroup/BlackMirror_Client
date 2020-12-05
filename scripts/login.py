#!/usr/bin/python
# add following line to show up when some one ssh to pi /etc/profile 
# sudo python /var/www/cron/login.py
# clear everything from /etc/motd to remove generic message.
# coding=utf-8
import socket, os, re, time, sys, subprocess, fcntl, struct
from threading import Thread
class bc:
	HEADER = '\033[0;36;40m'
	ENDC = '\033[0m'
	SUB = '\033[3;30;45m'
	WARN = '\033[0;31;40m'
	GREEN = '\033[0;32;40m'
	org = '\033[91m'
print bc.HEADER + " "	
print "   ____  _            _    __  __ _                     "
print "  |  _ \| |          | |  |  \/  (_)                    "
print "  | |_) | | __ _  ___| | _| \  / |_ _ __ _ __ ___  _ __ "
print "  |  _ <| |/ _` |/ __| |/ / |\/| | | '__| '__/ _ \| '__|"
print "  | |_) | | (_| | (__|   <| |  | | | |  | | | (_) | |   "
print "  |____/|_|\__,_|\___|_|\_\_|  |_|_|_|  |_|  \___/|_|   "
print " "
print "    "+bc.SUB + "PROJEKT INTELIGENTNEGO LUSTRA "+ bc.ENDC
print bc.WARN +" "
print "*************************************************************************"
print "* Witaj! Zalogowales sie do panelu admina, Smart Lustra                 *"
print "*                          Tworcy:                                      *"
print "*                          JAKUB LORC                                   *"
print "*                          ADRIAN SUTKOWSKI                             *"
print "*                          JAKUB WERWINSKI                              *"
print "*                          KRZYSZTOF WIECZOREK                          *"
print "*************************************************************************"
print bc.GREEN +"                                                  Baw sie dobrze - Tworcy"  + bc.ENDC

