#script to connect to Cisco device via SSH

import datetime
import pathlib
import os
import netmiko

from pathlib import Path
from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("Please enter your SSH username: ")
PASS = getpass("Please enter your SSH password: ")

myPath = Path.cwd()

d = datetime.datetime.now()

fileName = 'csrBackup'

fileExt = '.txt'

backup = fileName + '_' + str(d) + fileExt

write = 'w'

openBackup = open(backup, write)

vRTR_IP = '192.168.41.11'

device = {
    'ip': '192.168.41.11',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}

c = ConnectHandler(**device)

output = c.send_command('show run', 'x')

openBackup.write(output)

openBackup.close()
